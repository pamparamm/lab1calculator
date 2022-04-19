from decimal import Decimal

from variants.basevariant import IVariant


class V10(IVariant):
    @staticmethod
    def f(x: Decimal) -> Decimal:
        fn = 1 / (1 + x**3)
        return fn

    @staticmethod
    def f_transformed(t: Decimal):
        fnt = 1 / (2 * (((t + 1) / 2) ** 3 + 1))
        return fnt

    @staticmethod
    def f_derivative(x: Decimal) -> Decimal:
        return -3 * x**2 / (1 + x**3) ** 2

    @staticmethod
    def a() -> Decimal:
        return Decimal("0")

    @staticmethod
    def b() -> Decimal:
        return Decimal("1")

    @staticmethod
    def etalon() -> Decimal:
        return Decimal(
            "0.8356488482647210533371034597001107667865221274843319432301883149"
        )
