import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_substraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_substraction2(self):
        assert 100 == calculator.subtract(200, 100)

    def test_multipy(self):
        assert 20000 == calculator.multiply(200, 100)

    def test_divide(self):
        assert 100 == calculator.divide(1000, 10)

    def test_mod(self):
        assert 1 == calculator.mod(4, 3)
