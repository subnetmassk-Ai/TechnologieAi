import sys
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

class AutoDialerApp(App):
    def build(self):
        # طلب أذونات الأندرويد فور فتح التطبيق لتجنب الانهيار (Crash)
        if platform == 'android':
            self.request_android_permissions()

        # إنشاء واجهة المستخدم الأساسية
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.status_label = Label(
            text="مرحباً بك في WhatsApp Auto Dialer\nالتطبيق يعمل بنجاح!",
            font_size='18sp',
            halign='center'
        )
        layout.add_widget(self.status_label)

        btn = Button(
            text="ابدأ تسجيل الرقم",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.7, 0.3, 1)
        )
        btn.bind(on_press=self.on_start_click)
        layout.add_widget(btn)

        return layout

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
        self.status_label.text = "جاري الاستماع للرقم..."
        # هنا يتم استدعاء وظيفة التعرف على الصوت والاتصال

if __name__ == '__main__':
    AutoDialerApp().run()
