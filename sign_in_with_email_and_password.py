import argparse
import json
import os
import requests
import pprint

FIREBASE_WEB_API_KEY = os.environ.get("FIREBASE_WEB_API_KEY")
rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"


def get_args():
    parser = argparse.ArgumentParser(description="Sign in a Firebase user with email and password")

    parser.add_argument("--email", required=True, help="The email address which the user wants to sign in with.")
    parser.add_argument("--password", required=True, help="The password of the user.")

    return parser.parse_args()


def sign_in_with_email_and_password(email: str, password: str, return_secure_token: bool = True):
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": return_secure_token
    })

    r = requests.post(rest_api_url,
                      params={"key": FIREBASE_WEB_API_KEY},
                      data=payload)

    return r.json()


if __name__ == "__main__":
    args = get_args()
    token = sign_in_with_email_and_password(args.email, args.password)
    pprint.pprint(token)
