import os
import random

import cherrypy

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""


class Battlesnake(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "ArtiskOnGit",  # TODO: Your Battlesnake Username
            "color": "#FFDFBA",  # TODO: Personalize
            "head": "smile",  # TODO: Personalize
            "tail": "sharp",  # TODO: Personalize
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        data = cherrypy.request.json

        print("START")
        return "ok"





    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
# {
#   "id": "totally-unique-snake-id",
#   "name": "Sneky McSnek Face",
#   "health": 54,
#   "body": [
#     {"x": 0, "y": 0},
#     {"x": 1, "y": 0},
#     {"x": 2, "y": 0}
#   ],
#   "latency": "123",
#   "head": {"x": 0, "y": 0},
#   "length": 3,
#   "shout": "why are we shouting??",
#   "squad": "1"
# }



        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        data = cherrypy.request.json
        head = data["you"]["head"] #{"x": 0, "y": 0}
        possible_moves = ["up", "down", "left", "right"]

        headminusone = data["you"]["body"][1]
        if head["x"] == headminusone["x"] + 1:
            possible_moves.remove("left")
        if head["x"] == headminusone["x"] - 1:
            possible_moves.remove("right")
        if head["y"] == headminusone["y"] + 1:
            possible_moves.remove("up")
        if head["y"] == headminusone["y"] - 1:
            possible_moves.remove("down")




        # Choose a random direction to move in
        possible_moves = ["up", "down", "left", "right"]
        move = random.choice(possible_moves)

        print(f"MOVE: {move}")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json

        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
