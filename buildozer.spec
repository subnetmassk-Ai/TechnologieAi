[app]
title = TechnologieAi
package.name = technologieai
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,mp3

version = 0.1

requirements = python3,kivy==2.2.1,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO

android.api = 35
android.minapi = 23
android.ndk = 28c

android.accept_sdk_license = True

android.archs = arm64-v8a

android.allow_backup = True

log_level = 2
warn_on_root = 1
