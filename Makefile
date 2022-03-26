# Minimal makefile for Sphinx documentation
#
# You can set these variables from the command line.
ifneq (,$(filter grouped-target,$(.FEATURES)))
GROUPED_TARGET  := 1
else
$(warning WARNING: This version of make does not support grouped-target, disabling parallel jobs.)
.NOTPARALLEL:
endif

LOCALES         := en
LOCALEFILES     := $(LOCALES:%=locales/%/LC_MESSAGES/package.po)
PONAMES         := package sphinx
POTS            := $(PONAMES:%=locales/%.pot)

export LANGUAGES    := fr $(LOCALES)
export LATEXMKOPTS  := -quiet

SPHINXLANG      := -D language=$(LOCALE)
SPHINXOPTS      += -a $(if $(CI),,-q)
SPHINXBUILD     ?= sphinx-build
SPHINXBUILDERS  := html dirhtml singlehtml epub latex text man texinfo
SPHINXLBUILDERS := $(foreach b,$(SPHINXBUILDERS),$(LANGUAGES:%=$b/%))
SPHINXHBUILDERS := $(SPHINXBUILDERS:%=_%)
SPHINXCMDS      := pickle json htmlhelp changes xml pseudoxml linkcheck doctest coverage
SOURCEDIR       := .
BUILDDIR        := _build
MDFILES         := index.md $(shell find . -type f -name '*.md')
TEMPLATES       := $(shell find _templates -type f -name '*.html')

PUBHOST         ?= club1.fr
PUBDIR          ?= /var/www/docs

# Put it first so that "make" without argument is like "make help".
help:
	$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $O

.PHONY: help clean update-po gettext latexpdf info publish $(SPHINXBUILDERS) $(SPHINXLBUILDERS) $(SPHINXHBUILDERS) $(SPHINXCMDS)

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

latexpdf info: %: $(LANGUAGES:%=\%/%)

$(LANGUAGES:%=latexpdf/%): latexpdf/%: latex/%
	$(MAKE) -C $(BUILDDIR)/$<

$(LANGUAGES:%=info/%): info/%: texinfo/%
	$(MAKE) -C $(BUILDDIR)/$<

publish:
	rsync -av --del --exclude='.*' _build/html/ $(USER)@$(PUBHOST):$(PUBDIR)

# Shinx builders that builds localized versions.
$(SPHINXBUILDERS): %: $(LANGUAGES:%=\%/%)

# Localized Sphinx builders
$(SPHINXLBUILDERS):
	$(MAKE) _$(@D) LOCALE=$(@F)

# Hidden Sphinx builders that need the LOCALE variable
$(SPHINXHBUILDERS): _%: $(if $(filter fr,$(LOCALE)),,$(PONAMES:%=locales/$(LOCALE)/LC_MESSAGES/%.po))
	$(SPHINXBUILD) -b $* "$(SOURCEDIR)" "$(BUILDDIR)/$*/$(LOCALE)" -D language=$(LOCALE) $(SPHINXOPTS) $O

# Other Sphinx commands for autocompletion
$(SPHINXCMDS):
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $O

clean:
	rm -f locales/*/LC_MESSAGES/*.mo
	rm -rf locales/.doctrees
	rm -rf $(BUILDDIR)/*
