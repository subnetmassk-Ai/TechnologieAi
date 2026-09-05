import re
import subprocess

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class MarKossApp(App):

    VOICE_REQUEST = 100

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
                "contacts": "👥 اختيار الاسم من جهات الاتصال",
                "whatsapp": "🟢 WhatsApp",
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
                "search_contact_hint": "ابحث عن اسم...",
                "select_contact": "اختر جهة اتصال",
                "contact_ready": "👤 {name} جاهز",
                "no_result": "❌ لم أجد رقم أو اسم",
            },

            "en": {
                "title": "MarKoss AI",
                "subtitle": "Your Smart Assistant",
                "language": "🌐 العربية",
                "voice": "🎙️ Voice Search",
                "manual": "⌨️ Manual Search",
                "name_search": "👤 Search by Name",
                "contacts": "👥 Choose from Contacts",
                "whatsapp": "🟢 WhatsApp",
                "call": "📞 Call",
                "manual_hint": "Enter phone number",
                "name_hint": "Enter contact name",
                "ready": "Ready 🚀",
                "enter_number": "⚠️ Enter a phone number",
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
                "search_contact_hint": "Search name...",
                "select_contact": "Choose a contact",
                "contact_ready": "👤 {name} ready",
                "no_result": "❌ No number or name found",
            }
        }

        root = BoxLayout(
            orientation="vertical",
            padding=[dp(20), dp(10), dp(20), dp(20)],
            spacing=dp(10)
        )

        language_bar = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(45)
        )

        language_bar.add_widget(Label(text=""))

        self.language_button = Button(
            text=self.t("language"),
            size_hint_x=None,
            width=dp(130),
            font_size="16sp"
        )

        self.language_button.bind(
            on_press=self.toggle_language
        )

        language_bar.add_widget(self.language_button)
        root.add_widget(language_bar)

        self.title_label = Label(
            text=self.t("title"),
            font_size="32sp",
            bold=True,
            size_hint_y=None,
            height=dp(55)
        )

        root.add_widget(self.title_label)

        self.subtitle_label = Label(
            text=self.t("subtitle"),
            font_size="18sp",
            size_hint_y=None,
            height=dp(35)
        )

        root.add_widget(self.subtitle_label)

        self.input_box = TextInput(
            hint_text=self.t("manual_hint"),
            multiline=False,
            font_size="19sp",
            size_hint_y=None,
            height=dp(55)
        )

        root.add_widget(self.input_box)

        self.voice_button = Button(
            text=self.t("voice"),
            font_size="19sp",
            size_hint_y=None,
            height=dp(55)
        )

        self.voice_button.bind(
            on_press=self.voice_search
        )

        root.add_widget(self.voice_button)

        self.manual_button = Button(
            text=self.t("manual"),
            font_size="19sp",
            size_hint_y=None,
            height=dp(55)
        )

        self.manual_button.bind(
            on_press=self.manual_search
        )

        root.add_widget(self.manual_button)

        self.name_button = Button(
            text=self.t("name_search"),
            font_size="19sp",
            size_hint_y=None,
            height=dp(55)
        )

        self.name_button.bind(
            on_press=self.name_search
        )

        root.add_widget(self.name_button)

        self.contacts_button = Button(
            text=self.t("contacts"),
            font_size="19sp",
            size_hint_y=None,
            height=dp(55)
        )

        self.contacts_button.bind(
            on_press=self.load_contacts
        )

        root.add_widget(self.contacts_button)

        self.whatsapp_button = Button(
            text=self.t("whatsapp"),
            font_size="20sp",
            size_hint_y=None,
            height=dp(58)
        )

        self.whatsapp_button.bind(
            on_press=self.open_whatsapp
        )

        root.add_widget(self.whatsapp_button)

        self.call_button = Button(
            text=self.t("call"),
            font_size="20sp",
            size_hint_y=None,
            height=dp(58)
        )

        self.call_button.bind(
            on_press=self.call_number
        )

        root.add_widget(self.call_button)

        self.status = Label(
            text=self.t("ready"),
            font_size="16sp"
        )

        root.add_widget(self.status)

        return root

    # =========================================================
    # LANGUAGE
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
    # MANUAL SEARCH
    # =========================================================

    def manual_search(self, instance):
        self.input_box.hint_text = self.t("manual_hint")
        self.input_box.focus = True

    # =========================================================
    # SEARCH BY NAME
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
    # PHONE NUMBER
    # =========================================================

    def clean_number(self, number):
        number = str(number).strip()

        arabic_digits = str.maketrans(
            "٠١٢٣٤٥٦٧٨٩",
            "0123456789"
        )

        number = number.translate(arabic_digits)

        number = re.sub(
            r"[^0-9]",
            "",
            number
        )

        if number.startswith("00961"):
            number = number[2:]

        if number.startswith("0"):
            number = number[1:]

        if len(number) == 8 and number[0] in "3789":
            number = "961" + number

        return number

    def valid_number(self, number):
        number = self.clean_number(number)

        if not number:
            return False

        if len(number) == 11 and number.startswith("961"):
            return True

        if 8 <= len(number) <= 15:
            return True

        return False

    # =========================================================
    # WHATSAPP
    # =========================================================

    def open_whatsapp(self, instance):
        value = self.input_box.text.strip()

        if not value:
            self.status.text = self.t("enter_number")
            return

        if not re.search(r"\d", value):
            number = self.find_contact_number(value)

            if not number:
                self.status.text = self.t("not_found")
                return
        else:
            number = value

        number = self.clean_number(number)

        if not self.valid_number(number):
            self.status.text = self.t("invalid")
            return

        try:
            subprocess.run(
                [
                    "am",
                    "start",
                    "-a",
                    "android.intent.action.VIEW",
                    "-d",
                    "https://wa.me/" + number
                ],
                check=False
            )

            self.status.text = self.t("whatsapp_open")

        except Exception:
            self.status.text = self.t("whatsapp_error")

    # =========================================================
    # CALL
    # =========================================================

    def call_number(self, instance):
        value = self.input_box.text.strip()

        if not value:
            self.status.text = self.t("enter_number")
            return

        if not re.search(r"\d", value):
            number = self.find_contact_number(value)

            if not number:
                self.status.text = self.t("not_found")
                return
        else:
            number = value

        number = self.clean_number(number)

        if not self.valid_number(number):
            self.status.text = self.t("invalid")
            return

        try:
            subprocess.run(
                [
                    "am",
                    "start",
                    "-a",
                    "android.intent.action.DIAL",
                    "-d",
                    "tel:+" + number
                ],
                check=False
            )

            self.status.text = self.t("phone_open")

        except Exception:
            self.status.text = self.t("phone_error")

    # =========================================================
    # VOICE SEARCH
    # =========================================================

    def voice_search(self, instance):
        self.status.text = self.t("speaking")

        try:
            from jnius import autoclass

            PythonActivity = autoclass(
                "org.kivy.android.PythonActivity"
            )

            Intent = autoclass(
                "android.content.Intent"
            )

            RecognizerIntent = autoclass(
                "android.speech.RecognizerIntent"
            )

            intent = Intent(
                RecognizerIntent.ACTION_RECOGNIZE_SPEECH
            )

            intent.putExtra(
                RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
            )

            if self.language == "ar":
                intent.putExtra(
                    RecognizerIntent.EXTRA_LANGUAGE,
                    "ar-LB"
                )
            else:
                intent.putExtra(
                    RecognizerIntent.EXTRA_LANGUAGE,
                    "en-US"
                )

            intent.putExtra(
                RecognizerIntent.EXTRA_PROMPT,
                self.t("speaking")
            )

            PythonActivity.mActivity.startActivityForResult(
                intent,
                self.VOICE_REQUEST
            )

        except Exception:
            self.status.text = self.t("voice_error")

    def on_activity_result(
        self,
        request_code,
        result_code,
        intent
    ):
        if request_code != self.VOICE_REQUEST:
            return

        try:
            from jnius import autoclass

            Activity = autoclass(
                "android.app.Activity"
            )

            if result_code != Activity.RESULT_OK:
                self.status.text = self.t("no_voice")
                return

            results = intent.getStringArrayListExtra(
                "android.speech.extra.RESULTS"
            )

            if not results:
                self.status.text = self.t("not_understood")
                return

            text = str(results.get(0))

            self.status.text = (
                self.t("heard") + text
            )

            number = self.extract_spoken_number(text)

            if number:
                self.input_box.text = number

                self.status.text = (
                    self.t("number_found") + number
                )

                return

            contact = self.find_contact(text)

            if contact:
                self.input_box.text = contact["number"]

                self.status.text = (
                    self.t("contact_found")
                    + contact["name"]
                )

                return

            self.status.text = self.t("no_result")

        except Exception:
            self.status.text = self.t("not_understood")

    # =========================================================
    # VOICE NUMBER EXTRACTION
    # =========================================================

    def extract_spoken_number(self, text):
        arabic_digits = str.maketrans(
            "٠١٢٣٤٥٦٧٨٩",
            "0123456789"
        )

        text = text.translate(arabic_digits)

        digits = re.findall(
            r"\d+",
            text
        )

        if digits:
            number = "".join(digits)

            if len(number) >= 8:
                return self.clean_number(number)

        words = (
            text.lower()
            .replace("-", " ")
            .split()
        )

        numbers = {
            "صفر": "0",
            "واحد": "1",
            "اثنين": "2",
            "اثنان": "2",
            "ثلاثة": "3",
            "ثلاث": "3",
            "أربعة": "4",
            "اربعة": "4",
            "أربع": "4",
            "خمسة": "5",
            "خمس": "5",
            "ستة": "6",
            "ست": "6",
            "سبعة": "7",
            "سبع": "7",
            "ثمانية": "8",
            "تمانية": "8",
            "ثمان": "8",
            "تسعة": "9",
            "تسع": "9",
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }

        result = ""

        for word in words:
            if word in numbers:
                result += numbers[word]

        if len(result) >= 8:
            return self.clean_number(result)

        return ""

    # =========================================================
    # CONTACT PERMISSION
    # =========================================================

    def request_contacts_permission(self):
        try:
            from android.permissions import request_permissions
            from android.permissions import Permission

            request_permissions(
                [
                    Permission.READ_CONTACTS
                ]
            )

            return True

        except Exception:
            return False

    # =========================================================
    # LOAD CONTACTS
    # =========================================================

    def load_contacts(self, instance):
        self.status.text = self.t("reading_contacts")

        try:
            self.request_contacts_permission()

            from jnius import autoclass

            PythonActivity = autoclass(
                "org.kivy.android.PythonActivity"
            )

            ContentResolver = (
                PythonActivity
                .mActivity
                .getContentResolver()
            )

            ContactsContract = autoclass(
                "android.provider.ContactsContract"
            )

            Phone = (
                ContactsContract
                .CommonDataKinds
                .Phone
            )

            cursor = ContentResolver.query(
                Phone.CONTENT_URI,
                None,
                None,
                None,
                Phone.DISPLAY_NAME + " ASC"
            )

            contacts = []

            if cursor:
                name_index = cursor.getColumnIndex(
                    Phone.DISPLAY_NAME
                )

                number_index = cursor.getColumnIndex(
                    Phone.NUMBER
                )

                while cursor.moveToNext():
                    name = cursor.getString(
                        name_index
                    )

                    number = cursor.getString(
                        number_index
                    )

                    contacts.append(
                        {
                            "name": str(name),
                            "number": str(number)
                        }
                    )

                cursor.close()

            self.contacts = contacts

            self.status.text = self.t(
                "contacts_loaded"
            ).format(
                count=len(self.contacts)
            )

            self.show_contacts()

        except Exception:
            self.status.text = self.t(
                "contacts_error"
            )

    # =========================================================
    # CONTACT POPUP
    # =========================================================

    def show_contacts(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(5)
        )

        search_box = TextInput(
            hint_text=self.t(
                "search_contact_hint"
            ),
            multiline=False,
            size_hint_y=None,
            height=dp(50)
        )

        layout.add_widget(search_box)

        result_label = Label(
            text=self.t("select_contact"),
            size_hint_y=None,
            height=dp(40)
        )

        layout.add_widget(result_label)

        buttons = BoxLayout(
            orientation="vertical",
            spacing=dp(5)
        )

        layout.add_widget(buttons)

        popup = Popup(
            title=self.t("contacts_title"),
            content=layout,
            size_hint=(0.9, 0.85)
        )

        def refresh(*args):
            buttons.clear_widgets()

            query = search_box.text.strip().lower()

            shown = 0

            for contact in self.contacts:

                if (
                    query
                    and query not in contact["name"].lower()
                ):
                    continue

                button = Button(
                    text=(
                        contact["name"]
                        + "\n"
                        + contact["number"]
                    ),
                    size_hint_y=None,
                    height=dp(60)
                )

                def select_contact(
                    instance,
                    c=contact
                ):
                    self.input_box.text = c["number"]

                    self.status.text = self.t(
                        "contact_ready"
                    ).format(
                        name=c["name"]
                    )

                    popup.dismiss()

                button.bind(
                    on_press=select_contact
                )

                buttons.add_widget(button)

                shown += 1

                if shown >= 30:
                    break

        search_box.bind(
            text=refresh
        )

        refresh()

        popup.open()

    # =========================================================
    # FIND CONTACT
    # =========================================================

    def find_contact(self, name):
        name = str(name).strip().lower()

        for contact in self.contacts:
            if name == contact["name"].lower():
                return contact

        for contact in self.contacts:
            if name in contact["name"].lower():
                return contact

        return None

    def find_contact_number(self, name):
        contact = self.find_contact(name)

        if contact:
            return contact["number"]

        return None


if __name__ == "__main__":
    MarKossApp().run()

