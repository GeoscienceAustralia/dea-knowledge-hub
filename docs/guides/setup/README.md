# Getting started with DEA

This section focusses on getting started with Digital Earth Australia (DEA) through pre-built instances. These instances come with examples that teach you how to use DEA, as well as data and software you can use for your own work. The primary software for DEA is the [Open Data Cube](https://www.opendatacube.org/) (ODC), which can be easily integrated with other Python packages.

:::{contents} In this guide
:local:
:backlinks: none
:::

## Which DEA Services to use?

DEA provides several services and there can be multiple ways to access them. That's why we have created this matrix to help you decide.

<table class="colour-coded-table">
    <thead>
        <tr>
            <td></td>
            <td><strong>DEA Knowledge Hub</strong></td>
            <td><strong>DEA Maps</strong></td>
            <td><strong>DEA Explorer</strong></td>
            <td><strong>DEA Sandbox</strong></td>
            <td><strong>STAC</strong></td>
            <td><strong>AWS</strong></td>
            <td><strong>DEA WMS</strong></td>
            <td><strong>DEA WCS</strong></td>
        </tr>
   </thead>
    <tbody>
        <tr>
            <td><strong>Understand the data</strong></td>
            <td class="high"><a href="/">Browse the DEA Knowledge Hub</a></td>
            <td class="medium">Partial</td>
            <td class="medium">Partial</td>
            <td class="medium">Partial</td>
            <td class="medium">Partial</td>
            <td class="medium">Partial</td>
            <td class="medium">Partial</td>
            <td class="medium">Partial</td>
        </tr>
        <tr>
            <td><strong>View large data volumes</strong></td>
            <td class="low">No</td>
            <td class="high"><a href="/guides/setup/dea_maps/">View data on a map</a></td>
            <td class="low">No</td>
            <td class="medium">Partial</td>
            <td class="high"><a href="/guides/setup/gis/stac/">View data using STAC</a></td>
            <td class="low">No</td>
            <td class="high"><a href="/guides/setup/gis/web_map_service/">View data on the WMS</a></td>
            <td class="medium">Partial</td>
        </tr>
        <tr>
            <td><strong>Download data</strong></td>
            <td class="low">No</td>
            <td class="medium">Partial</td>
            <td class="high"><a href="/guides/setup/explorer_guide/">Download via Explorer</a></td>
            <td class="medium">Partial</td>
            <td class="high"><a href="/guides/setup/gis/stac/">Download via STAC</a></td>
            <td class="high"><a href="/guides/setup/AWS/data_and_metadata/">Download via AWS</a></td>
            <td class="low">No</td>
            <td class="high"><a href="/guides/setup/gis/web_coverage_service/">Download via WCS</a></td>
        </tr>
        <tr>
            <td><strong>Analyse data</strong></td>
            <td class="low">No</td>
            <td class="low">No</td>
            <td class="low">No</td>
            <td class="high"><a href="/guides/setup/Sandbox/sandbox/">Analyse in the Sandbox</a></td>
            <td class="medium">Partial</td>
            <td class="low">No</td>
            <td class="low">No</td>
            <td class="high"><a href="/guides/setup/gis/web_coverage_service/">Analyse using the WCS</a></td>
        </tr>
        <tr>
            <td><strong>Explore data availability</strong></td>
            <td class="low">No</td>
            <td class="medium">Partial</td>
            <td class="high"><a href="/guides/setup/explorer_guide/">Explore availability in the Explorer</a></td>
            <td class="medium">Partial</td>
            <td class="high"><a href="/guides/setup/gis/stac/">Query availability using STAC</a></td>
            <td class="low">No</td>
            <td class="low">No</td>
            <td class="low">No</td>
        </tr>
        <tr>
            <td><strong>Difficulty level</strong></td>
            <td>Beginner</td>
            <td>Beginner</td>
            <td>Intermediate</td>
            <td>Intermediate</td>
            <td>Intermediate</td>
            <td>Beginner</td>
            <td>Advanced</td>
            <td>Intermediate</td>
        </tr>
   </tbody>
</table>

## Instances

There are two available pre-built instances: the [Digital Earth Australia Sandbox](/guides/setup/Sandbox/sandbox/) and the [National Computational Infrastructure](/guides/setup/NCI/README/) (NCI). The Sandbox is suitable for all users, containing a representative sample of available data. The NCI contains all available data, but users must apply and be approved to gain an account.

## Examples

The examples are provided as Jupyter Notebooks, which can be run in either instance. Jupyter Notebooks contain code and explanations side-by-side so that you can understand the steps involved in an analysis. Our [Jupyter Notebooks](/guides/setup/jupyter/) page provides a quick introduction to using Jupyter Notebooks. For a more detailed introduction, visit the [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html).

The examples contained in each instance are the same as those covered in the [User Guide](/notebooks/Beginners_guide/README/).

## Getting help

You can ask questions (and view previously asked questions) on the [Open Data Cube Stack Exchange](https://gis.stackexchange.com/questions/tagged/open-data-cube) page. When asking a question, tag it with `open-data-cube`.

You can also join our [Open Data Cube Discord chat](https://discord.com/invite/4hhBQVas5U) for help setting up or using Digital Earth Australia.

