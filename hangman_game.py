#make hangman game
import random
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

def words():
    #se encarga de buscar los datos
    # remidn appendm more databases
    with open("./ahorcado/datos.txt", "r", encoding = "utf-8") as f:
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
     
def options():
    pass

def attemps(word_random, tabs): 
    life = 3
    print(f'tienes {life} vidas\n')
    letter_good =""
    while life > 0:
        intento= input("Adivina una letra:\n")
        intento = intento.lower()
        letra_repite = 0
        for i in range(len(word_random)):
            if intento in word_random[i]:
                #recupera hasta un espacio antes donde está esa letra, luego suma la letra y depsues rellena con tabs
                tabs = tabs[:i] + word_random[i] + tabs[i+1:]
                letra_repite += 1
        #guarda el numero de veces que se repite una letra
        letter_good += intento*letra_repite
        if intento not in word_random:
            print("Letra incorrecta, tu puedes !")
            life -= 1
        for intento in tabs:
            print(intento, end=" ")
        
        print()
        if len(letter_good) == len(word_random):
            print("Fin del juego")
        print(letter_good)
        if life == 0:
            print(f'Te quedaste sin vidas, la palabra era {word_random}')
def run():
    pass
if __name__=='__main__':
    words()

