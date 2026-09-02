name: Build Android APK

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:

      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Java 17
        uses: actions/setup-java@v5
        with:
          distribution: temurin
          java-version: "17"

      - name: Setup Python 3.10
        uses: actions/setup-python@v6
        with:
          python-version: "3.10.12"

      - name: Install system dependencies
        run: |
          sudo apt-get update

          sudo apt-get install -y \
            build-essential \
            git \
            zip \
            unzip \
            autoconf \
            automake \
            cmake \
            libffi-dev \
            libssl-dev \
            libsqlite3-dev \
            zlib1g-dev \
            libbz2-dev \
            libltdl-dev \
            libtool \
            pkg-config \
            patch

      - name: Install Buildozer
        run: |
          python -m pip install --upgrade pip setuptools wheel
          python -m pip install "cython<3"
          python -m pip install "buildozer==1.6.0"

      - name: Install Android SDK tools
        run: |
          SDKMANAGER="$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager"

          yes | "$SDKMANAGER" --licenses || true

          "$SDKMANAGER" \
            "platform-tools" \
            "platforms;android-33" \
            "build-tools;33.0.2" \
            "ndk;28.2.13676358"

      - name: Verify Android SDK and NDK
        run: |
          echo "ANDROID_HOME=$ANDROID_HOME"
          echo "ANDROID_SDK_ROOT=$ANDROID_SDK_ROOT"

          ls -la "$ANDROID_HOME/ndk/28.2.13676358"

          java -version
          python --version
          buildozer --version

      - name: Clean previous build
        run: |
          rm -rf .buildozer
          rm -rf bin

      - name: Configure NDK path
        run: |
          sed -i \
           
