# Network Testing

## Requirements
- Tested on Ubuntu 24.04
```
sudo apt install python3-virtualenv
sudo apt install wireshark

# For pyShark
sudo apt install tshark
# For scapy pdf dump
sudo apt-get install 

# Setup repo
virtualenv -p python3 .venv 
source .venv/bin/activate
pip -r requirements.txt
```

## Run
```
# If super user privilege needed
sudo .venv/bin/python3 netTest.py
```

