# POII - Trabalho02: Programação Não Linear Multivariável Irrestrito
Desenvolvimento dos métodos para determinação de ponto mínimo de problemas não lineares, multivariáveis e irrestrito. As rotinas desenvolvidas são: Hooke & Jeeves, Newton, Gradiente, Fletcher & Reeves e Davidon-Fletcher-Powell.


### Como abrir o executável do projeto: ###
dist > po2_trabalho2 > po2_trabalho2.exe

### Como abrir o fonte do projeto: ###
po2_trabalho2.py

#### Grupo: ####
Giulia Rossatto Rocha

Larissa de Castro Bonadio

Larissa Mayumi Barela Hondo

#### Informações: ####
Trabalho realizado em Python 3.

O trabalho apresenta o desenvolvimento de um programa que determina o ponto de mínimo de uma função sem restrições, sendo resolvida por um dos métodos abaixo:
    
    1. Hooke & Jeeves
    
    2. Newton 
    
    3. Gradiente 
    
    4. Fletcher & Reeves 
    
    5. Davidon-Fletcher-Powell
    
 O usuário poderá escolher entre os métodos acima, e a partir da sua escolha inserir as informações de entrada necessárias para obter a solução, juntamente com a quantidade de iterações feita pelo método.

Neste trabalho foi utilizado o avaliador de expressão matemática py_expression_eval, na linguagem de programação Python. Abaixo serão descrito alguns aspectos e restrições para o uso adequado do avaliador.

Operadores:

    + : Soma

    - : Subtração

    * : Multiplicação

    / : Divisão

    ^ : Potência
    
    % : Divisão inteira

    sqrt(x): Raiz Quadrada

Constantes:

    E = 2.718281828459045 (Constante de Euler)

    PI = 3,141592653589793 (PI) 

Funções Trigonométricas:

    sin(x)	: Seno

    cos(x)	: Cosseno

    tan(x)	: Tangente

    asin(x) : Arco seno

    acos(x) : Arco cosseno 

    atan(x) : Arco tangente


Outras Funções:

    log(x)	: Logaritmo com base 10

    log(x, base) : Logaritmo com base da escolha do usuário

    abs(x)	: Valor absoluto

    ceil(x) : Teto de x (o menor inteiro que é >= x)

    floor(x) : Piso de x (o maior inteiro que é <= x)

    round(x) : Arredondado para o número inteiro mais próximo

    exp(x) : Exponencial


Segue alguns exemplos de como utilizar o programa:

    Valor decimal (utiliza-se .): 0.5

    Escrita da função: 
                    
                     x^2-3*x+2

                     E^x+2

                     x*sin(PI*x)

                     sqrt(16)

                     log(2.7)

                     log(E)
                     
                     (x1-2)+5*(x2-5)^2
                     
                     x1*x2*x3

### OBSERVAÇÕES IMPORTANTES: ###

Para multiplicação é OBRIGATÓRIO o uso do multiplicador *:

    ERRADO: 2x

    CERTO: 2*x
    
    
    ERRADO: 5(x1-x2) + x1x2
    
    CERTO: 5*(x1-x2) + x1*x2

    
Para utilizações das funções acima, é necessário utilizar a mesma escrita para o interpretador reconhecer:

    ERRADO: seno(x), sen(x)

    CERTO: sin(x)


NÃO UTILIZAR VÍRGULA PARA REPRESENTAR DECIMAIS

    ERRADO: 0,01
    
    CERTO: 0.01

NÃO UTILIZAR BASE 10 PARA INSERIR VALORES DE EPSILON (ε):

    ERRADO: 10^(-2)
    
    CERTO: 0.01
    
Ao inserir o ponto inicial para as funções, utilizar parênteses e vírgula entre os valores. Por exemplo, para x¹ = (1.2    1.2):

    ERRADO: 1.2,1.2
    
    ERRADO: 1.2 1.2
    
    ERRADO: (1.2 1.2)
    
    CERTO: (1.2,1.2)
    
    CERTO: (1.2 , 1.2)
    
    CERTO: (1.2, 1.2)


EXEMPLO PARA MÉTODO DE NEWTON:

![Fotos 10_08_2021 17_35_12](https://user-images.githubusercontent.com/85367213/128931688-04aa6b8a-724d-4ebe-bb9a-1293a1312ee0.png)


O exemplo acima deve ser inserido como na imagem abaixo: 

![Newton 10_08_2021 17_36_12](https://user-images.githubusercontent.com/85367213/128931716-e3ddd16f-ba13-43f5-a09b-d329617ab969.png)

