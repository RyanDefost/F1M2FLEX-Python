class Character:

    speed = 10
    lives = 3
    sprite = None

    def __init__(self):
        print("De constructor van Character")

    def walk(self):
        print("Character loopt meet de snelheid: ", self.speed)
#---------------------------------------------------------


class Mario(Character):

    points = 0
    item = None
    

    def __init__(self):
        # We vullen aan op de constructor van de Character:
        super().walk()

        #De snelheid van Mario is hoger
        self.speed = 30

    
    #De "Walk" funtie van Character ga ik overschrijven:
    def walk(self):
        print("Mario loopt heel anders, maar wel met de snelheid", self.speed)

    def jump(self):
        print("Mario springt")
#---------------------------------------------------------

class SlimmeMario(Mario):

    iq = 200

    def walk(self):
        super().walk()
        print("En ik loop ook heel erg slim om dingen heen met mij")
#---------------------------------------------------------

# Instances:
player1 = Character()
player2 = Mario()

player1.speed = 20
player2.walk()

print("Snelheid van player1: ", player1.speed)
print("Snelheid van player2: ", player2.speed)

# Het resultaat in de console geeft een geheugenadres weer.
# Dit geheugenadres verwijst naar de locatie van het volledige object:
print(player2)
