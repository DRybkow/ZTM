import webbrowser
from stop import stop

## Wyświetlenie wybranego przystanku na mapie google
def naMapie(t,nr):
    k=input('wyświetlić wybrany przystanek na mapie? -> wpisz: "tak" \nbez wyświetlania                        -> wciśnij:"enter"\n')
    stop(k)
    if k.upper()=='TAK':
        webbrowser.open(f'https://www.google.pl/maps/@{t[int(nr)-1][4]},{t[int(nr)-1][5]},17z')
