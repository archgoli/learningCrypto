"""
Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A => X
"""

class Rotor: 
    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch # when initializing a rotor object, the notch will be a letter

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

    def show(self): 
        print(self.left)
        print(self.right)
        print()
    
    def rotate(self, n=1, forward = True): 
        for i in range(n):
            # if direction is forward, then shift alphabet upwards by step n.  
            if forward: 
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            # if direction is not forward, shift alphabet downwards by step n. 
            else: 
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]

    def rotate_to_letter(self, letter):
        """Rotates alphabet so the given letter is at position 0."""
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter) # find position of letter
        self.rotate(n) # rotate the number of times equal to the letter's index so the letter will be at position 0

    def set_ring(self, n):
        """Shifting the rotors and finding the new turnover notch while accounting for the rotor shift."""
        # rotate the rotor backwards
        self.rotate(n-1, forward=False) # n-1 because when n is 1, no change

        # adjust the turnover notch in relationship to the wiring
        n_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch) # finds what position is turnover notch in alphabet - the position we're at right now
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_notch - n + 1) % 26] # subtracts the number of steps we shifted from the current position mod 26


# I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
# II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
# III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
# IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
# V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
