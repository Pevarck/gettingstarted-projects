import flet as ft
import datetime

def main(page):
    title = ft.Text("Travazap")
    
    
    def message_sent_tunnel(message):
        text = ft.Text(message)
        chat.controls.append(text)
        page.update()
        
        
    page.pubsub.subscribe(message_sent_tunnel)
    
    
    def message_sent(event):
        username_box = username_id.value
        message_box = send_message_field.value
        message = f"{username_box}:{message_box}"
        page.pubsub.send_all(message)
        send_message_field.value = ""
        page.update()
        
    
    send_message_field = ft.TextField(label="type your message", on_submit=message_sent)
    message_buttom = ft.ElevatedButton(text="Send", on_click=message_sent)
    
    messagepage_layout = ft.Row([send_message_field, message_buttom])
    
    
    chat = ft.Column()
    
    
    def join_chat(event):
        popup.open = False
        page.remove(title)
        page.remove(buttom)
        page.add(chat)
        page.add(messagepage_layout)
        username_box = username_id.value
        message_txt = f"{username_box} joined the chat"
        page.pubsub.send_all(message_txt)
        page.update()
        
    
    popup_title = ft.Text("Welcome to Travazap")
    username_id = ft.TextField(label="Enter your nickname")
    buttom_join = ft.ElevatedButton("Join Chat", on_click=join_chat)
    popup = ft.AlertDialog(title=popup_title, content=username_id, actions=[buttom_join])
    
 
    def open_popup(event):
        page.dialog = popup
        popup.open = True
        page.update()
    
    
    buttom = ft.ElevatedButton("Start Chat", on_click=open_popup)
    
    
    page.add(title)
    page.add(buttom)
       
   
ft.app(main, view=ft.WEB_BROWSER, port=8000)