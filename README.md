# DEA Knowledge Hub

To contribute content to this site, please [follow the publication process](https://geoscienceau.sharepoint.com/:w:/r/sites/DEA/_layouts/15/Doc.aspx?sourcedoc=%7BE75F31A8-1648-4DA3-9E36-9BB8135921B2%7D&file=DEA%20Publication%20Process.docx&action=default&mobileredirect=true).

## Git workflow

You should do your work on the `develop` branch or, ideally, branch off into your own branch (e.g. `alex` branch or `feature/something` branch). Then, preview your changes by pushing to one of the demo branches (`demo1`, `demo2`, or `demo3`) before merging into `develop` and then creating a pull request into the `main` branch.

![Git workflow diagram](https://mermaid.ink/svg/pako:eNqNkT9PAzEMxb9KZOl0SxmgW0aoxMIGYxY3cS8Rl-SUOlTVKd-d9C_t6RBsz88_20_yCDoaAglNM7rgWIpRtJ3j14SDbWvVbm3cvUTvHb_hmvrqbbDfUimiNI0KKlxo8fEsVRBCH-GDWicM2gpDX9TH4dizpD9j5jtvyu9jTg8n_evMxZuy110zKXx8nDAzmz2ljv4VYe7A098HbujlHePRhZ8E5wlYQK1ry9QfjYe2ArbkSYGs0tAGc88KVCgVxczxfR80SE6ZFpAHg0wrh11CfzLLN_hJsJw)

<!-- ```mermaid -->
<!-- %%{init: { 'gitGraph': {'showCommitLabel': false}} }%% -->
<!--  -->
<!-- gitGraph TB: -->
<!--   commit -->
<!--   branch develop -->
<!--   checkout develop -->
<!--   commit -->
<!--   branch your-branch -->
<!--   checkout develop -->
<!--   checkout your-branch -->
<!--   commit -->
<!--   commit -->
<!--   branch demo1 -->
<!--   commit -->
<!--   checkout develop -->
<!--   merge your-branch -->
<!--   checkout develop -->
<!--   commit -->
<!--   branch demo2 -->
<!--   commit -->
<!--   checkout develop -->
<!--   branch demo3 -->
<!--   checkout main -->
<!--   merge develop -->
<!-- ``` -->

# Overwriting demo branches

Instead of merging into the demo branches, it's easier to overwrite them with the exact contents of your branch.

```bash
git checkout demo1
git reset --hard your-branch
git push origin demo1 --force
```
