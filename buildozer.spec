[app]

# (str) Application versioning
version = 0.1

# (str) Title of your application
title = TechnologieAi

# (str) Package name
package.name = technologieai

# (str) Package domain
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,wav,mp3

# (list) Application requirements
requirements = python3==3.10.12,kivy==2.2.1,SpeechRecognition,requests

# (str) Supported orientations
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API supported
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (str) Android NDK version
android.ndk = 25.2.9519653

# (bool) Accept SDK licenses
android.accept_sdk_license = True

# (list) Target architectures
android.archs = arm64-v8a

# (bool) Auto-backup
android.allow_backup = True

# (int) Log level
log_level = 2

# (int) Warning on root
warn_on_root = 1
