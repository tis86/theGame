from Hero import Hero as Character

print("Hello in the game!")
name = input("Choose your name: ")
newHero = Character(name, 10, 0, 0, 0)
print(newHero)
while True:
    action = input("What will you do?\n")
    if action == "forward":
        print(newHero.move_forward())
    elif action == "back":
        print(newHero.move_back())
    elif action == "right":
        print(newHero.move_right())
    elif action == "left":
        print(newHero.move_left())
    elif action == "hero":
        print(newHero)
    elif action == "exit":
        break
