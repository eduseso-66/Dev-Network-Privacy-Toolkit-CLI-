import psutil
import socket

def is_tor_process_running():
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'] and "tor" in process.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

def is_tor_port_open(port=9050):
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=3):
            return True
    except:
        return False

def detect_tor_port():
    for port in [9050, 9150]:
        if is_tor_port_open(port):
            return port
    return None

def detect_tor_status():
    process_running = is_tor_process_running()
    port = detect_tor_port()
    if not process_running and not port:
        return "No se detecta Tor"
    elif process_running and port:
        return f"Tor detectado (proceso y puerto {port} activos)"
    elif process_running:
        return "Tor detectado (proceso activo, puerto no detectado)"
    else:        
        return f"Tor detectado (puerto {port} abierto, proceso no detectado)"
    
    
