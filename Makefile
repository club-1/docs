# Minimal makefile for Sphinx documentation
#
# You can set these variables from the command line.
LOCALE          ?= fr
PUBHOST         ?= club1.fr
PUBDIR          ?= /var/www/docs

ifneq "$(LOCALE)" "fr"
override NOTFR   = 1
else
override NOTFR   =
endif

ifneq (,$(filter grouped-target,$(.FEATURES)))
GROUPED_TARGET   = 1
else
$(warning WARNING: This version of make does not support grouped-target, disabling parallel jobs.)
.NOTPARALLEL:
endif

SPHINXLANG       = -D language=$(LOCALE)
SPHINXOPTS      += -a
SPHINXBUILD     ?= sphinx-build
SPHINXBUILDERS   = html dirhtml singlehtml epub latex text man texinfo
SPHINXCMDS       = pickle json htmlhelp changes xml pseudoxml linkcheck doctest coverage
SOURCEDIR        = .
BUILDDIR         = _build
MDFILES          = index.md $(shell find . -type f -name '*.md')
TEMPLATES        = $(shell find _templates -type f -name '*.html')
LOCALES          = en
LOCALEFILES      = $(LOCALES:%=locales/%/LC_MESSAGES/package.po)
PONAMES          = package sphinx
POTS             = $(PONAMES:%=locales/%.pot)

export LANGUAGES = fr $(LOCALES)

# Put it first so that "make" without argument is like "make help".
help:
	$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $O

.PHONY: help clean update-po gettext latexpdf info publish $(SPHINXBUILDERS) $(SPHINXCMDS)

update-po: $(LOCALEFILES)

gettext: $(POTS)

$(LOCALEFILES): locales/%/LC_MESSAGES/package.po: $(POTS)
	sphinx-intl update -p $(<D) -l $*
	@touch $@

ifdef GROUPED_TARGET
$(POTS)&: $(MDFILES) $(TEMPLATES)
else
$(POTS): $(MDFILES) $(TEMPLATES)
endif
	$(SPHINXBUILD) -b gettext "$(SOURCEDIR)" locales $(SPHINXOPTS) $O
	@touch $(POTS)

latexpdf: latex
	$(MAKE) -C $(BUILDDIR)/latex/$(LOCALE)

info: texinfo
	$(MAKE) -C $(BUILDDIR)/texinfo/$(LOCALE)

publish:
	rsync -av --del --exclude='.*' _build/html/ $(USER)@$(PUBHOST):$(PUBDIR)

# Shinx commands that need locales (builders).
$(SPHINXBUILDERS): $(if $(NOTFR),$(PONAMES:%=locales/$(LOCALE)/LC_MESSAGES/%.po))
	$(SPHINXBUILD) -b $@ "$(SOURCEDIR)" "$(BUILDDIR)/$@/$(LOCALE)" $(SPHINXLANG) $(SPHINXOPTS) $O

# Other Sphinx commands for autocompletion
$(SPHINXCMDS):
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $O

clean:
	rm -f locales/*/LC_MESSAGES/*.mo
	rm -rf locales/.doctrees
	rm -rf $(BUILDDIR)/*
