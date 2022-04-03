```
PROGRAM TextBasedGame:
    SET the game characters (names)
    SET the game map
        map format is [room]: {[direction: room][1..4], [item: 'item name']}[8..n]

    SET a list of available items that can be retrieved
    SET the collected items to be empty
    SET the current room to be the start room

    SHOW the user a welcome message, including the game story and instructions to play the game

    WHILE the user has not won, lost, or quit the game
        SHOW the game status (current room, collected items, any unretrieved item that is in the current room)

        IF no available items and encountered villain
            THEN SHOW message to user that they won the game and exit
        ELSE IF the villain is encountered
            THEN SHOW message to user that they have lost the game and either restart or exit

        WHILE we don't have a valid command (i.e., go North, go East, etc)
            ask the user what their next move is

            MATCH command issued
                CASE go North, move to room connected to the North
                CASE go East, move to room connected to the  East
                CASE go South, move to room connected to the  South
                CASE go West, move to room connected to the  West
                CASE get 'item name', move item to collected items
                CASE DEFAULT SHOW error message
END
```