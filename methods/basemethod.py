from abc import ABCMeta, abstractmethod
from decimal import Decimal
from typing import Type

from variants.basevariant import IVariant


class IMethod:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def p() -> int:
        """Алгебраическая точность метода"""
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def calc_quadrature(v: Type[IVariant], step: Decimal) -> Decimal:
        raise NotImplementedError

    @classmethod
    def cptn_wrungel(cls, variant: Type[IVariant], step: Decimal) -> Decimal:
        """Погрешность по Рунге

        Args:
            variant (Type[IVariant]): вариант лабы
            step (Decimal): шаг составной квадратурной формулы
        """
        return abs(
            cls.calc_quadrature(variant, step)
            - cls.calc_quadrature(variant, step * 2)
        ) / ((2 ** cls.p()) - 1)

    @classmethod
    def p_fact(cls, variant: Type[IVariant], step: Decimal) -> Decimal:
        """Фактическая алгебраическая точность метода

        Args:
            variant (Type[IVariant]): вариант лабы
            step (Decimal): шаг составной квадратурной формулы
        """
        return (
            cls.cptn_wrungel(variant, step)
            / cls.cptn_wrungel(variant, step / 2)
        ).ln() / Decimal("2").ln()
