import re

UPI_PATTERN = re.compile(r"^[a-zA-Z0-9._-]{2,256}@[a-zA-Z]{2,64}$")


class Validator:
    """Checks payment details (card number or UPI id). Same class name as the
    order validator on purpose - they live in different packages."""

    def validate(self, method, value):
        if method == "card":
            return self.is_valid_card(value)
        if method == "upi":
            return bool(UPI_PATTERN.match(value))
        raise ValueError(f"unsupported payment method: {method}")

    def is_valid_card(self, number):
        digits = number.replace(" ", "")
        if not digits.isdigit() or not 13 <= len(digits) <= 19:
            return False
        # Luhn check
        total = 0
        for i, d in enumerate(reversed(digits)):
            n = int(d)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0
