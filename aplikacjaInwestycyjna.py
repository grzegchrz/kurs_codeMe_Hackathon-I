"""
Obliczenie zysku z lokaty -> użytkownik podaje kwotę zainwestowania, liczbę miesięcy, procent. W odpowiedzi wyświetlany
będzie zysk z lokaty (suma, rozbicie na miesiące, podatek)
"""

kwotaInwestycji = int(input("Wprowadź kwotę do zainwestowania: "))
okresInwestycji = int(input("Wprowadź ilość miesięcy lokaty: "))
procentInwestycji = int(input("Wprowadź procent lokaty: "))
podatekInwestycji = 19

zyskLokaty = (kwotaInwestycji*okresInwestycji*(365/12)*(procentInwestycji/100))/365

podatekInwestycji = zyskLokaty*(podatekInwestycji/100)
print(f"Zysk lokaty wygenrowany przez {okresInwestycji} miesięcy to {zyskLokaty}")
print(f"Podatek z inwestycji {podatekInwestycji} zł")
print(f"Zarobiłeś {zyskLokaty-podatekInwestycji} zł przez {okresInwestycji} miesięcy")

zyskMiesieczny = 0
for i in range(okresInwestycji):
    zyskMiesieczny =+zyskMiesieczny + (kwotaInwestycji*(365/12)*(procentInwestycji/100))/(365/12)
    print(f"Zysk netto {zyskMiesieczny - zyskMiesieczny*(podatekInwestycji/100)} zł . W {i+1} miesięcu zysk wynosi {zyskMiesieczny}. Podatek wynosi {zyskMiesieczny*(podatekInwestycji/100)} zł")