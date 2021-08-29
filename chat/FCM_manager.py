import firebase_admin
from firebase_admin import credentials, messaging


cred = credentials.Certificate('./fir-test1-33bdc-firebase-adminsdk-w8gwg-b343afcfc9.json')
firebase_admin.initialize_app(cred)


def send_push(title, msg, registration_token, dataObject=None):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(title=title, body=msg),
        data=dataObject,
        tokens=registration_token
    )
    response = messaging.send_multicast(message)
    print('sucess:', response)
