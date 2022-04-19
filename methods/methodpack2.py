from decimal import Decimal
from typing import Type

from variants.basevariant import IVariant

from methods.basemethod import IMethod


class TrapMethod(IMethod):
    @staticmethod
    def p() -> int:
        return 2

    @staticmethod
    def calc_quadrature(v: Type[IVariant], step: Decimal) -> Decimal:
        result = Decimal("0")
        n = int((v.b() - v.a()) / step)

        for i in range(1, n):
            x_i = v.a() + i * step
            result += v.f(x_i)

        return (result + ((v.f(v.a()) + v.f(v.b())) / 2)) * step


class SimpsonKotMethod(IMethod):
    @staticmethod
    def p() -> int:
        return 4

    @staticmethod
    def calc_quadrature(v: Type[IVariant], step: Decimal) -> Decimal:
        result = Decimal("0")
        n = int((v.b() - v.a()) / step)

        # Реализация тупо в лоб, оптимизировать мне влом
        for i in range(0, n):
            x_i = v.a() + i * step
            x_i_next = v.a() + (i + 1) * step
            result += v.f(x_i) + 4 * v.f((x_i + x_i_next) / 2) + v.f(x_i_next)

        return result * (step / 6)


class ThreeByEightMethod(IMethod):
    @staticmethod
    def p() -> int:
        return 4

    @staticmethod
    def calc_quadrature(v: Type[IVariant], step: Decimal) -> Decimal:
        result = Decimal("0")
        n = int((v.b() - v.a()) / step)

        # Реализация тупо в лоб, оптимизировать мне влом
        for i in range(0, n):
            x_i = v.a() + i * step
            x_i_next = v.a() + (i + 1) * step
            result += (
                v.f(x_i)
                + 3 * v.f((2 * x_i + x_i_next) / 3)
                + 3 * v.f((x_i + 2 * x_i_next) / 3)
                + v.f(x_i_next)
            )

        return result * (step / 8)
