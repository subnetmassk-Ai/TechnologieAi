[app]
title = WhatsApp Assistant
package.name = whatsappapp
package.[app]
title = WhatsApp Voice Assistant
package.name = whatsappvoiceapp
package.domain = org.test
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,spec

# المتطلبات المتوافقة تماماً مع البناء بدون أخطاء
requirements = python3,kivy==2.2.1,pyjnius,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 23b
android.build_tools_version = 31.0.0
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
n = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,spec

requirements = python3,kivy==2.2.1,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 23b
android.build_tools_version = 31.0.0
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
