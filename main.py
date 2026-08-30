import os
import re
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import speech_recognition as sr

class WhatsAppAutomationApp(App):
    def build(self):
        self.title = "WhatsApp Automation & Voice Assistant"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Header
        layout.add_widget(Label(
            text="[b]تطبيق الواتساب الذكي[/b]", 
            markup=True, 
            font_size='22sp'
        ))
        
        # Section 1: Manual Input
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
        
        # Section 2: Voice Action
        btn_voice = Button(
            text="🎤 معالجة الصوت واستخراج الرقم", 
            size_hint_y=None, 
            height='50dp',
            background_color=(0.2, 0.5, 0.9, 1)
        )
        btn_voice.bind(on_press=self.start_voice_processing)
        layout.add_widget(btn_voice)
        
        # Status Label
        self.status_label = Label(
            text="الحالة: التطبيق جاهز للعمل", 
            font_size='14sp'
        )
        layout.add_widget(self.status_label)
        
        return layout

    def open_manual_whatsapp(self, instance):
        phone_number = self.phone_input.text.strip()
        if phone_number:
            self.status_label.text = f"جاري فتح المحادثة للرقم: {phone_number}"
            webbrowser.open(f"https://wa.me/{phone_number}")
        else:
            self.status_label.text = "يرجى كتابة رقم الهاتف أولاً."

    def start_voice_processing(self, instance):
        self.status_label.text = "جاري قراءة ملف الصوت..."
        Clock.schedule_once(self.process_audio, 0.5)

    def process_audio(self, dt):
        # مسار الملف الصوتي الذي تم إعداده
        audio_path = "recorded_audio.wav"
        
        if not os.path.exists(audio_path):
            self.status_label.text = "خطأ: لم يتم العثور على ملف الصوت recorded_audio.wav"
            return
            
        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(audio_path) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data, language="ar-SA")
                
                # استخراج الأرقام فقط
                extracted_numbers = "".join(re.findall(r'\d+', text))
                
                if extracted_numbers:
                    self.status_label.text = f"تم العثور على الرقم: {extracted_numbers}"
                    webbrowser.open(f"https://wa.me/{extracted_numbers}")
                else:
                    self.status_label.text = "لم يتم العثور على أرقام داخل الصوت."
        except Exception as err:
            self.status_label.text = f"خطأ في معالجة الصوت: {str(err)}"

if __name__ == "__main__":
    WhatsAppAutomationApp().run()
