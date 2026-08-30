[app]

# (str) Title of your application
title = TechnologieAi

# (str) Package name
package.name = technologieai

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,wav,mp3

# (list) Application requirements
# تم ضبط إصدار Python بوضوح لمنع استخدام إصدارات غير مستقرة
requirements = python3==3.10.12,kivy==2.2.1,SpeechRecognition,requests

# (str) Custom source folders for requirements
# requirements.source.kivy =

# (list) Garden requirements
# garden_requirements =

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientations (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services = MyServiceName:./service.py

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the standard names
# android.presplash_color = red

# (list) Permissions
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25.2.9519653

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
# android.ant_path =

# (bool) If True, then skip python-for-android packaging step.
# android.skip_update = False

# (bool) If True, then accept all SDK licences automatically
android.accept_sdk_license = True

# (list) List of Android architectures to build for
android.archs = arm64-v8a

# (bool) Enable Android auto-backup feature
android.allow_backup = True

#
# Python for Android (p4a) specific
#

# (str) p4a fork to use, defaults to upstream
# p4a.fork = kivy

# (str) p4a branch to use, defaults to master
# p4a.branch = master

# (str) p4a source directory or URL
# p4a.source_dir =

# (str) List of extra stage building recipes
# p4a.local_recipes =

# (str) Filename to the hook for p4a
# p4a.hook =

# (str) Bootstrap to use for android build
# p4a.bootstrap = sdl2

#
# Buildozer options
#

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
