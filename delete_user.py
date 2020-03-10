import argparse

from firebase_admin import auth

from initialise_firebase_admin import app


def get_user_id_arg():
    parser = argparse.ArgumentParser(description="Delete user in Firebase")
    parser.add_argument("--user-id", required=True, help="The user id of the user to be deleted.")

    return parser.parse_args()


def delete_user(user_id: str):
    return auth.delete_user(user_id)


if __name__ == "__main__":
    args = get_user_id_arg()

    user = delete_user(args.user_id)
    print(f"Firebase has deleted user with user id - {args.user_id}")
