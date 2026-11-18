""" Alusta
Küsi kasutajalt perekonnanime
Küsi kasutajalt sugu (m või n)
Kui sugu == "m" väljasta "Tere, härra [Perekonnanimi]!"
Muidu KUI sugu == "n"väljasta "Tere, proua [Perekonnanimi]!"
Muidu väljasta "Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis)."
Lõpeta """

perekonnanimi = input("Sisesta oma perekonnanimi: ")
sugu = input("Sisesta oma sugu (m/n): ")

if sugu == "m":
    print(f"Tere, härra {perekonnanimi}!")
elif sugu == "n":
    print(f"Tere, proua {perekonnanimi}!")
else:
    print(f"Tere tulemast, {perekonnanimi}! (sugu ei olegi tähtis).") 