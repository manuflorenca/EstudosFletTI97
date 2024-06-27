from flet import Page,TextField,ElevatedButton,app,Text

#Page: é usado para criar e configurar a aparencia da pagina, na verdade do projeto
#é nela que trabalhamos as routes de novas telas.

#TextField: Campo de entrada de Texto, n qual entramos com dados, podemos configurar diferentes parametros de entrada

#ElevateButton: Que nada mais é que um botão

def main (pagina:Page):
    #Esse parametro vai ter tudo que uma page faz e tem
    pagina.title="Segunda Tela"
    #Usando o window_max quer dizer que você só pode abrir até essa medida
    pagina.window_max_width = 600
    pagina.window_max_height = 700

    #Essa é a largura real dela
    pagina.window_width = 600
    pagina.window_width = 700

    #Definindo o tamanho minimo
    pagina.window_min_width = 400
    pagina.window_max_height = 550

    #Posso carregar meu projeto no centro da tela
    pagina.window_center()

    pagina.bgcolor="#FFF0F5"

    #Colocando elementos na tela

    #vai permitir pegar dados da tela
    t_field_Nome=TextField(label="Digite o seu nome")
    t_field_salario=TextField(label="Salario",prefix_text="R$")

    #O text é o texto que aparece dentro do botão
    btn_calcular=ElevatedButton(text="Calcular")

    def calculando(e):
        #eu posso pegar o valor do text field usando o atribuito value

        txt_resposta.value=f"Nome: {t_field_Nome.value} tem o salario R$ {t_field_salario.value}"
        t_field_Nome.value=""
        t_field_Nome.update()
        t_field_salario.value=""
        t_field_salario.update()
        txt_resposta.update()

    #Todo evento é contruido dentro de uma função
    btn_calcular.on_click=calculando


    #O value vai ser o valor inicial do nosso texto
    txt_resposta=Text(value="Resposta",size=20)

    #Estou usando add para adicionar elementos na minha tela
    pagina.add(t_field_Nome)
    pagina.add(t_field_salario)
    pagina.add(btn_calcular)

    pagina.add(txt_resposta)


    pagina.update()

#Ela carrega o nosso projeto
#Responsavel de determinar se vai ser uma aplicação local ou web
app(target=main)

