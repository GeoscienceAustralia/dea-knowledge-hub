# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = DigitalEarthAustralia
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile livehtml docker-live fetchnotebooks clean

requirements.in:
	pass

requirements.txt: requirements.in
	pip-compile --output-file=requirements.txt requirements.in --upgrade -v

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

fetchnotebooks:
	[ -d notebooks ] || git clone --branch stable --depth 1 https://github.com/GeoscienceAustralia/dea-notebooks.git notebooks
	cd notebooks && git checkout stable && git reset --hard origin/stable && git pull 

livehtml:
	sphinx-autobuild --open-browser --port 8001 --ignore notebooks --ignore .direnv --ignore _build/ --ignore .git/ --ignore .idea/ -b html $(SPHINXOPTS) . $(BUILDDIR)/html

docker-live: requirements.txt
	docker-compose build
	UID_GID="$(shell id -u):$(shell id -g)" docker-compose up

clean:
	rm -rf _build
	rm -rf notebooks/Tools/gen/
