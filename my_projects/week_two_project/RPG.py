#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
import requests


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      give[item]

      To win the game reach the Witch Hut and give the ugly witch her potion!
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    if "person" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['person'],'\n')
        if  rooms[currentRoom]['person'] == 'Centaur':
            answer = input("Welcome to my lair! I have a riddle for you, try it if you dare! If you your answer is incorrect I will break your neck, but if your answer is right I will point you towards the light! Riddle: Give me a drink and I will die. Feed me, and I'll get bigger. What am I?\n")
            if answer  == "fire":
                print("That is correct! Go west to find your way to the light!")
            else:
                print("Sorry your neck is broken.")
                exit()

        if rooms[currentRoom]['person'] == 'Sphinx':
            url = "https://facts-by-api-ninjas.p.rapidapi.com/v1/facts"
            querystring = {"limit":"1"}
            headers = {
	"X-RapidAPI-Key": "c09cd3dd48msh2adb42dbd235ca6p14c356jsnc57836113f5e",
	"X-RapidAPI-Host": "facts-by-api-ninjas.p.rapidapi.com"
}
            response = requests.request("GET", url, headers=headers, params=querystring)
            print("Greetings! I am the Sphinx and I have a fun fact for you!\n",response.json()[0]['fact'])


    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south': 'Kitchen',
                  'east': 'Dining Room',
                  'item': 'key',
                  'room': 'Hall'
                },

            'Kitchen' : {
                  'north': 'Hall',
                  'person': 'monster',
                  'south': 'Trapdoor',
                  'room': 'Kitchen'
                },
            'Dining Room': {
                   'west': 'Hall',
                   'south': 'Garden',
                   'item': 'potion',
                   'room': 'Dining Room'
                   },
            'Garden': {
                   'north': 'Dining Room',
                   'south': 'Creepy Cave',
                   'room': 'Garden'
                   },
            'Creepy Cave': {
                'west': 'Stinky Mud Pit',
                'north': 'Garden',
                'person': 'Centaur',
                'item': 'old boot',
                'room': 'Creepy Cave'
                },
            'Stinky Mud Pit': {
                'north': 'Trapdoor',
                'east': 'Creepy Cave',
                'south': 'Cave Opening',
                'person': 'Sphinx',
                'room': 'Stinky Mud Pit',
                },
            'Trapdoor':{
                'north':'Kitchen',
                'south':'Stinky Mud Pit',
                'room': 'trap'
                },
            'Cave Opening': {
                'north': 'Stinky Mud Pit',
                'east': 'Forest',
                'person': 'Dragon',
                'room': 'Cave Opening'
                },
            'Forest': {
                'east': 'Witch Hut',
                'west': 'Cave Opening',
                'room': 'Forest'
                },
            'Witch Hut': {
                'person': 'Witch',
                'east': 'Forest',
                'room': 'Witch Hut'
                }
            }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 2)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if move[0] == 'give':
        if 'person' in rooms[currentRoom] and move[2] in inventory:
            print(move[2]+ ' given to ' + move[1])
            inventory.remove(move[2])

        else:
            print('Can\'t give '+move[2]+' to '+move[1])



    ## If a player enters a room with a monster
    if 'person' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['person'] :
        print('A monster has got you... GAME OVER!')
        break
    ## If a player enters a trap door
    if  move[1] == 'north' and 'trap' in rooms[currentRoom]['room']:
        print('You hit a trap door! Good luck with the monster!')
        print('A monster ate your head...GAME OVER!')
        exit()
    else:
        continue
    ## Define how a player can win
    if currentRoom == 'Witch Hut'  and 'potion' not in inventory:
        print('You escaped the house and gave that big ole ulgy witch the potion... YOU WIN!')
        break
