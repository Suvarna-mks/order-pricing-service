from dataclasses import dataclass, field


@dataclass
class LineItem:
    sku: str
    qty: int


@dataclass
class Order:
    items: list[LineItem]
    coupon: str | None = None
    express: bool = False
    state: str = "KA"
    notes: list[str] = field(default_factory=list)
