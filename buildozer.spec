[app]

# (str) Title of your application
title = WhatsApp Auto Dialer

# (str) Package name
package.name = whatsappautodialer

# (str) Package domain
package.domain = org.test

# (str) Source code location
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Permissions required
android.permissions = INTERNET, RECORD_AUDIO, CALL_PHONE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (str) Android NDK version
android.ndk = 25b

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (str) The Android arch to build for (تم تقليلها لمعمارية واحدة لتجنب مشاكل الـ Linker)
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True

[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
