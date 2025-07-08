import flet as ft


class Tab(ft.Container):
    def __init__(self, label: str, icon_path: str):
        super().__init__()
        self.bgcolor = "#363636"
        self.content = ft.Row([ft.Text(label), ft.Icon(icon_path)], alignment=ft.MainAxisAlignment.CENTER)
        self.border = None
        self.width = 300
        self.height = 30
        self.border_radius = 12
        self.alignment = ft.alignment.center
        self.shadow = ft.BoxShadow(blur_radius=3,
                                   offset=ft.Offset(5, 3),
                                   color=ft.Colors.BLACK26)
