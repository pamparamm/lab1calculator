from decimal import Decimal
from typing import Type
from methods.basemethod import IMethod
from variants.basevariant import IVariant


class EilerMethod(IMethod):
    @staticmethod
    def p() -> int:
        return 4

    @staticmethod
    def calc_quadrature(v: Type[IVariant], step: Decimal) -> Decimal:
        result = step / 2 * (v.f(v.a()) + v.f(v.b()))
        n = int((v.b() - v.a()) / step)

        inter_result = Decimal(0)
        for i in range(1, n):
            inter_result += 2 * v.f(v.a() + step * i)

        result += inter_result * step / 2
        result += (v.f_derivative(v.a()) -
                   v.f_derivative(v.b())) * step**2 / 12
        return result


class MethodGriga(IMethod):
    @staticmethod
    def p() -> int:
        return 4

    @staticmethod
    def calc_quadrature(v: Type[IVariant], step: Decimal) -> Decimal:
        result = step / 2 * (v.f(v.a()) + v.f(v.b()))
        n = int((v.b() - v.a()) / step)

        inter_result = Decimal(0)
        for i in range(1, n):
            inter_result += 2 * v.f(v.a() + step * i)

        result += inter_result * step / 2
        result += step / 24 * (-3 * v.f(v.a()) + 4 * v.f(v.a() + step) - v.f(
            v.a() + step * 2) - v.f(v.b() - step * 2) + 4 * v.f(v.b() - step) - 3 * v.f(v.b()))
        return result
