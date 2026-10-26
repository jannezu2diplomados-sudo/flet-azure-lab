# Laboratorio Flet + GitHub + Azure for Students

Este ZIP contiene el código fuente del laboratorio. No incluye credenciales,
una suscripción ni un despliegue hecho. Consulta el Word para los pasos completos.

## Windows / PowerShell

1. Extraer la carpeta y abrirla en Visual Studio Code.
2. Instalar Python 3.13, Git y la extensión Python de Microsoft.
3. Crear y activar el entorno:

    py -3.13 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install "flet[cli,web]==1.0.5"

Si PowerShell bloquea la activación, usar una terminal CMD y ejecutar:

    .venv\Scripts\activate.bat

No cambiar la política global de PowerShell.

## Desarrollo

Desde la raíz del proyecto con el entorno activo:

    flet run --web src/main.py

Detener con Ctrl+C.

## Crear la carpeta publicable

    flet publish src/main.py --distpath ../dist --python-version 3.13
    python -m http.server 8000 --directory dist

Abrir http://localhost:8000 y detener con Ctrl+C al terminar.
En esta versión --distpath se resuelve desde src/; ../dist genera dist/ en la raíz.
No abrir index.html con file://. La primera carga necesita internet para el runtime.

## GitHub y Azure

- Subir src/, .gitignore y dist/ completa. README.md puede subirse también.
- No subir .venv/, .env, credenciales ni datos personales.
- Crear Azure Static Web App con la suscripción Students activa y el plan Free.
- Conectar el repositorio y la rama main.
- En el workflow generado por Azure, conservar el secreto de despliegue y usar:

    app_location: "dist"
    api_location: ""
    output_location: ""
    skip_app_build: true

Es un fragmento del bloque with, no un workflow completo.
No inventar ni reemplazar el nombre del secreto creado por Azure.
Después de que Azure cree el workflow, ejecutar git pull --rebase origin main
con el árbol de trabajo limpio antes del próximo push.

## Actualizaciones

Editar src/main.py, regenerar dist/, probar por HTTP, confirmar ambos cambios
y hacer push. Esperar la ejecución verde en GitHub Actions y comprobar la URL pública.
El contador es por sesión y se reinicia al recargar. No hay backend ni base de datos.

Fuentes:
https://flet.dev/docs/publish/web/static-website
https://flet.dev/docs/cli/flet-publish
https://learn.microsoft.com/en-us/azure/static-web-apps/get-started-portal
https://learn.microsoft.com/en-us/azure/static-web-apps/build-configuration
