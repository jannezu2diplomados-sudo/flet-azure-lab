import flet as ft


def main(page: ft.Page):
    page.title = "Mi primer sitio Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F4F7FB"
    page.padding = 32
    page.scroll = ft.ScrollMode.AUTO

    nombre = ft.TextField(label="Tu nombre", width=360)
    mensaje = ft.Text("Escribe tu nombre y pulsa Saludar.")
    contador = ft.Text("Visitas de esta sesión: 0")
    visitas = 0

    def saludar(e):
        nonlocal visitas
        texto = (nombre.value or "").strip()
        if not texto:
            nombre.error = "Escribe un nombre."
        else:
            nombre.error = None
            visitas += 1
            mensaje.value = f"¡Hola, {texto}! Mi sitio ya es web."
            contador.value = f"Visitas de esta sesión: {visitas}"
        page.update()

    page.add(
        ft.Text("LABORATORIO · FLET + AZURE", size=14,
                color="#2783DE"),
        ft.Text("Mi primer sitio web", size=32,
                weight=ft.FontWeight.BOLD),
        ft.Text("Creado con Python en Visual Studio Code."),
        ft.Container(height=12),
        nombre,
        ft.Button(content="Saludar", on_click=saludar),
        mensaje,
        contador,
        ft.Divider(),
        ft.Text("Versión 1 · Publicación estática en Azure"),
        ft.Text("Demostración: no guarda datos en una base de datos.",
                size=12),
    )


if __name__ == "__main__":
    ft.run(main)
