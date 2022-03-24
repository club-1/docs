# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
override LOCALE := $(or $(LOCALE),fr)
PUBHOST         ?= club1.fr
PUBDIR          ?= /var/www/docs/$(LOCALE)

ifneq "$(LOCALE)" "fr"
override NOTFR   = 1
else
override NOTFR   =
endif

SPHINXLANG       = -D language=$(LOCALE)
SPHINXOPTS      ?=
SPHINXBUILD     ?= sphinx-build
SPHINXLCMDS      = html latexpdf man
SPHINXCMDS       = clean gettext
SOURCEDIR        = .
BUILDDIR         = _build
LOCALES          = en
LOCALESDIRS      = $(LOCALES:%=locales/%)

# Put it first so that "make" without argument is like "make help".
help:
	$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $O

.PHONY: help locales publish Makefile $(SPHINXLCMDS) $(SPHINXCMDS)

locales: $(LOCALESDIRS)

$(LOCALESDIRS): gettext
	sphinx-intl update -p $(BUILDDIR)/gettext -l $(@F)
	touch $@

publish: html
	rsync -av --del _build/html/ $(USER)@$(PUBHOST):$(PUBDIR)

# Shinx commands that need locales.
$(SPHINXLCMDS): $(if $(NOTFR),locales/$(LOCALE))
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXLANG) $(SPHINXOPTS) $O

# Other Sphinx commands for autocompletion
$(SPHINXCMDS):
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $0

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $O
