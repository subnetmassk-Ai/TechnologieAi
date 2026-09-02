[app]

title = TechnologieAi
package.name = technologieai
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,wav,mp3,json
source.exclude_dirs = .buildozer,bin,.git

version = 0.1

requirements = python3==3.10.12,hostpython3==3.10.12,kivy==2.2.1,pyjnius

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 28c

android.archs = arm64-v8a

android.permissions = INTERNET,RECORD_AUDIO

android.enable_androidx = True

android.allow_backup = True
android.private_storage = True

p4a.branch = master


[buildozer]

log_level = 2
warn_on_root = 1
