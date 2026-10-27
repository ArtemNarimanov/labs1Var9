@echo off
setlocal enabledelayedexpansion
chcp 1251 >nul

rem ============================================================
rem  PROC.bat - запуск KUTIL2 дл€ каждой задачи
rem
rem  ƒл€ каждого подкаталога task\* последовательно:
rem    0. проверка возобновлени€: если в логе запуска есть маркер
rem       "*** FINISHED" - задача уже обработана и пропускаетс€
rem       полностью (без удалени€ файлов, симлинков и запуска exe);
rem    1. удал€ет старый kutlis;
rem    2. создаЄт симлинки korsar.exe, kutil2.exe, nwsp_dat из REPO;
rem    3. запускает kutil2.exe (симлинк в папке задачи) с выводом
rem       в лог работы;
rem    4. ведЄт логи: result\log_<задача>_proc_start.txt и
rem       result\log_<задача>_proc.txt (ANSI/CP1251).
rem ============================================================

set "taskRoot=%~dp0task"
set "repo=%~dp0..\labs1Var9"
set "logDir=%~dp0result"

rem --- создаЄм каталог результатов, если его нет
if not exist "%logDir%" mkdir "%logDir%"

rem --- провер€ем наличие каталога задач
if not exist "%taskRoot%" (
    echo  аталог задач не найден: %taskRoot%
    exit /b 1
)

rem --- провер€ем, что в каталоге задач есть хот€ бы одна подпапка
set "hasTask="
for /d %%D in ("%taskRoot%\*") do set "hasTask=1"
if not defined hasTask (
    echo ¬ каталоге задач нет подпапок с задачами: %taskRoot%
    exit /b 1
)

rem --- последовательна€ обработка подкаталогов задач
for /d %%D in ("%taskRoot%\*") do (
    set "taskName=%%~nxD"
    set "startLog=%logDir%\log_!taskName!_proc_start.txt"
    set "calcLog=%logDir%\log_!taskName!_proc.txt"

    rem --- проверка возобновлени€: маркер "*** FINISHED" в логе запуска
    if exist "!startLog!" (
        findstr /c:"FINISHED" "!startLog!" >nul 2>&1
        if !errorlevel!==0 (
            echo «адача !taskName! уже обработана, пропускаем
        ) else (
            call :processTask "%%D" "!startLog!" "!calcLog!"
        )
    ) else (
        call :processTask "%%D" "!startLog!" "!calcLog!"
    )
)

rem --- готово
echo ¬се задачи обработаны. Ћоги: %logDir%

exit /b 0

rem ============================================================
rem  :processTask - обработка одной задачи
rem    %1 - путь к папке задачи, %2 - лог запуска, %3 - лог работы
rem ============================================================
:processTask
set "taskDir=%~1"
set "startLog=%~2"
set "calcLog=%~3"

rem --- перезаписываем лог запуска
type nul > "%startLog%"
call :log Starting KUTIL2 !DATE! !TIME!
call :log Task directory: %taskDir%

rem --- удал€ем старый kutlis (отсутствие файла - не ошибка)
del "%taskDir%\kutlis" 2>nul

rem --- создаЄм симлинки из REPO (существующий файл/ссылку удал€ем)
call :link "korsar.exe"
call :link "kutil2.exe"
call :link "nwsp_dat"

rem --- запускаем KUTIL2 через симлинк в папке задачи, вывод в лог работы
pushd "%taskDir%"
start /BELOWNORMAL /WAIT cmd /s /c "chcp 1251 >nul & kutil2.exe > "%calcLog%" 2>&1"
set "rc=!errorlevel!"
popd

if !rc!==0 (
    call :log Finishing KUTIL2: exit code 0
    call :log *** FINISHED !DATE! !TIME!
) else (
    call :log Finishing KUTIL2 with error, exit code: !rc!
)
exit /b 0

rem ============================================================
rem  :link - создаЄт симлинк в папке задачи на файл %1 из REPO
rem          (существующий файл/ссылку сначала удал€ем)
rem ============================================================
:link
if exist "%taskDir%\%~1" del "%taskDir%\%~1" 2>nul
mklink "%taskDir%\%~1" "%repo%\%~1"
if errorlevel 1 call :log Ќе удалось создать симлинк %~1
exit /b 0

rem ============================================================
rem  :log - печатает строку и в консоль, и в лог запуска
rem        (без аргумента - пуста€ строка)
rem ============================================================
:log
set "msg=%*"
if defined msg (
    echo %msg%
    >> "%startLog%" echo %msg%
) else (
    echo.
    >> "%startLog%" echo.
)
exit /b 0
