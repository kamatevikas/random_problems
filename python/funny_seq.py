# list of tuples [(f, num), (f, num)....] gets generated from previously generated list

import unittest

class FunkyFib:

    def __init__(self):
        pass 

    def generate_sequence(self, seq_len=1):
        if seq_len < 1:
            return ""
        sequence = "1"    
        return self._generate_sequence(seq_len, sequence)

    def _generate_sequence(self, seq_len=1, sequence="1"):
        if len(sequence) >= seq_len:
            return sequence
        else:
            new_sequence = ""
            current_element = sequence[0]
            count = 1
            for index in range(1, len(sequence)):
                if current_element == sequence[index]:
                    count += 1
                else:
                    new_sequence += str(count) 
                    new_sequence += str(current_element)
                    current_element = sequence[index]
                    count = 1
            new_sequence += str(count)
            new_sequence += str(current_element)
            return self._generate_sequence(seq_len, new_sequence)        
    

class TestFunkyFib(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.testff = FunkyFib()

    def test_one(self):
        seq = self.testff.generate_sequence(1)
        print(f"test_one: {seq}")
        self.assertEqual("1", seq)

    def test_two(self):
        seq = self.testff.generate_sequence(2)
        print(f"test_two: {seq}")
        self.assertEqual("11", seq)

    def test_seven(self):
        seq = self.testff.generate_sequence(7)
        print(f"test_seven: {seq}")
        self.assertEqual("13112221", seq)

    def test_random(self):
        seq_17 = self.testff.generate_sequence(17)
        print(f"test_17: {seq_17}")
        seq_30 = self.testff.generate_sequence(30)
        print(f"test_30: {seq_30}")


if __name__ == "__main__":
    unittest.main()
