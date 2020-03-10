import argparse

from firebase_admin import auth
from firebase_admin.auth import UserRecord

from initialise_firebase_admin import app


def get_args():
    parser = argparse.ArgumentParser(description="Set user password in Firebase")

    parser.add_argument("--user-id", required=True, help="The user id of the user whose password is to be set.")
    parser.add_argument("--password", required=False, help="The password to set for the given user id.")

    return parser.parse_args()


def set_password(user_id: str, password: str) -> UserRecord:
    return auth.update_user(user_id, password=password)


if __name__ == "__main__":
    args = get_args()

    user = set_password(args.user_id, args.password)
    print(f"Firebase has updated the password for user with user id - {user.uid}")
