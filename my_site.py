import flet as ft

def main(page: ft.Page):
    page.title = "Controle de validade digital"
    produtos = []
    produtos_list_view = ft.ListView()
    #partes visuais
    desc = ft.TextField(label="Descrição")
    ean = ft.TextField(label="EAN do Produto")
    quantidade = ft.TextField(label="Quantidade")
    data = ft.DatePicker(datetime.datetime.now())
    #o botão salvar fica dentro do pageButton
    salvar = ft.TextButton(icon=ft.icons.SAVE, text="Salvar", on_click="")
    page.bottom_appbar = ft.BottomAppBar(bgcolor=ft.colors.TRANSPARENT, content=ft.Row(controls=[salvar]))
    add_button = ft.FloatingActionButton("Adicionar", on_click="" ,width=100)
    cleanAllButton = ft.FloatingActionButton("Limpar Lista", on_click="", width=100)
    date_button = ft.ElevatedButton("Validade do Produto", icon=ft.icons.CALENDAR_MONTH, on_click=lambda _: data.pick_date())
    list_container = ft.Container(content=produtos_list_view, height=300, expand=True)

    #adiciona os itens a tela
    page.overlay.append(data)
    page.add(ft.Column([desc, ean, quantidade, date_button]))
    page.add(ft.Row([add_button, cleanAllButton]))
    page.add(list_container)
ft.app(main)
    
