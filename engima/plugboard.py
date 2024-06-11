"""
Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A => X
"""

class Plugboard: 
    def __init__(self, pairs): 
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs: # loop through every pair of letters
            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A) # where A is to be found in the alphabet
            pos_B = self.left.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A + 1:] # change left inside wiring so that A and B are swapped positions 
            self.left = self.left[:pos_B] + A + self.left[pos_B + 1:]
    
    def forward(self, signal): 
        """Signal comes in at a certain position, this function finds what letter is at this position in the right inside alphabet. 
        Then, it finds that letter in the left inside alphabet and outputs that position."""
        letter = self.right[signal] 
        signal = self.left.find(letter)
        return signal

    def backward(self, signal): 
        """Signal comes in at a certain position, this function finds what letter is at this position in the left inside alphabet. 
        Then, it finds that letter in the right inside alphabet and outputs that position."""
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal




