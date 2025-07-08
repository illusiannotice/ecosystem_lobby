import flet as ft
from typing import Optional


class Link(ft.Container):
    def __init__(self, path: str, ident: Optional[str]):
        super().__init__()
        self.height = 40
        self.width = 40
        self.id = ident
        self.content = ft.Image()
class TaskBar(ft.Container):

    def __init__(self, cont: list[Link]):
        super().__init__()
        self.bgcolor = "#363636"
        self.content = ft.Row(cont, alignment=ft.MainAxisAlignment.CENTER, spacing=10)
        self.margin = 0
        self.padding = 0
        self.width = len(cont)*50 - 10 + 24
        self.height = 50
        self.border_radius = 10
        self.alignment = ft.alignment.center
        self.shadow = ft.BoxShadow(blur_radius=3,
                                   offset=ft.Offset(5, 3),
                                   color=ft.Colors.BLACK26)




