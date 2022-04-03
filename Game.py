# game characters
HERO = "Incredible Geo"
VILLAIN = "Dangerous Monarch"

GAME_MAP = { # a dictionary linking a room to other rooms
    "Throne Room": {"East": "Garderobe", "South": "Queen's Room", "Item": "Spores"},
    "Garderobe": {"West": "Throne Room", "Item": "Doubloons"},
    "Queen's Room": {"North": "Throne Room", "East": "Atrium", "Item": "Key"},
    "Refectory": {"East": "Passageway 1", "South": "Galley", "West": "Atrium", "Item": "Silver Knife"},
    "Atrium": {"East": "Refectory", "South": "Meditation Room", "West": "Queen's Room"},
    "Passageway 1": {"East": "Passageway 2", "South": "Peasant's Mess", "West": "Refectory"},
    "Passageway 2": {"North": "Stables", "East": "Depository", "South": "Passageway 3", "West": "Passageway 1"},
    "Passageway 3": {"North": "Passageway 2", "East": "Storage Room", "South": "Study"},
    "Meditation Room": {"North": "Atrium", "South": "Sunroom", "Item": "Ouija Board"},
    "Galley": {"North": "Refectory", "East": "Peasant's Mess", "Item": "Rancid Cheesecake"},
    "Peasant's Mess": {"North": "Passageway 1", "South": "Chapel", "West": "Galley", "Item": "Health Potion"},
    "Chapel": {"North": "Peasant's Mess", "West": "Sunroom", "Item": "Sweets"},
    "Sunroom": {"North": "Meditation Room", "East": "Chapel", "South": "Courtyard", "Item": "Swim Trunks"},
    "Stables": {"South": "Passageway 2", "Item": "Rat Poison"},
    "Depository": {"West": "Passageway 2", "Item": "Excrement"},
    "Storage Room": {"West": "Passageway 3", "Item": "Tacks"},
    "Study": {"North": "Passageway 3", "Item": "Manual"},
    "Courtyard": {"North": "Sunroom", "Item": VILLAIN}
}

availableItems = [] # create list for available items
collectedItems = [] # create list for collected items
curRoom = "" # create string to keep track of current room

# provide player with the story of the game
def showStory():
    print("                  ", VILLAIN, "Text Adventure Game\n")
    print("------------------------------------------------------------------------")
    print("You're the", HERO, "visiting the", VILLAIN, "\b's castle. The")
    print(VILLAIN, "is creating havoc in the castle and the", HERO)
    print("must prevent the", VILLAIN, "from creating too much havoc upon the")
    print("castle and it's visitors.")
    print("------------------------------------------------------------------------")

# provide player with instructions on how to play
def showInstructions():
    print("************************************************************************")
    print("Collect all items to win the game or be defeated by the", VILLAIN, "\b!")
    print("Move commands: go North, go East, go South, go West")
    print("Add to Inventory: get 'item name'")
    print("Show the Story or Instructions: story, help")
    print("Quit playing: quit")
    print("************************************************************************")

# provide player with current status of game play
def showStatus():
    global curRoom, collectedItems, availableItems
    # print the player's current status, collected items & item in room, if there is one
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("You are currently in the", curRoom)
    print("Collected Items:", collectedItems)
    print("Available Items:", availableItems)
    if(showItem(curRoom) is not False):
        print("You see a", showItem(curRoom))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# show the item in specified room
def showItem(room):
    global availableItems
    if("Item" in GAME_MAP[room].keys() and (GAME_MAP[room]["Item"] in availableItems or GAME_MAP[room]["Item"] is VILLAIN)):
        return GAME_MAP[room]["Item"]
    else:
        return False

# move thru the room exit to the direction specified
def moveTo(direction):
    global curRoom

    if(direction in GAME_MAP[curRoom].keys()):
        curRoom = GAME_MAP[curRoom][direction]
        return True
    else:
        print(direction, "is an invalid directional movement for", curRoom)
        return False

# add an item to the inventory, if it's found in the current room and not already retrieved
# remove item from available items if successful
def addToInventory(item, inventory):
    global curRoom, availableItems

    # check that item belongs to this room and is available
    if("Item" in GAME_MAP[curRoom] and GAME_MAP[curRoom]["Item"] == item and item in availableItems):
        inventory.append(item)
        availableItems.remove(item)
        print(item, "retrieved!")
        return True
    else:
        print(item, "not found in", curRoom)
        return False

# reset game play to starting status (Atrium, all items available, no items collected)
def reset():
    global availableItems, collectedItems, curRoom

    availableItems.clear()
    for room in GAME_MAP:
        if("Item" in GAME_MAP[room].keys() and GAME_MAP[room]["Item"] is not VILLAIN):
            availableItems.append(GAME_MAP[room]["Item"])

    collectedItems.clear()
    curRoom = "Atrium"

# allow user to quit the game
def quit():
    print("Thanks for playing!")
    input("Press any key to close")
    exit()

def main():
    global availableItems, collectedItems, curRoom

    reset()
    showStory()
    showInstructions()

    while True:
        showStatus()

        # determine if game is won
        if(not availableItems and showItem(curRoom) is VILLAIN):
            print("You see the", VILLAIN, "& slay it by collecting all of the available items required!")
            break
        # determine if game is lost, or collect room item
        elif(showItem(curRoom) is VILLAIN):
            print("OH NO! You've encountered the", VILLAIN, "before collecting all items. You died X(")

            if input("Would you like to play again? (Y/N) ") in ('Y', 'y', 'Yes', 'yes', 'YES'):
                reset()
                continue
            else:
                quit()

        # get the player's next 'move'
        while True:
            # perform next move
            match input("What's your next move? ").split():
                case ["go", "North"]: moveTo("North")
                case ["go", "East"]: moveTo("East")
                case ["go", "South"]: moveTo("South")
                case ["go", "West"]: moveTo("West")
                case ["get", *object]: addToInventory(' '.join(object), collectedItems)
                case ["help"]: showInstructions()
                case ["story"]: showStory()
                case ["restart"]:
                    reset()
                    break
                case ["quit"]: quit()
                case _:
                    print("Invalid move, try again. For a reminder, type 'help'.")
                    continue
            break
    quit()

if __name__ == "__main__":
    main()