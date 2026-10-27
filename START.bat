@echo off
setlocal enabledelayedexpansion
chcp 1251 >nul

rem ============================================================
rem  START.bat - запуск KORSAR для каждой задачи
rem
rem  Для каждого подкаталога task\* последовательно:
rem    1. удаляет старые korlis, korres, kutlis и *.dat;
rem    2. запускает korsar.exe на задачу;
rem    3. ведёт лог в result\log_start.txt (ANSI/CP1251).
rem ============================================================

set "taskRoot=%~dp0task"
set "logDir=%~dp0result"
set "logFile=%logDir%\log_start.txt"

rem --- создаём каталог результатов, если его нет
if not exist "%logDir%" mkdir "%logDir%"

rem --- проверяем наличие каталога задач
if not exist "%taskRoot%" (
    call :log Каталог задач не найден: %taskRoot%
    exit /b 1
)

rem --- проверяем, что в каталоге задач есть хотя бы одна подпапка
set "hasTask="
for /d %%D in ("%taskRoot%\*") do set "hasTask=1"
if not defined hasTask (
    call :log В каталоге задач нет подпапок с задачами: %taskRoot%
    exit /b 1
)

rem --- очищаем лог перед запуском
type nul > "%logFile%"
call :log Файл лога: %logFile%

rem --- последовательная обработка подкаталогов задач
for /d %%D in ("%taskRoot%\*") do (
    call :log
    call :log ================== TASK: %%~nxD ==================
    call :log Starting KORSAR !DATE! !TIME!
    call :log Task directory: %%D

    rem --- удаляем старые файлы результатов перед запуском (отсутствие файлов - не ошибка)
    del "%%D\korlis" 2>nul
    del "%%D\korres" 2>nul
    del "%%D\kutlis" 2>nul
    del "%%D\*.dat"      2>nul

    rem --- запускаем задачу KORSAR с выводом в файл лога
    pushd "%%D"
    if exist "korsar.exe" (
        cmd /c ""korsar.exe" >> "%logFile%" 2>&1"
        set "rc=!errorlevel!"
    ) else (
        call :log korsar.exe не найден в каталоге задачи: %%D
        set "rc=1"
    )
    popd

    call :log Finishing KORSAR !DATE! !TIME!, exit code: !rc!
)

rem --- готово
call :log
call :log Все задачи обработаны. Лог: %logFile%

rem --- в конце открываем текстовый файл лога
notepad "%logFile%"

exit /b 0

rem ============================================================
rem  :log - печатает строку и в консоль, и в файл лога
rem        (без аргумента - пустая строка)
rem ============================================================
:log
set "msg=%*"
if defined msg (
    echo %msg%
    >> "%logFile%" echo %msg%
) else (
    echo.
    >> "%logFile%" echo.
)
exit /b 0
