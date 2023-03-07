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

export AUTHORS      := $(shell awk '{printf t $$0; t=", "}' AUTHORS)
export PACKAGE      := CLUB1
export VERSION      := main
export RELEASE      := $(DATE)-g$(REVISION)
export EMAIL        := nicolas@club1.fr

export LOCALE       := fr
export LANGUAGES    := $(LOCALE) $(LOCALES)
export LATEXMKOPTS  := -file-line-error $(if $(CI),,-quiet)

SPHINXLANG      := -D language=$(LOCALE)
SPHINXOPTS      += -a $(if $(CI),,-q)
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
		--copyright-holder='$(AUTHORS)' --package-name='$(PACKAGE)' \
		--package-version='$(VERSION)' --msgid-bugs-address='$(EMAIL)'
DIFF         := diff -u --color

PUBHOST         ?= club1.fr
PUBDIR          ?= /var/www/docs

# Put it first so that "make" without argument is like "make help".
help:
	$(SPHINXBUILD) -M help $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $O

.PHONY: help clean update-po latexpdf info publish $(ALL) $(SPHINXBUILDERS) $(SPHINXLBUILDERS) $(SPHINXCMDS)

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

.SECONDEXPANSION:
$(LOCALEFILES): $(LOCALEDIR)/%.po: $(if $(UPDATEPO),$(LOCALEDIR)/$$(*F).pot)
	msgmerge -q --previous --update $@ $< --backup=none -w 79
	@touch $@

$(LOCALEDIR)/package.pot: $(BUILDDIR)/gettext/package.pot $(PYSRC)
	$(XGETTEXT) $< $(PYSRC) -o $@

$(LOCALEDIR)/sphinx.pot: $(BUILDDIR)/gettext/sphinx.pot
	$(XGETTEXT) $< -o $@

$(BUILDDIR)/gettext/%.pot: gettext;

latexpdf info: %: $(LANGUAGES:%=\%/%);

$(LANGUAGES:%=latexpdf/%): latexpdf/%: latex/%
	cat _templates/style.xdy >> $(BUILDDIR)/$</sphinx.xdy
	mogrify -strip -resize '800x600>' -define png:compression-level=9 $(BUILDDIR)/$</*.png
	max_print_line=110 $(MAKE) -C $(BUILDDIR)/$<

$(LANGUAGES:%=info/%): info/%: texinfo/%
	$(MAKE) -C $(BUILDDIR)/$<

$(BUILDDIR)/html/index.html: _templates/index.html | $(BUILDDIR)/html
	cp $< $@

$(BUILDDIR)/html/.htaccess: _templates/.htaccess .FORCE | $(BUILDDIR)/html
	sed -e 's/{{release}}/$(RELEASE)/' $< > $@

$(BUILDDIR)/html/metadata.yaml: .FORCE | $(BUILDDIR)/html
	echo 'release: $(RELEASE)' > $@

publish:
	rsync -av --del --include='.htaccess' --exclude='.*' _build/html/ $(USER)@$(PUBHOST):$(PUBDIR)

# Build the full docs ready to be published for a language
all: $(ALL) $(BUILDDIR)/html/index.html $(BUILDDIR)/html/.htaccess $(BUILDDIR)/html/metadata.yaml;
$(ALL): export DOWNLOADS = club1-$(@F)-latest.pdf club1-$(@F)-latest.epub
$(ALL): all/%: html/% latexpdf/% epub/% | $(BUILDDIR)/html/%
	cp $(BUILDDIR)/latex/$*/club1.pdf $(BUILDDIR)/html/$*/club1-$*-$(RELEASE).pdf
	cp $(BUILDDIR)/epub/$*/CLUB1.epub $(BUILDDIR)/html/$*/club1-$*-$(RELEASE).epub

# Shinx builders that builds localized versions.
$(filter-out html,$(SPHINXBUILDERS)): %: $(LANGUAGES:%=\%/%);

html: $(LANGUAGES:%=html/%) $(BUILDDIR)/html/index.html $(BUILDDIR)/html/.htaccess $(BUILDDIR)/html/metadata.yaml

# Localized Sphinx builders
.SECONDEXPANSION:
$(SPHINXLBUILDERS): $$(if $$(filter fr,$$(@F)),,$(LOCALEDIR)/$$(@F)/LC_MESSAGES/package.mo $(LOCALEDIR)/$$(@F)/LC_MESSAGES/sphinx.mo)
	LOCALE=$(@F) $(SPHINXBUILD) -b $(@D) -d $(BUILDDIR)/doctrees/$(@F) $(SOURCEDIR) $(BUILDDIR)/$(@D)/$(@F) $(SPHINXOPTS) $O
	$(patsubst %,patch -p1 -d $(BUILDDIR)/$@ < %; ,$(wildcard _patches/$(@D)/*))

# Other Sphinx commands for autocompletion
$(SPHINXCMDS):
	$(SPHINXBUILD) -M $@ $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $O

clean:
	rm -f $(LOCALEDIR)/*/LC_MESSAGES/*.mo
	rm -f *.log
	rm -rf $(BUILDDIR)/*
	rm -rf _ext/__pycache__

.PHONY: .FORCE
.FORCE:
