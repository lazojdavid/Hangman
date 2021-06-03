#make hangman game
import random
import os
cls = lambda : os.system("cls")
body =[''' 
       +---+

     |   |

         |

         |

         |

         |

  =========''', 


  '''
    +---+

    |   |

    O   |

        |

        |

        |

  =========''', 

  '''
    +---+

    |   |

    O   |

    |   |

        |

        |
   =========''',


  '''
    +---+

    |   |

    O   |

   /|   |

        |

        |

  =========''', 

  '''
    +---+

    |   |

   O   |

   /|\  |

        |

        |

  =========''',

  '''
    +---+

    |   |

    O   |

   /|\  |

   /    |

        |

  =========''', 

  '''
    +---+

    |   |

    O   |

   /|\  |

   / \  |

        |

  =========''']

def words(a):
    #se encarga de buscar los datos
    # remidn appendm more databases
    if a == 1:
        print("Lista de palabras ROPA")
        with open("./base_datos/list_clothes.txt", "r", encoding = "utf-8") as f:
            list_words = []
            for line in f:
                list_words.append(line.strip("\n"))
            select_word(list_words)

    if a == 2:
        print("Lista de palabras ROPA")
        with open("./base_datos/list_animals.txt", "r", encoding = "utf-8") as f:
            list_words = []
            for line in f:
                list_words.append(line.strip("\n"))
            select_word(list_words)

    if a == 3:
        print("Lista de palabras ROPA")
        with open("./base_datos/list_familiar.txt", "r", encoding = "utf-8") as f:
            list_words = []
            for line in f:
                list_words.append(line.strip("\n"))
            select_word(list_words)
# draw_man recibe la lista con las palabras
def select_word(list_words):
    #selecciono la palabra al azar
    size = len(list_words)
    index_random = random.randint(0,size-1)
    word_random = list_words[index_random]
    tabs ="_" * len(word_random)
    attemps(word_random,tabs)       
def menu():
    # para hacer mi menú de las palabras que quiero usar
    print(""" 
             (0 0) 
     ---oOO-- (_) ----oOO---    
    ╔═════════════════════════╗ 
    ║ WELCOME TO HANGMAN GAME ║ 
    ╚═════════════════════════╝ 
       -------------------
            |__|__| 
             || || 
            ooO Ooo 

    Por: vasquezlazoj
            """)
    
    options = int(input("Seleciona una lista:\n1. Ropa:\n2. Animales\n3. Familiares\n"))
    if options == 1:
        cls()
        words(1)
    if options == 2:
        cls()
        words(2)
    if options == 3:
        cls()
        words(3)


    pass
def draw_body(b):
    print(body[b])
def attemps(word_random, tabs): 
    life = 3
    print(f'Empiezas con {life} vidas\n')
    letter_good =""
    body_ini = print(body[0])
    tabs_ini ="_ "*len(word_random)
    b = 0
    print(tabs_ini)
    while life > 0:
        intento = input("Adivina una letra: \n")
        while len(intento) == 0:
            print("Debes ingresar al menos una letra: ")
            intento = input()
        intento = intento.lower()
        cls()
        if life < 3:
            draw_body(b)
        letra_repite = 0
        for i in range(len(word_random)):
            if intento in word_random[i]:
                #recupera hasta un espacio antes donde está esa letra, luego suma la letra y depsues rellena con tabs
                tabs = tabs[:i] + word_random[i] + tabs[i+1:]
                letra_repite += 1
        #guarda el numero de veces que se repite una letra
        letter_good += intento*letra_repite
        if intento not in word_random:
            b +=2
            cls()
            print("Letra incorrecta ! !")
            draw_body(b)
            life -= 1
            if life == 0:
                print("***PERDISTE***")
                print(f'Te quedaste sin vidas, la palabra era {word_random}')        
                respueta = int(input("Quieres volver a jugar?:\n1. Si\n2: No\n"))
                cls()
                if respueta == 1:
                    menu()
                else:
                    break
                    
            print(f'te quedan {life} vidas, tu puedes ! ')
        else:
            cls()
            print("Muy bien sigue asi")
            draw_body(b)
        for intento in tabs:        
            print(intento, end=" ")
        print()
        if len(letter_good) == len(word_random):
            print("***Lo lograste***")
            print()
            respueta = int(input("Quieres volver a jugar?:\n1. Si\n2: No\n"))
            if respueta == 1:
                cls()
                menu()    
            else:
                break
def run():
    pass
if __name__=='__main__':
    menu()
