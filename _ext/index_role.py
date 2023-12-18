from sphinx.application import Sphinx
from sphinx.domains.index import IndexRole
from docutils import nodes


class SurroundingIndexRole(IndexRole):
    def run(self):
        (elems, msgs) = super().run()
        index = elems[0]
        target = elems[1]
        text = elems[2]
        assert isinstance(target, nodes.Element), "target is not an Element node"
        target += text
        return [index, target], msgs

def setup(app: Sphinx):
    app.add_role('index', SurroundingIndexRole(), override=True)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
