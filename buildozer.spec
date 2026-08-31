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
requirements = python3==3.10.12,kivy==2.2.1,SpeechRecognition,requests

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25.2.9519653

# (bool) Accept all SDK licences automatically
android.accept_sdk_license = True

# (list) List of Android architectures to build for
android.archs = arm64-v8a

# (bool) Enable Android auto-backup feature
android.allow_backup = True

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
