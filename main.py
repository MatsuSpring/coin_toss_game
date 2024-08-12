import flet as ft

# 引数がTrueなら表、Falseなら裏のコインの相対パスを返す
def get_coin_pass(flag):
    if flag:
        return "images/coin_heads.png"
    else:
        return  "images/coin_tails.png"

def main(page: ft.Page):
    # 中央揃え
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Trueなら表、Falseなら裏を表すものとする。
    coin_flag = True
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
        src=get_coin_pass(coin_flag),
        width=200,
        height=200,
    )
    # コイントスを実行するボタン
    toss_button = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Text(
                value="TOSS!!",
                size=25
            ),
            padding=ft.padding.symmetric(10, 5)
        )
    )

    page.add(title, text, coin_image, toss_button)

ft.app(main)
