"""
Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A => X
"""

import pygame 

class Keyboard: 

    def forward(self, letter): 
        """User presses a letter on the keyboard that is then transformed into a signal. """
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter) # position of letter in alphabet
        return signal

    def backward(self, signal): 
        """Takes a signal and then converts it back into a letter. """
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal] # index alphabet at position signal
        return letter

    def draw(self, screen, x, y, w, h, font): 
        
        # rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width = 2, border_radius = 15)

        # letters 
        for i in range(26): 
            letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x+w/2, y + (i + 1)* h/27))
            screen.blit(letter, text_box)
