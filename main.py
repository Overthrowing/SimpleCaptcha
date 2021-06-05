
"""
/,'  ^1*  |\/!  l0  !    ]`_        /*`  /\   !Q  *]^   /`' 1.,l  /\
 _/  ,],  1  1  1   1,_  !.         \,. /*'\  !    !    \.. 1  1 /*`\
"""

import random

verticalLines = [  # "|"
    '1', '!', '|', '[', ']', 'l'
]

bottomHorizontalLines = [  # "_"
    '_', '.', ','
]

topHorizontalLines = [  # "`"
    "`", "'", "*", '^'
]

middleHorizontalLines = [  # "-"
    '-', '=', '~'
]

empty = [  # " "
    " "
]

forwardSlants = [  # "/"
    '/'
]

backwardSlants = [  # "\"
    '\\'
]

circles = [  # "O"
    'O', "@", "0", "Q",
]



TYPE_MAPS = {
    "|": verticalLines,
    " ": empty,
    "_": bottomHorizontalLines,
    "-": middleHorizontalLines,
    "`": topHorizontalLines,
    "/": forwardSlants,
    "\\": backwardSlants,
    "O": circles
}

LETTER_MAPS = {  # 2x4 grid
    "A": [" ", "/", "\\" ," ",
        "/", "`", "`", "\\"],
    "B": [" ", "|", "O", " ",
          " ", "|", "O", " "],
    "C": [" ", "/", "`", "`",
          " ", "\\", "_", "_", " "],
    "D": ["|", "`", "`", "\\",
          "|", "_", "_", "/"],
    "E": ["|", "`", "_", " ",
          "|", "_", " ", " "],
    "F": [" ", "|", "`", "`",
          " ", "|", "`", " "],
    "G": ["/", "`", " ", "_",
          "\\", "_", "_", "/"],
    "H": ["|", "_", "_", "|",
          "|", " ", " ", "|"],
    "I": ["`", "|", "`", " ", # Alternative "_" [" ", "|", " ", " ", " ", "|", " ", " "],
          "_", "|", "_", " "],
    "J": [" ", " ", "|", " ", # Alternative "J" [" ", " ", "|", " ", "\\", "_", "/", " "],
          "\\", "_", "/", " "],
    "K": [" ", "|", "/", " ",
          " ", "|", "\\", " "],
    "L": ["|", " ", " ", " ",
          "|", "_", "_", " "],
    "M": ["|", "\\", "/", "|",
          "|", " ", " ", "|"],
    "N": ["|", "\\", " ", "|",
          "|", " ", "\\", "|"],
    "O": ["/", "`", "`", "\\",
          "\\", "_", "_", "/"],
    "P": [" ", "|", "O", " ",
          " ", "|", " ", " "],
    "Q": ["/", "`", "\\", " ",
          "\\", "_", "/", "_"],
    "R": [" ", "|", "O", " ",
          " ", "|", "\\", " "],
    "S": ["/", "_", "`", " ",
          " ", "_", "/", " "],
    "T": ["`", "|", "`", " ",
          " ", "|", " ", " "],
    "U": ["|", " ", " ", "|",
          "\\", "_", "_", "/"],
    "V": ["\\", " ", " ", "/",
          " ", "\\", "/", " "],
    "W": ["|", " ", " ", "|",
          "\\", "/", "\\", "/"],
    "X": [" ", "\\", "/", " ",
          " ", "/", "\\", " "],
    "Y": [" ", "\\", "/", " ",
          " ", "/", " ", " "],
    "Z": ["`", "`", "/", " ",
          "/", "_", "_", " "],
    " ": [" ", " ", " ", " ",
          " ", " ", " ", " "],
}

def generate_captcha(phrase, map = LETTER_MAPS):
    top = ""
    bottom = ""
    phrase = phrase.upper()
    for letter in phrase:
        for c in range(4):
            top += random.choice(TYPE_MAPS[map[letter][c]])
        top += " "
        for c in range(4, 8):
            bottom += random.choice(TYPE_MAPS[map[letter][c]])
        bottom += " "

    return top + "\n" + bottom


# Example
def main():
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    text = random.choice(Alphabet) + random.choice(Alphabet) + random.choice(Alphabet) + random.choice(Alphabet) + random.choice(Alphabet)

    Captcha = generate_captcha(text)
    print(Captcha)
    input = input("\nEnter the phrase in the captcha: ")
    if input.upper() == text:
        print("Login Successful")
    else:
        print("Login Unsuccessful")

if __name__ == '__main__':
    main()
