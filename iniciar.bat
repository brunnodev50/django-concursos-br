@echo off
echo ====================================
echo   ConcursosBR - Iniciando servidor
echo ====================================

:: Verificar se .venv existe
if not exist ".venv\Scripts\python.exe" (
    echo [ERRO] Ambiente virtual nao encontrado.
    echo Execute: python -m venv .venv
    echo Depois:  .venv\Scripts\pip install -r requirements.txt
    pause
    exit /b 1
)

:: Criar admin se solicitado
if "%1"=="--criar-admin" (
    echo.
    echo Criando superusuario...
    .venv\Scripts\python.exe manage.py createsuperuser
)

:: Rodar migrations pendentes
echo.
echo Verificando migrations...
.venv\Scripts\python.exe manage.py migrate --run-syncdb

:: Coletar estáticos (opcional em dev)
:: .venv\Scripts\python.exe manage.py collectstatic --noinput

echo.
echo Servidor iniciando em http://localhost:8000
echo Admin em: http://localhost:8000/admin/
echo Pressione Ctrl+C para parar.
echo.
.venv\Scripts\python.exe manage.py runserver
pause
