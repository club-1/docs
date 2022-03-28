# Minimal makefile for Sphinx documentation
#
# You can set these variables from the command line.

LOCALES         := en
LOCALEFILES     := $(LOCALES:%=locales/%/LC_MESSAGES/package.po) $(LOCALES:%=locales/%/LC_MESSAGES/sphinx.po)

export AUTHORS      := $(shell awk '{printf t $$0; t=", "}' AUTHORS)
export PACKAGE      := CLUB1
export VERSION      := main
export EMAIL        := nicolas@club1.fr

export LANGUAGES    := fr $(LOCALES)
export LATEXMKOPTS  := -quiet

SPHINXLANG      := -D language=$(LOCALE)
SPHINXOPTS      += -a $(if $(CI),,-q)
SPHINXBUILD     ?= sphinx-build
SPHINXBUILDERS  := html dirhtml singlehtml epub latex text man texinfo
SPHINXLBUILDERS := $(foreach b,$(SPHINXBUILDERS),$(LANGUAGES:%=$b/%))
SPHINXCMDS      := gettext pickle json htmlhelp changes xml pseudoxml linkcheck doctest coverage
SOURCEDIR       := .
BUILDDIR        := _build

PUBHOST         ?= club1.fr
PUBDIR          ?= /var/www/docs

# Put it first so that "make" without argument is like "make help".
help:
	$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $O

.PHONY: help clean update-po latexpdf info publish $(SPHINXBUILDERS) $(SPHINXLBUILDERS) $(SPHINXCMDS)

update-po: $(LOCALEFILES);

%.mo: %.po
	msgfmt -o $@ $<

.SECONDEXPANSION:
$(LOCALEFILES): locales/%.po: locales/$$(*F).pot
	msgmerge -q --update $@ $< --backup=none -w 77
	@touch $@

locales/package.pot locales/sphinx.pot: locales/%.pot: $(BUILDDIR)/gettext/%.pot
	xgettext $< -o $@ -w 77 \
	--copyright-holder='$(AUTHORS)' --package-name='$(PACKAGE)' \
	--package-version='$(VERSION)' --msgid-bugs-address='$(EMAIL)'

$(BUILDDIR)/gettext/%.pot: gettext;

latexpdf info: %: $(LANGUAGES:%=\%/%);

$(LANGUAGES:%=latexpdf/%): latexpdf/%: latex/%
	$(MAKE) -C $(BUILDDIR)/$<

$(LANGUAGES:%=info/%): info/%: texinfo/%
	$(MAKE) -C $(BUILDDIR)/$<

publish:
	rsync -av --del --exclude='.*' _build/html/ $(USER)@$(PUBHOST):$(PUBDIR)

# Shinx builders that builds localized versions.
$(SPHINXBUILDERS): %: $(LANGUAGES:%=\%/%);

# Localized Sphinx builders
.SECONDEXPANSION:
$(SPHINXLBUILDERS): $$(if $$(filter fr,$$(@F)),,locales/$$(@F)/LC_MESSAGES/package.mo locales/$$(@F)/LC_MESSAGES/sphinx.mo)
	LANGUAGE=$(@F) $(SPHINXBUILD) -b $(@D) "$(SOURCEDIR)" "$(BUILDDIR)/$(@D)/$(@F)" $(SPHINXOPTS) $O

# Other Sphinx commands for autocompletion
$(SPHINXCMDS):
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $O

clean:
	rm -f locales/*/LC_MESSAGES/*.mo
	rm -rf locales/.doctrees
	rm -rf $(BUILDDIR)/*

.PHONY: .FORCE
.FORCE:
