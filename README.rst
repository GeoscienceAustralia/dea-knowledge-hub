To build a local copy of the DEA docs, install the programs in
requirements.txt and run 'make fetchnotebooks html'.
After building for the first time, you only need to run 'make html'.
The instructions below are specific to building the docs ``develop`` branch with the `dea-notebooks <https://github.com/GeoscienceAustralia/dea-notebooks/tree/develop>`_ ``develop`` branch.
If you use the conda package manager these commands will suffice::

  git clone https://github.com/GeoscienceAustralia/dea-docs.git
  cd dea-docs
  conda create -c conda-forge -n deadocs --file requirements.txt
  conda activate deadocs
  git checkout develop
  make fetchnotebooks html
  open _build/html/index.html
  
See the `contribution instructions <https://github.com/GeoscienceAustralia/dea-docs/wiki/Contribution-instructions>`_ for more details.
