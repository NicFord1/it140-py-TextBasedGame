```
PROGRAM TextBasedGame:
    SET the game characters (names)
    SET the game map
        map format is [room]: {[direction: room][1..4], [item: 'item name']}[8..n]

    SET the available items to be empty
    SET the collected items to be empty
    SET the current room to be the start room

    FUNCTION showStory
        Pass In: nothing
        SHOW game story to user
        Pass Out: nothing
    END show Story

    FUNCTION showInstructions
        Pass In: nothing
        SHOW game instructions to user
        Pass Out: nothing
    END showInstruction

    FUNCTION showStatus
        Pass In: nothing
        SHOW player's current status, collected items
        IF item in room is not yet collected
            SHOW item
        Pass Out: nothing
    END showStatus

    FUNCTION getItem
        Pass In: room
        IF item in room is not yet collected OR is the villain
            return item in room
        ELSE
            return False
    END getItem

    FUNCTION moveTo
        Pass In: direction
        IF a room is accessible in the direction
            set current room
            return True
        ELSE
            SHOW error message to user
            return False
    END moveTo

    FUNCTION addToInventory
        Pass In: item, inventory
        IF item is in current room AND not yet collected
            ADD item to inventory
            REMOVE item from available items
            SHOW user item was retrieved
            return True
        ELSE
            SHOW error message
            return False
    END addToInventory

    FUNCTION reset
        Pass In: nothing
        RESET available items to all items
        CLEAR collected items
        SET current room to Atrium
    END reset

    FUNCTION quit
        Pass In: nothing
        SHOW goodbye message to user
        EXIT
    END quit

    FUNCTION main
        Pass In: nothing
    
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
                    CASE go North, moveTo room connected to the North
                    CASE go East, moveTo room connected to the  East
                    CASE go South, moveTo room connected to the  South
                    CASE go West, moveTo room connected to the  West
                    CASE get 'item name', move item to collected items
                    CASE DEFAULT SHOW error message
    END main
END
```