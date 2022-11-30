import re
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.writers.html5 import HTML5Translator
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging
from docutils import nodes
from markupsafe import escape

from typing import Callable, Optional


class TermTooltips(SphinxPostTransform):
    default_priority = 5
    logger = logging.getLogger('term_tooltips')
    apply: Optional[Callable[[str], str]]
    single_newlines = re.compile('(?<!\n)\n')

    def run(self) -> None:
        if self.app.builder.format != 'html':
            return
        self.apply = self.app.config.term_tooltips_apply_function
        # Get dictionary of terms from the standard domain.
        stddomain = self.env.get_domain('std')
        self.stdterms = stddomain.data.setdefault('terms', {})
        for node in self.document.findall(addnodes.pending_xref):
            if node['reftype'] == 'term':
                self.logger.debug(f'found termref: {node}')
                self.process_termref(node)

    def process_termref(self, termref: addnodes.pending_xref) -> None:
        # Get key from termref's target.
        target: str = termref['reftarget'].lower()
        # Get object from dictionary of terms.
        obj = self.stdterms.get(target, None)
        if obj == None:
            self.logger.debug(f'could not find object in std domain for target: "{target}"')
            return
        # get document and refid from object found in the standard domain.
        docname, refid = obj[:2]
        self.logger.debug(f'document: {docname}, refid: {refid}')
        document = self.env.get_doctree(docname)
        term: nodes.Element
        # Find corresponding term node from its doctree.
        term = document.ids[refid]
        self.logger.debug(f'found term: {term}')
        parent = term.parent
        assert isinstance(parent, nodes.Element), f'parent {parent} is not an Element !?'
        index = parent.first_child_matching_class(nodes.definition)
        assert index is not None, f'term {term} has no definition !?'
        deftext = parent[index].astext()
        deftext = self.single_newlines.sub(' ', deftext)
        if self.apply != None:
            deftext = self.apply(deftext)
        newnode = nodes.abbreviation()
        newnode['explanation'] = escape(deftext)
        newnode += termref.deepcopy()
        termref.replace_self(newnode)

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
