# https://github.com/MyPingO/FlaskProgressBarTutorial (fork)

from asyncio import sleep
from website import create_app
from flask import render_template, Response
from flask_socketio import SocketIO

app = create_app()
socketio = SocketIO(app)

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/progress/<socketid>", methods = ["POST"])
async def progress(socketid):
    
    for x in range(0,6):
        socketio.emit("update progress", x * 20, to=socketid) 
        await sleep(1)    

    return Response(status=204)

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    socketio.run(app=app, debug=True, host="0.0.0.0", port = 25565)