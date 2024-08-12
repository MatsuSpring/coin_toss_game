import flet as ft

# 引数がTrueなら表、Falseなら裏のコインの相対パスを返す
def get_coin_pass(flag):
    if flag:
        return "images/coin_heads.png"
    else:
        return  "images/coin_tails.png"

def main(page: ft.Page):
    # Trueなら表、Falseなら裏を表すものとする。
    coin_flag = True
    coin_image = ft.Image(
        src=get_coin_pass(coin_flag),
        width=200,
        height=200,
    )

    page.add(coin_image)

ft.app(main)
