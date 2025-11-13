enemies = 1


def increase_enemies():


    global enemies

    enemies = 4

    

    enemies = enemies + 3

    print(f"The value of enemies inside def is {enemies}")


increase_enemies()


enemies = enemies + 9

print(f"The value of enemies outside def is {enemies}")




    
