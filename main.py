import sys
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

class AutoDialerApp(App):
    def build(self):
        if platform == 'android':
            self.request_android_permissions()

        self.current_lang = 'en'  # اللغة الافتراضية

        # القواميس للغتين
        self.texts = {
            'en': {
                'title': "Welcome to WhatsApp Auto Dialer",
                'btn_start': "Start Recording",
                'btn_lang': "تغيير للغة العربية",
                'listening': "Listening for number..."
            },
            'ar': {
                'title': "مرحباً بك في تطبيق الاتصال التلقائي",
                'btn_start': "ابدأ تسجيل الرقم",
                'btn_lang': "Switch to English",
                'listening': "جاري الاستماع للرقم..."
            }
        }

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # تحديد الخط العربي إذا كان الملف موجوداً
        font_path = 'arabic.ttf' if os.path.exists('arabic.ttf') else None

        self.status_label = Label(
            text=self.texts['en']['title'],
            font_name=font_path,
            font_size='18sp',
            halign='center'
        )
        layout.add_widget(self.status_label)

        # زر بدء التسجيل
        self.btn_start = Button(
            text=self.texts['en']['btn_start'],
            font_name=font_path,
            size_hint=(1, 0.2),
            background_color=(0.2, 0.7, 0.3, 1)
        )
        self.btn_start.bind(on_press=self.on_start_click)
        layout.add_widget(self.btn_start)

        # زر التبديل بين اللغات
        self.btn_lang = Button(
            text=self.texts['en']['btn_lang'],
            font_name=font_path,
            size_hint=(1, 0.15),
            background_color=(0.2, 0.4, 0.8, 1)
        )
        self.btn_lang.bind(on_press=self.toggle_language)
        layout.add_widget(self.btn_lang)

        return layout

    def toggle_language(self, instance):
        # التبديل بين العربية والإنجليزية
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
