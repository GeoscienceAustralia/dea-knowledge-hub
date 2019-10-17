To build a local copy of the DEA docs, install the programs in
requirements.txt and run 'make fetchnotebooks html'.
After building for the first time, you only need to run 'make html'.
If you use the conda package manager these commands will suffice::

  git clone https://github.com/GeoscienceAustralia/dea-docs.git
  cd dea-docs
  conda create -c conda-forge -n deadocs --file requirements.txt
  conda activate deadocs
  make fetchnotebooks html
  open _build/html/index.html
  
See the `contribution instructions <https://github.com/GeoscienceAustralia/dea-docs/wiki/Contribution-instructions>`_ for more details.
