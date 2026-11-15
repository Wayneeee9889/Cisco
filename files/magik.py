import random

losowaLiczbaMagika = random.randint(0,100)

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
    for i in range(5):
        zgadywanie = int(input("podaj liczbę: "))
        while zgadywanie != losowaLiczbaMagika:
           if losowaLiczbaMagika == zgadywanie:
              print("Brawo! Zgadnąłeś/aś!")
               return
           elif losowaLiczbaMagika > zgadywanie:
              print("""
              +===============================================+
              |Nie zgadnąłeś/aś, ale mogę dać małą podpowiedż:|
              |moja liczba jest większa ;)                    |
              +===============================================+
              """)
           elif losowaLiczbaMagika < zgadywanie:
               print("""
               +===============================================+
               |Nie zgadnąłeś/aś, ale mogę dać małą podpowiedż:|
               |moja liczba jest mniejsza ;)                   |
               +===============================================+
               """)
           else:
                print("Twój czas się skończył")
                return

zgadywanieprzezu()
# bez while
