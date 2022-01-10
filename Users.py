import time
from sqlite3 import *


class Load(object):

    def __init__(self, UserID, Name, Username, Status, Phone):
        self.UserID = UserID
        self.Name = Name
        self.Username=Username
        self.Status = Status
        self.Phone=Phone



class Users():

    def LoadUsers(self):
        try:

            Datalist = []
            conn = connect('dump\cache4.db')
            cur = conn.cursor()  # reader
            sql3 = "SELECT uid from contacts;"
            cur.execute(sql3)
            record = cur.fetchall()
            if record is not None:
                for rec in record:
                    UserID=str(rec[0])
                    sql3 = "SELECT * from users WHERE uid = "+UserID+" AND status !=0 ;"
                    cur.execute(sql3)
                    record = cur.fetchall()
                    if record is not None:
                     for rec in record:
                        UserID = rec[0]
                        if rec[1]:
                            Name = rec[1]
                            a, b = Name.split(";;;")
                            Name=a
                            Username=b
                            if Username == "":
                                Username = "No username assigned"

                        if rec[2] :
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
                        Datalist.append(Load(str(UserID), str(Name),str(Username), str(Status),str(Phone)))

        except Error as e:
            print('Error', e)
        return Datalist
