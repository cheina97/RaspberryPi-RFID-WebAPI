#!/usr/bin/env bash

if [ ! -d "/opt/rfidWebService" ]; then
    mkdir -p /opt/rfidWebService
fi

echo "Copying application files file..."

cp -R ./services /opt/rfidWebService/
cp -R ./app.py /opt/rfidWebService/
cp -R ./waitress_server.py /opt/rfidWebService/
cp -R ./scripts/run.sh /opt/rfidWebService/

echo "Copying systemd service ..."

cp ./systemd/rfidwebservice.service /etc/systemd/system/

echo "Reloading systemd deamon ..."
systemctl daemon-reload

echo "Starting rfidwebservice daemon ..."

systemctl start rfidwebservice.service
sleep 5
systemctl status rfidwebservice.service
systemctl enable rfidwebservice.service



