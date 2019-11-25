To build a local copy of the DEA docs, install the programs in
requirements.txt and run 'make fetchnotebooks html'.
After building for the first time, you only need to run 'make html'.
If you use the conda package manager these commands will suffice::

  git clone https://github.com/GeoscienceAustralia/dea-docs.git
  cd dea-docs
  conda create -c conda-forge -n deadocs python=3.7 pandoc
  conda activate deadocs
  pip install -r requirements.txt
  make fetchnotebooks html
  open _build/html/index.html
  
See the `contribution instructions <https://github.com/GeoscienceAustralia/dea-docs/wiki/Contribution-instructions>`_ for more details.
