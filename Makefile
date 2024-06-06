# Minimal makefile for Sphinx documentation
# heavily customized for internationalization.
#
# You can set these variables from the command line.

LOCALES         := en
LOCALEDIR       := _locales
LOCALEFILES     := $(LOCALES:%=$(LOCALEDIR)/%/LC_MESSAGES/package.po) $(LOCALES:%=$(LOCALEDIR)/%/LC_MESSAGES/sphinx.po)
UPDATEPO        := $(filter update-po,$(MAKECMDGOALS))

DATE                := $(shell date +%F)
REVISION            := $(shell git describe --always --dirty --abbrev=4)
COPYRIGHT           := Membres de CLUB1

export AUTHORS      := $(shell awk '{printf t $$0; t=", "}' AUTHORS)
export PACKAGE      := CLUB1
export VERSION      := main
export RELEASE      := $(DATE)-g$(REVISION)
export EMAIL        := nicolas@club1.fr

export LOCALE       := fr
export LANGUAGES    := $(LOCALE) $(LOCALES)
export LATEXMKOPTS  := -file-line-error $(if $(CI),,-quiet)

SPHINXOPTS      += $(if $(CI),,-q -j auto)
SPHINXBUILD     ?= sphinx-build
SPHINXBUILDERS  := html dirhtml singlehtml epub latex text man texinfo linkcheck
SPHINXLBUILDERS := $(foreach b,$(SPHINXBUILDERS),$(LANGUAGES:%=$b/%))
SPHINXCMDS      := gettext changes xml pseudoxml
SOURCEDIR       := .
BUILDDIR        := _build
DIRS            := $(SPHINXBUILDERS:%=$(BUILDDIR)/%) $(SPHINXLBUILDERS:%=$(BUILDDIR)/%)
ALL             := $(LANGUAGES:%=all/%)

PYSRC        := conf.py
XGETTEXT     := xgettext -x $(LOCALEDIR)/exclude.po -w 79 --add-comments \
		--copyright-holder='$(COPYRIGHT)' --package-name='$(PACKAGE)' \
		--package-version='$(VERSION)' --msgid-bugs-address='$(EMAIL)'
DIFF         := diff -u --color

RTDVERSION   := 2.0.0

PUBHOST         ?= club1.fr
PUBDIR          ?= /var/www/docs

# Put it first so that "make" without argument is like "make help".
help:
	$(SPHINXBUILD) -M help $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $O

.PHONY: help deps clean update-po latexpdf info publish $(ALL) $(SPHINXBUILDERS) $(SPHINXLBUILDERS) $(SPHINXCMDS)
.SECONDEXPANSION:

$(DIRS):
	mkdir -p $@

update-po: $(LOCALEFILES);

check-po: $(LOCALEFILES:%=check-po/%)
	msgfmt --check-domain _locales/exclude.po
	msgcat $(LOCALEDIR)/exclude.po --sort-output | $(DIFF) - $(LOCALEDIR)/exclude.po

$(LOCALEFILES:%=check-po/%): check-po/%:
	msgfmt --check $*

%.mo: %.po
	msgfmt -o $@ $<

ifdef UPDATEPO
$(LOCALEFILES): $(LOCALEDIR)/%.po: $(LOCALEDIR)/$$(*F).pot
	msgmerge -q --previous --update $@ $< --backup=none -w 79
	@touch $@
endif

$(LOCALEDIR)/package.pot: $(PYSRC)
$(LOCALEDIR)/%.pot: $(BUILDDIR)/gettext/%.pot
	$(XGETTEXT) $^ -o $@

$(BUILDDIR)/gettext/%.pot: gettext;

# Special Sphinx builders that need two steps
latexpdf info: %: $(LANGUAGES:%=\%/%)

$(LANGUAGES:%=latexpdf/%): latexpdf/%: latex/%
	cat _templates/style.xdy >> $(BUILDDIR)/$</sphinx.xdy
	mogrify -strip -resize '800x600>' -define png:compression-level=9 $(BUILDDIR)/$</*.png
	max_print_line=110 $(MAKE) -C $(BUILDDIR)/$<

$(LANGUAGES:%=info/%): info/%: texinfo/%
	$(MAKE) -C $(BUILDDIR)/$<

# Add some dependencies to the html builders
html: $(BUILDDIR)/html/index.html $(BUILDDIR)/html/.htaccess $(BUILDDIR)/html/metadata.yaml
$(LANGUAGES:%=html/%): _static/js/theme.js

$(BUILDDIR)/html/index.html: _templates/index.html | $(BUILDDIR)/html
	cp $< $@

$(BUILDDIR)/html/.htaccess: _templates/.htaccess .FORCE | $(BUILDDIR)/html
	sed -e 's/{{release}}/$(RELEASE)/' $< > $@

$(BUILDDIR)/html/metadata.yaml: .FORCE | $(BUILDDIR)/html
	echo 'release: $(RELEASE)' > $@

publish:
	rsync -av --checksum --fuzzy --delete-delay --include='.htaccess' --exclude='.*' _build/html/ $(USER)@$(PUBHOST):$(PUBDIR)

# Build the full docs ready to be published for a language
all: $(ALL) html latexpdf epub
$(ALL): export DOWNLOADS = club1-$(@F)-latest.pdf club1-$(@F)-latest.epub
$(ALL): all/%: html/% latexpdf/% epub/% | $(BUILDDIR)/html/%
	cp $(BUILDDIR)/latex/$*/club1.pdf $(BUILDDIR)/html/$*/club1-$*-$(RELEASE).pdf
	cp $(BUILDDIR)/epub/$*/CLUB1.epub $(BUILDDIR)/html/$*/club1-$*-$(RELEASE).epub

# Shinx builders that builds localized versions.
$(SPHINXBUILDERS): %: $(LANGUAGES:%=\%/%)

# Localized Sphinx builders
$(SPHINXLBUILDERS): $$(if $$(filter fr,$$(@F)),,$(LOCALEDIR)/$$(@F)/LC_MESSAGES/package.mo $(LOCALEDIR)/$$(@F)/LC_MESSAGES/sphinx.mo)
	LOCALE=$(@F) $(SPHINXBUILD) -b $(@D) -d $(BUILDDIR)/doctrees/$(@F) $(SOURCEDIR) $(BUILDDIR)/$(@D)/$(@F) $(SPHINXOPTS) $O

# Other Sphinx commands for autocompletion
$(SPHINXCMDS):
	$(SPHINXBUILD) -M $@ $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $O

deps: _static/js/theme.js;

_static/js/theme.js: _static/js/theme.js.orig
	patch $< _patches/theme-js-nav-no-reset.diff -o $@
	rm $<

.INTERMEDIATE: _static/js/theme.js.orig;

_static/js/theme.js.orig:
	wget -q https://raw.githubusercontent.com/readthedocs/sphinx_rtd_theme/$(RTDVERSION)/src/theme.js -O $@

mostlyclean:
	rm -f $(LOCALEDIR)/*/LC_MESSAGES/*.mo
	rm -f *.log
	rm -rf $(BUILDDIR)/*
	rm -rf _ext/__pycache__

clean: mostlyclean
	rm -f _static/js/theme.js*

.PHONY: .FORCE
.FORCE:
