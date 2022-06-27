from sphinx.application import Sphinx
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging
from docutils import nodes


class TermTooltips(SphinxPostTransform):
    default_priority = 900
    logger = logging.getLogger('term_tooltips')

    def run(self) -> None:
        # Get dictionary of terms from the standard domain.
        stddomain = self.env.get_domain('std')
        self.stdterms = stddomain.data.setdefault('terms', {})
        for termref in self.document.findall(nodes.reference):
            if isinstance(termref[0], nodes.Inline) and 'std-term' in termref[0]['classes']:
                self.logger.debug(f'found termref: {termref}')
                self.process_termref(termref)

    def process_termref(self, termref: nodes.reference) -> None:
        # Get current doc name
        docname = self.env.docname
        refid = termref.get('refid', '')
        # If 'refid' is not defined, then the ref is from another document
        # and we need to find it from the standard domain.
        if refid == '':
            # Get key from termref's text.
            reftext: str = termref.astext().lower()
            # Get object from dictionary of terms.
            obj = self.stdterms.get(reftext, None)
            if obj == None:
                self.logger.warning(f'could not find object in std domain for reftext: "{reftext}"')
                return
            # Override document and refid with those found from the standard domain.
            docname = obj[0]
            refid = obj[1]
        self.logger.debug(f'document: {docname}, refid: {refid}')
        document = self.env.get_doctree(docname)
        term: nodes.Element
        # Find corresponding term node from its doctree.
        for term in document.findall(nodes.term):
            ids = term.get('ids', [])
            if refid in ids:
                self.logger.debug(f'found term: {term}')
                parent = term.parent
                assert isinstance(parent, nodes.Node), "parent is not a node !!"
                termref['reftitle'] = parent.children[1].astext()
                break

def setup(app: Sphinx):
    app.add_post_transform(TermTooltips)
