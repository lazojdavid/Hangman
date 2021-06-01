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
    tabs ="_ " * len(word_random)
    attemps(word_random,tabs)  
     
def options():
    pass

def attemps(word_random, tabs):
    print("Welcome to the hangman game:\n ")
    life = 3
    i = 0
    #imprime el cuerpo de acuerdo a los intentos
    while life > 0:
        print(body[i])
        print(tabs)
        attemp = input("Guees the word: ")
        if attemp not in word_random:
            print("Caracter incorrecto")
        i +=1
        life -=1
    
        print("intenta de nuevo")
    print(f'Fallaste, la palabra era {word_random}')

def run():
    pass

if __name__=='__main__':
    words()

