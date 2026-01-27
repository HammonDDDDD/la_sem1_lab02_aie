from abc import ABC, abstractmethod
from type import DenseMatrix, Shape


class Matrix(ABC):
    def __init__(self, shape: Shape):
        self.shape = shape

    @abstractmethod
    def to_dense(self) -> DenseMatrix:
        """Преобразует разреженную матрицу в плотную."""
        pass

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Сложение матриц."""
        if self.shape != other.shape:
            raise ValueError("Размерности матриц не совпадают")
        return self._add_impl(other)

    @abstractmethod
    def _add_impl(self, other: 'Matrix') -> 'Matrix':
        """Реализация сложения с другой матрицей."""
        pass

    def __mul__(self, scalar: float) -> 'Matrix':
        """Умножение на скаляр."""
        return self._mul_impl(scalar)

    @abstractmethod
    def _mul_impl(self, scalar: float) -> 'Matrix':
        """Реализация умножения на скаляр."""
        pass

    def __rmul__(self, scalar: float) -> 'Matrix':
        """Обратное умножение на скаляр."""
        return self.__mul__(scalar)

    @abstractmethod
    def transpose(self) -> 'Matrix':
        """Транспонирование матрицы."""
        pass

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        """Умножение матриц."""
        if self.shape[1] != other.shape[0]:
            raise ValueError("Несовместимые размерности для умножения")
        return self._matmul_impl(other)

    @abstractmethod
    def _matmul_impl(self, other: 'Matrix') -> 'Matrix':
        """Реализация умножения матриц."""
        pass

