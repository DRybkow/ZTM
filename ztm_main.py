import json,  logging
import time, os,threading
from stop import stop
from mapa import naMapie
from wydrukTabeli import printTable
from wydrukTabeli import table
from url import urlErr
from id import StopID
from ulubione import DB

'''
ver.02
opis funkcji
refaktoring funkcjonowania tak żeby control flow był w main a funkcje robiły to co mają robić
dodanie ZTM Gda+
dostosowanie wyświetlacza Gda do Gdy(czas)
nowa funkcjonalność zapisu bazy przystanków do pliku
możliwość powrotu do listy wyszukiwania wraz z "odśwież" i "nowy"
dodanie funkcji zatrzymującej działanie programu na każdym etpie wprowadzania danych przez użytkownika
wielowątkowość w kwestii zaciągnięcia bazy ID przystanków(ograniczyłem do timeout na wprowadzenie z klawiatury www)
opcja wyszukiwania po współrzędnych, dostosowanie struktury
wyświetlanie wybranego przystanku na mapie
ver.03
usunięcie rozgraniczenia na import Gda/Gdy
dostosowanie funkcjonalności do JSON Gda
exept na złe połączenie internetowe
ver.04
rozbicie na packages
wprowadzenie class
dodanie funkcji ulubionych w SQLite3
'''
class Net():

    ## Pobranie danych w formacie JSON z API witryny ckan.multimediagdansk.pl z bazą ID przystanków
    def jsonData(self): 
        url ='https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json'
        response=urlErr(url)
        busStopTab = json.loads(response.text)
        with open('busStopData.json', 'w') as f:
            json.dump(busStopTab, f)
        return busStopTab

    ## Odczyt ID przystanków w formacie JSON z pliku
    def jsonDataFile(self):
        with open('busStopData.json') as f:
            busStopTab = json.load(f)
        return busStopTab

    ## Pobranie danych w formacie JSON z API witryny https://mapa.ztm.gda.pl/
    def jsonDataStop(t):
        url ='https://mapa.ztm.gda.pl/departures?stopId=%s' % (t[int(nr)-1][1])
        # logging.info(url)
        response=urlErr(url)
        stopData = json.loads(response.text)
        return stopData

#***********************************************************************************
#START programu 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Początek programu')
# logging.disable(logging.CRITICAL) ## wł/wył LOGGING

## opcja uruchomienia importowania danych ID z serwera
timeout = 10
th = threading.Timer(timeout, print, ['\nZatwierdź wykożystanie bazy ID przystanków z pliku:'])
th.start()
os.system('cls')
prompt = f'\nWitaj User One!\n\n{timeout} sekund na wprowadzenie "www" w celu zaciągnięcia najnowszej/inicjacyjnej bazy przystanków\nw przeciwnym wypadku kontynuuj z pliku -> ENTER\nwpisz "X" w dowolnym momencie żeby zakończyć program\n'
xs = input(prompt)
th.cancel()
stop(xs)
if xs.upper()=='WWW':
    stops=Net().jsonData()
else:
    stops=Net().jsonDataFile()
while True:
    xt=input('''Będziemy wyszukiwać po:
->nazwie przystanku:    Wcisnij: "enter"
->ulubionych:           Wcisnij: "u"
->współrzędnych:        Wprowadź: "wsp"\n''')
    stop(xt)
    while True:
        if xt.upper()=='WSP':
            d=0.003
            t,j=StopID.poWsp(stops)
        elif xt.upper()=='U':
            u=DB.ulubione()
            t,j=StopID.poUlubionych(u)
        else:
            t,j=StopID.poNazwie(stops)
        if j>=30:
            print ('Liczba przystanków 30, doprecyzuj kryteria wyszukiwania...')
            break
        if t==[]:
            print('Brak przystanku w bazie spełniającego kryteria wyszukiwania.\n')
            break
        else:
            print ('\nWybierz przystanek do wyświetlenia, wpisz nr i zatwierdź ENTER: ')
            while True:
                nr=input()
                stop(nr)
                if nr.isdigit() and 0<int(nr)<=j:
                    break
                print('Podaj poprawny numer:')
            naMapie(t,nr)
            while True:
                stopData=Net.jsonDataStop(t)
                printTable(table(stopData),nr,t)
                xl=input('''
-> Odśwież                              -> wciśnij: "enter" 
-> Nowe wyszukiwanie                    -> wpisz:   "nowe" 
-> Wybierz ponownie z listy             -> wpisz:   "lista"
-> Wyświel na mapie                     -> wpisz:   "mapa"
-> Dodaj do ulubionych                  -> wpisz:   "u"
-> Aby zakończyć                        -> wpisz:   "x"\n''')
                stop(xl)
                if xl.upper()=='LISTA':
                    break
                elif xl.upper()=='MAPA':
                    naMapie(t,nr)
                elif xl.upper()=='NOWE':
                    break
                elif xl.upper()=='U':
                    DB.wstaw(t[int(nr)-1])
                print('Odświeżanie.',end='')
                for x in range (3):
                    time.sleep(0.3)
                    print('.',end='')
            if xl.upper()=='LISTA':
                print('Przystanek z listy...')
            elif xl.upper()=='NOWE':
                print('\nNowe wyszukiwanie...')
                break
