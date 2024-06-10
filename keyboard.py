"""
Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A => X
"""

class Keyboard: 

    def forward(self, letter): 
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal

    def backward(self, signal): 
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter

