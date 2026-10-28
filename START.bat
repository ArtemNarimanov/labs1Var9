@echo off
setlocal enabledelayedexpansion
chcp 1251 >nul

rem ============================================================
rem  START.bat - очистка задач и запуск KORSAR
rem
rem  Для каждого подкаталога task\* последовательно:
rem    0. проверка возобновления: если в логе есть маркер
rem       "*** FINISHED [имя_задачи]" - задача уже рассчитана
rem       и пропускается полностью (без удаления файлов,
rem       симлинков и запуска exe);
rem    1. удаляет старые korlis, korres, kutlis и result*.dat;
rem    2. создаёт симлинки korsar.exe, nwsp_dat из REPO;
rem    3. запускает korsar.exe (симлинк в папке задачи) с выводом
rem       в лог;
rem    4. ведёт единый лог: result\start.log (ANSI/CP1251),
rem       все задачи дописываются в порядке прогона.
rem
rem  Опция: START.bat --force - игнорировать маркер возобновления
rem          и пересчитать все задачи.
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

set "sharedLog=%logDir%\start.log"

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
        echo Задача !taskName! уже рассчитана, пропускаем
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
call :log Starting KORSAR !DATE! !TIME!

rem --- удаляем старые файлы (отсутствие файла - не ошибка)
del "%taskDir%\korlis" 2>nul
del "%taskDir%\korres" 2>nul
del "%taskDir%\kutlis" 2>nul
del "%taskDir%\result*.dat" 2>nul

rem --- создаём симлинки из REPO (существующий файл/ссылку удаляем)
call :link "korsar.exe"
if errorlevel 1 exit /b 1
call :link "nwsp_dat"
if errorlevel 1 exit /b 1

rem --- запускаем KORSAR через симлинк в папке задачи, вывод в лог
pushd "%taskDir%" >nul
korsar.exe >> "!logFile!" 2>&1
set "rc=!errorlevel!"
popd >nul

if !rc!==0 (
    call :log Finishing KORSAR: exit code 0
    call :log *** FINISHED [!taskName!] !DATE! !TIME!
) else (
    call :log Finishing KORSAR with error, exit code: !rc!
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
