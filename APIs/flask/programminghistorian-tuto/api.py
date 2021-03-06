import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    string = str("<h1>Distant Reading Archive</h1><p>This "
                 + "site is a prototype API for distant "
                 + "reading of science fiction novels.</p>")

    return string


app.run()
