class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
        self._size = 0

    def __str__(self):
        return("🍪"*self.size)


    def deposit(self, n):
        self.size = self.size + n
        if self.size > self._capacity:
            raise ValueError

    def withdraw(self, n):
        self.size = self.size - n
        if self.size < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,n):
        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,n):
        self._size = n











