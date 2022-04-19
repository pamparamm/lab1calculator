from decimal import Decimal
from variants.basevariant import IVariant


class V5(IVariant):
    @staticmethod
    def f(x: Decimal) -> Decimal:
        return (1 + x**2).ln()

    @staticmethod
    def f_transformed(t: Decimal):
        return (1 + ((t + 1) / 2) ** 2).ln() / 2

    @staticmethod
    def f_derivative(x: Decimal):
        return 2 * x / (x**2 + 1)

    @staticmethod
    def a() -> Decimal:
        return Decimal("0")

    @staticmethod
    def b() -> Decimal:
        return Decimal("1")

    @staticmethod
    def etalon() -> Decimal:
        return Decimal(
            "0.2639435073548419286485538130979280101740848340478081646081523056"
        )
