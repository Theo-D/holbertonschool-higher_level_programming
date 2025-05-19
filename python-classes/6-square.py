#!/usr/bin/python
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        for i in value:
            if not isinstance(i, int):
                isInt = False
            else:
                isInt = True
        if len(value) != 2 and isInt is True:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[0] > 0:
                print(f"{'\n' * self.__position[0]}", end="")
            for i in range(self.__size):
                if self.__position[1] > 0:
                    print(f"{'_' * self.__position[1]}", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
