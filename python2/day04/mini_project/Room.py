class Room:
    def __init__(self, left, right, up, down):
        self.__left = left
        self.__right = right
        self.__up = up
        self.__down = down

    def getLeft(self) -> int:
        return self.__left

    def getRight(self) -> int:
        return self.__right

    def getUp(self) -> int:
        return self.__up
    
    def getDown(self) -> int:
        return self.__down
