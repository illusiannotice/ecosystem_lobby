import flet as ft
from components import tab as tb
from components.taskbar import TaskBar, Link
def main(page: ft.Page):
    page.window.height = 1080
    page.window.width = 1920
    page.padding = 0
    page.window.full_screen = True
    taskbar = TaskBar([Link("", "pycharm"), Link("", "pycharm"), Link("", "pycharm"),
                       Link("", "pycharm"), Link("", "pycharm"), Link("", "pycharm")])
    MAIN_PAGE = ft.Column([ft.Container(ft.Row([tb.Tab(label="test", icon_path=""), tb.Tab(label="test", icon_path=""),
                                                tb.Tab(label="test", icon_path=""), tb.Tab(label="test", icon_path=""),
                                                tb.Tab(label="test", icon_path=""), tb.Tab(label="test", icon_path="")],
                                               alignment=ft.MainAxisAlignment.CENTER),
                                        width=page.window.width, height=page.window.height//2,
                                        alignment=ft.alignment.top_center,
                                        bgcolor=ft.Colors.YELLOW,
                                        margin=0,
                                        padding=10),
                           ft.Container(ft.Row([ft.Container(content=ft.Container(),
                                                             bgcolor=ft.Colors.BLUE,
                                                             width=page.window.width // 2,
                                                             height=page.window.height // 2,
                                                             margin=0),
                                                ft.Container(taskbar,
                                                             width=page.window.width // 2,
                                                             height=page.window.height // 2,
                                                             bgcolor=ft.Colors.ORANGE,
                                                             alignment=ft.alignment.bottom_center,
                                                             margin=0,
                                                             padding=50)],
                                               spacing=0))],
                          spacing=0)
    page.add(MAIN_PAGE)


if __name__ == "__main__":
    ft.app(main)
