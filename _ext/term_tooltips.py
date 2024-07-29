import re
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.domains.std import StandardDomain
from sphinx.writers.html5 import HTML5Translator
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging
from docutils import nodes

from typing import Callable, Optional, Tuple


class TermTooltips(SphinxPostTransform):
    cache = dict()
    default_priority = 5
    logger = logging.getLogger('term_tooltips')
    start_after: Optional[str]
    end_before: Optional[str]
    single_newlines = re.compile('(?<!\n)\n(?!\n)')
    too_much_newlines = re.compile('\n{3,}')
    stddomain: StandardDomain

    def run(self) -> None:
        if self.app.builder.format != 'html':
            return
        self.start_after = self.app.config.term_tooltips_start_after
        self.end_before = self.app.config.term_tooltips_end_before
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
        reftype: str = termref['reftype']

        # First check if the definition is in the cache
        cache_key = (reftype, target)
        deftext = self.cache.get(cache_key, None)
        if deftext:
            self.build_abbrev_and_wrap_node(termref, deftext)
            return
        # Get object from dictionary of terms.
        obj = self.stdterms.get(target, None)
        if obj == None:
            self.logger.debug(f'could not find object in std domain for target: "{target}"')
            return
        deftext = self.build_definition_text(obj, nodes.definition)
        self.cache[cache_key] = deftext
        self.build_abbrev_and_wrap_node(termref, deftext)

    def process_stdref(self, objref: addnodes.pending_xref) -> None:
        # Get key from termref's target.
        reftarget: str = objref['reftarget']
        reftype: str = objref['reftype']

        # First check if the definition is in the cache
        cache_key = (reftype, reftarget)
        deftext = self.cache.get(cache_key, None)
        if deftext:
            self.build_abbrev_and_wrap_node(objref, deftext)
            return
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
        deftext = self.build_definition_text(obj, addnodes.desc_content)
        self.cache[cache_key] = deftext
        self.build_abbrev_and_wrap_node(objref, deftext)

    def build_definition_text(self, target: Tuple[str,str], definition_node_type: type) -> str:
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
        deftext = self.too_much_newlines.sub('\n\n', deftext)
        if self.start_after != None:
            deftext = deftext.split(self.start_after, 1)[-1].lstrip()
        if self.end_before != None:
            deftext = deftext.split(self.end_before, 1)[0].rstrip()
        return deftext

    def build_abbrev_and_wrap_node(self, ref: addnodes.pending_xref, deftext: str):
        newnode = nodes.abbreviation()
        newnode['explanation'] = deftext
        newnode += ref.deepcopy()
        ref.replace_self(newnode)

class TooltipsHTMLTranslator(HTML5Translator):
    """This custom HTML5 translator allows line breaks in attributes values.
    """
    def attval(self, text, whitespace=re.compile('[\r\t\v\f]')):
        return super().attval(text, whitespace)

def setup(app: Sphinx):
    app.add_config_value(
            name='term_tooltips_start_after',
            default=None,
            rebuild='html')
    app.add_config_value(
            name='term_tooltips_end_before',
            default=None,
            rebuild='html')
    app.add_post_transform(TermTooltips)
    app.set_translator('html', TooltipsHTMLTranslator)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
