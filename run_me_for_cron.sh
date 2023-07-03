#!/bin/bash

echo -e "0 0 * * * ansible python3 /opt/scripts/backups/backup.py" > /etc/cron.d/cisco_ios_24


