# Unicode characters for game visuals
MISSIONARY = '\U0001f9d9'  # 🧙 Wizard
CANNIBAL = '\U0001f9df'    # 🧟 Zombie
BOAT = '\U0001f6f3'        # 🛳️ Passenger ship
WATER = '\U0001f30a'       # 🌊 Water wave

# Initial game state
boat_side = 'Right'        # Boat starts on the right bank
missionaries_on_right = 3  # Number of missionaries on right bank
cannibals_on_right = 3     # Number of cannibals on right bank
missionaries_on_left = 0   # Number of missionaries on left bank
cannibals_on_left = 0      # Number of cannibals on left bank

# Function to display current game state using emojis
def display():
    # Build left side visuals
    left = MISSIONARY * missionaries_on_left + CANNIBAL * cannibals_on_left

    # Water between banks
    water = WATER * 5  

    # Build right side visuals
    right = MISSIONARY * missionaries_on_right + CANNIBAL * cannibals_on_right

    # Show boat position depending on which side it's on
    if boat_side == 'Right':
        print(left + "|" + water + water + BOAT + "|" + right)
    else:
        print(left + "|" + BOAT + water + water + "|" + right)

# Show the initial game state
display()

# Main game loop
while True:
    # Get number of missionaries to move
    missionaries = int(input('No of missionaries or enter 10 to quit : '))
    if missionaries == 10:
        print('You Quit. Game Over!')
        break

    # Get number of cannibals to move
    cannibals = int(input('No of cannibals : '))

    # Check boat capacity — only 1 or 2 passengers allowed
    if (missionaries + cannibals) != 1 and (missionaries + cannibals) != 2:
        print('Invalid Move')
        continue  # Skip rest of loop and ask again

    # If boat is currently on the right bank
    if boat_side == 'Right':
        # Prevent moving more people than exist on the right bank
        if missionaries_on_right < missionaries or cannibals_on_right < cannibals:
            print('Invalid Move')

        # Move people from right to left
        missionaries_on_right -= missionaries
        cannibals_on_right -= cannibals
        missionaries_on_left += missionaries
        cannibals_on_left += cannibals

        # Boat now moves to left bank
        boat_side = 'Left'

    # If boat is currently on the left bank
    else:
        # Prevent moving more people than exist on the left bank
        if missionaries_on_left < missionaries or cannibals_on_left < cannibals:
            print('Invalid Move')

        # Move people from left to right
        missionaries_on_left -= missionaries
        cannibals_on_left -= cannibals
        missionaries_on_right += missionaries
        cannibals_on_right += cannibals

        # Boat now moves to right bank
        boat_side = 'Right'

    # Show updated game state
    display()

    # Lose condition: Cannibals outnumber missionaries on any side (with at least 1 missionary present)
    if (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0) or \
       (missionaries_on_left < cannibals_on_left and missionaries_on_left > 0):
        print('You Lose')
        break

    # Win condition: All 3 missionaries and cannibals safely on the left bank
    if missionaries_on_left == 3 and cannibals_on_left == 3:
        print('You Win')
        break
