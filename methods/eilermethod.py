from decimal import Decimal
from typing import Type
from methods.basemethod import IMethod
from variants.basevariant import IVariant


class EilerMethod(IMethod):
    @staticmethod
    def p() -> int:
        return 2

    @staticmethod
    def calc_quadrature(v: Type[IVariant], step: Decimal) -> Decimal:
        """пук-пук-среньк"""
        return step**2
