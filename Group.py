import datetime
import struct
import time
from sqlite3 import *
from sys import getsizeof


class SortItems(object):

    def __init__(self, mid, sender, namef, timestamp, msgsize, msg):
        self.mid = mid
        self.sender = sender
        self.namef = namef
        self.msgsize = msgsize
        self.timestamp = timestamp
        self.msg = msg

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.sender == other.sender and self.namef == other.namef

    def __lt__(self, other):
        return self.timestamp < other.timestamp

class Group():

    def getData(Self):
        try:
            conn = connect('dump/cache4.db')
            list =[]
            cur = conn.cursor()  # reader
            sql = "SELECT * from messages;"
            cur.execute(sql)
            records = cur.fetchall()


            if records != None:
                for rec in records:
                    if rec[4] != 0:
                        mid = rec[0]
                        uid = rec[1]
                        data = rec[5]
                        midLen = str(mid)

                        #print(mid)
                        if ((mid > 0) and (len(midLen) < 16) and (uid < 0) and (data[0:4].hex() != '6258082b') and (data[0:4].hex() != 'fa555555') and (uid != 777000)):
                            #print(mid)
                            #print("this is a group")
                            # mid the same so mid = mid
                            senderID = (data[16:20].hex())
                            senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))
                            name = abs(uid)
                            name = str(name)
                            timestamp = rec[4]
                            timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))
                            offset32 = (data[32:33].hex())  # hexa value of offset32
                            #print(mid)
                            if offset32 != '':
                                res = int(offset32, 16)  # convert to decimal
                                msg = data[33:33 + res]
                                if offset32 != 'fe' and len(msg) != 0:
                                    msg = (data[33:33 + res]).decode("utf-8")
                                    msgsize = getsizeof(msg)
                                else:
                                    offset33 = (data[33:36].hex())  # convert to hexa
                                    res = int(offset33, 16)  # convert to decimal
                                    msg = (data[36:36 + res]).decode("utf-8")
                                    msgsize = getsizeof(msg)

                                sql = "SELECT name from chats where uid=" + name + ";"
                                cur = conn.cursor()
                                cur.execute(sql)
                                namerrec = cur.fetchone()
                                namef = namerrec[0]
                                sql = "SELECT name from users where uid=" + senderID + ";"
                                cur = conn.cursor()
                                cur.execute(sql)
                                senderrec = cur.fetchone()
                                sender = senderrec[0]

                                #print(mid, namef, sender, timestamp, msgsize, msg)
                               # print("________________________________________")
                                if msgsize != 0:
                                 list.append(SortItems(str(mid), str(sender), str(namef), str(timestamp), str(msgsize)+" B", msg))


        except Error as e:
            print('Error', e)

        list_sorted = sorted(list)
        return list_sorted