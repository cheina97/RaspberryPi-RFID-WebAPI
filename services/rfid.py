#!/usr/bin/env python3

from pirc522 import RFID

rdr = RFID()
util = rdr.util()
err_exc = Exception("Exception in RFID service")


def read_RFID():
    print("RFID service called")
    print("Waiting for an RFID tag ...")
    rdr.wait_for_tag()
    (error, data) = rdr.request()
    if error:
        print("Error: cannot read the card")
        raise err_exc
    print("Detected: " + format(data, "02x"))
    (error, uid) = rdr.anticoll()
    if error:
        print("Error: cannot read the card")
        raise err_exc
    uid = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
    print("Card read UID: "+uid)
    return uid


def close_RFID():
    rdr.cleanup()
