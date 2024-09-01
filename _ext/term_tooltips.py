import re
from docutils import nodes, writers
from docutils.io import StringOutput
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.builders.dummy import DummyBuilder
from sphinx.domains.std import StandardDomain
from sphinx.environment import BuildEnvironment
from sphinx.util.docutils import new_document
from sphinx.writers.html5 import HTML5Translator
from sphinx.writers.text import TextTranslator, TextWriter
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.locale import _
from sphinx.util import logging

from typing import Optional, Tuple

class TooltipTranslator(TextTranslator):
    def visit_table(self, node: nodes.Element) -> None:
        title = next(node.findall(nodes.title), None)
        caption = _('Table: %s') % title.astext() if title else _('Table')
        self.add_text('[%s]' % caption)
        raise nodes.SkipNode

    def new_state(self, indent: int = 0) -> None:
        """Override new_state() to disable indentation by default."""
        super().new_state(indent)

    def visit_emphasis(self, node: nodes.Element) -> None:
        pass

    def depart_emphasis(self, node: nodes.Element) -> None:
        pass

    def visit_inline(self, node: nodes.Element) -> None:
        if 'xref' in node['classes'] or 'term' in node['classes']:
            self.add_text('[')

    def depart_inline(self, node: nodes.Element) -> None:
        if 'xref' in node['classes'] or 'term' in node['classes']:
            self.add_text(']')

    def visit_literal_block(self, node: nodes.Element) -> None:
        self.new_state(indent=3)


class TooltipBuilder(DummyBuilder):
    default_translator_class = TooltipTranslator


class TermTooltips(SphinxPostTransform):
    cache = dict()
    default_priority = 5
    logger = logging.getLogger('term_tooltips')
    start_after: Optional[str]
    end_before: Optional[str]
    stddomain: StandardDomain
    writer: writers.Writer

    def __init__(self, document: nodes.document, startnode: nodes.Node | None = None):
        super().__init__(document, startnode)
        builder = TooltipBuilder(self.app, BuildEnvironment(self.app))
        self.writer = TextWriter(builder) # type: ignore

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
        tmpdoc = new_document(document.settings)
        tmpdoc += parent[index]
        destination = StringOutput(encoding='unicode')
        self.writer.write(tmpdoc, destination)
        deftext: str = destination.destination.strip() # type: ignore
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
