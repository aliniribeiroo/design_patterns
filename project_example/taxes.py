

"""
Diferença entre método e função:
Método pertence a uma classe, função não.
"""
from project_example.budget import Budget


class ISS:
    def calculate(self, budget: Budget):
        return budget.value * 0.1


class ICMS:
    def calculate(self, budget: Budget):
        return budget.value * 0.5
