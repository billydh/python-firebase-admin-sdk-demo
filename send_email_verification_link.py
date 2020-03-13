import argparse
import json
import os
from pprint import pprint

import requests

FIREBASE_WEB_API_KEY = os.environ.get("FIREBASE_WEB_API_KEY")
rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"


def get_id_token_arg():
    parser = argparse.ArgumentParser(description="Send email verification link to user")

    parser.add_argument("--firebase-id-token", required=True, help="The Firebase ID token of the user to verify.")

    return parser.parse_args()


def send_email_verification_link(id_token: str):
    payload = json.dumps({
        "requestType": "VERIFY_EMAIL",
        "idToken": id_token
    })

    r = requests.post(rest_api_url,
                      params={"key": FIREBASE_WEB_API_KEY},
                      data=payload)

    return r.json()


if __name__ == "__main__":
    arg = get_id_token_arg()
    email_address_to_verify = send_email_verification_link(arg.firebase_id_token)
    pprint(email_address_to_verify)
