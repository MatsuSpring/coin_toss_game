import flet as ft
import random
import time

# 引数がTrueなら表、Falseなら裏のコインの相対パスを返す
def get_coin_pass(flag):
    if flag:
        return r"\coin_heads.png"
    else:
        return r"\coin_tails.png"

def main(page: ft.Page):

    # 中央揃え
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 表と裏が入れ替わる回数をランダムにして、表と裏どちらかをランダムに結果として表示する
    def toss_coin(e):
        # toss_buttonを無効化
        toss_button.disabled = True
        toss_button.update()
        result.value=""
        result.update()
        # 入れ替わる回数
        swicth_time = random.randint(10, 11)
        for i in range(swicth_time):
            coin_image.data = not coin_image.data
            coin_image.src = get_coin_pass(coin_image.data)
            coin_image.update()
            time.sleep(0.3)
        # resultを適切に表示
        if coin_image.data:
            result.value = "結果は表です！"
        else:
            result.value = "結果は裏です！"
        result.update()
        # toss_buttonを有効化
        toss_button.disabled = False
        toss_button.update()

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
        src=get_coin_pass(True),  # はじめは表
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

    # トス結果を表示するコントロール
    result = ft.Text(
        value="",
        size=15
    )

    page.add(title, text, coin_image, toss_button, result)

ft.app(main)
