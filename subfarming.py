import crop3
def subsistence():
    print("choose crop")
    print("1.cabbage")
    print("2.cassava")
    print("3.greens")
    crop=int(("Enter choice of crop(1-3): "))
    if (crop == 1):
        print("You chose cabbage")
        crop3.cabbage()
    elif (crop == 2):
        print("You chose cassava")
        crop3.cassava()
    elif (crop == 3):
        print("you chose greens")      
        crop3.greens()