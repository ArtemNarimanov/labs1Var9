@echo off
setlocal enabledelayedexpansion
chcp 1251 >nul

rem ============================================================
rem  PROC.bat - запуск KUTIL2 для каждой задачи
rem
rem  Для каждого подкаталога task\* последовательно:
rem    0. проверка возобновления: если в логе есть маркер
rem       "*** FINISHED [имя_задачи]" - задача уже обработана
rem       и пропускается полностью (без удаления файлов,
rem       симлинков и запуска exe);
rem    1. удаляет старый kutlis;
rem    2. создаёт симлинки kutil2.exe, nwsp_dat из REPO;
rem    3. запускает kutil2.exe (симлинк в папке задачи) с выводом
rem       в лог;
rem    4. ведёт единый лог: result\proc.log (ANSI/CP1251),
rem       все задачи дописываются в порядке прогона.
rem
rem  Опция: PROC.bat --force - игнорировать маркер возобновления
rem          и обработать все задачи заново.
rem
rem  Внимание: файловые симлинки требуют прав администратора
rem          или включённого Developer Mode.
rem ============================================================

set "taskRoot=%~dp0task"
set "repo=%~dp0..\labs1Var9"
set "logDir=%~dp0result"

rem --- нормализуем пути к абсолютным (убираем ..)
for %%I in ("%taskRoot%") do set "taskRoot=%%~fI"
for %%I in ("%repo%") do set "repo=%%~fI"
for %%I in ("%logDir%") do set "logDir=%%~fI"

rem --- проверяем наличие репозитория
if not exist "%repo%\" (
    echo Ошибка: не найден репозиторий: %repo%
    exit /b 1
)

set "sharedLog=%logDir%\proc.log"

rem --- создаём каталог результатов, если его нет
if not exist "%logDir%" mkdir "%logDir%"

rem --- проверяем наличие каталога задач
if not exist "%taskRoot%\" (
    echo Каталог задач не найден: %taskRoot%
    exit /b 1
)

rem --- проверяем, что в каталоге задач есть хотя бы одна подпапка
set "hasTask="
for /d %%D in ("%taskRoot%\*") do set "hasTask=1"
if not defined hasTask (
    echo В каталоге задач нет подпапок с задачами: %taskRoot%
    exit /b 1
)

rem --- опция --force: игнорировать маркер возобновления
set "force=0"
if /i "%~1"=="--force" set "force=1"

set "failCount=0"
set "failedTasks="

rem --- последовательная обработка подкаталогов задач
for /d %%D in ("%taskRoot%\*") do (
    set "taskName=%%~nxD"
    set "skip=0"
    if "!force!"=="0" if exist "%sharedLog%" (
        findstr /c:"*** FINISHED [!taskName!]" "%sharedLog%" >nul 2>&1
        if !errorlevel!==0 set "skip=1"
    )
    if "!skip!"=="1" (
        echo Задача !taskName! уже обработана, пропускаем
    ) else (
        call :processTask "%%D" "%sharedLog%"
        if !errorlevel! neq 0 (
            set /a "failCount+=1"
            set "failedTasks=!failedTasks! !taskName!"
        )
    )
)

rem --- итог
echo.
if !failCount! gtr 0 (
    echo ОШИБКА: не удалось обработать задач: !failCount!
    echo!failedTasks!
    >> "%sharedLog%" echo ==================================================
    >> "%sharedLog%" echo ОШИБКА: не удалось обработать задач: !failCount!
    exit /b 1
)
echo Все задачи обработаны. Лог: %sharedLog%
>> "%sharedLog%" echo ==================================================
>> "%sharedLog%" echo Все задачи обработаны !DATE! !TIME!
exit /b 0

rem ============================================================
rem  :processTask - обработка одной задачи
rem    %1 - путь к папке задачи, %2 - общий лог-файл
rem ============================================================
:processTask
set "taskDir=%~1"
set "logFile=%~2"

call :log ==================================================
call :log Задача: !taskName!
call :log Starting KUTIL2 !DATE! !TIME!

rem --- удаляем старый kutlis (отсутствие файла - не ошибка)
del "%taskDir%\kutlis" 2>nul

rem --- создаём симлинки из REPO (существующий файл/ссылку удаляем)
call :link "kutil2.exe"
if errorlevel 1 exit /b 1
call :link "nwsp_dat"
if errorlevel 1 exit /b 1

rem --- запускаем KUTIL2 через симлинк в папке задачи, вывод в лог
pushd "%taskDir%" >nul
kutil2.exe >> "!logFile!" 2>&1
set "rc=!errorlevel!"
popd >nul

if !rc!==0 (
    call :log Finishing KUTIL2: exit code 0
    call :log *** FINISHED [!taskName!] !DATE! !TIME!
) else (
    call :log Finishing KUTIL2 with error, exit code: !rc!
)
exit /b !rc!

rem ============================================================
rem  :link - создаёт симлинк в папке задачи на файл %1 из REPO
rem          (существующий файл/ссылку сначала удаляем;
rem           любой сбой = ошибка, задача прерывается)
rem ============================================================
:link
set "src=%repo%\%~1"
set "dst=%taskDir%\%~1"
if not exist "%src%" (
    call :log Ошибка: не найден %src%
    exit /b 1
)
del "%dst%" 2>nul
rmdir "%dst%" 2>nul
mklink "%dst%" "%src%" >nul
if errorlevel 1 (
    call :log Ошибка: симлинк %~1
    exit /b 1
)
exit /b 0

rem ============================================================
rem  :log - печатает строку и в консоль, и в общий лог
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
