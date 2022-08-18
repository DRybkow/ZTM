import datetime, colorama, os

## Stworzenie zasobów do wyświetlenia
def table(stopData):
    tab=[['Linia Nr ', 'Jazda w kierunku', 'Przyjazd za']]
    for departures in stopData['departures']:
        t1=datetime.datetime.strptime(departures['timestamp'],'%Y-%m-%dT%H:%M:%SZ')
        t2=datetime.datetime.strptime(departures['estimatedTime'],'%Y-%m-%dT%H:%M:%SZ')
        l=departures['routeId']
        if l>1000:
            l=l%1000
        if (t2-t1)<datetime.timedelta(hours=0.5):
            minutes=int((t2-t1)/datetime.timedelta(minutes=1))
            tab.append([str(l),departures['headsign'],'%s min'% minutes])
        else:
            tab.append([str(l),departures['headsign'],str(t2+datetime.timedelta(hours=2))[11:16]]) 
    return tab

##wydruk tabeli
def printTable(tab, nr,t):
    colWidths=[0] * 3
    for i in range (len(tab)):    
        for j in range (3):
            if len(tab[i][j])>colWidths[j]:
                colWidths[j]=len(tab[i][j])  
    os.system('cls')
    now=datetime.datetime.now().strftime('%H:%M:%S')
    print('PRZYSTANEK: ',t[int(nr)-1][2], ' - ',t[int(nr)-1][3], '\nN:',t[int(nr)-1][4], '\nE:',t[int(nr)-1][5])
    colorama.init()
    print(f"{colorama.Fore.YELLOW}")
    print(' '*colWidths[0]+' '*colWidths[1]+ now.rjust(colWidths[2]+2))
    print(tab[0][0].ljust(colWidths[0], '-')+tab[0][1].center(colWidths[1], '-')+tab[0][2].rjust(colWidths[2]+2, '-'))
    print('*'*colWidths[0]+'*'*colWidths[1]+'*'*(colWidths[2]+2))
    #logging.info('tablica danych do wydruku',tab)
    for m in tab[1:]:
        print(m[0].ljust(colWidths[0], '.')+ m[1].center(colWidths[1],'.')+ m[2].rjust(colWidths[2]+2,'.'))
    print(f"{colorama.Fore.WHITE}")
