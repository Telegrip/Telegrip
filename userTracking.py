import time
from sqlite3 import *

from NormalChat import NormalChat
from SecretChat import SecretChat

class userTracking(object):

    def __init__(self, UserID, Name, Username, Status, Phone):
        self.UserID = UserID
        self.Name = Name
        self.Username = Username
        self.Status = Status
        self.Phone = Phone


class Track():

    def usr(self):
        Datalist = []
        conn = connect('dump\cache4.db')
        sql3 = "SELECT * from users WHERE status !=0;"
        cur = conn.cursor()  # reader
        cur.execute(sql3)
        record = cur.fetchall()
        UserID=""
        Name=""
        username=""
        Status=""
        Phone=""

        try:
            if record is not None:
                for rec in record:
                    UserID = rec[0]

                    if rec[1]:
                        Name = rec[1]
                        a, b = Name.split(";;;")
                        Name = a
                        username = b
                        if username=="":
                            username="No username assigned"

                    if rec[2]:
                        Status = rec[2]
                        if Status == -100 or Status == -101 or Status == -102:
                            Status = "Last seen recently"

                        else:
                            Status = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(Status))

                    if rec[3]:
                        Phone = ''
                        value = rec[3]
                        for i in range(0, len(value)):
                            hexx = value[i]
                            hexx = hex(hexx)[2:]
                            if hexx == 'c':
                                Phone = (value[i + 1:i + 13]).decode("utf-8")


                            if Phone == '':
                                Phone = "No Number assigned "

                    Datalist.append(userTracking(str(UserID), str(Name), str(username), str(Status), str(Phone)))

        except Error as e:
            print('Error', e)
        return Datalist



# u=userTracking()
# u.usr()