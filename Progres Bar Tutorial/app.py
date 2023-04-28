# https://github.com/MyPingO/FlaskProgressBarTutorial (fork)
# progress bar JS example 
#    - https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_progressbar_3

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

    import subprocess, json
    """
    # execute subprocess with script
    continue_loop = True
    text = ""
    x = 0
    while continue_loop:    
        text = subprocess.run(["cmd", "/c", "python.exe", "py_script.py"],capture_output=True)
        while text == "":
            print(f"Text: {text}\n")
            socketio.emit("update progress", x * 20, to=socketid)
            await sleep(1)   
            if x <101:
                x = x + 20
            else:
                x = 0
        continue_loop = False
    """             

    for x in range(0,6):
        socketio.emit("update progress", x * 20, to=socketid) 
        await sleep(1)    

    return Response(status=204)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/pbExample")
def pbExample():
    return render_template("pbExample.html")


if __name__ == "__main__":
    socketio.run(app=app, debug=True, host="0.0.0.0", port = 25565)