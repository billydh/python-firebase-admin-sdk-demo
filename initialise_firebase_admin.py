import firebase_admin
from firebase_admin import App

app: App = firebase_admin.initialize_app()

if __name__ == "__main__":
    print(app)
