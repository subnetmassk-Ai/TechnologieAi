[app]
title = WhatsApp Assistant
package.name = whatsappapp
package.domain = org.test
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,spec

requirements = python3,kivy==2.2.1,SpeechRecognition,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
