# Dev-Network-Privacy-Toolkit-CLI-
Cross-platform CLI tool designed for developers who need to test applications under different network conditions using local proxy configurations and Tor verification.

Built for controlled development and testing environments only.

  ![animacion](https://media1.tenor.com/m/eRD89_uiAvsAAAAC/nerd-well-actually.gif)


##  Features

- Detects operating system automatically (Windows / Linux / macOS)
- Verifies if Tor process is running
- Detects active SOCKS port (9050 / 9150)
- Validates real Tor network connection
- Activates / deactivates proxy environment variables
- Retrieves public IP
- Logs activity to file
- Modular architecture for scalability



The project follows a modular design to allow easy expansion into a full development toolkit.

---

## ⚙️ Installation

###  Clone the repository

```bash
git clone https://github.com/yourusername/dev-network-privacy-toolkit.git
cd dev-network-privacy-toolkit

```
###  Create virtual environment
```bash
python -m venv venv
```
Activate in Linux/MacOS
```bash
source venv/bin/activate
```
Activate in Windows
```bash
venv\Scripts\activate
```
###  Install dependencies
```bash
pip install -r requirements.txt
```
### ▶️ Usage
```bash
python main.py
```

## The tool will:

Detect OS

Show current public IP

Check Tor status

Allow proxy activation/deactivation

###  Requirements

Python 3.9+

Tor installed (if Tor verification is required)


### ⚠️ Disclaimer

This project is intended strictly for development testing, educational purposes, and controlled environments.
It is not designed to bypass services, evade restrictions, or perform unauthorized activities.


## 🔧 Installing Tor

This tool can verify Tor connectivity if Tor is running locally.

### Linux (Debian/Ubuntu-based)

```bash
sudo apt update && upgrade
sudo apt install tor
sudo systemctl start tor
```
Default SOCKS port: 9050


### Windows

Download Tor Browser from:
https://www.torproject.org/download/

Launch Tor Browser once to start the local SOCKS proxy (usually port 9150).

## Verify Tor is running
```bash
sudo systemctl status tor
```
Tor is not required for basic proxy environment testing, but it is necessary for full Tor network verification.
