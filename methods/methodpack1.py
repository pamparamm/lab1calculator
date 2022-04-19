from decimal import Decimal
from typing import Type

from variants.basevariant import IVariant

from methods.basemethod import IMethod


class LeftRectMethod(IMethod):
    @staticmethod
    def p() -> int:
        return 1

    @staticmethod
    def calc_quadrature(v: Type[IVariant], step: Decimal) -> Decimal:
        result = Decimal("0")
        n = int((v.b() - v.a()) / step)

        for i in range(0, n):
            x_i = v.a() + i * step
            result += v.f(x_i)

        return result * step


class RightRectMethod(IMethod):
    @staticmethod
    def p() -> int:
        return 1

    @staticmethod
    def calc_quadrature(v: Type[IVariant], step: Decimal) -> Decimal:
        result = Decimal("0")
        n = int((v.b() - v.a()) / step)

        for i in range(1, n + 1):
            x_i = v.a() + i * step
            result += v.f(x_i)

        return result * step


class MiddleRectMethod(IMethod):
    @staticmethod
    def p() -> int:
        return 2

    @staticmethod
    def calc_quadrature(v: Type[IVariant], step: Decimal) -> Decimal:
        result = Decimal("0")
        n = int((v.b() - v.a()) / step)

        for i in range(0, n):
            x_i = v.a() + i * step + step / 2
            result += v.f(x_i)

        return result * step
