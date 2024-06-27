import flet as ft

#Layout da pagina
def main(page:ft.Page):
    page.title="Primeira pagina"
    tf_nome=ft.TextField(label="Digite o seu nome")
    btn_cadastrar=ft.ElevatedButton(text="Cadastrar")

    page.add(tf_nome)
    page.add(btn_cadastrar)

    #Criando o evento
    def enviarNome(e):
        print(tf_nome.value)

    btn_cadastrar.on_click=enviarNome

    #Toda vez que eu alterar a minha pagina eu devo dar um update
    page.update()

if __name__ == '__main__':
    ft.app(main)