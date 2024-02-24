# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:41:46 2024

@author: ikowa
"""
 
import json
            
        
def getMenuChoice():
    print("""
          0) exit
       1) load default game
       2) load a game file
       3) save the current game
       4) edit or add a node
       5) play the current game
    """)
    menu = input("Select a number")
    return menu
def getDefaultGame():
    
    defaultGame = {"start": ["default start node", "start over", "start","Quit","quit"],}
    print("Loaded default game")
    return defaultGame
def playGame(game):
    keepGoing2  = True
    currentNode = playNode(game,"start")
    while keepGoing2:
        if currentNode == "quit":
            print("game over!")
            keepGoing2 = False
        else:
            currentNode = playNode(game,currentNode)
def loadGame():
    infile = open("game.json","r")
    game = json.load(infile)
    print(game)
    infile.close()
    return game
def saveGame(game):
    outfile = open("game.json","w")
    json.dump(game,outfile,indent =2)
    outfile.close()
    print(json.dumps(game, indent = 2))
    print("saved story data to game.json")

def editField(game,node):
    gamelayout = ("Description","MenueA","NodeA","MenueB","NodeB")
    for index,changenode in enumerate(game[node]):
        userinput = input(f"{gamelayout[index]} ({game[node][index]}):")
        if userinput == "":
            game[node][index] = changenode
        else:
            game[node][index] = userinput
def editNode(game):
    print("Create or edit a node")
    print("Current nodes:")
    for item in game.keys():
        print(item)
    userinput = input("Choose node to edit or enter new node")
    if userinput in game.keys():
        editField(game,userinput)
    else:
        game[userinput] = ["","","","",""]
        editField(game,userinput)
   

    
def playNode(game,currentNode):
    
    if currentNode in game.keys():
   
        (desc, menuA, nodeA, menuB, nodeB) = game[currentNode]
    
        print(f'{game[currentNode][0]}')
        decision = input(f"""Choose your next move
        1. {game[currentNode][1]}
        2. {game[currentNode][3]} """)
        if decision == "1":
            currentNode = nodeA
        elif decision == "2":
            currentNode = nodeB
        
        else:
            print("That's not an option! Type 1 or 2")
            return currentNode
    
        #this should be playnode, playgame should be the main from last week 
        
    else:
        print(f"That node, {currentNode} doesn't exist! Ending the game")
        currentNode = "quit"
    
    return currentNode
def main():
   keepGoing = True
   game = getDefaultGame()
   #Just do if staments for code
   while keepGoing:
       menu = getMenuChoice()
       if menu == "0":
          keepGoing = False
       elif menu == "1":
          game = getDefaultGame()
       elif menu =="2":
           game=loadGame()
       elif menu =="3":
          saveGame(game)
       elif menu =="4":
           editNode(game)
       elif menu =="5":
           playGame(game)
       else:
           print("That's not right! try again")
           main()
           #menu = getMenuChoice()
main()