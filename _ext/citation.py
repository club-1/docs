from datetime import date
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective

bibtex_months = ['', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
bibtex_template = r'''
@manual{%s,
  title = {%s},
  author = {%s},
  edition = {%s},
  year = %d,
  month = %s,
  note = {\texttt{%s}},
  url = {%s}
}
'''

class Bibtex(SphinxDirective):
    def run(self):
        bibtex = bibtex_template % (self.env.config.project + 'Documentation',
                                    self.env.config.citation_bibtex_title or self.env.config.html_title,
                                    self.env.config.author.replace(',', ' and '),
                                    self.env.config.release,
                                    self.env.config.citation_date.year,
                                    bibtex_months[self.env.config.citation_date.month],
                                    self.env.config.html_baseurl,
                                    self.env.config.html_baseurl)
        paragraph_node = nodes.literal_block(text=bibtex, language='bibtex')
        return [paragraph_node]


def setup(app: Sphinx):
    app.add_directive('citation:bibtex', Bibtex)
    app.add_config_value('citation_date', date.today(), 'env')
    app.add_config_value('citation_bibtex_title', '', 'env')

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
