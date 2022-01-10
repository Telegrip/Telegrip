import struct
import time
import os
from sqlite3 import *

class SortItems(object):

    def __init__(self, msgID, sendername,recivedname,timestamp,file,Patth,type):
        self.msgID = msgID
        self.sendername = sendername
        self.recivedname = recivedname
        self.file = file
        self.timestamp = timestamp
        self.Patth = Patth
        self.type=type

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.sendername == other.sendername and self.recivedname == other.recivedname

    def __lt__(self, other):
        return self.timestamp < other.timestamp

class ParsingDoc():
    def getData(self):
        conn = connect('dump\cache4.db')
        directory = r'dump\cache'
        list = []
        for filename in os.listdir(directory):
            if filename.endswith(".docx") or filename.endswith(".pptx") or filename.endswith(".pdf") or filename.endswith(".xlsx") or filename.endswith(".pages") or filename.endswith(".ppt")  or filename.endswith(".doc"):

                DocPath=os.path.join(directory, filename)
                file=filename

                filename=filename[2:]
                if file.endswith(".pdf") or filename.endswith(".doc") or filename.endswith(".ppt"):
                    filename = str(hex(int(filename[:len(filename)-4])))
                elif file.endswith(".pages"):
                    filename = str(hex(int(filename[:len(filename) - 6])))
                else:
                    filename = str(hex(int(filename[:len(filename)-5])))
                filename = filename[2:]#clip the begaining (0x)
                originalhex = bytearray.fromhex(filename)
                originalhex.reverse()
                originalhex=originalhex.hex()

                try:

                    sql = "SELECT * from media_v2 where type = '1';"
                    cur = conn.cursor()  # reader
                    cur.execute(sql)
                    records = cur.fetchall()
                    if records != None:

                        for rec in records:
                            data = rec[4]
                            
                            if originalhex in data.hex():


                                if data[0:4].hex() == 'fa555555' and rec[2]!=0:
                                    msgID = (data[8:12].hex())  # hexa
                                    msgID = int((struct.pack('<L', int(msgID, base=16))).hex(), 16)
                                    msgID = -((msgID) & 0x80000000) | ((msgID) & 0x7fffffff)
                                    senderID = (data[16:20].hex())
                                    senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))
                                    recivedID = (data[24:28].hex())
                                    recivedID = str(int((struct.pack('<L', int(recivedID, base=16))).hex(), 16))
                                    timestamp = rec[2]
                                    timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))

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
                                    type='Secret message'
                                    list.append(SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                          str(file), str(DocPath),str(type)))






                except Error as e:
                    print('Error', e)


            else:
             continue
        directory = r'dump\Telegram Documents'
        for filename in os.listdir(directory):
            if filename.endswith(".docx") or filename.endswith(".pptx") or filename.endswith(".pdf") or filename.endswith(".xlsx") or filename.endswith(".pages") or filename.endswith(".ppt")  or filename.endswith(".doc"):

                DocPath = os.path.join(directory, filename)
                file = filename


                filename = filename[2:]
                if file.endswith(".pdf") or filename.endswith(".doc") or filename.endswith(".ppt"):
                    filename = str(hex(int(filename[:len(filename) - 4])))
                elif file.endswith(".pages"):
                    filename = str(hex(int(filename[:len(filename) - 6])))
                else:
                    filename = str(hex(int(filename[:len(filename) - 5])))
                filename = filename[2:]
                originalhex = bytearray.fromhex(filename)
                originalhex.reverse()
                originalhex = originalhex.hex()

                try:

                    sql = "SELECT * from media_v2 where type = '1';"
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
                            if sentrec != None:
                                data = sentrec[5]

                                if originalhex in data.hex() and sentrec[4]!=0:

                                    msgID = (data[8:12].hex())  # hexa
                                    msgID = int((struct.pack('<L', int(msgID, base=16))).hex(), 16)
                                    senderID = (data[16:20].hex())
                                    senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))
                                    recivedID = (data[24:28].hex())
                                    recivedID = str(int((struct.pack('<L', int(recivedID, base=16))).hex(), 16))
                                    timestamp = sentrec[4]
                                    timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))

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
                                    typeN = 'Normal message'
                                    list.append(SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                          str(file), str(DocPath),str(typeN)))





                except Error as e:
                    print('Error', e)


            else:
                continue
        for filename in os.listdir(directory):
            if filename.endswith(".docx") or filename.endswith(".pptx") or filename.endswith(".pdf") or filename.endswith(".xlsx") or filename.endswith(".pages") or filename.endswith(".ppt")  or filename.endswith(".doc"):

                DocPath = os.path.join(directory, filename)
                file = filename


                filename = filename[2:]
                if file.endswith(".pdf") or filename.endswith(".doc") or filename.endswith(".ppt"):
                    filename = str(hex(int(filename[:len(filename) - 4])))
                elif file.endswith(".pages"):
                    filename = str(hex(int(filename[:len(filename) - 6])))
                else:
                    filename = str(hex(int(filename[:len(filename) - 5])))
                filename = filename[2:]
                originalhex = bytearray.fromhex(filename)
                originalhex.reverse()
                originalhex = originalhex.hex()

                try:

                    sql = "SELECT * from media_v2 where type = '1';"
                    cur = conn.cursor()  # reader
                    cur.execute(sql)
                    mediarec = cur.fetchall()





                    for rec in mediarec:
                        mediaBlob=rec[4]
                        if ((mediaBlob[0:4].hex() != 'fa555555') and (rec[1] > 0)):
                                midrec = rec[0]

                                sql = "SELECT * from messages where mid="+str(midrec)+" and out='0' ;"
                                cur = conn.cursor()
                                cur.execute(sql)
                                sentrec = cur.fetchone()
                                if sentrec != None:
                                    data = sentrec[5]

                                    if originalhex in data.hex() and sentrec[4]!=0:



                                        msgID = (data[8:12].hex())  # hexa
                                        msgID = int((struct.pack('<L', int(msgID, base=16))).hex(), 16)
                                        senderID = (data[16:20].hex())
                                        senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))

                                        timestamp = sentrec[4]
                                        timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))


                                        sql = "SELECT name from users where uid=" + senderID + ";"
                                        cur = conn.cursor()
                                        cur.execute(sql)
                                        senderrec = cur.fetchone()
                                        sendername=""
                                        if senderrec != None:
                                            sendername = senderrec[0]
                                        recivedname="Host"
                                        typeN = 'Normal message'
                                        list.append(
                                            SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                      str(file), str(DocPath),str(typeN)))








                except Error as e:
                    print('Error', e)


            else:
             continue

        for filename in os.listdir(directory):
            if filename.endswith(".docx") or filename.endswith(".pptx") or filename.endswith(".pdf") or filename.endswith(".xlsx") or filename.endswith(".pages") or filename.endswith(".ppt")  or filename.endswith(".doc"):

                DocPath = os.path.join(directory, filename)
                file = filename


                filename = filename[2:]
                if file.endswith(".pdf") or filename.endswith(".doc") or filename.endswith(".ppt"):
                    filename = str(hex(int(filename[:len(filename) - 4])))
                elif file.endswith(".pages"):
                    filename = str(hex(int(filename[:len(filename) - 6])))
                else:
                    filename = str(hex(int(filename[:len(filename) - 5])))
                filename = filename[2:]
                originalhex = bytearray.fromhex(filename)
                originalhex.reverse()
                originalhex = originalhex.hex()

                try:

                    sql = "SELECT * from media_v2 where type = '1';"
                    cur = conn.cursor()  # reader
                    cur.execute(sql)
                    mediarec = cur.fetchall()





                    for rec in mediarec:
                        mediaBlob = rec[4]
                        mid = rec[0]
                        uid = rec[1]
                        midLen = str(mid)
                        if ((mid > 0) and (len(midLen) < 16) and (uid < 0) and (mediaBlob[0:4].hex() != '6258082b') and (mediaBlob[0:4].hex() != 'fa555555') and (uid != 777000)):
                                midrec = rec[0]

                                sql = "SELECT * from messages where mid="+str(midrec)+";"
                                cur = conn.cursor()
                                cur.execute(sql)
                                sentrec = cur.fetchone()
                                if sentrec != None:
                                    data = sentrec[5]

                                    if originalhex in data.hex() and sentrec[4]!=0:



                                        msgID = sentrec[0]
                                        senderID = (data[16:20].hex())
                                        senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))
                                        name = abs(sentrec[1])
                                        name = str(name)
                                        timestamp = sentrec[4]
                                        timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))

                                        sql = "SELECT name from chats where uid=" + name + ";"
                                        cur = conn.cursor()
                                        cur.execute(sql)
                                        namerrec = cur.fetchone()
                                        namef = namerrec[0]

                                        sql = "SELECT name from users where uid=" + senderID + ";"
                                        cur = conn.cursor()
                                        cur.execute(sql)
                                        senderrec = cur.fetchone()
                                        sendername=""
                                        if senderrec != None:
                                            sendername = senderrec[0]

                                        recivedname="Broadcast to " + namef
                                        typeN = 'Group message'
                                        list.append(
                                            SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                      str(file), str(DocPath),str(typeN)))








                except Error as e:
                    print('Error', e)


            else:
             continue

        for filename in os.listdir(directory):
            if filename.endswith(".docx") or filename.endswith(".pptx") or filename.endswith(".pdf") or filename.endswith(".xlsx") or filename.endswith(".pages") or filename.endswith(".ppt")  or filename.endswith(".doc"):

                DocPath = os.path.join(directory, filename)
                file = filename


                filename = filename[2:]
                if file.endswith(".pdf") or filename.endswith(".doc") or filename.endswith(".ppt"):
                    filename = str(hex(int(filename[:len(filename) - 4])))
                elif file.endswith(".pages"):
                    filename = str(hex(int(filename[:len(filename) - 6])))
                else:
                    filename = str(hex(int(filename[:len(filename) - 5])))
                filename = filename[2:]
                originalhex = bytearray.fromhex(filename)
                originalhex.reverse()
                originalhex = originalhex.hex()

                try:

                    sql = "SELECT * from media_v2 where type = '1';"
                    cur = conn.cursor()  # reader
                    cur.execute(sql)
                    mediarec = cur.fetchall()





                    for rec in mediarec:
                        mediaBlob = rec[4]
                        mid = rec[0]
                        uid = rec[1]
                        midLen = str(mid)
                        if ((mid > 0) and (len(midLen) >= 16) and (uid < 0) and (
                                mediaBlob[0:4].hex() != '6258082b')):
                                midrec = rec[0]

                                sql = "SELECT * from messages where mid="+str(midrec)+";"
                                cur = conn.cursor()
                                cur.execute(sql)
                                sentrec = cur.fetchone()
                                if sentrec != None:
                                    data = sentrec[5]

                                    if originalhex in data.hex() and sentrec[4]!=0:



                                        msgID = sentrec[0]


                                        name = abs(sentrec[1])
                                        name = str(name)
                                        timestamp = sentrec[4]
                                        timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))

                                        sql = "SELECT name from chats where uid=" + name + ";"
                                        cur = conn.cursor()
                                        cur.execute(sql)
                                        namerrec = cur.fetchone()
                                        namef = namerrec[0]


                                        sendername = "Broadcast"

                                        recivedname="Broadcast to " + namef
                                        typeN = 'Channel message'
                                        list.append(
                                            SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                      str(file), str(DocPath),str(typeN)))








                except Error as e:
                    print('Error', e)


            else:
             continue


        list_sorted = sorted(list)
        return list_sorted
