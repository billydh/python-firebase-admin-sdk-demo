import argparse

from firebase_admin import auth
from firebase_admin.auth import UserRecord

from initialise_firebase_admin import app


def get_args():
    parser = argparse.ArgumentParser(description="Update user details in Firebase")

    parser.add_argument("--user-id", required=True, help="The user id of the user whose details are to be updated.")
    parser.add_argument("--email", required=False, help="The new email address to replace the existing email.")
    parser.add_argument("--mobile-number", required=False, help="The new mobile number to replace the existing number.")
    parser.add_argument("--display-name", required=False, help="The new display name to replace the existing name.")

    return parser.parse_args()


def update_email(user_id: str, email: str) -> UserRecord:
    return auth.update_user(user_id, email=email)


def update_mobile(user_id: str, mobile_no: str) -> UserRecord:
    return auth.update_user(user_id, phone_number=mobile_no)


def update_display_name(user_id: str, display_name: str) -> UserRecord:
    return auth.update_user(user_id, display_name=display_name)


if __name__ == "__main__":
    args = get_args()

    if args.email:
        updated_user = update_email(args.user_id, args.email)
        print(f"Updated user email to {updated_user.email}")

    if args.mobile_number:
        updated_user = update_mobile(args.user_id, args.mobile_number)
        print(f"Updated user mobile number to {updated_user.phone_number}")

    if args.display_name:
        updated_user = update_display_name(args.user_id, args.display_name)
        print(f"Updated user display name to {updated_user.display_name}")
