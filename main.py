import sys
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

# مكتبات معالجة النص العربي
try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    HAS_ARABIC_SUPPORT = True
except ImportError:
    HAS_ARABIC_SUPPORT = False

def reshape_ar(text):
    if HAS_ARABIC_SUPPORT:
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)
    return text

class AutoDialerApp(App):
    def build(self):
        if platform == 'android':
            self.request_android_permissions()

        self.current_lang = 'en'
        self.font_path = 'font.ttf' if os.path.exists('font.ttf') else None

        self.texts = {
            'en': {
                'title': "Welcome to WhatsApp Auto Dialer\nApp is working successfully!",
                'btn_start': "Start Recording",
                'btn_lang': "اللغة العربية",
                'listening': "Listening for number..."
            },
            'ar': {
                'title': reshape_ar("مرحباً بك في تطبيق الاتصال التلقائي\nالتطبيق يعمل بنجاح!"),
                'btn_start': reshape_ar("ابدأ تسجيل الرقم"),
                'btn_lang': "English",
                'listening': reshape_ar("جاري الاستماع للرقم...")
            }
        }

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.status_label = Label(
            text=self.texts['en']['title'],
            font_name=self.font_path,
            font_size='18sp',
            halign='center'
        )
        layout.add_widget(self.status_label)

        self.btn_start = Button(
            text=self.texts['en']['btn_start'],
            font_name=self.font_path,
            size_hint=(1, 0.2),
            background_color=(0.2, 0.7, 0.3, 1)
        )
        self.btn_start.bind(on_press=self.on_start_click)
        layout.add_widget(self.btn_start)

        self.btn_lang = Button(
            text=self.texts['en']['btn_lang'],
            font_name=self.font_path,
            size_hint=(1, 0.15),
            background_color=(0.2, 0.4, 0.8, 1)
        )
        self.btn_lang.bind(on_press=self.toggle_language)
        layout.add_widget(self.btn_lang)

        return layout

    def toggle_language(self, instance):
        self.current_lang = 'ar' if self.current_lang == 'en' else 'en'
        lang = self.current_lang

        self.status_label.text = self.texts[lang]['title']
        self.btn_start.text = self.texts[lang]['btn_start']
        self.btn_lang.text = self.texts[lang]['btn_lang']

    def request_android_permissions(self):
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.RECORD_AUDIO,
                Permission.CALL_PHONE,
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE
            ])
        except Exception as e:
            print(f"Permissions error: {e}")

    def on_start_click(self, instance):
        self.status_label.text = self.texts[self.current_lang]['listening']

if __name__ == '__main__':
    AutoDialerApp().run()
