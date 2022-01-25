# Principais aspectos da programação orientada a objetos:

##### Encapsulamento
O encapsulamento oculta atributos e métodos de uma classe.
O comportamento do objeto fica oculto para o mundo externo, ouy os objetos mantêm suas informações de estado como privadas.
No python, não possuímos palavras reservadas, como em outras linguagens. Utilizamos o prefixo __ no nome da variável ou função.

##### Polimorfismo
O polimorfismo pode ser de dois tipos:
 - Um objeto oferecer diferentes impementações de um método, de acordo com o parâmetro de entrada
 - A mesma interface sendo utilizada por objetos diferentes.
 Em Python o polimorfismo já é embutido na linguagem, Ex: ao acessar o indice de uma string, tupla ou lista.\
 
##### Herança
A Herança indica que a classe deriva de uma classe-pai. É utilizada para reutilizar funcionalidades definidas na classe base.
Ela cria hierarquia por meio de relacionamentos entre objetos e classes diferentes.
 
##### Abstração
Abstrai a complexidade de classes internas com uma interface, onde o client não precisa conhecer as implementações internas. 

##### Composição
Combinação entre objetos. Ex: Dentro da classe Person eu chamo a classe x pra buscar algum dado.


Padrões de Projeto são separados em padrões de criação, 

## Padrões de criação:
- Singleton
- Factory

# Padrão de projeto Singleton 
Garante que a classse tenha apenas uma instância. 
Um grande exemplo de Singleton são as importações de módulos em Python:
 - Ele verifica se um módulo Pythin foi importado;
 - Em caso afirmativo, devolve o objeto para o módulo, Caso contratio, importa e instancia o módulo.
 - Quando o módulo for importado, ele será inicializado. Se o módulo for importado novamente, ele não será inicializado mais uma vez.
 
##### Vantagens:
- Evita o uso excessivo de recursos;
- É um método comprovado que resiste ao teste do tempo.
 
##### Desvantagens:
 - Pode ter um impacto inesperado, por trabalharem com variaveis globais, que podem ser alteradas por engano;
 - Pode gerar um alto acoplamento;
 - Várias referências podem ser utilizadas para o mesmo objeto.
 


# Padrão de projeto Factory
Em Programação orientada a objetos, o termo Factory, refere-se a uma classe responsável por criar objetos de outros tipos.

##### Vantagens:
- Baixo acoplamento
- O client não precisa conhecer a classe que cria o objeto, apenas a interface;
- Pode ser adicionada novas classes para serem criadas na Factory, sem o client alterar o código;
- A Factory pode reutilizar objetos existentes.

