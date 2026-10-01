import pytest

from order_pricing.shipping import shipping_fee


@pytest.mark.parametrize("amount,fee", [(500, 49), (999, 49), (999.01, 0), (1500, 0)])
def test_free_shipping_boundary(amount, fee):
    assert shipping_fee(amount) == fee


def test_express_and_remote_add_up():
    assert shipping_fee(500, express=True, state="LA") == 49 + 99 + 150
