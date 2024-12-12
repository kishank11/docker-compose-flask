from datetime import time
from flask import Flask
import redis
import redis.exceptions


cache = redis.Redis(host='redis',port=6379)
import os
app = Flask(__name__)

def hit_count():
    retries = 5
    while True:
        try:
            cache.reset()
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)



        

@app.route("/",methods=['GET'])
def home():
    count = hit_count()
    return "HELLO MR KK! I have seen {} times. \n".format(count)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)