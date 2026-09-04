import re

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class MarKossApp(App):

    VOICE_REQUEST = 1001

    def build(self):
        self.title = "MarKoss"
        self.contacts = []
        self.language = "ar"

        self.tr = {
            "ar": {
                "title": "MarKoss AI",
                "subtitle": "مساعدك الذكي",
                "language": "🌐 English",
                "voice": "🎙️ البحث الصوتي",
                "manual": "⌨️ البحث اليدوي",
                "name_search": "👤 البحث حسب الاسم",
                "contacts": "👥 جهات الاتصال",
                "whatsapp": "🟢 فتح WhatsApp",
                "call": "📞 اتصال",
                "manual_hint": "أدخل رقم الهاتف",
                "name_hint": "أدخل اسم جهة الاتصال",
                "ready": "جاهز 🚀",
                "enter_number": "⚠️ أدخل رقم الهاتف",
                "enter_name": "⚠️ أدخل اسم جهة الاتصال",
                "not_found": "❌ لم أجد جهة الاتصال",
                "invalid": "❌ الرقم غير صالح",
                "whatsapp_open": "🟢 تم فتح WhatsApp",
                "whatsapp_error": "❌ تعذر فتح WhatsApp",
                "phone_open": "📞 تم فتح الهاتف",
                "phone_error": "❌ تعذر فتح الهاتف",
                "speaking": "🎙️ تحدث الآن...",
                "voice_error": "❌ التعرف الصوتي غير متاح",
                "no_voice": "لم يتم التقاط الصوت",
                "not_understood": "❌ لم أفهم الكلام",
                "heard": "سمعت: ",
                "number_found": "🔢 تم استخراج الرقم: ",
                "contact_found": "👤 تم العثور على: ",
                "reading_contacts": "👥 قراءة جهات الاتصال...",
                "contacts_loaded": "👥 تم تحميل {count} جهة اتصال",
                "contacts_error": "❌ تعذر قراءة جهات الاتصال",
                "contacts_title": "جهات الاتصال",
                "search_contact_hint": "ابحث عن اسم أو رقم...",
                "select_contact": "اختر جهة اتصال",
                "contact_ready": "👤 {name} جاهز",
                "permission_error": "⚠️ يجب السماح بالوصول إلى جهات الاتصال",
                "no_result": "❌ لم أجد رقمًا أو اسمًا",
            },

            "en": {
                "title": "MarKoss AI",
                "subtitle": "Your Smart Assistant",
                "language": "🌐 العربية",
                "voice": "🎙️ Voice Search",
                "manual": "⌨️ Manual Search",
                "name_search": "👤 Search by Name",
                "contacts": "👥 Contacts",
                "whatsapp": "🟢 Open WhatsApp",
                "call": "📞 Call",
                "manual_hint": "Enter phone number",
                "name_hint": "Enter contact name",
                "ready": "Ready 🚀",
                "enter_number": "⚠️ Enter phone number",
                "enter_name": "⚠️ Enter contact name",
                "not_found": "❌ Contact not found",
                "invalid": "❌ Invalid number",
                "whatsapp_open": "🟢 WhatsApp opened",
                "whatsapp_error": "❌ Could not open WhatsApp",
                "phone_open": "📞 Phone opened",
                "phone_error": "❌ Could not open phone",
                "speaking": "🎙️ Speak now...",
                "voice_error": "❌ Voice recognition unavailable",
                "no_voice": "No voice was captured",
                "not_understood": "❌ I could not understand",
                "heard": "Heard: ",
                "number_found": "🔢 Number extracted: ",
                "contact_found": "👤 Found: ",
                "reading_contacts": "👥 Reading contacts...",
                "contacts_loaded": "👥 Loaded {count} contacts",
                "contacts_error": "❌ Could not read contacts",
                "contacts_title": "Contacts",
                "search_contact_hint": "Search name or number...",
                "select_contact": "Choose a contact",
                "contact_ready": "👤 {name} ready",
                "permission_error": "⚠️ Contacts permission is required",
                "no_result": "❌ No number or name found",
            },
        }

        self.root = BoxLayout(
            orientation="vertical",
            padding=[dp(20), dp(10), dp(20), dp(20)],
            spacing=dp(10),
        )

        # Language
        language_bar = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(45),
        )

        language_bar.add_widget(Label(text=""))

        self.language_button = Button(
            text=self.t("language"),
            size_hint_x=None,
            width=dp(130),
            font_size="16sp",
        )

        self.language_button.bind(
            on_press=self.toggle_language
        )

        language_bar.add_widget(self.language_button)
        self.root.add_widget(language_bar)

        # Title
        self.title_label = Label(
            text=self.t("title"),
            font_size="32sp",
            bold=True,
            size_hint_y=None,
            height=dp(55),
        )

        self.root.add_widget(self.title_label)

        self.subtitle_label = Label(
            text=self.t("subtitle"),
            font_size="18sp",
            size_hint_y=None,
            height=dp(35),
        )

        self.root.add_widget(self.subtitle_label)

        # Input
        self.input_box = TextInput(
            hint_text=self.t("manual_hint"),
            multiline=False,
            font_size="19sp",
            size_hint_y=None,
            height=dp(55),
        )

        self.root.add_widget(self.input_box)

        # Voice
        self.voice_button = Button(
            text=self.t("voice"),
            font_size="19sp",
            size_hint_y=None,
            height=dp(55),
        )

        self.voice_button.bind(
            on_press=self.voice_search
        )

        self.root.add_widget(self.voice_button)

        # Manual
        self.manual_button = Button(
            text=self.t("manual"),
            font_size="19sp",
            size_hint_y=None,
            height=dp(55),
        )

        self.manual_button.bind(
            on_press=self.manual_search
        )

        self.root.add_widget(self.manual_button)

        # Name
        self.name_button = Button(
            text=self.t("name_search"),
            font_size="19sp",
            size_hint_y=None,
            height=dp(55),
        )

        self.name_button.bind(
            on_press=self.name_search
        )

        self.root.add_widget(self.name_button)

        # Contacts
        self.contacts_button = Button(
            text=self.t("contacts"),
            font_size="19sp",
            size_hint_y=None,
            height=dp(55),
        )

        self.contacts_button.bind(
            on_press=self.load_contacts
        )

        self.root.add_widget(self.contacts_button)

        # WhatsApp
        self.whatsapp_button = Button(
            text=self.t("whatsapp"),
            font_size="20sp",
            size_hint_y=None,
            height=dp(58),
        )

        self.whatsapp_button.bind(
            on_press=self.open_whatsapp
        )

        self.root.add_widget(self.whatsapp_button)

        # Call
        self.call_button = Button(
            text=self.t("call"),
            font_size="20sp",
            size_hint_y=None,
            height=dp(58),
        )

        self.call_button.bind(
            on_press=self.call_number
        )

        self.root.add_widget(self.call_button)

        # Status
        self.status = Label(
            text=self.t("ready"),
            font_size="16sp",
        )

        self.root.add_widget(self.status)

        # Android activity callback
        try:
            from android import activity

            activity.bind(
                on_activity_result=self.on_activity_result
            )

        except Exception:
            pass

        return self.root

    # =========================================================
    # TRANSLATION
    # =========================================================

    def t(self, key):
        return self.tr[self.language][key]

    def toggle_language(self, instance):

        if self.language == "ar":
            self.language = "en"
        else:
            self.language = "ar"

        self.update_language()

    def update_language(self):

        self.language_button.text = self.t("language")
        self.title_label.text = self.t("title")
        self.subtitle_label.text = self.t("subtitle")
        self.voice_button.text = self.t("voice")
        self.manual_button.text = self.t("manual")
        self.name_button.text = self.t("name_search")
        self.contacts_button.text = self.t("contacts")
        self.whatsapp_button.text = self.t("whatsapp")
        self.call_button.text = self.t("call")

        if not self.input_box.text.strip():
            self.input_box.hint_text = self.t("manual_hint")
            self.status.text = self.t("ready")

    # =========================================================
    # MANUAL
    # =========================================================

    def manual_search(self, instance):

        self.input_box.hint_text = self.t("manual_hint")
        self.input_box.focus = True

    # =========================================================
    # SEARCH NAME
    # =========================================================

    def name_search(self, instance):

        self.input_box.hint_text = self.t("name_hint")

        name = self.input_box.text.strip()

        if not name:
            self.status.text = self.t("enter_name")
            self.input_box.focus = True
            return

        if not self.contacts:
            self.load_contacts(instance)
            return

        contact = self.find_contact(name)

        if contact:

            self.input_box.text = contact["number"]

            self.status.text = (
                self.t("contact_found")
                + contact["name"]
            )

        else:

            self.status.text = self.t("not_found")

    # =========================================================
    # NUMBER CLEANING
    # =========================================================

    def clean_number(self, number):

        if number is None:
            return ""

        number = str(number).strip()

        arabic_digits = str.maketrans(
            "٠١٢٣٤٥٦٧٨٩",
            "0123456789"
        )

        persian_digits = str.maketrans(
            "۰۱۲۳۴۵۶۷۸۹",
            "0123456789"
        )

        number = number.translate(arabic_digits)
        number = number.translate(persian_digits)

        number = re.sub(
            r"[^0-9]",
            "",
            number
        )

        # 00961xxxxxxxx
        if number.startswith("00961"):
            number = number[2:]

        # +961xxxxxxxx
        if number.startswith("961"):
            return number

        # Lebanese local number
        if number.startswith("0"):
            number = number[1:]

        # Lebanese 8 digit number
        if len(number) == 8:
            number = "961" + number

        return number

    def valid_number(self, number):

        number = self.clean_number(number)

        if not number:
            return False

        if (
            len(number) == 11
            and number.startswith("961")
        ):
            return True

        if 8 <= len(number) <= 15:
            return True

        return False

    # =========================================================
    # ANDROID INTENT
    # =========================================================

    def start_android_intent(
        self,
        action,
        uri,
        package_name=None
    ):

        try:

            from jnius import autoclass

            PythonActivity = autoclass(
                "org.kivy.android.PythonActivity"
            )

            Intent = autoclass(
                "android.content.Intent"
            )

            Uri = autoclass(
                "android.net.Uri"
            )

            activity = PythonActivity.mActivity

            intent = Intent(
                action,
                Uri.parse(uri)
            )

            if package_name:
                intent.setPackage(package_name)

            activity.startActivity(intent)

            return True

        except Exception as e:

            print(
                "Android Intent error:",
                e
            )

            return False

    # =========================================================
    # WHATSAPP
    # =========================================================

    def open_whatsapp(self, instance):

        value = self.input_box.text.strip()

        if not value:

            self.status.text = self.t("enter_number")
            return

        # If user typed a name
        if not re.search(r"\d", value):

            if not self.contacts:
                self.status.text = self.t("not_found")
                return

            number = self.find_contact_number(value)

            if not number:

                self.status.text = self.t("not_found")
                return

        else:

            number = value

        number = self.clean_number(number)

        if not self.valid_number(number):

            self.status.text = self.t("invalid")
           
