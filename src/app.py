from flask import Flask

from config.setup_app import setup_app

app = Flask(__name__)
setup_app(app)

if __name__ == "__main__":
    app.run()
