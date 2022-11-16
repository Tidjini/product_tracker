class Notification:

    message: str = ""
    context: str = ""
    token: str = ""
    send_date: str = ""


class ProductNotification(Notification):

    product: dict = {}
