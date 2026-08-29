[app]
title = WhatsApp Auto Dialer
package.name = whatsappautodialer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy

orientation = portrait

# Android specific
android.permissions = INTERNET, RECORD_AUDIO, CALL_PHONE
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
