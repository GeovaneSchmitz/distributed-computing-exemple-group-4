from flask import Flask, request
#cors 
from flask_cors import CORS
from uuid import uuid4
from time import sleep
from random import randint
from time import time
app = Flask(__name__)
# Enable CORS for all routes
CORS(app)
my_uuid = str(uuid4())

def busy_wait(dt):   
    current_time = time()
    while (time() < current_time+dt):
        pass

@app.route("/random")
def get_data():
    max_number = request.args.get("max_number", default=10, type=int)
    sleep_time = request.args.get("sleep_time", default=0, type=int)
    if sleep_time < 0:
        sleep_time = 0
    if sleep_time != 0:
        busy_wait(sleep_time)

    return {
        "uuid": my_uuid,
        "x": randint(0, max_number),
        "y": randint(0, max_number),
    }

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path

if __name__ == "__main__":
    # Run the Flask app
    # Host '0.0.0.0' makes the server accessible from outside the container
    # Port 5000 is the default Flask port
    app.run(host="0.0.0.0", port=5000)
