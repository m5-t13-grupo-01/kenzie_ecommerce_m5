class NotAvailableException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


def isAvailableProduct(product):
    if not product.is_available:
        raise NotAvailableException("Product isn't available.")
