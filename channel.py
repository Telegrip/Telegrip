import datetime
import struct
import time
from sqlite3 import *
from sys import getsizeof


class SortItems(object):
    def __init__(self, msgID, namef, timestamp, msgsize, msg):
        self.msgID = msgID
        self.namef = namef
        self.msgsize = msgsize
        self.timestamp = timestamp
        self.msg = msg

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.namef == other.namef

    def __lt__(self, other):
        return self.timestamp < other.timestamp

class channel():

    def getData(Self):
        try:
            list = []
            conn = connect('dump/cache4.db')
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

                        if ((mid > 0) and (len(midLen) >= 16) and (uid < 0) and (data[0:4].hex() != '6258082b')):

                            name = abs(uid)
                            name = str(name)
                            timestamp = rec[4]
                            timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))
                            offset32 = (data[24:25].hex())  # hexa value of offset32

                            if offset32 != '':
                                res = int(offset32, 16)  # convert to decimal
                                msg = data[25:25 + res]
                                if offset32 != 'fe' and len(msg) != 0:
                                    msg = (data[25:25 + res]).decode("utf-8")
                                    msgsize = getsizeof(msg)
                                else:
                                    offset33 = (data[25:28].hex())  # convert to hexa
                                    res = int(offset33, 16)  # convert to decimal
                                    msg = (data[28:28 + res]).decode("utf-8")
                                    msgsize = getsizeof(msg)

                                sql = "SELECT name from chats where uid=" + name + ";"
                                cur = conn.cursor()
                                cur.execute(sql)
                                namerrec = cur.fetchone()
                                namef = namerrec[0]

                                if msgsize !=0 :
                                 list.append(SortItems(str(mid), str(namef), str(timestamp), str(msgsize)+" B", msg))



        except Error as e:
            print('Error', e)

        list_sorted = sorted(list)
        return list_sorted

