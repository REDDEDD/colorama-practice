from colorama import init, Fore, Back, Style

init()

COLOURS = [ Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.RED, Fore.LIGHTRED_EX, Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.YELLOW, Fore.LIGHTYELLOW_EX, Fore.BLUE, Fore.LIGHTBLUE_EX,
Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.CYAN, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.LIGHTWHITE_EX ]
BACKS = [ Back.BLACK, Back.LIGHTBLACK_EX, Back.RED, Back.LIGHTRED_EX, Back.GREEN, Back.LIGHTGREEN_EX, Back.YELLOW, Back.LIGHTYELLOW_EX, Back.BLUE, Back.LIGHTBLUE_EX,
Back.MAGENTA, Back.LIGHTMAGENTA_EX, Back.CYAN, Back.LIGHTCYAN_EX, Back.WHITE, Back.LIGHTWHITE_EX ]
STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

NAMES = {
    Fore.BLACK: 'Black', Fore.LIGHTBLACK_EX: 'L.Black', Fore.RED: 'Red', Fore.LIGHTRED_EX: 'L.Red', Fore.GREEN: 'Green', Fore.LIGHTGREEN_EX: 'L.Green',
    Fore.YELLOW: 'Yellow', Fore.LIGHTYELLOW_EX: 'L.Yellow', Fore.BLUE: 'Blue', Fore.LIGHTBLUE_EX: 'L.Blue', Fore.MAGENTA: 'Magenta', Fore.LIGHTMAGENTA_EX: 'L.Magenta',
    Fore.CYAN: 'Cyan', Fore.LIGHTCYAN_EX: 'L.Cyan', Fore.WHITE: 'White', Fore.LIGHTWHITE_EX: 'L.White'
    , Fore.RESET: 'reset',
    Back.BLACK: 'Black', Back.LIGHTBLACK_EX: 'L.Black', Back.RED: 'Red', Back.LIGHTRED_EX: 'L.Red', Back.GREEN: 'Green', Back.LIGHTGREEN_EX: 'L.Green',
    Back.YELLOW: 'Yellow', Back.LIGHTYELLOW_EX: 'L.Yellow', Back.BLUE: 'Blue', Back.LIGHTBLUE_EX: 'L.Blue', Back.MAGENTA: 'Magenta', Back.LIGHTMAGENTA_EX: 'L.Magenta',
    Back.CYAN: 'Cyan', Back.LIGHTCYAN_EX: 'L.Cyan', Back.WHITE: 'White', Back.LIGHTWHITE_EX: 'L.white'
    , Back.RESET: 'reset'
}

# Initial space
print('            ',end=" ")
# For each colour print the name
for c in COLOURS:
    print('%s%-9s' % (c, NAMES[c]),end=" ")
print()

# For each background-colour print a row with the name and the assigned colour
for b in BACKS:
    print('%s%-10s%s %s' % (b, NAMES[b], Back.RESET, b),end="")
    # For each column
    for c in COLOURS:
        print(c,end=" ")
        # Print 3 'P' one for each style
        for st in STYLES:
            print('%-5sP ' % st,end="")
        # Reset
        print(Style.RESET_ALL + ' ' + b,end="")
    # Another reset
    print(Style.RESET_ALL)