@ECHO OFF
set env_name=venv
IF "%1"=="" (
    set env_name=venv
) ELSE (
    set env_name=%1
)

call "%~dp0%env_name%\Scripts\activate"
ECHO ON
echo Virtual environment activated (%env_name%)

