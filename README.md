# DEA Knowledge Hub

To contribute content to this site, please [follow the publication process](https://geoscienceau.sharepoint.com/:w:/r/sites/DEA/_layouts/15/Doc.aspx?sourcedoc=%7BE75F31A8-1648-4DA3-9E36-9BB8135921B2%7D&file=DEA%20Publication%20Process.docx&action=default&mobileredirect=true).

## Git workflow

```mermaid
%%{init: { 'gitGraph': {'showCommitLabel': false}} }%%

gitGraph TB:
  commit
  branch develop
  checkout develop
  commit
  branch your-branch
  checkout develop
  checkout your-branch
  commit
  commit
  branch demo1
  commit
  checkout develop
  merge your-branch
  checkout develop
  commit
  branch demo2
  commit
  checkout develop
  branch demo3
  checkout main
  merge develop
```
