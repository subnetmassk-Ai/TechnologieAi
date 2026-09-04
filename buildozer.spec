[app]

title = MarKoss
package.name = markoss
package.domain = org.markoss

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,wav,mp3

version = 0.1

requirements = python3==3.10.12,hostpython3==3.10.12,kivy==2.3.1,requests,legacy-cgi
orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 23
android.ndk = 28c
android.ndk_api = 23

android.permissions = INTERNET,RECORD_AUDIO,READ_CONTACTS

android.archs = arm64-v8a

android.accept_sdk_license = True


[buildozer]

log_level = 2
warn_on_root = 1
