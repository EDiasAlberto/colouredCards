import random
import time

class card:
    def __init__(self, colour, value):
        self.colour = colour
        self.value = value

class player:

    def __init__(self, name, password, deck, currentCard):
        self.deck=deck
        self.name=name
        self.password=password
        self.currentCard=currentCard

    def winCard(self,card):
        self.deck.append(card)

    def verify(self):
        usrName=input("Please enter a username:")
        psWord=input("Please enter a password:")
        if usrName==self.name and psWord==self.password:
            print("Login Successful")
        else:
            print("Incorrect Username/Password. Please try again.")
            self.verify()

player1=player("David", "password123", [], "")
player2=player("John", "password456", [], "")
gameDeck=[]

for y in ["red", "black", "yellow"]:
    for x in range(1, 11):
        gameDeck.append(card(y,x))

random.shuffle(gameDeck)

print("Please login, player 1.")
player1.verify()
print("\nPlease login, player 2.")
player2.verify()

while len(gameDeck)>0:
    print("Drawing cards...")
    time.sleep(1)
    player1.currentCard=gameDeck.pop(0)
    player2.currentCard=gameDeck.pop(0)
    print(f"Player 1's card: {player1.currentCard.colour},{player1.currentCard.value}")
    print(f"Player 2's card: {player2.currentCard.colour},{player2.currentCard.value}")
    if player1.currentCard.colour==player2.currentCard.colour:
        if player1.currentCard.value>player2.currentCard.value:
            player1.deck.append(player1.currentCard)
            player1.deck.append(player2.currentCard)
            print("Player 1 wins this round.")
        elif player1.currentCard.value<player2.currentCard.value:
            player2.deck.append(player1.currentCard)
            player2.deck.append(player2.currentCard)
            print("Player 2 wins this round.")
    elif (player1.currentCard.colour=="red" and player2.currentCard.colour=="black") or (player1.currentCard.colour=="yellow" and player2.currentCard.colour=="red") or (player1.currentCard.colour=="black" and player2.currentCard.colour=="yellow"):
            player1.deck.append(player1.currentCard)
            player1.deck.append(player2.currentCard)
            print("Player 1 wins this round.")
    elif (player2.currentCard.colour=="red" and player1.currentCard.colour=="black") or (player2.currentCard.colour=="yellow" and player1.currentCard.colour=="red") or (player2.currentCard.colour=="black" and player1.currentCard.colour=="yellow"):
            player2.deck.append(player1.currentCard)
            player2.deck.append(player2.currentCard)
            print("Player 2 wins this round.")
    print()
    print(f"Player 1 has {len(player1.deck)} cards. \nPlayer 2 has {len(player2.deck)} cards.")
    print()

file=open("output.txt", "a")

if len(player1.deck)>len(player2.deck):
    print("Player 1 wins the game.")
    print("Player 1's deck:")
    for x in player1.deck:
        print(x.colour, x.value)
    dataToWrite=f"{player1.name}, {len(player1.deck)}\n"
    file.write(dataToWrite)
elif len(player2.deck)>len(player1.deck):
    print("Player 2 wins the game.")
    print("Player 2's deck:")
    for x in player2.deck:
        print(x.colour, x.value)
    dataToWrite=f"{player2.name}, {len(player2.deck)}\n"
    file.write(dataToWrite)
else:
    print("The game ends in a draw.")
    print("Player 1's deck:")
    for x in player1.deck:
        print(x.colour, x.value)
    print()
    print("Player 2 wins the game.")
    print("Player 2's deck:")
    for x in player2.deck:
        print(x.colour, x.value)

file.close()

fileData=[]
file=open("output.txt", "r")
line=file.readline()
data=line.strip().split(",")
while line!="":
    fileData.append(data)
    line=file.readline()
    data=line.strip().split(",")

print()

fileData=sorted(fileData, key=lambda x:x[1], reverse=True)
print("Top 5 Player Scores:")
for x in range(5):
    print(fileData[x][0], fileData[x][1])
file.close()
