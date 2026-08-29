[app]

# (str) Title of your application
title = WhatsApp Auto Dialer

# (str) Package name
package.name = whatsappautodialer

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO, CALL_PHONE

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a

# (str) The orientation
orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 or 1)
warn_on_root = 1
