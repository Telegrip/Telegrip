import datetime
import struct
import time
from sqlite3 import *
from sys import getsizeof

class SortItems(object):

    def __init__(self, msgID, sendername,recivedname,timestamp,msgsize,msg):
        self.msgID = msgID
        self.sendername = sendername
        self.recivedname = recivedname
        self.msgsize = msgsize
        self.timestamp = timestamp
        self.msg = msg

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.sendername == other.sendername and self.recivedname == other.recivedname

    def __lt__(self, other):
        return self.timestamp < other.timestamp

class SecretChat():
    def getData(self):
        try:
            list = []
            conn=connect('dump/cache4.db')
            sql = "SELECT * from messages;"
            cur = conn.cursor() #reader
            cur.execute(sql)
            records = cur.fetchall()
            if records != None:

              for rec in records:
                data=rec[5]

                if data[0:4].hex() == 'fa555555' and rec[4]!=0:
                    msgID=(data[8:12].hex())
                    msgID=int((struct.pack('<L', int(msgID, base=16))).hex(),16)
                    msgID = -((msgID) & 0x80000000) | ((msgID) & 0x7fffffff)
                    senderID=(data[16:20].hex())
                    senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))
                    recivedID = (data[24:28].hex())
                    recivedID = str(int((struct.pack('<L', int(recivedID, base=16))).hex(), 16))
                    timestamp = rec[4]
                    timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))
                    print("Raw data:", data)
                    offset32 = (data[32:33].hex())  # hexa value of offset32
                    if offset32 != '':
                        res = int(offset32, 16)  # convert to decimal
                        msg = data[33:33 + res]
                        if offset32 != 'fe' and len(msg) != 0:
                            msg = (data[33:33 + res]).decode("utf-8")
                            print("Human readable format:", msg)
                            msgsize = getsizeof(msg)
                        else:
                            offset33 = (data[33:36].hex())  # convert to hexa
                            res = int(offset33, 16)  # convert to decimal
                            msg=(data[36:36+res]).decode("utf-8")
                            msgsize = getsizeof(msg)
                    sql = "SELECT * from enc_chats where admin_id="+senderID+" and user="+recivedID+" ;"
                    cur = conn.cursor()
                    cur.execute(sql)
                    records = cur.fetchall()
                    if records != None:
                        sql = "SELECT name from users where uid=" + senderID+";"
                        cur = conn.cursor()
                        cur.execute(sql)
                        senderrec = cur.fetchone()
                        sendername=senderrec[0]
                        sql = "SELECT name from users where uid=" + recivedID + " ;"
                        cur = conn.cursor()
                        cur.execute(sql)
                        recivedrec = cur.fetchone()
                        recivedname = recivedrec[0]
                   # print(str(msgID) + "\t\t" + str(sendername) +"\t\t"+ str(recivedname) + "\t\t\t\t"+ str(timestamp)+"\t\t"+str(msgsize)+"\t\t"+msg)

                    list.append(SortItems(str(msgID), str(sendername) , str(recivedname) , str(timestamp) ,str(msgsize)+" B",msg))




        except Error as e:
            print('Error', e)

        list_sorted = sorted(list)
        return list_sorted





