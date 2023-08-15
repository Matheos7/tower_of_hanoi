import copy
import sys
import time

TOTAL_DISKS = 5

SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))

print(SOLVED_TOWER)


def main():
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

    while True:  # Run a single iteration of game on each loop
        # Display towers with disks at the start of each loop
        display_towers(towers)

        # Ask for user input, where to take the disk from and where to put it
        from_tower, to_tower = get_player_move(towers)

        # Move top disk from from_tower to to_tower
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)

        # Check if player has solved the puzzle
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            display_towers(towers)
            print("You have solved the puzzle!")
            sys.exit()


def get_player_move(towers):
    """Asks the player for a move. Returns tuple (from_tower, to_tower)"""

    while True:
        print("Enter letters of 'from' and 'to' towers, or QUIT")
        print("eg 'AB' moves disk from tower A to tower B")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing.")
            sys.exit()

        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("enter either one of 'AB, AC, BA, BC, CA, CB'")
            continue

        from_tower, to_tower = response[0], response[1]

        if len(towers[from_tower]) == 0:
            print("You selected tower without a disk")
            continue
        elif len(towers[to_tower]) == 0:
            return from_tower, to_tower
        elif towers[to_tower][-1] < towers[from_tower][-1]:
            print("Can't put larger disk on top of a smaller one")
            continue
        else:  # This must be a valid move
            return from_tower, to_tower


def display_towers(towers):
    """
    Takes dictionary of towers and then loops through all levels (equal to total disks + 1) in the tower and then all towers.
    It prints line by line current state of all 3 towers, from the top. First line is always empty.
    Uses display_disk function to print each of the disks.
    """
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disk(0)
            else:
                display_disk(tower[level])
        print()

    # Display the tower labels A, B and C
    empty_space = " " * (TOTAL_DISKS)
    print(f"{empty_space} A{empty_space}{empty_space} B{empty_space}{empty_space} C\n")


def display_disk(width):
    """
    Function used by display_towers. Prints single row/disk.
    """
    empty_space = " " * (TOTAL_DISKS - width)

    if width == 0:
        print(f"{empty_space}||{empty_space}", end="")
    else:
        disk = "@" * width
        num_label = str(width).rjust(2, " ")
        time.sleep(0.2)
        print(f"{empty_space}{disk}{num_label}{disk}{empty_space}", end="")


main()
