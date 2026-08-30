import os
import re
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

class WhatsAppAutomationApp(App):
    def build(self):
        self.title = "WhatsApp Assistant"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(
            text="[b]تطبيق الواتساب الذكي[/b]", 
            markup=True, 
            font_size='22sp'
        ))
        
        self.phone_input = TextInput(
            hint_text="أدخل رقم الهاتف مع الرمز الدولي...", 
            input_filter='int',
            multiline=False,
            size_hint_y=None,
            height='50dp'
        )
        layout.add_widget(self.phone_input)
        
        btn_manual = Button(
            text="فتح الواتساب يدويًا", 
            size_hint_y=None, 
            height='50dp',
            background_color=(0.1, 0.7, 0.3, 1)
        )
        btn_manual.bind(on_press=self.open_manual_whatsapp)
        layout.add_widget(btn_manual)
        
        self.status_label = Label(
            text="الحالة: التطبيق جاهز للعمل", 
            font_size='14sp'
        )
        layout.add_widget(self.status_label)
        
        if platform == 'android':
            self.request_android_permissions()
            
        return layout

    def request_android_permissions(self):
        from android.permissions import request_permissions, Permission
        request_permissions([
            Permission.INTERNET,
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE
        ])

    def open_manual_whatsapp(self, instance):
        phone_number = self.phone_input.text.strip()
        if phone_number:
            self.status_label.text = f"جاري فتح المحادثة للرقم: {phone_number}"
            webbrowser.open(f"https://wa.me/{phone_number}")
        else:
            self.status_label.text = "يرجى كتابة رقم الهاتف أولاً."

if __name__ == "__main__":
    WhatsAppAutomationApp().run()
