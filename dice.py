from random import randint
from flask import Flask, request, render_template

app = Flask(__name__)

# start of the application -> returning the page to ask users to enter their names
@app.route('/')
def load():
    return render_template('dice-start.html')

# start of game -> after entering their names, the players are routed to the game's main page
@app.route('/game', methods=['POST'])
def loadgame():
    player1 = request.form['player1']
    player2 = request.form['player2']
    player = player1
    p1score = 0
    p2score = 0
    dice = 0

    return render_template('dice-game.html', player1=player1, player2=player2, p1score=p1score, p2score=p2score, player=player, dice=dice)

# player chooses to "ROLL"
@app.route('/roll', methods=['POST'])
def roll():
    # take all current values of the form
    player1 = request.form['player1']
    player2 = request.form['player2']
    player = request.form['player']
    p1score = int(request.form['p1score'])
    p2score = int(request.form['p2score'])
    winner = ""

    # get a random number from 1 to 6 every time(like rolling a dice)
    dice = randint(1, 6) 

    # while the current player is player 1
    while(player == player1):
    
        # if they roll a one, their score resets and it is player 2's turn
        if (dice == 1):
            p1score = 0
            player = player2
            
            return render_template('dice-game.html', player1=player1, player2=player2, p1score=p1score, p2score=p2score, player=player, dice=dice)

        # if they roll 2-6, add it to their current score
        else:
            p1score = p1score + dice
            break
    
    # while the current player is player 2
    while(player == player2):
    
        # if they roll a one, their score resets and it is player 1's turn
        if (dice == 1):
            p2score = 0
            player = player1

            return render_template('dice-game.html', player1=player1, player2=player2, p1score=p1score, p2score=p2score, player=player, dice=dice)

        # if they roll 2-6, add it to their current score
        else:
            p2score = p2score + dice
            break


    # First to reach 20 points wins, and they are returned to the home page
    if(p1score >= 20):
        winner = player1 + " won the last game!"
        return render_template('dice-start.html', player1=player1, player2=player2, winner=winner)
    
    if(p2score >= 20):
        winner = player2 + " won the last game!"
        return render_template('dice-start.html', player1=player1, player2=player2, winner=winner)

    return render_template('dice-game.html', player1=player1, player2=player2, p1score=p1score, p2score=p2score, player=player, dice=dice)

# player chooses to "HOLD"
@app.route('/hold', methods=['POST'])
def hold():
    # take current form values
    player1 = request.form['player1']
    player2 = request.form['player2']
    player = request.form['player']
    p1score = int(request.form['p1score'])
    p2score = int(request.form['p2score'])  
    dice = 0

    # if the current player is player 1, it becomes player 2's turn
    if(player == player1):
        player = player2

        return render_template('dice-game.html',player1=player1, player2=player2, p1score=p1score, p2score=p2score, player=player, dice=dice)

    # if the current player is player 2, it becomes player 1's turn
    if(player == player2):
        player = player1

        return render_template('dice-game.html',player1=player1, player2=player2, p1score=p1score, p2score=p2score, player=player, dice=dice)

if __name__ == '__main__':
    app.run(debug=True)
