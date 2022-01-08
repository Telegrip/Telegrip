import os
from subprocess import check_output, CalledProcessError


class Info(object):

    def __init__(self, version, name,brand,model,country):
        self.version = version
        self.name = name
        self.brand = brand
        self.model = model
        self.country = country

class Imageinfo():

    def DeviceData(self):
        try:
            Datalist = []
            adb_output = check_output(["C:\Telegrip-platform-tools/platform-tools/adb", "devices"])
            if len(adb_output)>35:
                version = os.popen("C:\Telegrip-platform-tools/platform-tools/adb shell getprop ro.build.version.release").read()
                name = os.popen("C:\Telegrip-platform-tools/platform-tools/adb shell getprop ro.product.name ").read()
                brand = os.popen("C:\Telegrip-platform-tools/platform-tools/adb shell getprop ro.product.brand ").read()
                model = os.popen("C:\Telegrip-platform-tools/platform-tools/adb shell getprop ro.product.model ").read()
                country = os.popen("C:\Telegrip-platform-tools/platform-tools/adb shell getprop ro.csc.country_code ").read()

                Datalist.append(Info(str(version), str(name), str(brand), str(model), str(country)))
                return Datalist




            else:
             Datalist.append(Info("No device attached", "No device attached", "No device attached", "No device attached", "No device attached"))
             return Datalist

        except CalledProcessError as e:
            print (e.returncode)





