import sqlite3
import serial
from math import sin, cos, sqrt, atan2, radians

def check(k):
     m=cp.execute("SELECT * FROM cool WHERE ID=?",(k,))
     m=m.fetchall()
     try:
             m=m[0]
             bal=cp.execute("SELECT BALANCE FROM cool WHERE ID=?",(k,))
             bal=bal.fetchall()
             bal=bal[0]
             for i in bal:
                           bal=i
                           break

             bal1=bal
             print(bal1)
             if bal1<150:
                      
                      return('not')

             else:
                        
                     return('ok')
                
     except IndexError:
                     return('not1')
            
  

                
def bill(k,b,c):
        idList.remove(k)
        idList.remove(k)
        a=cp.execute("SELECT LONGITUDE,LATITUDE from cool where id=?",(k,))
        a=a.fetchall()
        a=a[0]
        
        conn.commit()
        q=list()
        for i in a:
                q.append(i)
        R = 6373.0       
        lat2=float(b)
        lon2=float(c)
        lon1=float(q[0])
        lat1=float(q[1])
        lat2=radians(lat2)
        lon2=radians(lon2)
        lat1=radians(lat1)
        lon1=radians(lon1)
        #print(lat2,lon2,lat1,lon1)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        w = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        e = 2 * atan2(sqrt(w), sqrt(1 - w))
        distance = R * e       
                
        print("DISTANCE ",distance)
        if distance>0 and distance<=10:
                print("YOUR BILL IS 40")
                bal=cp.execute("SELECT BALANCE FROM cool WHERE ID=?",(k,))
                bal=bal.fetchall()
                bal=bal[0]
                for i in bal:
                        bal=i
                        break
               
                bal1=bal-40
                print(bal1)
                if bal1<50:
                        print("LOW BALANCE!! ")
                        
                cp.execute("UPDATE cool SET BALANCE=?  WHERE ID=?",(bal1,k))
                conn.commit()
                
        elif distance>10 and distance<=20:
                print("YOUR BILL IS 90")
                bal=cp.execute("SELECT BALANCE FROM cool WHERE ID=?",(k,))
                bal=bal.fetchall()
                bal=bal[0]
                for i in bal:
                        bal=i
                        break
                #print(bal)
                bal1=bal-90

                if bal1<50:
                     print("LOW BALANCE!! ")
                     
                cp.execute("UPDATE cool SET BALANCE=?  WHERE ID=?",(bal1,k))
                conn.commit()
        else:
                print("YOUR BILL IS 150")
                bal=cp.execute("SELECT BALANCE FROM cool WHERE ID=?",(k,))
                bal=bal.fetchall()
                bal=bal[0]
                for i in bal:
                        bal=i
                        break
                #print(bal)
                bal1=bal-150
                if bal1<50:
                    print("LOW BALANCE!! ")
                    
                cp.execute("UPDATE cool SET BALANCE=?  WHERE ID=?",(bal1,k))
                conn.commit()
                

def ins(k,b,c):
        if idList.count(k)==1:
                
                cp.execute("UPDATE cool SET LONGITUDE=? WHERE ID=?",(c[1],k))
                conn.commit()
                cp.execute("UPDATE cool SET LATITUDE=? WHERE ID=?",(b[1],k))
                conn.commit()
                print("YOU ARE BOARDING! ")
                conn.commit()
        else:
                cp.execute("SELECT * from cool where id=?",(k,))
                print("YOU ARE DEBOARDING !!!")
                bill(k,b[1],c[1])

def scan():
        global conn,cp
        #masterId=['14801BD3','4E775043']
        conn = sqlite3.connect('C://Users//Nirmayee//Downloads//project database.db')
        cp = conn.cursor()
        ser = serial.Serial('COM3')

        a=ser.readline()
        b=ser.readline()
        c=ser.readline()
        d=ser.readline()
        b=b.decode('utf-8')
        a=a.decode('utf-8')
        c=c.decode('utf-8')
        d=d.decode('utf-8')


        b=b.split('Latitude in Decimal Degrees : ')
        c=c.split('Longitude in Decimal Degrees : ')
        a=a.split('Reader 0: Card UID: ')
        print(" ")
        print(a[1],b[1],c[1])
        k=a[1].rstrip()
        k=k.replace(" ","")
        l=(k,)
        y=check(k)
        if y=='not' or y=='not1':
                print("LOW BALANCE OR YOU ARE NOT AUTHENTICATED!! SORRY! ")
                ser.close()
                scan()
        else:        
                idList.append(k)
                ins(k,b,c)
        
        #bill(l)

def init():
        global idList
        idList=list()
init()
while True:
        
        scan()

        
