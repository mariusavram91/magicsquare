import unittest
'''
'''


def get_square_dimension():
    n = None
    try:
        n = int(input("Please enter any positive odd integer: "))
        if n and n % 2 != 0 and n >= 0:
            return n
    except ValueError:
        print("Only integers accepted.")
        return get_square_dimension()
    else:
        return get_square_dimension()


def create_magic_square(n):
    magic_square = [[0] * n] * n

    return magic_square


def display_magic_square(magic_square):
    n = len(magic_square)

    print("\nMagic square is (dimension n=" + str(n) + "):")

    for row in magic_square:
        for number in row:
            print(str(number), end='\t')
        print()


def is_magic_square(magic_square):
    size = len(magic_square)

    flat_magic_square = [number for row in magic_square for number in row]

    if not all(isinstance(element, int) for element in flat_magic_square):
        return False
    if len(set(flat_magic_square)) != len(flat_magic_square):
        return False

    sums = []
    sums.extend([sum(row) for row in magic_square])
    sums.extend([sum(col) for col in zip(*magic_square)])
    sums.append(sum(magic_square[i][i] for i in range(size)))
    sums.append(sum(magic_square[i][size-i-1] for i in range(size)))

    if len(set(sums)) > 1:
        return False
    return True


def magic_square():
    n = get_square_dimension()
    magic_square = create_magic_square(n)
    display_magic_square(magic_square)

    if is_magic_square(magic_square):
        print("Correct!")
    print()

    return

magic_square()


class MagicSquareValidityTest(unittest.TestCase):
    def setup(self):
        pass

    def test_dimension_of_created_square_is_n(self):
        magic_square = create_magic_square(3)
        self.assertTrue(len(magic_square) == len(magic_square[0]) == 3)

    def test_square_allows_only_integers(self):
        magic_square = [[1, 2, 'a'], [4, 5, 6], [7, 8, 9]]
        self.assertFalse(is_magic_square(magic_square))

    def test_square_does_not_allow_duplicate_integers(self):
        magic_square = [[1, 1, 2], [4, 5, 6], [7, 8, 9]]
        self.assertFalse(is_magic_square(magic_square))

    def test_square_is_invalid_because_of_sums(self):
        magic_square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertFalse(is_magic_square(magic_square))

    def test_square_is_correct(self):
        magic_square = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
        self.assertTrue(is_magic_square(magic_square))

if __name__ == '__main__':
    unittest.main()
