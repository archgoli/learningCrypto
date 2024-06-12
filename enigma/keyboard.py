"""
Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A => X
"""

class Keyboard: 

    def forward(self, letter): 
        """User presses a letter on the keyboard that is then transformed into a signal. """
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter) # position of letter in alphabet
        return signal

    def backward(self, signal): 
        """Takes a signal and then converts it back into a letter. """
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal] # index alphabet at position signal
        return letter

