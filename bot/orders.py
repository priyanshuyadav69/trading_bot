import logging
from .client import get_client

def place_order(symbol, side, order_type, quantity, price=None):

    client = get_client()

    try:
        logging.info(f"Sending order: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )
        
        

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
        
        

        logging.info(f"Response: {order}")

        return order

    except Exception as e:
        logging.error(f"Order failed: {str(e)}")
        raise