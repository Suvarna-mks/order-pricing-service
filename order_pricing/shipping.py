FREE_SHIPPING_ABOVE = 999
STANDARD_FEE = 49
EXPRESS_FEE = 99
REMOTE_STATES = {"AN", "LD", "LA"}  # Andaman, Lakshadweep, Ladakh
REMOTE_SURCHARGE = 150


def shipping_fee(amount_after_discount, express=False, state="KA"):
    fee = 0 if amount_after_discount > FREE_SHIPPING_ABOVE else STANDARD_FEE
    if express:
        fee += EXPRESS_FEE
    if state in REMOTE_STATES:
        fee += REMOTE_SURCHARGE
    return fee
