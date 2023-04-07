@echo off

for /f "delims=" %%i in ('dir /s/b *.txt') do (

for /f "delims=" %%a in ('type "%%~fi"') do (

set "foo=%%a"

call,set foo=%%foo:Danger=-Danger-%%
call,set foo=%%foo:Drink=-Drink-%%
call,set foo=%%foo:Phone=-Phone-%%
call,set foo=%%foo:Safe=-Safe-%%

call,echo/%%foo%%>>"%%~fi._"

)

move "%%~fi._" "%%~fi"

)

exit