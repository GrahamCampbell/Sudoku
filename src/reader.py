class Reader:

    def __init__(self, checker, size: int):
        self.checker = checker
        self.size = size

    def read(self, path: str):
        f = open(path, 'rb')

        data = [0] * self.size
        for i in range(self.size):
            data[i] = [0] * self.size

        col = 0
        row = 0

        try:
            while True:
                byte = f.read(1)
                if (byte == b""):
                    break
                if (byte == b"\n" or byte == b"\r"):
                    continue
                if (row >= self.size):
                    raise ValueError('The input file too long')
                data[row][col] = int(byte)
                col = (col + 1) % self.size
                if (col == 0):
                    row += 1
        finally:
            f.close()

        if (col != 0 or row != self.size):
            raise ValueError('The input file was too short')

        for row in range(self.size):
            for col in range(self.size):
                if (not self.checker.check((row, col), data)):
                    raise ValueError('The input file had invalid entries')

        return data
