# Clock Sort

Clock Sort to autorskie sortowanie które dzieli tablice na wybraną ilość pomniejszych tablic. 
Nawet jeśli liczba w zegarze jest mniejsza od wskazanej to algorytm dopisze '0'.

Sotowanie powstało w przeznaczeniu w odnajdowaniu kilku największych liczb,
jednak przerobiłem program tak aby spełniał wymogi zadania czyli sortuje wszystko.

Można zmienić ustawienia sortowania w pliku clockSetup:
- CLOCK_LENGTH - Zmiena długości pojedyńczego zegara
- ADD_ZEROS - Przełączyć dodawanie zer do zegara (nie przełączać Plz)
- ONLY_LAST_CLOCK - Uruchomia program zgodnie ze swoim przeznaczeniem czyli wyszukanie największych cyfr

Zmian można dokonać także w wyświetlaniu konsoli:
- AVERAGE_TIME - if True pokazuje średni czas 10 przykładów
- SHOW_ARRAYS - if True pokazuje każdą tablice
- TRIAL_VERSION - if True wrzuca do kodu niewielką tablice żeby pokazać działanie algorytmu

###Przykład działania:
`ONLY_LAST_CLOCK = False`
`CLOCK_LENGTH = 5`

`array = array = [100, 50, 5, 90, 7, 11, 4, 67, 34, 22, 12, 20, 54, 22, 6, 66]`

`[[100, 50, 5, 90, 7], [11, 4, 67, 34, 22], [12, 20, 54, 22, 6], [66, 0, 0, 0, 0]]`

`[[0, 0, 0, 0, 4], [5, 6, 7, 11, 12], [20, 22, 22, 34, 50], [54, 66, 67, 90, 100]]`

`----------------------------------------------------------------------------------`

`ONLY_LAST_CLOCK = True`
`CLOCK_LENGTH = 5`

`array = [100, 50, 5, 90, 7, 11, 4, 67, 34, 22, 12, 20, 54, 22, 6, 66]`

`[[100, 50, 5, 90, 7], [11, 4, 67, 34, 22], [12, 20, 54, 22, 6], [66, 0, 0, 0, 0]]`

`[[0, 0, 0, 0, 5], [7, 4, 11, 34, 22], [12, 20, 50, 22, 6], [54, 66, 67, 90, 100]]`

### Czas trwania algorytmu

Średni czas sortowania dla 1000 elementów w zakresie 1 - 100 w trybie `ONLY_LAST_CLOCK = False`

`--- 0.08550441265106201 seconds---`

Średni czas sortowania dla 1000 elementów w zakresie 1 - 100 w trybie `ONLY_LAST_CLOCK = True`

`--- 0.000797891616821289 seconds---`

Zwiększenie wielkości zegara przyśpiesza działanie programu