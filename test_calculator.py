import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_substraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_substraction2(self):
        assert 100 == calculator.subtract(200, 100)
