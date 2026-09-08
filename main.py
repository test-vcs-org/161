import certifi
import requests


def fetch(url: str) -> int:
    response = requests.get(url, verify=certifi.where(), timeout=10)
    return response.status_code


if __name__ == "__main__":
    print(fetch("https://example.com"))
