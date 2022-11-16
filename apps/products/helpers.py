def built_data(product, message, send_date):
    """Create data for Notification

    Send formatted notification to server
    """
    return {
        "id": "",
        "message": message,
        "product": product.reference,
        "context": "PRODUCT",
        "token": "",
        "send_date": send_date,
    }


def creation_message(product, date_time):
    """Custom creation message, will do for updates also"""
    return f"""{product.designation} a était mis a jours {product.reference}. avec qte: {product.tonne}
        valeur: {product.value}, date/heure: {date_time:%d-%m-%Y} at {date_time:%H:%m}
        """
