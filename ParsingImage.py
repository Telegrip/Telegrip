import datetime
import os
import struct
import time
from sqlite3 import *
from sys import getsizeof


class SortItems(object):

    def __init__(self, msgID, sendername, recivedname, timestamp, file, Patth, type):
        self.msgID = msgID
        self.sendername = sendername
        self.recivedname = recivedname
        self.file = file
        self.timestamp = timestamp
        self.Patth = Patth
        self.type = type

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.sendername == other.sendername and self.recivedname == other.recivedname

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class ParsingImage():
    def getData(self):
        conn = connect('dump\cache4.db')
        directory = r'dump\cache'
        list = []
        for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                Patth = os.path.join(directory, filename)

                file = filename
                if ((file[0:1] != '-') and (file[0:1] != 'q') and (file.find('_') != -1)):

                    char = file.index('_')
                    part1 = filename[:char]  # take the first part before _
                    part1Hex = str(hex(int(part1)))  # convert to hexa
                    part1Hex = part1Hex[2:]  # clip the begaining (0x)
                    part1Hex = bytearray.fromhex(part1Hex)  # bytecode
                    part1Hex.reverse()  # bytecode reverse
                    part1Hex = part1Hex.hex()
                    originalhex = part1Hex

                    try:

                        sql = "SELECT * from media_v2 where type = '0';"
                        cur = conn.cursor()  # reader
                        cur.execute(sql)
                        records = cur.fetchall()
                        if records != None:

                            for rec in records:
                                data = rec[4]

                                # print(data.hex())
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
                                        list.append(
                                            SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                      str(file), str(Patth), str(type)))
                                        # os.system("start " + ImagePath)
                                        # os.startfile(ImagePath, 'open')




                    except Error as e:
                        print('Error', e)


            else:
                continue

        directory = r"dump\Telegram Images"
        for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                Patth = os.path.join(directory, filename)

                file = filename

                char = file.index('_')
                part1 = filename[:char]  # take the first part before _
                part2 = filename[char + 1:len(file) - 4]  # clip the last+take the seconed part after _

                part1Hex = str(hex(int(part1)))  # convert to hexa
                part1Hex = part1Hex[2:]  # clip the begaining (0x)

                part2Hex = str(hex(int(part2)))  # convert to hexa
                part2Hex = part2Hex[2:]  # clip the begaining (0x)
                if len(part2Hex) == 5:
                    part2Hex = "0" + part2Hex

                part1Hex = bytearray.fromhex(part1Hex)  # bytecode
                part1Hex.reverse()  # bytecode reverse
                part1Hex = part1Hex.hex()
                part2Hex = bytearray.fromhex(part2Hex)  # bytecode
                part2Hex.reverse()  # bytecode reverse
                part2Hex = part2Hex.hex()

                originalhex = str(part1Hex) + "000000" + str(part2Hex)


                try:

                    sql = "SELECT * from media_v2 where type = '0';"
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
                                # print("blob "+data.hex())
                                # print("vedio "+originalhex)
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

                                    typeM='Normal message'
                                    list.append(
                                        SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                  str(file), str(Patth),str(typeM)))
                                    # os.system("start " + VedioPath)
                                    # os.startfile(ImagePath, 'open')






                except Error as e:
                    print('Error', e)


            else:
                continue
        for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                Patth = os.path.join(directory, filename)

                file = filename

                char = file.index('_')
                part1 = filename[:char]  # take the first part before _
                part2 = filename[char + 1:len(file) - 4]  # clip the last+take the seconed part after _

                part1Hex = str(hex(int(part1)))  # convert to hexa
                part1Hex = part1Hex[2:]  # clip the begaining (0x)

                part2Hex = str(hex(int(part2)))  # convert to hexa
                part2Hex = part2Hex[2:]  # clip the begaining (0x)
                if len(part2Hex) == 5:
                    part2Hex = "0" + part2Hex

                part1Hex = bytearray.fromhex(part1Hex)  # bytecode
                part1Hex.reverse()  # bytecode reverse
                part1Hex = part1Hex.hex()
                part2Hex = bytearray.fromhex(part2Hex)  # bytecode
                part2Hex.reverse()  # bytecode reverse
                part2Hex = part2Hex.hex()

                originalhex = str(part1Hex) + "000000" + str(part2Hex)

                try:

                    sql = "SELECT * from media_v2 where type = '0';"
                    cur = conn.cursor()  # reader
                    cur.execute(sql)
                    mediarec = cur.fetchall()

                    for rec in mediarec:
                        mediaBlob = rec[4]
                        if ((mediaBlob[0:4].hex() != 'fa555555') and (rec[1] > 0)):
                            midrec = rec[0]
                            # print("msgID  "+str(midrec))
                            sql = "SELECT * from messages where mid=" + str(midrec) + " and out='0' ;"
                            cur = conn.cursor()
                            cur.execute(sql)
                            sentrec = cur.fetchone()
                            if sentrec != None:
                                data = sentrec[5]
                                # print("blob "+data.hex())
                                # print("vedio "+originalhex)
                                if originalhex in data.hex() and sentrec[4]!=0:

                                    msgID = (data[8:12].hex())  # hexa
                                    msgID = int((struct.pack('<L', int(msgID, base=16))).hex(), 16)
                                    senderID = (data[16:20].hex())
                                    senderID = str(int((struct.pack('<L', int(senderID, base=16))).hex(), 16))

                                    # recivedID = (data[24:28].hex())
                                    # recivedID = str(int((struct.pack('<L', int(recivedID, base=16))).hex(), 16))
                                    timestamp = sentrec[4]
                                    timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))



                                    sql = "SELECT name from users where uid=" + senderID + ";"
                                    cur = conn.cursor()
                                    cur.execute(sql)
                                    senderrec = cur.fetchone()
                                    sendername = ""
                                    if senderrec != None:
                                        sendername = senderrec[0]

                                    recivedname = "Host"

                                    typeM = 'Normal message'
                                    list.append(
                                        SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                  str(file), str(Patth), str(typeM)))
                                    # os.system("start " + VedioPath)
                                    # os.startfile(ImagePath, 'open')






                except Error as e:
                    print('Error', e)


            else:
                continue

        for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                Patth = os.path.join(directory, filename)

                file = filename

                char = file.index('_')
                part1 = filename[:char]  # take the first part before _
                part2 = filename[char + 1:len(file) - 4]  # clip the last+take the seconed part after _

                part1Hex = str(hex(int(part1)))  # convert to hexa
                part1Hex = part1Hex[2:]  # clip the begaining (0x)

                part2Hex = str(hex(int(part2)))  # convert to hexa
                part2Hex = part2Hex[2:]  # clip the begaining (0x)
                if len(part2Hex) == 5:
                    part2Hex = "0" + part2Hex

                part1Hex = bytearray.fromhex(part1Hex)  # bytecode
                part1Hex.reverse()  # bytecode reverse
                part1Hex = part1Hex.hex()
                part2Hex = bytearray.fromhex(part2Hex)  # bytecode
                part2Hex.reverse()  # bytecode reverse
                part2Hex = part2Hex.hex()

                originalhex = str(part1Hex) + "000000" + str(part2Hex)

                try:

                    sql = "SELECT * from media_v2 where type = '0';"
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
                            # print("msgID  "+str(midrec))
                            sql = "SELECT * from messages where mid=" + str(midrec) + ";"
                            cur = conn.cursor()
                            cur.execute(sql)
                            sentrec = cur.fetchone()
                            if sentrec != None:
                                data = sentrec[5]
                                # print("blob "+data.hex())
                                # print("vedio "+originalhex)
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
                                    sendername = ""
                                    if senderrec != None:
                                        sendername = senderrec[0]

                                    recivedname = "Broadcast to " + namef
                                    typeM='Group message'
                                    list.append(
                                        SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                  str(file), str(Patth), str(typeM)))







                except Error as e:
                    print('Error', e)


            else:
                continue
        for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                Patth = os.path.join(directory, filename)

                file = filename

                char = file.index('_')
                part1 = filename[:char]  # take the first part before _
                part2 = filename[char + 1:len(file) - 4]  # clip the last+take the seconed part after _

                part1Hex = str(hex(int(part1)))  # convert to hexa
                part1Hex = part1Hex[2:]  # clip the begaining (0x)

                part2Hex = str(hex(int(part2)))  # convert to hexa
                part2Hex = part2Hex[2:]  # clip the begaining (0x)
                if len(part2Hex) == 5:
                    part2Hex = "0" + part2Hex

                part1Hex = bytearray.fromhex(part1Hex)  # bytecode
                part1Hex.reverse()  # bytecode reverse
                part1Hex = part1Hex.hex()
                part2Hex = bytearray.fromhex(part2Hex)  # bytecode
                part2Hex.reverse()  # bytecode reverse
                part2Hex = part2Hex.hex()

                originalhex = str(part1Hex) + "000000" + str(part2Hex)

                try:

                    sql = "SELECT * from media_v2 where type = '0';"
                    cur = conn.cursor()  # reader
                    cur.execute(sql)
                    mediarec = cur.fetchall()

                    for rec in mediarec:
                        mediaBlob = rec[4]
                        mid = rec[0]
                        uid = rec[1]
                        midLen = str(mid)
                        if ((mid > 0) and (len(midLen) >= 16) and (uid < 0) and (mediaBlob[0:4].hex() != '6258082b')):
                            midrec = rec[0]

                            sql = "SELECT * from messages where mid=" + str(midrec) + ";"
                            cur = conn.cursor()
                            cur.execute(sql)
                            sentrec = cur.fetchone()
                            if sentrec != None:
                                data = sentrec[5]
                                # print("blob "+data.hex())
                                # print("vedio "+originalhex)
                                if originalhex in data.hex() and sentrec[4]!=0:

                                    msgID = sentrec[0]


                                    timestamp = sentrec[4]
                                    timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))
                                    name = abs(sentrec[1])
                                    name = str(name)

                                    sql = "SELECT name from chats where uid=" + name + ";"
                                    cur = conn.cursor()
                                    cur.execute(sql)
                                    namerrec = cur.fetchone()
                                    namef = namerrec[0]

                                    sendername = "Broadcast"
                                    recivedname = "Broadcast to " + namef
                                    typeM='Channel message'
                                    list.append(
                                        SortItems(str(msgID), str(sendername), str(recivedname), str(timestamp),
                                                  str(file), str(Patth), str(typeM)))




                except Error as e:
                    print('Error', e)


            else:
                continue
        list_sorted = sorted(list)
        return list_sorted



