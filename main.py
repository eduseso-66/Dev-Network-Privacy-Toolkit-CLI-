from core.os_detector import detect_os
from core.network_check import get_public_ip
from core.proxy_manager import activate_proxy, deactivate_proxy
from core.logger import setup_logger
from core.tor_detector import detect_tor_status
import json

def load_config():
    with open("config/settings.json", "r") as f:
        return json.load(f)

def main():
    logger = setup_logger()
    config = load_config()
    tor_status = detect_tor_status()
    logger.info(f"Estado de Tor: {tor_status}")

    if tor_status.startswith("No se detecta Tor"):
        print("No se detecta Tor en el sistema.")
    else:        
        print(f"Estado de Tor: {tor_status}")

    os_name = detect_os()
    print(f"Sistema detectado: {os_name}")

    current_ip = get_public_ip()
    print(f"IP actual: {current_ip}")

    while True:
        print("\n1. Activar Proxy")
        print("2. Desactivar Proxy")
        print("3. Ver IP actual")
        print("4. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            activate_proxy(config["proxy"])
            logger.info("Proxy activado")
            print("Proxy activado.")
        elif choice == "2":
            deactivate_proxy()
            logger.info("Proxy desactivado")
            print("Proxy desactivado.")
        elif choice == "3":
            print(f"IP actual: {get_public_ip()}")
        elif choice == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()