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
@click.option("--stop_price", type=float)

def main(symbol, side, order_type, quantity, price ,stop_price):

    try:
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)

        if order_type == "LIMIT":
            if price is None:
                raise ValueError("LIMIT orders require price")

        if order_type == "STOP_LIMIT":                          
            if price is None:
                raise ValueError("STOP_LIMIT orders require --price (the limit execution price)")
            if stop_price is None:
                raise ValueError("STOP_LIMIT orders require --stop_price (the trigger price)")
            if stop_price == price:
                raise ValueError("--stop_price and --price must be different values")

        print("\nOrder Request Summary")
        print("----------------------")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)
        print("Price:", price)
        print("Stop Price:", stop_price) 

        order = place_order(symbol, side, order_type, quantity, price , stop_price)



        print("\nOrder Response")
        print("----------------------")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice"))

        print("\nOrder placed successfully")

    except Exception as e:
        msg = str(e)
        if "4164" in msg:
            print("\nError: Order value too small. Quantity × Price must be at least $100.")
            print("Tip: Increase your --quantity and try again.")
        else:
            print("\nError:", msg)


if __name__ == "__main__":
    main()