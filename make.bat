REM This is the script for building the site locally on Windows. In the Command Prompt, enter the command:
REM make.bat

docker build -t dea-docs .

docker run -it --rm --name dea-docs --publish 8062:8062 --volume ".\docs\notebooks":"/docs/notebooks" --volume ".\output":"/output" --env-file .env dea-docs

