import flet as ft
import random
import time

# 引数がTrueなら表、Falseなら裏のコインの相対パスを返す
def get_coin_pass(flag):
    if flag:
        return "images/coin_heads.png"
    else:
        return  "images/coin_tails.png"

def main(page: ft.Page):

    # 中央揃え
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 表と裏が入れ替わる回数をランダムにして、表と裏どちらかをランダムに結果として表示する
    def toss_coin(e):
        # 入れ替わる回数
        swicth_time = random.randint(7, 15)
        for i in range(swicth_time):
            coin_image.data = not coin_image.data
            coin_image.src = get_coin_pass(coin_image.data)
            coin_image.update()
            time.sleep(0.7)

    # アプリの説明のためのテキストコントロール
    title = ft.Text(
        value="コイントスゲーム",
        size=40
    )
    text = ft.Text(
        value="ボタンを押すと、\nコインの表か裏どちらかが表示されます。",
        text_align=ft.TextAlign.CENTER
    )
    # コインを表示するImageコントロール
    coin_image = ft.Image(
        src=get_coin_pass(True),
        width=200,
        height=200,
        data=False  # このプロパティがTrueなら表、Falseなら裏とする。
    )
    # コイントスを実行するボタン
    toss_button = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Text(
                value="TOSS!!",
                size=25
            ),
            padding=ft.padding.symmetric(10, 5)
        ),
        on_click=toss_coin
    )

    page.add(title, text, coin_image, toss_button)

ft.app(main)
