# •Criar uma aplicação que vai pegar o nome e o endereço da pessoa, pegue a rua, numero, bairro, cep separados,
# e vai mostrar na tela em dois elementos Text:
# •Nome: Carlos
# •Endereço: Rua srrsrrs Numero srsr CEP:00000

from flet import Page,TextField,ElevatedButton,app,Text

def main (pagina:Page):
    pagina.title="Cadastrando endereço"

    pagina.window_max_width = 600
    pagina.window_max_height = 700

    pagina.window_width = 600
    pagina.window_height = 700

    pagina.window_min_width = 400
    pagina.window_max_height = 550

    pagina.window_center()

    pagina.bgcolor="#E6E6FA"

    #Botoes

    t_field_Nome=TextField(label="Digite o seu nome:")
    t_field_Rua=TextField(label="Digite a sua rua:")
    t_field_Numero=TextField(label="Digite o numero da tua casa:")
    t_field_Cep=TextField(label="Digite o seu cep:")

    btn_endereco=ElevatedButton(text="Mostre o endereço")

    def endereco(e):

        txt_resposta_nome.value=f" Nome:{t_field_Nome.value}"
        txt_resposta_nome.update()
        t_field_Nome.value=""
        t_field_Nome.update()

        txt_resposta_endereco.value=f" Rua: {t_field_Rua.value}, Numero: {t_field_Numero.value}, Cep: {t_field_Cep.value} "
        txt_resposta_endereco.update()
        t_field_Rua.value=""
        t_field_Rua.update()

        t_field_Numero.value=""
        t_field_Rua.update()

        t_field_Cep.value=""
        t_field_Cep.update()

    btn_endereco.on_click=endereco

    txt_resposta_nome=Text(value="Nome:",size=20)
    txt_resposta_endereco=Text(value="Endereço:",size=20)

    pagina.add(t_field_Nome)
    pagina.add(t_field_Rua)
    pagina.add(t_field_Numero)
    pagina.add(t_field_Cep)
    pagina.add(btn_endereco)

    pagina.add(txt_resposta_nome)
    pagina.add(txt_resposta_endereco)



    pagina.update()


app(target=main)