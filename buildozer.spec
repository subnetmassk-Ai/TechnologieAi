[app]

title = TechnologieAi
package.name = technologieai
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,wav,mp3,json

version = 0.1

requirements = python3==3.10.12,kivy==2.2.1,pyjnius,requests

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 23
android.sdk = 35
android.ndk = 28c

android.archs = arm64-v8a

android.permissions = INTERNET,RECORD_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.enable_androidx = True

android.allow_backup = True

android.private_storage = True

android.entrypoint = org.kivy.android.PythonActivity


[buildozer]

log_level = 2
warn_on_root = 1
