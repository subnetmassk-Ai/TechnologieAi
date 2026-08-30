[app]
title = WhatsApp Assistant
package.name = whatsappapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav

version = 0.1
requirements = python3,kivy,SpeechRecognition,requests

orientation = portrait
osx.kivy_version = 2.2.1

fullscreen = 0

# Android permissions & SDK settings
android.permissions = INTERNET, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 1

warn_on_root = 1
