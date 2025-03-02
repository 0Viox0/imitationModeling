class MersenneTwister:
    def __init__(self, seed=None):
        self.m = 2**32 - 1
        self.n = 624
        self.mt = [0] * self.n
        self.index = self.n + 1

        if seed is None:
            import time
            seed = int(time.time())

        self._init_genrand(seed)

    def _init_genrand(self, seed):
        self.mt[0] = seed & self.m
        for i in range(1, self.n):
            self.mt[i] = (1812433253 * (self.mt[i-1] ^ (self.mt[i-1] >> 30)) + i) & self.m

    def _twist(self):
        for i in range(self.n):
            x = (self.mt[i] & 0x80000000) + (self.mt[(i+1) % self.n] & 0x7FFFFFFF)
            self.mt[i] = self.mt[(i + 397) % self.n] ^ (x >> 1)
            if x % 2 != 0:
                self.mt[i] ^= 0x9908B0DF

        self.index = 0

    def genrand_int32(self):
        if self.index >= self.n:
            self._twist()

        y = self.mt[self.index]
        self.index += 1

        y ^= (y >> 11)
        y ^= (y << 7) & 0x9D2C5680
        y ^= (y << 15) & 0xEFC60000
        y ^= (y >> 18)

        return y & 0xFFFFFFFF

    def genrand_float(self):
        return self.genrand_int32() / float(0xFFFFFFFF)
