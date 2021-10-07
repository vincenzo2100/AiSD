def polacz(imie,nazwisko):
    nazwisko[0].upper()    
    print(imie[0].capitalize()+"."+nazwisko.capitalize())

def foo(imie,nazwisko,zd2):
    return zd2


print(foo("Michał","Chomczyk",polacz("Michał","Chomczyk")))