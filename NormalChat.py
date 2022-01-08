import datetime
import struct
import time
from sqlite3 import *
from sys import getsizeof


class SortItems(object):

    def __init__(self, mid, sender,reciver,timestamp,msgsize,msg):
        self.mid = mid
        self.sender = sender
        self.reciver = reciver
        self.msgsize = msgsize
        self.timestamp = timestamp
        self.msg = msg

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.sender == other.sender and self.reciver == other.reciver

    def __lt__(self, other):
        return self.timestamp < other.timestamp

class NormalChat():
    
    def getData(self):
        try:
            conn = connect('dump/cache4.db')
            list = []
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
                        out = rec[6]
                        midLen = str(mid)
                        if ((data[0:4].hex() != 'fa555555') and (data[0:4].hex() != '6258082b') and (out == 1) and (uid > 0)):
                            # mid the same so mid = mid
                            senderID = (data[16:20].hex())
                            senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))
                            recivedID = (data[24:28].hex())
                            recivedID = str(int((struct.pack('<L', int(recivedID, base=16))).hex(), 16))
                            timestamp = rec[4]
                            timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))
                            offset32 = (data[32:33].hex())  # hexa value of offset32

                            if offset32 != '':
                                res = int(offset32, 16)  # convert to decimal
                                msg = data[33:33 + res]
                                if offset32 != 'fe' and len(msg) != 0:
                                    msg = (data[33:33 + res]).decode("utf-8")
                                    msgsize = getsizeof(msg)
                                    # else:
                                    #     offset33 = (data[33:36].hex())  # convert to hexa
                                    #     res = int(offset33, 16)  # convert to decimal
                                    #     msg = (data[36:36 + res]).decode("utf-8")
                                    #     msgsize = len(msg)

                                    sql = "SELECT name from users where uid=" + senderID + ";"
                                    cur = conn.cursor()
                                    cur.execute(sql)
                                    senderrec = cur.fetchone()
                                    sender = senderrec[0]
                                    sql = "SELECT name from users where uid=" + recivedID + ";"
                                    cur = conn.cursor()
                                    cur.execute(sql)
                                    reciverrec = cur.fetchone()
                                    reciver = reciverrec[0]
                                    list.append(SortItems(str(mid), str(sender), str(reciver), str(timestamp), str(msgsize)+" B", msg))





                        elif ((data[0:4].hex() != 'fa555555') and (data[0:4].hex() != '6258082b') and (out == 0) and (uid != 777000) and (uid > 0) ):
                            # mid the same so mid = mid
                            senderID = (data[16:20].hex())
                            senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))
                            reciver = "Host"
                            checkreciver = (data[20:24].hex())
                            timestamp = rec[4]
                            timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))
                            offset24 = (data[24:25].hex())  # hexa value of offset24
                            sql = "SELECT name from users where uid=" + senderID + ";"
                            cur = conn.cursor()
                            cur.execute(sql)
                            senderrec = cur.fetchone()
                            sender = senderrec[0]

                            if checkreciver == "6dbcb19d":
                                offset24 = (data[32:33].hex())

                                if offset24 != '':
                                    res = int(offset24, 16)  # convert to decimal
                                    msg = data[33:33 + res]
                                    if offset24 != 'fe' and len(msg) != 0:
                                        msg = (data[33:33 + res]).decode("utf-8")
                                        msgsize = getsizeof(msg)
                                        list.append(SortItems(str(mid), str(sender), str(reciver), str(timestamp),
                                                              str(msgsize) + " B", msg))



                            else:

                                if offset24 != '':
                                    res = int(offset24, 16)  # convert to decimal
                                    msg = data[25:25 + res]

                                    if offset24 != 'fe' and len(msg) != 0:
                                        msg = (data[25:25 + res]).decode("utf-8")
                                        msgsize = getsizeof(msg)

                                        list.append(SortItems(str(mid), str(sender), str(reciver), str(timestamp), str(msgsize)+" B",msg))


    
    
        except Error as e:
            print('Error', e)

        list_sorted = sorted(list)
        return list_sorted
