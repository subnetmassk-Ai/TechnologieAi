[app]

# (str) Title of your application
title = WhatsApp Auto Dialer

# (str) Package name
package.name = whatsappautodialer

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# ملاحظة: تم الاقتصار على Kivy و PyJNIus لاستدعاء ميزات أندرويد الصوتية بدون أخطاء تجميع
requirements = python3,kivy,pyjnius

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO, CALL_PHONE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a

# (int) log_level = 0 I, 1 D, 2 V
log_level = 2
