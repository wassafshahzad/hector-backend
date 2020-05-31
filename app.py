from flask import Flask, request, jsonify
from AI.Hector import Hector
from AI.node import Node
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/tree',methods=['POST'])
def create_tree():
    if(request.json.get('index')):
        index = request.json.get('index')
        game = Node(['+']*9, 'player')
        hec = Hector(game)
        game.play_turn(int(index))
        hec.generate_move_tree(game)
        return jsonify(hec.moves)
    else:
        return {"value" : "no data sent"}
    

@app.route('/', methods = ["GET"])
def test_api():
    return {"s" : "clear"}

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)