from datetime import date
from docutils import nodes
from sphinx.util.docutils import SphinxDirective

now = date.today()
bibtex_months = ['', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
bibtex_template = r'''
@manual{%s,
  title = {{%s}},
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
                                    self.env.config.html_title,
                                    self.env.config.author.replace(',', ' and '),
                                    self.env.config.release,
                                    now.year,
                                    bibtex_months[now.month],
                                    self.env.config.html_baseurl,
                                    self.env.config.html_baseurl)
        paragraph_node = nodes.literal_block(text=bibtex, language='bibtex')
        return [paragraph_node]


def setup(app):
    app.add_directive("bibtex", Bibtex)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
