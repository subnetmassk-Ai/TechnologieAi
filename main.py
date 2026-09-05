import re

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


ARABIC_DIGITS = str.maketrans(
    "٠١٢٣٤٥٦٧٨٩",
    "0123456789"
)


class MarKossApp(App):

    VOICE_REQUEST = 100

    def build(self):
        self.lang = "ar"
        self.contacts = []

        root = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        self.lang_button = Button(
            text="English",
            size_hint_y=None,
            height=dp(50)
        )
        self.lang_button.bind(on_press=self.toggle_language)
        root.add_widget(self.lang_button)

        self.title_label = Label(
            text="MarKoss",
            font_size=dp(30),
            size_hint_y=None,
            height=dp(55)
        )
        root.add_widget(self.title_label)

        self.subtitle = Label(
            text="مساعد البحث والتواصل",
            font_size=dp(18),
            size_hint_y=None,
            height=dp(45)
        )
        root.add_widget(self.subtitle)

        self.input_box = TextInput(
            hint_text="أدخل رقم الهاتف أو اسم جهة الاتصال",
            multiline=False,
            font_size=dp(20),
            size_hint_y=None,
            height=dp(55),
            halign="right"
        )
        root.add_widget(self.input_box)

        self.voice_button = Button(
            text="🎤 البحث الصوتي",
            size_hint_y=None,
            height=dp(55)
        )
        self.voice_button.bind(on_press=self.voice_search)
        root.add_widget(self.voice_button)

        self.manual_button = Button(
            text="🔎 بحث يدوي",
            size_hint_y=None,
            height=dp(55)
        )
        self.manual_button.bind(on_press=self.manual_search)
        root.add_widget(self.manual_button)

        self.name_button = Button(
            text="👤 البحث بالاسم",
            size_hint_y=None,
            height=dp(55)
        )
        self.name_button.bind(on_press=self.name_search)
        root.add_widget(self.name_button)

        self.contacts_button = Button(
            text="📋 جهات الاتصال",
            size_hint_y=None,
            height=dp(55)
        )
        self.contacts_button.bind(on_press=self.request_contacts_permission)
        root.add_widget(self.contacts_button)

       
