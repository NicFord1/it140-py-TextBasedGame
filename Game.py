import os

#ANSI escape sequence constants for formating text
class Format:
    HEADER = '\033[95;1m'
    STATUS = '\033[94m'
    COMMAND = '\033[96m'
    INPUT = '\033[92m'
    WARNING = '\033[93;3m'
    FAIL = '\033[91;3m'
    RESET = '\033[0m'

    def printHeader(character): # print a header separator made of characters
        print(Format.HEADER, end = "")
        for col in range(os.get_terminal_size().columns - 1):
            print(character, end = "")
        print(Format.RESET, "")

    def printCentered(text, ignored = 0, end = "\n"):
        emptyColumns = int((os.get_terminal_size().columns - len(text) + ignored - 2) / 2)
        for col in range(emptyColumns):
            print(" ", end = "")
        print(text, end = "")
        print("", end = end)

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

def showStory(): # provide player with the story of the game
    print("                  ", VILLAIN, "Text Adventure Game\n")
    Format.printHeader("-")
    print("You're the", HERO, "visiting the", VILLAIN, "\b's castle. The")
    print(VILLAIN, "is creating havoc in the castle and the", HERO)
    print("must prevent the", VILLAIN, "from creating too much havoc upon the")
    print("castle and it's visitors.")
    Format.printHeader("-")

def showInstructions(): # provide player with instructions on how to play
    Format.printHeader("*")
    print("Collect all items & win the game or be defeated by the", VILLAIN + "!")
    print("Move commands:", Format.COMMAND + "go North, go East, go South, go West" + Format.RESET)
    print("Add to Inventory:", Format.COMMAND + "get 'item name'" + Format.RESET)
    print("Show the Story or Instructions:", Format.COMMAND + "story, help" + Format.RESET)
    print("Quit playing:", Format.COMMAND + "quit" + Format.RESET)
    Format.printHeader("*")

# provide player with current status (current room, collected items & item in room, if there is one) of game play
def showStatus(room, collectedInventory, availableInventory):
    item = getItem(room, availableInventory)

    Format.printHeader("+")
    print("You are currently in the", Format.STATUS + room + Format.RESET)
    print("Collected Items:" + Format.STATUS, collectedInventory, Format.RESET)

    if(item is not None and item is not VILLAIN):
        print("You see a", Format.STATUS + item + Format.RESET)
    elif(item is VILLAIN):
        print("You see the", Format.STATUS + item + Format.RESET, "and", Format.WARNING + "prepare for battle!" + Format.RESET)

    Format.printHeader("+")

def getItem(room, availableInventory): # return the item in specified room
    if(room in GAME_MAP.keys() and "Item" in GAME_MAP[room].keys() and (GAME_MAP[room]["Item"] in availableInventory or GAME_MAP[room]["Item"] is VILLAIN)):
        return GAME_MAP[room]["Item"]
    else:
        return None

# return the room the player is in after moving thru the exit to the direction specified
def moveTo(room, direction):
    if(room in GAME_MAP.keys() and direction in GAME_MAP[room].keys()):
        return GAME_MAP[room][direction]
    else:
        print(Format.FAIL + direction, "is an invalid directional movement for", room + Format.RESET)
        return room

# add an item to the inventory, if it's found in the current room and not already retrieved
# remove item from available items if successful
# return the success state of collecting the item
def collectItem(room, item, collectedInventory, availableInventory):
    # check that item belongs to this room and is available
    if("Item" in GAME_MAP[room] and GAME_MAP[room]["Item"] == item and item in availableInventory):
        collectedInventory.append(item)
        availableInventory.remove(item)
        print(item, "retrieved!")
        return True
    else:
        print(Format.WARNING + item, "not found in", room + Format.RESET)
        return False

# reset game play to starting status (Atrium, all items available, no items collected)
# return spawn point
def reset(availableInventory, collectedInventory):
    availableInventory.clear()
    for room in GAME_MAP:
        if("Item" in GAME_MAP[room].keys() and GAME_MAP[room]["Item"] is not VILLAIN):
            availableInventory.append(GAME_MAP[room]["Item"])

    collectedInventory.clear()
    return "Atrium"

def quit(): # allow user to quit the game
    print(Format.RESET)
    Format.printCentered("Thanks for playing!")
    Format.printCentered("Press <" + Format.COMMAND + "enter" + Format.RESET + "> to close", (len(Format.COMMAND) + len(Format.RESET)), end = "")
    input("")
    exit(0)

def main():
    availableItems = [] # create list for available items
    collectedItems = [] # create list for collected items
    curRoom = reset(availableItems, collectedItems)

    showStory()
    showInstructions()

    while curRoom != "Exit":
        seekNextCommand = True
        showStatus(curRoom, collectedItems, availableItems)

        # determine if game is won
        if(not availableItems and getItem(curRoom, availableItems) is VILLAIN):
            print("You see the", VILLAIN, "& slay it by collecting all of the available items required!")
            seekNextCommand = False
            curRoom = "Exit"
        # determine if game is lost, or collect room item
        elif(getItem(curRoom, availableItems) is VILLAIN):
            print(Format.FAIL + "OH NO! You've encountered the", VILLAIN, "before collecting all items. You died X(" + Format.RESET)

            if input("Would you like to play again? (" + Format.COMMAND + "Y/N" + Format.RESET + ") " + Format.INPUT).title() in ('Y', 'Yes'):
                curRoom = reset(availableItems, collectedItems)
                seekNextCommand = False
            else:
                seekNextCommand = False
                curRoom = "Exit"

        while seekNextCommand: # seek the player's next command
            seekNextCommand = False # don't seek another command, unless necessary
            
            try: # perform next command
                match input("What's your next move? " + Format.INPUT).title().split():
                    case ["Go", "North"]: curRoom = moveTo(curRoom, "North")
                    case ["Go", "East"]: curRoom = moveTo(curRoom, "East")
                    case ["Go", "South"]: curRoom = moveTo(curRoom, "South")
                    case ["Go", "West"]: curRoom = moveTo(curRoom, "West")
                    case ["Get", *object]: collectItem(curRoom, ' '.join(object), collectedItems, availableItems)
                    case ["Help"]: showInstructions()
                    case ["Story"]: showStory()
                    case ["Restart"]: curRoom = reset(availableItems, collectedItems)
                    case ["Quit"]: curRoom = "Exit"
                    case _: # invlaid command
                        print(Format.FAIL + "Invalid move, try again. For a reminder, type '" + Format.COMMAND + "help" + Format.FAIL + "'." + Format.RESET)
                        seekNextCommand = True
            except EOFError: seekNextCommand = True
            except KeyboardInterrupt: # User issued Ctrl+C on Keyboard, indicating close/terminate program
                seekNextCommand = False
                curRoom = "Exit"
    quit()

if __name__ == "__main__":
    main()