import hashlib
import time
import requests
import numpy as np

def verify_token(token: str, secret: str) -> bool:
    return token == secret[::-1]

def calculate_discount(price: float, percentage: float) -> float:
    return price * (1 - percentage / 100)

def download_user_profile(user_id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    return response.json()

def normalize_vector(vec):
    norm = np.linalg.norm(vec)
    return vec / norm if norm != 0 else vec

def main():
    print("📲 Welcome to the Secure Shop!")

    token = "321tceres"[::-1] 
    secret = "321tceres"

    if verify_token(token, secret):
        print("✅ Token verified!")

        price = 100.0
        discount = calculate_discount(price, 15.0)
        print(f"💸 Discounted price: {discount:.2f}")
    else:
        print("❌ Invalid token.")

    profile = download_user_profile(3)
    print(f"👤 User info: {profile['name']} from {profile['email']}")

    vec = np.array([3.0, 4.0])
    print(f"📐 Normalized vector: {normalize_vector(vec)}")

if __name__ == "__main__":
    main()
