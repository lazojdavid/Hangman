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
        draw_man(list_words)

# draw_man recibe la lista con las palabras
def draw_man(list_words):
    #selecciono la palabra al azar
    size = len(list_words)
    random_word = random.randint(0,size-1)
    print(list_words[random_word])

def attemps():
    pass

def run():
    pass
if __name__=='__main__':
    words()

