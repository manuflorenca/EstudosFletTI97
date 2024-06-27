# •Criar uma aplicação que a pessoa vai digitar o salário e
# vc vai calcular quanto é 10% desse salario e mostrar a resposta na tela

from flet import Page,TextField,ElevatedButton,app,Text
import math

def main (pagina:Page):
    pagina.title="Calcule seu salário"

    pagina.window_max_width = 600
    pagina.window_max_height = 700

    pagina.window_width = 600
    pagina.window_height = 700

    pagina.window_min_width = 400
    pagina.window_max_height = 550

    pagina.window_center()

    pagina.bgcolor="#F0FFF0"

    t_field_Nome=TextField(label="Digite o seu nome")
    t_field_salario=TextField(label="Digite seu Salario")

    btn_calcular=ElevatedButton(text="Calcular 10%")

    def calculando_10(e):
        perc=float(t_field_salario.value)*0.1
        txt_resposta.value=f"Nome: {t_field_Nome.value} tem 10%  salario R$ {perc}"
        t_field_Nome.value=""
        t_field_Nome.update()
        t_field_salario.value=""
        t_field_salario.update()
        txt_resposta.update()


    btn_calcular.on_click=calculando_10


    #Todo evento é contruido dentro de uma função
    btn_calcular.on_click=calculando_10


    #O value vai ser o valor inicial do nosso texto
    txt_resposta=Text(value="Resposta",size=20)

    #Estou usando add para adicionar elementos na minha tela
    pagina.add(t_field_Nome)
    pagina.add(t_field_salario)
    pagina.add(btn_calcular)

    pagina.add(txt_resposta)











    pagina.update()

app(target=main)