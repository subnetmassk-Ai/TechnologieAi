[app]
title = MarKoss
package.name = markoss
package.domain = org.markoss

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,wav,mp3

version = 0.1

requirements = python3,kivy==2.2.1,pyjnius

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 28c
android.permissions = INTERNET,RECORD_AUDIO

android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
