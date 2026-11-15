import random

losowaLiczbaMagika = random.randint(0,100)
# losujemy liczbe magika, obowiązkowo przed pętlami Zeby liczba nie zmieniała się za każdą próbą użytkownika ją zgadnąć

print(
    """
    +================================+
    | Cześć przyjacielu!             |
    | Zgadniesz moją liczbę -        |
    | wypuszce cię z mojej           |
    | magicznej pętli                |
    | No to co? Jaką liczbę podałem? |
    +================================+
    """)

def zgadywanieprzezu():
    # for i in range(5):
    i = 0
    while i < 5:
           zgadywanie = int(input("podaj liczbę: "))
           if losowaLiczbaMagika == zgadywanie:
              print("Brawo! Zgadnąłeś/aś!")
              return
           # jeśli liczba zostanie zgadnięta, program kończy pracę
           elif losowaLiczbaMagika > zgadywanie:
              print("""
              +===============================================+
              |Nie zgadnąłeś/aś, ale mogę dać małą podpowiedż:|
              |moja liczba jest większa ;)                    |
              +===============================================+
              """)
              i+=1
           # przy każdej próbie + 1 do liczby prób użytkownika
           elif losowaLiczbaMagika < zgadywanie:
               print("""
               +===============================================+
               |Nie zgadnąłeś/aś, ale mogę dać małą podpowiedż:|
               |moja liczba jest mniejsza ;)                   |
               +===============================================+
               """)
               i+=1
           #  i tutaj też
           # przy każdej próbie + 1 do liczby prób użytkownika
           if i == 5 and losowaLiczbaMagika!=zgadywanie:
                #jeślim próda = 5 i kiczba nie została zgadnięta 
                print("twój czas się skończył :(")

zgadywanieprzezu()
# wywołanie funkcji

