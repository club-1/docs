# Minimal makefile for Sphinx documentation
#
# You can set these variables from the command line.

LOCALES         := en
LOCALEDIR       := _locales
LOCALEFILES     := $(LOCALES:%=$(LOCALEDIR)/%/LC_MESSAGES/package.po) $(LOCALES:%=$(LOCALEDIR)/%/LC_MESSAGES/sphinx.po)

export AUTHORS      := $(shell awk '{printf t $$0; t=", "}' AUTHORS)
export PACKAGE      := CLUB1
export VERSION      := main
export EMAIL        := nicolas@club1.fr

export LOCALE       := fr
export LANGUAGES    := $(LOCALE) $(LOCALES)
export LATEXMKOPTS  := -quiet

SPHINXLANG      := -D language=$(LOCALE)
SPHINXOPTS      += -a $(if $(CI),,-q)
SPHINXBUILD     ?= sphinx-build
SPHINXBUILDERS  := html dirhtml singlehtml epub latex text man texinfo
SPHINXLBUILDERS := $(foreach b,$(SPHINXBUILDERS),$(LANGUAGES:%=$b/%))
SPHINXCMDS      := gettext changes xml pseudoxml linkcheck
SOURCEDIR       := .
BUILDDIR        := _build
DIRS            := $(SPHINXBUILDERS:%=$(BUILDDIR)/%)

PUBHOST         ?= club1.fr
PUBDIR          ?= /var/www/docs

# Put it first so that "make" without argument is like "make help".
help:
	$(SPHINXBUILD) -M help $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $O

.PHONY: help clean update-po latexpdf info publish $(SPHINXBUILDERS) $(SPHINXLBUILDERS) $(SPHINXCMDS)

$(DIRS):
	mkdir -p $@

update-po: $(LOCALEFILES);

%.mo: %.po
	msgfmt -o $@ $<

.SECONDEXPANSION:
$(LOCALEFILES): $(LOCALEDIR)/%.po: $(LOCALEDIR)/$$(*F).pot
	msgmerge -q --previous --update $@ $< --backup=none -w 79
	@touch $@

$(LOCALEDIR)/package.pot $(LOCALEDIR)/sphinx.pot: $(LOCALEDIR)/%.pot: $(BUILDDIR)/gettext/%.pot
	xgettext $< -o $@ -w 79 \
	--copyright-holder='$(AUTHORS)' --package-name='$(PACKAGE)' \
	--package-version='$(VERSION)' --msgid-bugs-address='$(EMAIL)'

$(BUILDDIR)/gettext/%.pot: gettext;

latexpdf info: %: $(LANGUAGES:%=\%/%);

$(LANGUAGES:%=latexpdf/%): latexpdf/%: latex/%
	$(MAKE) -C $(BUILDDIR)/$<

$(LANGUAGES:%=info/%): info/%: texinfo/%
	$(MAKE) -C $(BUILDDIR)/$<

$(BUILDDIR)/html/index.html: _templates/index.html | $(BUILDDIR)/html
	cp $< $@

publish:
	rsync -av --del --exclude='.*' _build/html/ $(USER)@$(PUBHOST):$(PUBDIR)

# Shinx builders that builds localized versions.
$(filter-out html,$(SPHINXBUILDERS)): %: $(LANGUAGES:%=\%/%);

html: $(LANGUAGES:%=html/%) $(BUILDDIR)/html/index.html

# Localized Sphinx builders
.SECONDEXPANSION:
$(SPHINXLBUILDERS): $$(if $$(filter fr,$$(@F)),,$(LOCALEDIR)/$$(@F)/LC_MESSAGES/package.mo $(LOCALEDIR)/$$(@F)/LC_MESSAGES/sphinx.mo)
	LOCALE=$(@F) $(SPHINXBUILD) -b $(@D) -d $(BUILDDIR)/doctrees/$(@F) $(SOURCEDIR) $(BUILDDIR)/$(@D)/$(@F) $(SPHINXOPTS) $O

# Other Sphinx commands for autocompletion
$(SPHINXCMDS):
	$(SPHINXBUILD) -M $@ $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $O

clean:
	rm -f $(LOCALEDIR)/*/LC_MESSAGES/*.mo
	rm -rf $(BUILDDIR)/*

.PHONY: .FORCE
.FORCE:
