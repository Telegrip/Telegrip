import datetime
import struct
import time
from sqlite3 import *


class SortItems(object):
    def __init__(self, namef, timestamp, adminrrec, Empty):
        self.namef = namef
        self.timestamp = timestamp
        self.adminrrec = adminrrec
        self.Empty=Empty

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.namef == other.namef

    def __lt__(self, other):
        return self.timestamp < other.timestamp

class channelInfo():

    def getData(Self):
        try:

            conn = connect('dump/cache4.db')
            list = []
            cur = conn.cursor()  # reader
            sql = "SELECT * from messages;"
            checkName=""
            cur.execute(sql)
            records = cur.fetchall()

            if records != None:
                for rec in records:
                    if rec[4] != 0:
                        mid = rec[0]
                        uid = rec[1]
                        data = rec[5]
                        midLen = str(mid)


                    if ((mid > 0) and (len(midLen) >= 16) and (uid < 0) and (data[0:4].hex() == '6258082b')):

                        chacreat = (data[16:20].hex())
                        chacreat = str(int((struct.pack('<L', int(chacreat, base=16))).hex(), 16))
                        name = abs(uid)
                        name = str(name)
                        timestamp = rec[4]
                        timestamp = time.strftime('%A %B %d, %Y %I:%M:%S %p', time.localtime(timestamp))

                        sql = "SELECT name from chats where uid=" + name + ";"
                        cur = conn.cursor()
                        cur.execute(sql)
                        namerrec = cur.fetchone()
                        namef = namerrec[0]

                        sql = "SELECT uid from channel_admins_v3 where did=" + name + ";"
                        cur.execute(sql)
                        admins = cur.fetchall()

                        a = ""
                        count=0
                        for ad in admins:
                            
                            adname = ad[0]

                            sql = "SELECT name from users where uid=" + str(
                                adname) + ";"  # (%s)" % admins #.format(admin_t) #% ",".join(map(str,admins))
                            cur = conn.cursor()
                            cur.execute(sql)
                            adminrrec = cur.fetchone()
                            admin = adminrrec[0]
                            count=count+1
                            a=a+" ("+str(count)+") "
                            a=a+admin

                            Empty=""
                        list.append(SortItems(str(namef), str(timestamp), str(a),Empty ))


        except Error as e:
            print('Error', e)

        list_sorted = sorted(list)
        return list_sorted
