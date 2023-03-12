import re
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.domains.std import StandardDomain
from sphinx.writers.html5 import HTML5Translator
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging
from docutils import nodes
from markupsafe import escape

from typing import Callable, Optional, Tuple


class TermTooltips(SphinxPostTransform):
    default_priority = 5
    logger = logging.getLogger('term_tooltips')
    apply: Optional[Callable[[str], str]]
    single_newlines = re.compile('(?<!\n)\n(?!\n)')
    stddomain: StandardDomain

    def run(self) -> None:
        if self.app.builder.format != 'html':
            return
        self.apply = self.app.config.term_tooltips_apply_function
        # Get dictionary of terms from the standard domain.
        stddomain = self.env.get_domain('std')
        assert isinstance(stddomain, StandardDomain), "'std' domain is not an instance of StandardDomain"
        self.stddomain = stddomain
        self.stdterms = self.stddomain.data.setdefault('terms', {})
        for node in self.document.findall(addnodes.pending_xref):
            if node['reftype'] == 'term':
                self.logger.debug(f'found termref: {node}')
                self.process_termref(node)
            elif node['refdomain'] == 'std':
                self.process_stdref(node)

    def process_termref(self, termref: addnodes.pending_xref) -> None:
        # Get key from termref's target.
        target: str = termref['reftarget'].lower()
        # Get object from dictionary of terms.
        obj = self.stdterms.get(target, None)
        if obj == None:
            self.logger.debug(f'could not find object in std domain for target: "{target}"')
            return
        self.build_abbrev_and_wrap_node(termref, obj, nodes.definition)

    def process_stdref(self, objref: addnodes.pending_xref) -> None:
        # Get key from termref's target.
        reftarget: str = objref['reftarget']
        reftype: str = objref['reftype']

        # Get object from stddomain's objects.
        obj = None
        objtypes = self.stddomain.objtypes_for_role(reftype) or []
        for objtype in objtypes:
            if (objtype, reftarget) in self.stddomain.objects:
                obj = self.stddomain.objects[objtype, reftarget]
                break
        if obj == None:
            self.logger.debug(f'could not find object in std domain for target: "{reftarget}"')
            return
        self.build_abbrev_and_wrap_node(objref, obj, addnodes.desc_content)

    def build_abbrev_and_wrap_node(self, ref: addnodes.pending_xref, target: Tuple[str, str], definition_node_type: type):
        # get document and refid from object found in the standard domain.
        docname, labelid = target[:2]
        self.logger.debug(f'document: {docname}, refid: {labelid}')
        document = self.env.get_doctree(docname)
        targetnode: nodes.Element
        # Find corresponding target element from its doctree.
        targetnode = document.ids[labelid]
        self.logger.debug(f'found term: {targetnode}')
        parent = targetnode.parent
        assert isinstance(parent, nodes.Element), f'parent {parent} is not an Element !?'
        index = parent.first_child_matching_class(definition_node_type)
        assert index is not None, f'element {targetnode} has no definition !?'
        deftext = parent[index].astext()
        deftext = self.single_newlines.sub(' ', deftext)
        if self.apply != None:
            deftext = self.apply(deftext)
        newnode = nodes.abbreviation()
        newnode['explanation'] = escape(deftext)
        newnode += ref.deepcopy()
        ref.replace_self(newnode)

class TooltipsHTMLTranslator(HTML5Translator):
    """This custom HTML5 translator allows line breaks in attributes values.
    """
    def attval(self, text, whitespace=re.compile('[\r\t\v\f]')):
        return super().attval(text, whitespace)

def setup(app: Sphinx):
    app.add_config_value(
            name='term_tooltips_apply_function',
            default=None,
            rebuild='html')
    app.add_post_transform(TermTooltips)
    app.set_translator('html', TooltipsHTMLTranslator)
