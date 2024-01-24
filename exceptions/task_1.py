def readint(prompt, min, max):
    try:
        num = int(input(prompt))
        assert max > num and num > min
        return num
    except AssertionError:
        print('Błąd: podana liczba jest spoza dozwolonego zakresu (-10..10)')
        raise
    except:
        print('Błąd: wprowadzono nieprawidłową liczbę')
        raise

try:
    v = readint("Podaj liczbe od -10 do 10: ", -10, 10)
    print("Liczba to:", v)
except:
    pass