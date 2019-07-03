!/usr/bin/env python3


class Maze():
    def __init__(self,dict={},inventory=[]):
        self.dict = dict
        self.inventory = inventory
		
    def showInstructions(self):
        print('''
        RPG Game
        ========================

        Get to the Garden with a key and a potion
        Avoid Monster!

        Commands:
        go [direction]
        get [item]

        -------------------------
        You are in the hall
        Inventory : %s
        You see a key
        =========================
        
        ''' % (self.inventory))
        c = input(' ')
        return c

    def nextRoom(self,currentRoom):
        print('currentRoom = %s'%(currentRoom))
        if currentRoom == 'Hall':
           c = self.showInstructions()
           if c == 'get key':
              if 'key' not in self.inventory:
                 self.inventory.append(self.dict[currentRoom]['item'])
                 print('type other direction')
                 self.nextRoom(currentRoom)
              else:
                 print('you cant go that way')
                 #c = input(' ')
                 self.nextRoom(currentRoom)
           elif c == 'go south':
                print('hi')
                self.nextRoom(list(self.dict.keys())[1])
           elif c == 'go east':
                self.nextRoom(list(self.dict.keys())[2])
           else:
                print('you cant go that way')
                 #c = input(' ')
                self.nextRoom(currentRoom)
                
        elif currentRoom == 'Kitchen':
             print('A monster has got you .... GAME OVER!!')
             return 0
        elif currentRoom == 'Dining Room':
             print('''
             _________________________
             You are in the Dining Room
             Inventory = %s
             You see a potion
             type command to get potion
             --------------------------
             '''%(self.inventory))
             
             c = input(' ')
             if c == 'get potion':
                if 'potion' not in self.inventory:
                   self.inventory.append(self.dict[currentRoom]['item'])
                   print('type other direction')
                   c = input(' ')
                   if c == 'go south':
                      self.nextRoom(list(self.dict.keys())[3])
                   elif c == 'go west':
                        self.nextRoom(list(self.dict.keys())[0])
                   else:
                        print('you cant go that way')
                        self.nextRoom(currentRoom)
                else:
                   print('type other direction')
                   self.nextRoom(currentRoom)             
             elif c == 'go south':
                  self.nextRoom(list(self.dict.keys())[3])
             elif c == 'go west':
                  self.nextRoom(list(self.dict.keys())[0])
             else:
                  print('you cant go that way')
                  c = input(' ')
                  self.nextRoom(currentRoom)
        elif currentRoom == 'Garden':
             print('''
             _________________________
             You are in the Garden
             Inventory = %s
             --------------------------
             '''%(self.inventory))
             if 'key' in self.inventory and 'potion' in self.inventory:
                print('You escaped the house .... YOU WIN!!')
                return 1
             else:
                print('type other direction')
                c = input(' ')
                if c == 'go north':
                   self.nextRoom(list(self.dict.keys())[2])
                elif c == 'go west':
                   self.nextRoom(list(self.dict.keys())[1])
                else:
                    print('you cant go that way')
                    c = input(' ')
                    self.nextRoom(currentRoom)
def main():
    
   rooms = {  'Hall': {
                      'south' : 'Kitchen',
                      'east'  : 'Dining Room',
                      'item'  : 'key'
                    },
           'Kitchen': {
                      'north' : 'Hall',
                      'item'  : 'Monster',
                      'east'  : 'Garden'
                      },
           'Dining Room':{
                         'west' : 'Hall',
                         'south' : 'Garden',
                         'item'  : 'potion'
                         },
           'Garden' :{
                     'north': 'Dining Room',
                     'west' : 'Kitchen'
                     }



}
   invent = []
   maze_game = Maze(rooms,invent)
   ######## get currentRoom #################
   currentRoom = list(maze_game.dict.keys())[0]
   print("currentRoom = %s"%(currentRoom))  
   
   
   maze_game.nextRoom(currentRoom)
    

main()
   
