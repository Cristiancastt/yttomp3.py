import flet as ft
from flet_core import BorderSide, RoundedRectangleBorder, MainAxisAlignment, margin, Theme

def main(page: ft.Page):
    page.title = "Youtube Converter"
    page.padding = 50
    page.fonts = {
        "Poppins": "./Poppins-SemiBold.ttf"
    }
    page.theme = Theme(font_family="Poppins")
    page.window_resizable=False
    page.window_title_bar_buttons_hidden=False
    page.window_width=600
    page.window_height=280

    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        swModo.label = (
            "Tema claro" if page.theme_mode == ft.ThemeMode.LIGHT else "Tema Oscuro"
        )
        page.update()
    page.theme_mode = ft.ThemeMode.SYSTEM
    swModo = ft.Switch(
        label="Tema Sistema",
        on_change=theme_changed,
    )

    ctnModo = ft.Container(
        content=swModo,
        alignment=ft.alignment.top_left,
        margin=margin.all(0),
    )

    btnIniciar = ft.FilledButton(
        text="Selecciona Ruta y Convierte",
        width=400,
        height=50,
        style=ft.ButtonStyle(
            side={
                ft.MaterialState.HOVERED: BorderSide(2, ft.colors.BLUE),
            },
            shape={
                ft.MaterialState.HOVERED: RoundedRectangleBorder(radius=50),
                ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=1000,
            bgcolor=ft.colors.ERROR_CONTAINER
        ),
    )
    ctnIniciar = ft.Container(
        content=btnIniciar,
        padding=5,
        alignment=ft.alignment.top_center,
    )

    lblUrl=ft.TextField(
        label="Pega Enlace Youtube",
        icon=ft.icons.LINK,
    )

    page.add(lblUrl, ctnIniciar)
    page.update()

ft.app(target=main)