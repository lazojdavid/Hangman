#probar reemplazar cadenas
word = "casa"
tabs = "_ "*len(word)
intento = input("Adivina una letra:\n")
if intento not in word:
    print("no")
else:
    print("yes")
    #replace
    a = tabs.replace("_ ",intento)
    print(a)
     
