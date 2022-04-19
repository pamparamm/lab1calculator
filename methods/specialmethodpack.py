from decimal import Decimal
from typing import Type

from variants.basevariant import IVariant


class GaussMethod:
    @staticmethod
    def p1() -> int:
        return 1

    @staticmethod
    def p2() -> int:
        return 3

    @staticmethod
    def p4() -> int:
        return 7

    @staticmethod
    def calc_gauss1(v: Type[IVariant]) -> Decimal:
        point1 = Decimal("0")
        coef1 = 2
        return coef1 * v.f_transformed(point1)

    @staticmethod
    def calc_gauss2(v: Type[IVariant]) -> Decimal:
        point1 = -1 / (Decimal("3").sqrt())
        point2 = -point1
        coef1 = 1
        coef2 = 1
        return coef1 * v.f_transformed(point1) + coef2 * v.f_transformed(
            point2
        )

    @staticmethod
    def calc_gauss4(v: Type[IVariant]) -> Decimal:
        point1 = -(
            Decimal("3") / 7 - ((Decimal("2") / 7) * (Decimal("6") / 5).sqrt())
        ).sqrt()
        point2 = -point1
        point3 = -(
            Decimal("3") / 7 + ((Decimal("2") / 7) * (Decimal("6") / 5).sqrt())
        ).sqrt()
        point4 = -point3
        coef1 = (18 + Decimal("30").sqrt()) / 36
        coef2 = coef1
        coef3 = (18 - Decimal("30").sqrt()) / 36
        coef4 = coef3

        return (
            coef1 * v.f_transformed(point1)
            + coef2 * v.f_transformed(point2)
            + coef3 * v.f_transformed(point3)
            + coef4 * v.f_transformed(point4)
        )
