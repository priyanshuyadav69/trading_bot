import click
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger

setup_logger()

@click.command()
@click.option("--symbol", required=True, help="Trading symbol e.g. BTCUSDT")
@click.option("--side", required=True, help="BUY or SELL")
@click.option("--order_type","order_type", required=True, help="MARKET or LIMIT")
@click.option("--quantity", required=True, type=float)
@click.option("--price", type=float)

def main(symbol, side, order_type, quantity, price):

    try:
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)

        if order_type == "LIMIT":
            if price is None:
                raise ValueError("LIMIT orders require price")

        print("\nOrder Request Summary")
        print("----------------------")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)
        print("Price:", price)

        order = place_order(symbol, side, order_type, quantity, price)

        print("\nOrder Response")
        print("----------------------")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice"))

        print("\nOrder placed successfully")

    except Exception as e:
        print("\nError:", str(e))


if __name__ == "__main__":
    main()