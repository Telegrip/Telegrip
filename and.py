import os
from subprocess import check_output, CalledProcessError




def DeviceData():
    try:

        os.system("C:\Telegrip-platform-tools/platform-tools/adb devices")
        version = os.popen("C:\Telegrip-platform-tools/platform-tools/adb shell getprop ro.build.version.release").read()
        name = os.popen("C:\Telegrip-platform-tools/platform-tools/adb shell getprop ro.product.name ").read()
        brand = os.popen("C:\Telegrip-platform-tools/platform-tools/adb shell getprop ro.product.brand ").read()
        model = os.popen("C:\Telegrip-platform-tools/platform-tools/adb shell getprop ro.product.model ").read()
        country = os.popen("C:\Telegrip-platform-tools/platform-tools/adb shell getprop ro.csc.country_code ").read()

        print(" Android version: ", version, "Device name: ", name, "Device brand: ", brand, "Device model: ", model,
              "Country: ", country)

    except CalledProcessError as e:
        print("no device connected")

DeviceData()
