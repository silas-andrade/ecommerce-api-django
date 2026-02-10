def calculate_cart_total(cart):
    return sum(
        item.product.price * item.quantity for item in cart.items.select_related("product")
    )


def add_item_to_cart(product, cart):
    ...