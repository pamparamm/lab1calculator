from decimal import Decimal
from variants.basevariant import IVariant
from utils.trig import cos, sin


class V2(IVariant):
    @staticmethod
    def f(x: Decimal) -> Decimal:
        return cos(pow(x, 3))

    @staticmethod
    def f_transformed(t: Decimal):
        return cos(pow((t+1)/2, 3)) / 2

    @staticmethod
    def f_derivative(x: Decimal):
        return -3 * pow(x, 2) * sin(pow(x, 3))

    @staticmethod
    def a() -> Decimal:
        return Decimal("0")

    @staticmethod
    def b() -> Decimal:
        return Decimal("1")

    @staticmethod
    def etalon() -> Decimal:
        return Decimal(
            "0.9317044405915442260769263906"
        )
