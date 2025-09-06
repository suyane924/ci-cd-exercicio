from app import soma, multiplica


def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0


def test_multiplica_positivos():
    assert multiplica(2, 3) == 6


def test_multiplica_negativos():
    assert multiplica(-2, -3) == 6


def test_multiplica_positivo_negativo():
    assert multiplica(-2, 3) == -6


def test_multiplica_por_zero():
    assert multiplica(0, 5) == 0
    assert multiplica(5, 0) == 0