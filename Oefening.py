
class Mario:

    _lives = 3
    _speed = 30.0

    def Test(self):
        print("Hello")
        print("Speed is: ", self._speed)


class Constructor:

    _lives = 0

    def __init__(self, levens):
        self.levens = levens


instanceMario = Mario()
nogEenMario = Mario()

print( instanceMario._lives )
instanceMario.Test()
instanceMario._speed = 50

print("instanceMario snelheid: ", instanceMario._speed)
print("NogEenMario snelheid: ", nogEenMario._speed)