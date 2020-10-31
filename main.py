import logging
from flaskr.routes import count
from init.getdata import initrawfiles
from flask import Flask

app = Flask(__name__)
app.register_blueprint(count)


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    logging.info("Starting ...")

    initrawfiles()

    app.run(debug=True)
