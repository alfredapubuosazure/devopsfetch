#!/bin/bash

# Update and install dependencies
sudo apt update
sudo apt install -y python3 python3-pip docker.io nginx
pip3 install prettytable

# Copy the devopsfetch script to /usr/local/bin
sudo cp devopsfetch.py /usr/local/bin/devopsfetch
sudo chmod +x /usr/local/bin/devopsfetch

# Setup systemd service
sudo cp devopsfetch.service /etc/systemd/system/devopsfetch.service
sudo systemctl daemon-reload
sudo systemctl enable devopsfetch.service
sudo systemctl start devopsfetch.service

# Setup log rotation
sudo tee /etc/logrotate.d/devopsfetch << EOF
/var/log/devopsfetch.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
    create 0640 root root
    postrotate
        systemctl reload devopsfetch.service > /dev/null 2>&1 || true
    endscript
}
EOF

echo "Installation complete."

