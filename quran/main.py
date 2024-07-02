import flet as ft

from test import getAyahForPage


def main(page: ft.Page):
    page.horizontal_alignment = page.vertical_alignment = "center"
    page.bgcolor = '#fefae0'
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    page.fonts={
        "Mcs Swer Al Quran3": "/fonts/Mcs-Swer-Al_Quran-3.ttf",
    }
    page.appbar = ft.AppBar(
        title=ft.Text("Quran App"),
        center_title=True,
        bgcolor=ft.colors.GREEN_300,
        automatically_imply_leading=False,
    )
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
            ]
        ),
    )
    
    unpacked_string = "".join(map(str, getAyahForPage("1")))
    unpacked_string2 = "".join(map(str, getAyahForPage("2")))
    pages = ft.Row( 
        scroll='auto',
        spacing=0,rtl=True,
        auto_scroll= False
    ).scroll_to(200)
    
    pages.controls.append(
        ft.Container(
        ft.Column(controls=[
            ft.Text("الفاتحة",rtl=True,size=35,text_align='CENTER'),
            ft.Row(controls=[ft.Text(unpacked_string,rtl=True,size=28,text_align='CENTER')],wrap=True,height=page.height,width=page.width,vertical_alignment="CENTER")
    ],width=page.width-20,horizontal_alignment='CENTER'),)
    )
    pages.controls.append(
        ft.Column(controls=[
            ft.Text("البقرة",rtl=True,size=24,text_align='CENTER'),
            ft.Row(controls=[ft.Text(unpacked_string2,rtl=True,size=24,)],wrap=True,height=page.height)
        ],width=page.width-20,horizontal_alignment='CENTER')
    )

    

    page.add(pages)
    """ page.add(ft.Text(page.window_width))
    page.add(ft.Text(page.width))
    page.add(ft.Text(page.height))
 """


    

ft.app(target=main,assets_dir="assets")
