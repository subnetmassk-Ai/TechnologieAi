import re
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

# استدعاء أدوات الأندرويد الأصلية للتعرف على الصوت
if platform == 'android':
    from jnius import autoclass, cast
    from android.permissions import request_permissions, Permission
    
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    RecognizerIntent = autoclass('android.speech.RecognizerIntent')

class WhatsAppAutomationApp(App):
    def build(self):
        self.title = "WhatsApp Voice Assistant"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(
            text="[b]الساعد الصوتي للواتساب[/b]", 
            markup=True, 
            font_size='22sp'
        ))
        
        self.phone_input = TextInput(
            hint_text="الرقم المستخرج يظهر هنا...", 
            multiline=False,
            size_hint_y=None,
            height='50dp'
        )
        layout.add_widget(self.phone_input)
        
        btn_voice = Button(
            text="🎤 اضغط للتحدث (تحويل اصوت لنص)", 
            size_hint_y=None, 
            height='55dp',
            background_color=(0.2, 0.6, 1, 1)
        )
        btn_voice.bind(on_press=self.start_voice_input)
        layout.add_widget(btn_voice)
        
        btn_manual = Button(
            text="فتح الواتساب بالرقم الحالي", 
            size_hint_y=None, 
            height='50dp',
            background_color=(0.1, 0.7, 0.3, 1)
        )
        btn_manual.bind(on_press=self.open_whatsapp)
        layout.add_widget(btn_manual)
        
        self.status_label = Label(
            text="الحالة: التطبيق جاهز", 
            font_size='14sp'
        )
        layout.add_widget(self.status_label)
        
        if platform == 'android':
            request_permissions([Permission.RECORD_AUDIO, Permission.INTERNET])
            
        return layout

    def start_voice_input(self, instance):
        if platform == 'android':
            try:
                # فتح الميكروفون الأصلي لجوجل المدمج بالنظام
                intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "ar-SA")
                
                current_activity = cast('android.app.Activity', PythonActivity.mActivity)
                current_activity.startActivityForResult(intent, 100)
                self.status_label.text = "جاري الاستماع..."
            except Exception as err:
                self.status_label.text = f"خطأ الميكروفون: {str(err)}"
        else:
            self.status_label.text = "ميزة الصوت تعمل فقط عند تثبيت الـ APK على الهاتف."

    def open_whatsapp(self, instance):
        phone_number = self.phone_input.text.strip()
        extracted_numbers = "".join(re.findall(r'\d+', phone_number))
        
        if extracted_numbers:
            self.status_label.text = f"جاري فتح المحادثة: {extracted_numbers}"
            webbrowser.open(f"https://wa.me/{extracted_numbers}")
        else:
            self.status_label.text = "يرجى إدخال أو نطق رقم هاتف صحيح."

if __name__ == "__main__":
    WhatsAppAutomationApp().run()
