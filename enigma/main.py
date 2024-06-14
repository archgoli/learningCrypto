"""
Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A => X
"""

import pygame 
pygame.init()

from keyboard import Keyboard
from plugboard import Plugboard 
from rotor import Rotor 
from reflector import Reflector 
from enigma import Enigma
from draw import draw

# setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma simulator")

# create fonts
MONO = pygame.font.SysFont("Arial Narrow", 20)
BOLD = pygame.font.SysFont("Arial Narrow", 20, bold = True)

# global variables
WIDTH = 1200
HEIGHT = .75*900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top": 100, "bottom": 100, "left":  50, "right": 50}
GAP = 60

INPUT = ""
OUTPUT = ""
PATH = []

# historical enigma rotors and reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q") # (wiring or inner right alphabet, turnover notch)
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# keyboard and plugboard
KB = Keyboard()
PB = Plugboard(["AB", "CD", "EF"])

# define enigma machine
ENIGMA = Enigma(B, I, II, III, PB, KB)

# set the rings
ENIGMA.set_rings((1, 1, 1))

# set message key
ENIGMA.set_key("CAT")

# encipher a message
message = "THISCOOLENIGMAMACHINE"
cipher_text = ""
for letter in message: 
    cipher_text = cipher_text + ENIGMA.encipher(letter)[1]
print(cipher_text)

# print(ENIGMA.encipher("A"))

# I.show()
# I.rotate_to_letter("j")
# I.show()

animating = True
while animating: 
    
    # background
    SCREEN.fill("#333333") # background color

    # text input
    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/2))
    SCREEN.blit(text, text_box)

    # text output
    text = MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/2+25))
    SCREEN.blit(text, text_box)

    # draw enigma machine
    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)

    # update screen
    pygame.display.flip() # updates entire screen

    # track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                II.rotate()
            else:  
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz": 
                    letter = key.upper()
                    INPUT = INPUT + letter
                    cipher = ENIGMA.encipher(letter)[1]
                    OUTPUT = OUTPUT + cipher
                    print(INPUT)
