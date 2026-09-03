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
    CONTACT_PERMISSION_REQUEST = 200

    def build(self):
        self.title = "MarKoss"

        self.contacts = []

        root = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(12)
        )

        title = Label(
            text="MarKoss AI",
            font_size="32sp",
            bold=True,
            size_hint_y=None,
            height=dp(55)
        )

        subtitle = Label(
            text="مساعدك الذكي",
            font_size="18sp",
            size_hint_y=None,
            height=dp(35)
        )

        root.add_widget(title)
        root.add_widget(subtitle)

        self.input_box = TextInput(
            hint_text="اكتب رقم الهاتف أو اسم جهة الاتصال",
            multiline=False,
            font_size="19sp",
            size_hint_y=None,
            height=dp(55)
        )

        root.add_widget(self.input_box)

        whatsapp = Button(
            text="🟢  فتح WhatsApp",
            font_size="20sp",
            size_hint_y=None,
            height=dp(58)
        )
        whatsapp.bind(on_press=self.open_whatsapp)
        root.add_widget(whatsapp)

        phone = Button(
            text="📞  اتصال",
            font_size="20sp",
            size_hint_y=None,
            height=dp(58)
        )
        phone.bind(on_press=self.call_number)
        root.add_widget(phone)

        voice = Button(
            text="🎙️  بحث صوتي",
            font_size="20sp",
            size_hint_y=None,
            height=dp(58)
        )
        voice.bind(on_press=self.voice_search)
        root.add_widget(voice)

        contacts = Button(
            text="👥  جهات الاتصال",
            font_size="20sp",
            size_hint_y=None,
            height=dp(58)
        )
        contacts.bind(on_press=self.load_contacts)
        root.add_widget(contacts)

        search = Button(
            text="🔎  بحث بالاسم",
            font_size="20sp",
            size_hint_y=None,
            height=dp(58)
        )
        search.bind(on_press=self.search_contact)
        root.add_widget(search)

        self.status = Label(
            text="جاهز 🚀",
            font_size="16sp"
        )

        root.add_widget(self.status)

        return root

    # ==================================================
    # تنظيف وتحويل الرقم
    # ==================================================

    def clean_number(self, number):

        number = str(number).strip()

        # تحويل الأرقام العربية إلى إنجليزية
        arabic_digits = str.maketrans(
            "٠١٢٣٤٥٦٧٨٩",
            "0123456789"
        )

        number = number.translate(arabic_digits)

        # الاحتفاظ بالأرقام فقط
        number = re.sub(r"[^0-9]", "", number)

        # لبنان
        if number.startswith("00961"):
            number = number[2:]

        if number.startswith("0"):
            number = number[1:]

        if len(number) == 8 and number[0] in "3789":
            number = "961" + number

        return number

    # ==================================================
    # فحص الرقم
    # ==================================================

    def valid_number(self, number):

        number = self.clean_number(number)

        if not number:
            return False

        # رقم لبناني
        if len(number) == 11 and number.startswith("961"):
            return True

        # رقم دولي عام
        if 8 <= len(number) <= 15:
            return True

        return False

    # ==================================================
    # WhatsApp
    # ==================================================

    def open_whatsapp(self, instance):

        value = self.input_box.text.strip()

        if not value:
            self.status.text = "⚠️ أدخل رقم أو اسم أولاً"
            return

        # إذا كان اسم جهة اتصال
        if not re.search(r"\d", value):

            number = self.find_contact_number(value)

            if not number:
                self.status.text = "❌ لم أجد جهة الاتصال"
                return

        else:
            number = value

        number = self.clean_number(number)

        if not self.valid_number(number):
            self.status.text = "❌ الرقم غير صالح"
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
                ]
            )

            self.status.text = "🟢 تم فتح WhatsApp"

        except Exception as e:

            self.status.text = "❌ تعذر فتح WhatsApp"

    # ==================================================
    # اتصال
    # ==================================================

    def call_number(self, instance):

        value = self.input_box.text.strip()

        if not value:
            self.status.text = "⚠️ أدخل رقم أو اسم أولاً"
            return

        if not re.search(r"\d", value):

            number = self.find_contact_number(value)

            if not number:
                self.status.text = "❌ لم أجد جهة الاتصال"
                return

        else:
            number = value

        number = self.clean_number(number)

        if not self.valid_number(number):
            self.status.text = "❌ الرقم غير صالح"
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
                ]
            )

            self.status.text = "📞 تم فتح الهاتف"

        except Exception:

            self.status.text = "❌ تعذر فتح الهاتف"

    # ==================================================
    # البحث الصوتي
    # ==================================================

    def voice_search(self, instance):

        self.status.text = "🎙️ تحدث الآن..."

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

            intent.putExtra(
                RecognizerIntent.EXTRA_PROMPT,
                "تحدث الآن"
            )

            PythonActivity.mActivity.startActivityForResult(
                intent,
                self.VOICE_REQUEST
            )

        except Exception:

            self.status.text = "❌ التعرف الصوتي غير متاح"

    # ==================================================
    # استقبال نتيجة الصوت
    # ==================================================

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
                self.status.text = "لم يتم التقاط الصوت"
                return

            results = intent.getStringArrayListExtra(
                "android.speech.extra.RESULTS"
            )

            if not results:
                self.status.text = "❌ لم أفهم الكلام"
                return

            text = str(results.get(0))

            self.status.text = "سمعت: " + text

            # البحث عن رقم
            number = self.extract_spoken_number(text)

            if number:

                self.input_box.text = number

                self.status.text = (
                    "🔢 تم استخراج الرقم: " + number
                )

                return

            # البحث عن اسم
            contact = self.find_contact(text)

            if contact:

                self.input_box.text = contact["name"]

                self.status.text = (
                    "👤 تم العثور على: "
                    + contact["name"]
                )

                return

            self.status.text = "❌ لم أجد رقم أو اسم"

        except Exception:

            self.status.text = (
                "❌ حدث خطأ في قراءة الصوت"
            )

    # ==================================================
    # استخراج رقم من الكلام
    # ==================================================

    def extract_spoken_number(self, text):

        arabic_digits = str.maketrans(
            "٠١٢٣٤٥٦٧٨٩",
            "0123456789"
        )

        text = text.translate(arabic_digits)

        digits = re.findall(r"\d+", text)

        if digits:

            number = "".join(digits)

            if len(number) >= 8:
                return self.clean_number(number)

        words = text.lower().replace("-", " ").split()

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
            "تسع": "9"
        }

        result = ""

        for word in words:

            if word in numbers:
                result += numbers[word]

        if len(result) >= 8:
            return self.clean_number(result)

        return ""

    # ==================================================
    # طلب صلاحية جهات الاتصال
    # ==================================================

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

    # ==================================================
    # قراءة جهات الاتصال
    # ==================================================

    def load_contacts(self, instance):

        self.status.text = "👥 قراءة جهات الاتصال..."

        try:

            self.request_contacts_permission()

            from jnius import autoclass

            PythonActivity = autoclass(
                "org.kivy.android.PythonActivity"
            )

            ContentResolver = PythonActivity.mActivity.getContentResolver()

            ContactsContract = autoclass(
                "android.provider.ContactsContract"
            )

            Phone = ContactsContract.CommonDataKinds.Phone

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

            self.status.text = (
                "👥 تم تحميل "
                + str(len(self.contacts))
                + " جهة اتصال"
            )

            self.show_contacts()

        except Exception:

            self.status.text = (
                "❌ تعذر قراءة جهات الاتصال"
            )

    # ==================================================
    # عرض جهات الاتصال
    # ==================================================

    def show_contacts(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(5)
        )

        search_box = TextInput(
            hint_text="ابحث عن اسم...",
            multiline=False,
            size_hint_y=None,
            height=dp(50)
        )

        layout.add_widget(search_box)

        result_label = Label(
            text="اختر جهة اتصال",
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
            title="جهات الاتصال",
            content=layout,
            size_hint=(0.9, 0.85)
        )

        def refresh(*args):

            buttons.clear_widgets()

            query = search_box.text.strip().lower()

            shown = 0

            for contact in self.contacts:

                if query and query not in contact["name"].lower():
                    continue

                button = Button(
                    text=contact["name"]
                    + "\n"
                    + contact["number"],
                    size_hint_y=None,
                    height=dp(60)
                )

                def select_contact(
                    instance,
                    c=contact
                ):

                    self.input_box.text = c["number"]

                    self.status.text = (
                        "👤 "
                        + c["name"]
                        + " جاهز"
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

    # ==================================================
    # البحث بالاسم
    # ==================================================

    def search_contact(self, instance):

        name = self.input_box.text.strip()

        if not name:
            self.status.text = (
                "⚠️ اكتب اسم جهة الاتصال"
            )
            return

        if not self.contacts:

            self.load_contacts(instance)
            return

        contact = self.find_contact(name)

        if contact:

            self.input_box.text = contact["number"]

            self.status.text = (
                "👤 "
                + contact["name"]
                + " → "
                + contact["number"]
            )

        else:

            self.status.text = (
                "❌ لم أجد جهة الاتصال"
            )

    # ==================================================
    # إيجاد جهة اتصال
    # ==================================================

    def find_contact(self, name):

        name = str(name).strip().lower()

        for contact in self.contacts:

            if name == contact["name"].lower():

                return contact

        for contact in self.contacts:

            if name in contact["name"].lower():

                return contact

        return None

    # ==================================================
    # الحصول على رقم جهة اتصال
    # ==================================================

    def find_contact_number(self, name):

        contact = self.find_contact(name)

        if contact:
            return contact["number"]

        return None


if __name__ == "__main__":
    MarKossApp().run()
