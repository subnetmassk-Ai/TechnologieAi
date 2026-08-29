[app]

# (str) Title of your application
title = WhatsApp Auto Dialer

# (str) Package name
package.name = whatsappautodialer

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (include font file if present)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) Application versioning
version = 0.1

# (list) Application requirements
# تشمل الكيفي ومكتبات معالجة النصوص العربية والأذونات
requirements = python3,kivy,pyjnius,arabic_reshaper,python-bidi

# (list) Permissions required by the app
android.permissions = INTERNET, RECORD_AUDIO, CALL_PHONE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be at least 27, 28, 29 or 31, 33, 34
android.api = 33

# (int) Minimum API required to run the app
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25.2.9519653

# (bool) If True, then skip building the NDK
android.skip_update = False

# (bool) If True, accept SDK license automatically
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.enable_androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable)
warn_on_root = 1
