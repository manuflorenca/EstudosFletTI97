from flet import *

def main(page:Page):

    page.title = "Trabalhando com Container"
    container1 = Container(
        bgcolor=colors.PINK_500,
        content=Text("Zeca-urubu",size=23,weight=FontWeight.W_600),
        width=300,
        height=200,
        padding=padding.only(top=100,left=90),
        border=border.all(5,color=colors.BLACK)
        )

    page.add(container1)
    page.update()

if __name__ == '__main__':
    app(target=main)