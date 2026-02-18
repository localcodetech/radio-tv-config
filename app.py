

import flask 


app = flask.Flask(__name__)


@app.route("/")
def index():
    return "hello"

@app.route("/admin")
def admin_page():
    pass







if __name__ =="__main__":
    app.run(debug=True)