```
setup the game characters (names)
setup the game map (dictionary of rooms each with a dictionary of {directional movements and the connected room} as well as an item found in the room)
    map format is [room]: {[direction: room][1..4], [item: 'item name']}[8..n]
setup a list of available items that can be retrieved

set the current room to be the start room
set the collected items to be empty

show the user a welcome message, including the game story and instructions to play the game

until the user wins, losses or quits the game
    show the game status (current room, collected items, any unretrieved item that is in the current room)

    if no available items and encountered villain
        show a message to the user that they won the game and exit
    else if the villain is encountered
        show a message to the user that they have lost the game and exit

    until the user enters a valid command (i.e., go North, go East, etc)
        ask the user what their next move is
```