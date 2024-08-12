import flet as ft

# 引数がTrueなら表、Falseなら裏のコインの相対パスを返す
def get_coin_pass(flag):
    if flag:
        return "images/coin_heads.png"
    else:
        return  "images/coin_tails.png"

def main(page: ft.Page):
    


ft.app(main)
