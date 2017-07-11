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
        string += "Your armor: " + str(self.armor)+ "\n"
        string += "And your location X: " + str(self.locationX) + " Y: " + str(self.locationY) + "\n"
        return string

    @staticmethod
    def move_forward():
        return "You move forward"

    @staticmethod
    def move_back():
        return "You move back"

    @staticmethod
    def move_right():
        return "You move right"

    @staticmethod
    def move_left():
        return "You move left"
