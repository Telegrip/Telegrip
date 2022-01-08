import struct
import time
import os
from sqlite3 import *
from sys import getsizeof


class SortItems(object):

    def __init__(self, msgID, sendername, recivedname, timestamp, url, type):
        self.msgID = msgID
        self.sendername = sendername
        self.recivedname = recivedname
        self.timestamp = timestamp
        self.url = url
        self.type = type

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.sendername == other.sendername and self.recivedname == other.recivedname

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class ParsingUrl():
    def getData(self):
        try:
            conn = connect('dump/cache4.db')
            list = []

            sql = "SELECT * from media_v2 where type = '3';"
            cur = conn.cursor()  # reader
            cur.execute(sql)
            records = cur.fetchall()
            if records != None:

                for rec in records:
                    data = rec[4]
                    # print(data.hex())
                    if data[0:4].hex() == 'fa555555' and rec[2] != 0:

                        msgID = (data[8:12].hex())
                        msgID = int((struct.pack('<L', int(msgID, base=16))).hex(), 16)
                        msgID = -((msgID) & 0x80000000) | ((msgID) & 0x7fffffff)
                        senderID = (data[16:20].hex())
                        senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))
                        recivedID = (data[24:28].hex())
                        recivedID = str(int((struct.pack('<L', int(recivedID, base=16))).hex(), 16))
                        timestamp = rec[2]
                        timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))
                        offset32 = (data[32:33].hex())  # hexa value of offset32

                        if offset32 != '':
                            res = int(offset32, 16)  # convert to decimal
                            url = data[33:33 + res]
                        if offset32 != 'fe' and len(url) != 0:
                            url = (data[33:33 + res]).decode("utf-8")
                            msgsize = len(url)
                        else:
                            offset33 = (data[33:36].hex())  # convert to hexa
                            res = int(offset33, 16)  # convert to decimal
                            url = (data[36:36 + res]).decode("utf-8")
                            msgsize = getsizeof(url)

                        sql = "SELECT * from enc_chats where admin_id=" + senderID + " and user=" + recivedID + " ;"
                        cur = conn.cursor()
                        cur.execute(sql)
                        records = cur.fetchall()
                        if records != None:
                            sql = "SELECT name from users where uid=" + senderID + ";"
                            cur = conn.cursor()
                            cur.execute(sql)
                            senderrec = cur.fetchone()
                            sendername = senderrec[0]
                            sql = "SELECT name from users where uid=" + recivedID + " ;"
                            cur = conn.cursor()
                            cur.execute(sql)
                            recivedrec = cur.fetchone()
                            recivedname = "Host"
                            if recivedrec != None:
                                recivedname = recivedrec[0]
                            type = "Secret chat"
                            list.append(SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                  str(url), str(type)))


        except Error as e:
            print('Error', e)

        try:
            sql = "SELECT * from media_v2 where type = '3';"
            cur = conn.cursor()  # reader
            cur.execute(sql)
            mediarec = cur.fetchall()

            for rec in mediarec:
                mediaBlob = rec[4]
                if ((mediaBlob[0:4].hex() != 'fa555555') and (rec[1] > 0)):

                    midrec = rec[0]

                    sql = "SELECT * from messages where mid=" + str(midrec) + " and out='1' ;"
                    cur = conn.cursor()
                    cur.execute(sql)
                    sentrec = cur.fetchone()
                    if sentrec != None and sentrec[4] != 0:
                        data = sentrec[5]

                        msgID = (data[8:12].hex())
                        msgID = int((struct.pack('<L', int(msgID, base=16))).hex(), 16)
                        senderID = (data[16:20].hex())
                        senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))
                        recivedID = (data[24:28].hex())
                        recivedID = str(int((struct.pack('<L', int(recivedID, base=16))).hex(), 16))
                        timestamp = sentrec[4]
                        timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))
                        offset32 = (data[32:33].hex())
                        if offset32 != '':
                            res = int(offset32, 16)  # convert to decimal
                            url = data[33:33 + res]
                            if offset32 != 'fe' and len(url) != 0:
                                url = (data[33:33 + res]).decode("utf-8")

                            else:
                                offset33 = (data[33:36].hex())  # convert to hexa
                                res = int(offset33, 16)  # convert to decimal
                                url = (data[36:36 + res]).decode("utf-8")

                            sql = "SELECT name from users where uid=" + senderID + ";"
                            cur = conn.cursor()
                            cur.execute(sql)
                            senderrec = cur.fetchone()
                            sendername = ""
                            if senderrec != None:
                                sendername = senderrec[0]
                            sql = "SELECT name from users where uid=" + recivedID + " ;"
                            cur = conn.cursor()
                            cur.execute(sql)
                            recivedrec = cur.fetchone()
                            recivedname = ""
                            if recivedrec != None:
                                recivedname = recivedrec[0]
                            type = "Normal chat"
                            list.append(SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                  str(url), str(type)))
        except Error as e:
            print('Error', e)
        try:
            sql = "SELECT * from media_v2 where type = '3';"
            cur = conn.cursor()  # reader
            cur.execute(sql)
            mediarec = cur.fetchall()

            for rec in mediarec:
                mediaBlob = rec[4]
                if ((mediaBlob[0:4].hex() != 'fa555555') and (rec[1] > 0)):

                    midrec = rec[0]
                    sql = "SELECT * from messages where mid=" + str(midrec) + " and out= 0 ;"
                    cur = conn.cursor()
                    cur.execute(sql)
                    sentrec = cur.fetchone()
                    if sentrec != None and sentrec[4] != 0:
                        data = sentrec[5]

                        msgID = (data[8:12].hex())
                        msgID = int((struct.pack('<L', int(msgID, base=16))).hex(), 16)
                        senderID = (data[16:20].hex())
                        senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))
                        timestamp = sentrec[4]
                        timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))
                        offset32 = (data[32:33].hex())
                        if offset32 != '':
                            res = int(offset32, 16)  # convert to decimal
                            url = data[33:33 + res]
                            if offset32 != 'fe' and len(url) != 0:
                                url = (data[33:33 + res]).decode("utf-8")

                            else:
                                offset33 = (data[33:36].hex())  # convert to hexa
                                res = int(offset33, 16)  # convert to decimal
                                url = (data[36:36 + res]).decode("utf-8")

                            sql = "SELECT name from users where uid=" + senderID + ";"
                            cur = conn.cursor()
                            cur.execute(sql)
                            senderrec = cur.fetchone()
                            sendername = ""
                            if senderrec != None:
                                sendername = senderrec[0]

                            recivedname = "Host"
                            type = "Normal chat"

                            list.append(SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                  str(url), str(type)))
        except Error as e:
            print('Error', e)

        try:

            sql = "SELECT * from media_v2 where type = '3';"
            cur = conn.cursor()  # reader
            cur.execute(sql)
            mediarec = cur.fetchall()

            for rec in mediarec:
                if rec[2] != 0:
                    mediaBlob = rec[4]
                    mid = rec[0]
                    uid = rec[1]
                    midLen = str(mid)
                    if ((mid > 0) and (len(midLen) < 16) and (uid < 0) and (mediaBlob[0:4].hex() != '6258082b') and (
                            mediaBlob[0:4].hex() != 'fa555555') and (uid != 777000)):
                        midrec = rec[0]

                        # print("msgID  "+str(midrec))
                        sql = "SELECT * from messages where mid=" + str(midrec) + ";"
                        cur = conn.cursor()
                        cur.execute(sql)
                        sentrec = cur.fetchone()
                        if sentrec != None:
                            data = sentrec[5]
                            msgID = sentrec[0]
                            senderID = (data[16:20].hex())
                            senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))
                            name = abs(sentrec[1])
                            name = str(name)
                            timestamp = sentrec[4]
                            timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))
                            offset32 = (data[32:33].hex())

                            if offset32 != '':
                                res = int(offset32, 16)  # convert to decimal
                                url = data[33:33 + res]
                                if offset32 != 'fe' and len(url) != 0:
                                    url = (data[33:33 + res]).decode("utf-8")

                                else:
                                    offset33 = (data[33:36].hex())  # convert to hexa
                                    res = int(offset33, 16)  # convert to decimal
                                    url = (data[36:36 + res]).decode("utf-8")


                            sql = "SELECT name from chats where uid=" + name + ";"
                            cur = conn.cursor()
                            cur.execute(sql)
                            namerrec = cur.fetchone()
                            namef = namerrec[0]

                            recivedname = "Brodcast to " + namef

                            sql = "SELECT name from users where uid=" + senderID + ";"
                            cur = conn.cursor()
                            cur.execute(sql)
                            senderrec = cur.fetchone()
                            sendername = senderrec[0]

                            type = 'Group message'
                            list.append(SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                  str(url), str(type)))

        except Error as e:
            print('Error', e)

        try:

            sql = "SELECT * from media_v2 where type = '3';"
            cur = conn.cursor()  # reader
            cur.execute(sql)
            mediarec = cur.fetchall()

            for rec in mediarec:
                if rec[2] != 0:
                    mediaBlob = rec[4]
                    mid = rec[0]
                    uid = rec[1]
                    midLen = str(mid)
                    if ((mid > 0) and (len(midLen) >= 16) and (uid < 0) and (mediaBlob[0:4].hex() != '6258082b')):

                        midrec = rec[0]

                        # print("msgID  "+str(midrec))
                        sql = "SELECT * from messages where mid=" + str(midrec) + ";"
                        cur = conn.cursor()
                        cur.execute(sql)
                        sentrec = cur.fetchone()
                        if sentrec != None:
                            data = sentrec[5]
                            msgID = sentrec[0]
                            name = abs(sentrec[1])
                            name = str(name)
                            timestamp = sentrec[4]
                            timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))
                            offset32 = (data[24:25].hex())  # hexa value of offset32

                            if offset32 != '':
                                res = int(offset32, 16)  # convert to decimal
                                url = data[25:25 + res]
                                if offset32 != 'fe' and len(url) != 0:
                                    url = (data[25:25 + res]).decode("utf-8")

                                else:
                                    offset33 = (data[25:28].hex())  # convert to hexa
                                    res = int(offset33, 16)  # convert to decimal
                                    url = (data[28:28 + res]).decode("utf-8")


                            sql = "SELECT name from chats where uid=" + name + ";"
                            cur = conn.cursor()
                            cur.execute(sql)
                            namerrec = cur.fetchone()
                            namef = namerrec[0]

                            sendername =" Broadcast"
                            recivedname = "Broadcast to " + namef

                            type = 'channel message'
                            list.append(SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                      str(url), str(type)))

        except Error as e:
            print('Error', e)


        list_sorted = sorted(list)
        return list_sorted
