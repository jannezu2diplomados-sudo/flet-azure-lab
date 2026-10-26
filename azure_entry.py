import flet as ft
from src.main import main

app = ft.run(main, export_asgi_app=True)
