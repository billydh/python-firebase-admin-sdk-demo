import argparse
from typing import Optional

from firebase_admin import auth
from firebase_admin.auth import UserRecord

from initialise_firebase_admin import app


def get_email_arg():
    parser = argparse.ArgumentParser(description="Create a new user in Firebase")
    parser.add_argument("--email", required=True, help="The email address of the new user to be created")
    parser.add_argument("--user-id", required=False,
                        help="The user id to assign to the new user. If this is not specified, "
                             "Firebase will generate a random string.")

    return parser.parse_args()


def create_user(email: str, user_id: Optional[str]) -> UserRecord:
    return auth.create_user(email=email, uid=user_id) if user_id else auth.create_user(email=email)


if __name__ == "__main__":
    arg = get_email_arg()
    new_user: UserRecord = create_user(arg.email, arg.user_id)

    print(f"Firebase successfully created a new user with email - {new_user.email} and user id - {new_user.uid}")
