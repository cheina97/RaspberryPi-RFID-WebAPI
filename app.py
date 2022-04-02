from services import rfid
from flask import Flask, jsonify, abort
from flask_cors import CORS
import atexit


def close_handler():
    print("Closing the application ...")
    rfid.close_RFID()
    print("Application closed")


atexit.register(close_handler)
app = Flask(__name__)
CORS(app)


@app.errorhandler(500)
def internal_server_error(e):
    return str(e), 500


@app.route("/rfid")
def getRFID():
    try:
        return {"uid": rfid.read_RFID()}, 200
    except Exception as err:
        abort(500, description=err)
