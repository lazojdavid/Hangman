
#probar reemplazar cadenas
life = 3
word = "casa"
tabs = "_"*len(word)
letras =""
while life > 0:
    intento = input("Adivina una letra:\n")
    numero_repite = 0
    for i in range(len(word)):
        if intento in word[i]:
    # primero quita el espacio vaio, luego pone la letra de ese indice que está y despues completa los demás espacios con guiones
    # y apartir del segundo espacio , prueba con los siguientes valores para saber si se encuentra y los reemplazará
            tabs = tabs[:i] + word[i] + tabs[i+1:]
            numero_repite += 1
    letras += intento*numero_repite
    if intento not in word:
        life -= 1
    for intento in tabs:
        print(intento, end=" ")
    
    print()
    print(f'te quedan {life} vidas\n')    
    if len(letras) == len(word):
        print("Fin del juego")
    print(letras)
