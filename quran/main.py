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
    
    
    pages = ft.Row( 
        scroll='auto',
        spacing=0,rtl=True,
        auto_scroll= False
    )
    global currentPage 
    currentPage = 1

    for i in range(604):
        unpacked_string = "".join(map(str, getAyahForPage(f"{i+1}")))
        pages.controls.append(
            ft.Container(
            ft.Column(controls=[
                
                ft.Row(controls=[ft.Text(unpacked_string,rtl=True,size=28,text_align='CENTER')],wrap=True,height=page.height,width=page.width,vertical_alignment="CENTER")
            ],width=page.width-20,horizontal_alignment='CENTER'),key=f"{i+1}")
            )

    def on_scroll(event):
        print(f"Event type: {event.event_type}")
        if event.event_type == "user":
            print(f"Scroll direction: {event.direction}")
        if event.event_type in ["start", "update", "end", "over"]:
            print(f"Scroll position: {event.pixels}")
            print(f"Min scroll extent: {event.min_scroll_extent}")
            print(f"Max scroll extent: {event.max_scroll_extent}")
            print(f"Viewport dimension: {event.viewport_dimension}")
        if event.event_type == "update":
            print(f"Scroll delta: {event.scroll_delta}")
            # slidePage(event.scroll_delta)
        if event.event_type == "over":
            print(f"Overscroll: {event.overscroll}")
            print(f"Velocity: {event.velocity}")

        
    def slidePage(direction):  
        global currentPage
        if direction > 0:
            currentPage += 1
            
        else:
            currentPage -= 1
        key = f"{currentPage}"
        print(key)
        pages.scroll_to(key=key, duration=1)
        print(currentPage)
    pages.on_scroll = on_scroll


    page.add(pages)
    """ page.add(ft.Text(page.window_width))
    page.add(ft.Text(page.width))
    page.add(ft.Text(page.height))
 """


    

ft.app(target=main,assets_dir="assets")
