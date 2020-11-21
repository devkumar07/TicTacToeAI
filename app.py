from flask import Flask, render_template, request, jsonify
from Board import *
from Cell import *
import json
app = Flask(__name__) 

game = Board()

@app.route('/') 
def hello_world(): 
    return render_template('index.html')

@app.route('/getBoard', methods = ['GET','POST'])
def get_board():
    game.new_game()
    result = game.get_table()
    return json.dumps(result)

@app.route('/init', methods = ['GET','POST'])
def init():
    result = game.get_table()
    return json.dumps(result)

@app.route('/game_status', methods = ['GET','POST'])
def g_status():
    result = game.find_winner()
    if result != '':
        return json.dumps({"result": result + "has won the game"})
    return json.dumps(result)

@app.route('/status', methods = ['GET','POST'])
def status():
    result = game.get_turn()
    return json.dumps({"result": result + "plays now"})

@app.route('/click', methods = ['GET','POST'])
def click():
    if request.method == "POST":
        data = request.json
        print(data)
        x = int(data['row'])
        y = int(data['col'])
        game.update_cell(x,y)
        result = game.get_table()
        return json.dumps(result)
    return json.dumps({'msg':"ERROR"})

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__': 
    app.run() 