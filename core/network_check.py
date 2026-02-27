import requests

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        return response.json()["ip"]
    except:
        return "No se pudo obtener IP"
    

def verify_tor_connection(port):
    proxies = {
        "http": f"socks5h://127.0.0.1:{port}",
        "https": f"socks5h://127.0.0.1:{port}"
    }

    try:
        response = requests.get(
            "https://check.torproject.org/api/ip",
            proxies=proxies,
            timeout=10
        )
        data = response.json()
        return data.get("IsTor", False)
    except:
        return False

