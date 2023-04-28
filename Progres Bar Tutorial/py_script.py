import time

for x in range(0,10):
    #socketio.emit("update progress", x * 20, to=socketid) 
    print(f"step: {x}\n")
    time.sleep(1)    
