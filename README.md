# Opis 
## **Wyświetlacz tablicy ZTM**
Program przetwarza zasoby API ZTM Gdańsk w formacie JSON w celu wyświetlenia tablicy przystankowej w obrębie transportu publicznego Trójmiasta i okolic.

# Funkcjonalności
* wyszukiwanie przez:
    * wprowadzenie nazwy przystanku
    * wybór ulubionego
    * wybór z mapy
* lista ulubionych
* wyświetlanie na mapie

# Instalacja
Python 3.10.3

Biblioteki:

pip install

`time` `webbrowser` `pyperclip` `redatetime` `sys` `sqlite3` `requests` `colorama` `os` `json` `logging` `threading`

# Obsługa programu
*uruchomienie*:
`ztm_main.py`

![alt text](files/1.PNG)

* w przypadku pierwszego uruchomienia należy wpisać `www` w przeciągu 10 sekund aby pobrać bazę przystanków
* wciśnięcie `enter` spowoduje przejście do opcji wyszukiwania
* w każdym momencie można wyjść z programu wybierając `x`

![alt text](files/3.PNG)
* wyszukiwanie przez:
    * wprowadzenie nazwy przystanku
    * wybór ulubionego
    * wybór z mapy

---
## Wyszukiwanie przez wprowadzenie nazwy przystanku
![alt text](files/4_2.PNG)

wybranie opcji wyszukiwania po nazwie `enter` podanie `”traug”` podaje listę z której wybieramy odpowiedni przystanek

![alt text](files/4_3.PNG)

po wprowadzeniu `<numeru>` i zatwierdzeniu `enter` mamy możliwość wyświetlenia przystanku na mapie wpisując `tak` bądź przejścia do wyświetlenia tablicy


![alt text](files/4_4.PNG)

Wyświetlacz pokazuje numer kierunek jazdy oraz czas przyjazdu w formacie, odliczanie do 30min powyżej 30 min godzina:minuta.

Dostępne są opcje odświeżania `enter` nowego wyszukiwania `nowe` ponownego wyboru z listy `nowe` wyświetlenie wybranego przystanku na mapie `mapa` oraz dodanie do ulubionych `u`.

---
## Wybór z mapy
![alt text](files/5_1.PNG)

Wyszukiwanie po współrzędnych przez skopiowanie z aplikacji `google.maps`


![alt text](files/5_2.PNG)

Rozwinięcie okna w dowolnym punkcie daje możliwość skopiowania pierwszego na liście zestawu współrzędnych.


![alt text](files/5_3.PNG)

Po zatwierdzeniu skopiowania otrzymujemy listę przystanków będących w zakresie ~300m od wskazanego punktu.


![alt text](files/5_4.PNG)

Jak w przypadku wyszukiwania po nazwie otrzymujemy wyświetlacz dla wybranego przystanku

---
## Wybór z ulubionych
![alt text](files/6_1.PNG)

Po dodaniu wyszukanych tablic możemy skorzystać z wyszukiwania z grupy ulubionych.
Edycja listy poprzez wpisanie numeru i zatwierdzenie. 
Samo zatwierdzenie `enter` da nam możliwość wpisania numeru do wyświetlenia.


*Print screen gif*
![alt text](files/ztm_gif.gif)


