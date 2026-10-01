import json

from order_pricing.cli import main


def test_cli_prints_priced_order(capsys):
    assert main(["examples/order.json"]) == 0
    assert json.loads(capsys.readouterr().out)["total"] == 1089.08


def test_cli_without_args_shows_usage(capsys):
    assert main([]) == 1
    assert "python -m order_pricing.cli" in capsys.readouterr().out
