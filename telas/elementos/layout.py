from flet import *
def main(page:Page):

    page.title = "Esudando Cards"
    produto = Card(

        content = Container(

            content = Column(

                controls = [

                    Row(controls=[Image(src="lancheee.png")],alignment=MainAxisAlignment.CENTER),
                    Row(controls=[Text("Lanche Vegano",color=colors.RED,font_family="")],alignment=MainAxisAlignment.CENTER),
                    Row(controls=[Text("Lanche com proteinas veganas")],alignment=MainAxisAlignment.CENTER),
                    Row(controls=[

                        Icon(cupertino_icons.HEART, color=colors.RED),
                        Icon(cupertino_icons.MONEY_DOLLAR, color=colors.GREEN)

                    ],alignment=MainAxisAlignment.CENTER)
                ]
            )

        )

    )

    page.add(produto)

if __name__ == '__main__':
    app(main)