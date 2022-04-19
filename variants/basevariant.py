from abc import ABCMeta, abstractmethod
from decimal import Decimal


class IVariant:
    """Вариант лабы по числакам

    Raises:
        NotImplementedError: не забудь переопределить методы
    """

    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def f(x: Decimal) -> Decimal:
        """Подынтегральная функция

        Args:
            x (Decimal): значение переменной x
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def f_transformed(t: Decimal) -> Decimal:
        """Преобразованная функция для формулы Гаусса

        Args:
            t (Decimal): значение переменной t
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def f_derivative(x: Decimal) -> Decimal:
        """Преобразованная функция для формулы Гаусса

        Args:
            t (Decimal): значение переменной t
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def a() -> Decimal:
        """Левая граница интегрирования"""
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def b() -> Decimal:
        """Правая граница интегрирования"""
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def etalon() -> Decimal:
        """Эталонное значение

        Считай его на WolframAlpha
        """
        raise NotImplementedError
