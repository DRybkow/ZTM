import time, webbrowser, pyperclip, re,datetime

from stop import stop
from ulubione import DB

class StopID():
    dt=datetime.datetime.today().strftime('%Y-%m-%d')
    d=0.003

    ## uzyskanie listy numerów ID przystanku w oparciu o wpółrzędne z mapy
    @classmethod
    def poWsp(cls,busStopTab):
        while True:
            print('\nskopiuj współrzędne z google.maps')
            time.sleep(2)
            k=input('otworzyć https://www.google.pl/maps/place/ ?   ->wpisz: "tak"\n')
            stop(k)
            if k.upper()=='TAK':
                webbrowser.open('https://www.google.pl/maps/@54.4296743,18.533523,11z' )
            input('podaj współrzędne, współrzędne skopiowane?')
            ne=pyperclip.paste()
            if re.compile(r'\d\d.+\d, \d\d.+\d').search(ne):
                n=float(ne[:16])
                e=float(ne[19:])
                print(f'Wprowadzono:\nN: {n}\nE: {e}\npromień wyszukiwania ~300m\n')
                break
            print(f'upewnij się, że masz skopiowane współrzędne\nobecnie ctr+v: {ne}')
        j=0
        t=[]
        for i in busStopTab[cls.dt]['stops']:
            while (n-cls.d)<i['stopLat']<(n+cls.d) and (e-cls.d)<i['stopLon']<(e+cls.d):
                j+=1
                StopID.iteracja(i,j,t)
                break
            if j>30:
                break
        return t,j

    ## uzyskanie listy numerów ID przystanku w oparciu o wybór z listy 
    @classmethod
    def poNazwie(cls,busStopTab): 
        print('''Wprowadź nazwę przystanku, który chcesz wyszukać:''')
        k=input()
        j=0
        stop(k)
        t=[]
        for i in busStopTab[cls.dt]['stops']:
            while k.capitalize() in i['stopDesc']:
                j+=1
                StopID.iteracja(i,j,t)
                break
            if j>30:
                break
        return t,j

    ## uzyskanie listy numerów ID przystanku w oparciu o wybór z ulubionych 
    @classmethod
    def poUlubionych(cls,u): 
        j=0
        t=[]
        for i in u:
            j+=1
            t.append([j,i[0],i[1],i[2],i[3],i[4]])
            print(j,'. ','ID: ',i[0] ,i[1],end="")
            print(' NAZWA: ',i[2],end='')
            print(' N:',i[3],' E:',i[4])
        if t==[]:
            return t,j
        print ('''
->zatwierdź                             Enter
->usuń przystanek z listy ulubionych,   wpisz nr ''')
        xr=input()
        stop(xr)
        if xr.isnumeric():
            if 0<int(xr)<=j:
                db=DB()
                db.usun(int(t[int(xr)-1][1]))
                del t[int(xr)-1]
                j-=1
        return t,j

    def iteracja(i,j,t):
        if i['zoneName']==None:
            i['zoneName']='Sterfa Gdynia'
        t.append([j,i['stopId'],i['zoneName'],i["stopDesc"],i["stopLat"],i["stopLon"]])
        print(j,'. ','ID: ',i['stopId'] ,i['zoneName'],end="")
        print(' NAZWA: ',i["stopDesc"],' KOD: ',i['stopCode'],end='')
        print(' N:',i["stopLat"],' E:',i["stopLon"])