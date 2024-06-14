class Enigma: 

    def __init__(self, re, r1, r2, r3, pb, kb):
        self.re = re
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.pb = pb
        self.kb = kb

    def set_rings(self, rings): 
        """Takes in a number, which represents the initial position of the letter pair that will be the turnover notch for each rotor. 
        When this letter pair is at position 0, the rotor will rotate."""
        self.r1.set_ring(rings[0])
        self.r2.set_ring(rings[1])
        self.r3.set_ring(rings[2])

    def set_key(self, key):
        """Sets what letter will be at position 0 for each rotor's inner alphabet - the starting positions for each rotor. """
        # rotate alphabet of each rotor so letter at position 0 of each rotor's left inner alphabet will match the respective key
        self.r1.rotate_to_letter(key[0]) 
        self.r2.rotate_to_letter(key[1])
        self.r3.rotate_to_letter(key[2])

    def encipher(self, letter): 
        """Encrypts the given letter."""

        # rotate the rotors when the turnover notch is at position 0 in the rotor's inner left alphabet, all rotors
        # up to the rotor left of the respective rotor will rotate. rotor 3 will always rotate once for each key
        # pressed.
        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch: 
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r2.left[0] == self.r2.notch: 
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r3.left[0] == self.r3.notch: 
            self.r2.rotate()
            self.r3.rotate()
        else: 
            self.r3.rotate()

        # pass signals through the machine
        signal = self.kb.forward(letter)
        path = [signal, signal]
        signal = self.pb.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r3.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r2.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r1.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.re.reflect(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r1.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r2.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r3.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.pb.backward(signal)
        path.append(signal)
        path.append(signal)
        letter = self.kb.backward(signal)
        return [path, letter]
