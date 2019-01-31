@ECHO OFF

:: Bootstrap dev environment
:: PyCharm | Settings > Tools > Termial -> Shell path
:: "cmd" /k ""z.cmd""

:: Init CMDER
if exist %CMDER_ROOT% call %CMDER_ROOT%/vendor/init.bat

:: Ensure Virtualenv is Active
if exist %~dp0\venv\Scripts\activate call %~dp0\venv\Scripts\activate
