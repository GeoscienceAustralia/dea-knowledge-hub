# Validation Report Scripts

# These scripts are used to generate the Validation Reports which are published to the DEA Knowledge Hub, including Site Reports, Quarterly Reports, and Yearly Reports.

# <https://knowledge.dea.ga.gov.au/validation/>

# How to use these scripts:

# 1. Upload these scripts to the DEA Sandbox.
# 2. Run this command in the Sandbox:
#     python __init__.py
# 3. The output will be generated, containing Markdown, Images, and CSV files.

from . import AddSite
from . import SingleDualPlot
from . import rgbPlot
from . import PlotBands
from . import CreateMarkdown
