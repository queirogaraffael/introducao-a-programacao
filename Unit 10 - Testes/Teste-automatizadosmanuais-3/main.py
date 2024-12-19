import math

class Bhaskara:

    def delta(self, a, b, c):
        return b ** 2 - 4 * a * c

    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)
        if d == 0:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            return 1, raiz1 # indica que tem uma raiz e o valor dela
        else:
            if d < 0:
                return 0
            else:
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                raiz2 = (-b - math.sqrt(d)) / (2 * a)
                return 2, raiz1, raiz2

#import Bhaskara
#import pytest

#class TestBhaskara:
    
    #refatoração
#    @pytest.fixture
 #   def b(self):
  #      return Bhaskara.Bhaskara()

    #def testa_uma_raiz(self, b):
#        assert b.calcula_raizes(1, 0, 0) == (1,0)

#    def testa_duas_raiz(self, b):
#        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)

#    def testa_tres_raiz(self, b):
#        assert b.calcula_raizes(10, 10, 10) == 0

#    def testa_raiz_negativa(self, b):
#        assert b.calcula_raizes(10, 20, 10) == (1, -1)
