import os

def activate_proxy(proxy_url):
    os.environ["http_proxy"] = proxy_url
    os.environ["https_proxy"] = proxy_url

def deactivate_proxy():
    os.environ.pop("http_proxy", None)
    os.environ.pop("https_proxy", None)