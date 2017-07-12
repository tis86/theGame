class Hero:
    def __init__(self, name, health, armor, location_x, location_y):
        print("Hello new world!")
        self.name = name
        self.health = health
        self.armor = armor
        self.locationY = location_y
        self.locationX = location_x

    def __str__(self):
        string = "Your name: " + self.name + "\n"
        string += "You have " + str(self.health) + " hearts\n"
        string += "Your armor: " + str(self.armor) + "\n"
        string += "And your location X: " + str(self.locationX) + " Y: " + str(self.locationY) + "\n"
        return string

    def move_forward(self):
        self.locationX += 1
        return "You move forward"

    def move_back(self):
        self.locationX -= 1
        return "You move back"

    def move_right(self):
        self.locationY += 1
        return "You move right"

    def move_left(self):
        self.locationY -= 1
        return "You move left"
