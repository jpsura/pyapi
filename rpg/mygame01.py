#!/usr/bin/env python3

def showInstructions():
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
    #print player status
    print('------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("------------------")

#an inventory
inventory = []

#a dictionary liking a room to other rooms
rooms = {
            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Hall',
                  'item'  : 'key'
                },
            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'Monster'
                },
            'Dining Hall' : {
                  'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'potion'
                  },
            'Garden' : {
                  'north' : 'Dining Hall'
                  }
        }
#start player in the hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player next move
  #.split() breaks it up into a list array
  #eg typing 'go east' would give the list:
  #['go', 'east']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  #if they go first
  if move [0] == 'go':
      #check they are allowed to go
    if move[1] in rooms [currentRoom]:
        #set the current rooms to a new room
      currentRoom = rooms[currentRoom][move[1]]
      #there is no door to a new room
    else:
        print('You can\'t go that way')
    #if they type 'get' first
  if move[0] == 'get':
      #if the room contains an item and the item is the one they want to get
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      inventory += [move[1]]

      print(move[1] + "picked up")
        
      del rooms[currentRoom]['item']

    else:
        print("You can't pick that up")
  if 'item' in rooms[currentRoom] and 'Monster' is rooms[currentRoom]['item']:
    print('A monster has got you.....game over man!')
    break
  if currentRoom == 'Garden' and 'key' in inventory and 'potion'in inventory:
    print('You escaped the house with the ultra rare key and magic potion....you win')
    break
