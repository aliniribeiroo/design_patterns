from project_example.taxes import ISS, ICMS
from project_example.budget import Budget

"""
Strategy

O método strategy nesta implementação é usado para que não 
precisamos realizar nenhum if dentro da nossa classe.

Criamos a estratégia e a passamos por parametro, para que
a função consiga executar o que precisa.

Duck-typing: Não importa qual isntancia é recebida, o que importa é que
tenha os mesmos métodos.

O padrão Strategy é muito útil quando temos um conjunto de algoritmos similares,
e precisamos alternar entre eles em diferentes pedaços da aplicação.

O Strategy nos oferece uma maneira flexível para escrever diversos algoritmos
diferentes, e de passar esses algoritmos para classes clientes que precisam deles.
Esses clientes desconhecem qual é o algoritmo "real" que está sendo executado,
e apenas manda o algoritmo rodar. Isso faz com que o código da classe cliente fique
bastante desacoplado das implementações dos algoritmos, possibilitando\
assim com que esse cliente consiga trabalhar com N diferentes algoritmos
sem precisar alterar o seu código.

"""
class TaxCalculator(object):

    def make_calculation(self, budget, taxes):
        return taxes.calculate(budget)


if __name__ == '__main__':
    calculator = TaxCalculator()
    budget = Budget(500)
    a = calculator.make_calculation(budget, ISS())
    b = calculator.make_calculation(budget, ICMS())

    print(a)
    print(b)
