from flask import Flask, render_template, request
import os,socket

app = Flask(__name__)

image = "graph.png"

@app.route('/')
def index():
    host_name = "{} to {}".format(socket.gethostname(), request.remote_addr)

    image_path = "/static/images/" + image

    return render_template('index.html', image_path=image_path, host_name=host_name)

# Main
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    try:
        app.run(host="0.0.0.0", port=port, debug=True)
    except Exception as ex:
        print(ex)
