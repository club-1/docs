from sphinx.application import Sphinx
from docutils.transforms import Transform
from docutils import nodes

"""Sphinx plugin for CLUB1."""

class FrenchTypography(Transform):
    """
    Replace some ASCII characters with typographic form fr French.

    Based on SmartQuotes Transform.
    """

    # Low priority
    default_priority = 888

    nodes_to_skip = (nodes.FixedTextElement, nodes.Special)
    """Do not apply FrenchTypo to instances of these block-level nodes."""

    literal_nodes = (nodes.FixedTextElement, nodes.Special,
                     nodes.image, nodes.literal, nodes.math,
                     nodes.raw, nodes.problematic)
    """Do not apply FrenchTypo to instances of these inline nodes."""

    def __init__(self, document, startnode):
        Transform.__init__(self, document, startnode=startnode)
        self.unsupported_languages = set()

    def replace_chars(self, text):
            # Always add NBSP before some ponctuation marks.
            text = text.replace(' :', ' :')
            text = text.replace(' !', ' !')
            text = text.replace(' ?', ' ?')
            return text

    def apply(self):
        document_language = self.document.settings.language_code

        # Replace some chars in normal text. Handle each block of text
        # (TextElement node) as a unit to keep context around inline nodes:
        for node in self.document.findall(nodes.TextElement):
            # skip preformatted text blocks and special elements:
            if isinstance(node, self.nodes_to_skip):
                continue
            # nested TextElements are not "block-level" elements:
            if isinstance(node.parent, nodes.TextElement):
                continue

            # list of text nodes in the "text block":
            txtnodes = [txtnode for txtnode in node.findall(nodes.Text)
                        if not isinstance(txtnode.parent,
                                          nodes.option_string)]

            # language: use typographical chars for language "fr"
            lang = node.get_language_code(document_language)
            if lang != 'fr':
                break

            for node in txtnodes:
                if (isinstance(node.parent, self.literal_nodes)
                    or isinstance(node.parent.parent, self.literal_nodes)):
                    continue
                node.parent.replace(node, nodes.Text(self.replace_chars(str(node))))

def setup(app: Sphinx):
    app.add_transform(FrenchTypography)
