import flet as ft



def main(page: ft.Page):
    page.title="meu app flet"
    def link(e):
        page.launch_url("https://www.youtube.com/")
    botao = ft.TextButton("link", on_click=link)
    page.add(ft.Text("Meu aplicativo"), botao)
ft.app(main)
