# tests/test_calculadora.py
import pytest

from calculadora import calcular


def test_somar():
    assert calcular(2, 3, "somar") == 5


def test_subtrair():
    assert calcular(10, 4, "subtrair") == 6


def test_multiplicar():
    assert calcular(6, 7, "multiplicar") == 42


def test_dividir():
    assert calcular(20, 5, "dividir") == 4


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        calcular(1, 0, "dividir")


def test_operacao_invalida():
    with pytest.raises(ValueError):
        calcular(1, 2, "potencia")
