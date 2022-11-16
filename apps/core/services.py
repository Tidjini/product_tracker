# push notifications for changes
import requests


class NotificationAPI:
    """Notification

    make sure to make it litle bit complet:
        - like users token creadential
        - context ...
    """

    @staticmethod
    def push(url, data):
        """Push notification post data to remote service.

        Node service work with socket IO.
        """

        try:
            response = requests.post(url, data=data, timeout=10)
        except Exception as e:
            print("Push Notification Exception due to: ", e)
