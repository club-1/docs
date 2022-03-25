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
SPHINXOPTS      += -a
SPHINXBUILD     ?= sphinx-build
SPHINXLCMDS      = html dirhtml singlehtml epub latex latexpdf latexpdfja text man texinfo info
SPHINXCMDS       = pickle json htmlhelp changes xml pseudoxml linkcheck doctest coverage
SOURCEDIR        = .
BUILDDIR         = _build
MDFILES          = index.md $(shell find . -type f -name '*.md')
LOCALES          = en
LOCALEFILES      = $(LOCALES:%=locales/%/LC_MESSAGES/package.po)
DIRS             = locales

# Put it first so that "make" without argument is like "make help".
help:
	$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $O

.PHONY: help clean update-po gettext publish $(SPHINXLCMDS) $(SPHINXCMDS)

update-po: $(LOCALEFILES)

gettext: locales/package.pot

$(LOCALEFILES): locales/%/LC_MESSAGES/package.po: locales/package.pot
	sphinx-intl update -p $(<D) -l $*
	@touch $@

locales/package.pot: $(BUILDDIR)/gettext/package.pot | locales
	cp $< $@

$(DIRS):
	mkdir -p $@

$(BUILDDIR)/gettext/package.pot: $(MDFILES)
	$(SPHINXBUILD) -M gettext "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $O
	@touch $@

publish: html
	rsync -av --del _build/html/ $(USER)@$(PUBHOST):$(PUBDIR)

# Shinx commands that need locales.
$(SPHINXLCMDS): $(if $(NOTFR),locales/$(LOCALE)/LC_MESSAGES/package.po)
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXLANG) $(SPHINXOPTS) $O

# Other Sphinx commands for autocompletion
$(SPHINXCMDS):
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $O

clean:
	rm -f locales/*/LC_MESSAGES/package.mo
	rm -rf $(BUILDDIR)/*
