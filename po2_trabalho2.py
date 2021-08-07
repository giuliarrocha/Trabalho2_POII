from tkinter.constants import TRUE
import PySimpleGUI as sg
from sympy.functions.combinatorial.numbers import nP
from sympy.polys.polyoptions import Symbols
from py_expression_eval import Parser
from sympy import *
import numpy as np
import math
from decimal import Decimal
from sympy.solvers import solve

from sympy.solvers.diophantine.diophantine import length, norm

sg.theme('LightBrown13')
parser = Parser()

## Janelas
def window_hookeJeeves():
    layout = [[sg.Text('HOOKE & JEEVES', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(35,1))],
            [sg.Text('Exemplo: x¹ = (0, 0) para R² o ponto inicial',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('x¹:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='ponto_inicial', size=(25,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaHooke1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaHooke2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaHooke3', text_color = 'black')]
            ]
    return sg.Window('Hooke & Jeeves', layout, size=(400, 400), finalize=True, resizable=True)

def window_gradiente():
    layout = [[sg.Text('GRADIENTE', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(35,1))],
            [sg.Text('Exemplo: x¹ = (0, 0) para R² o ponto inicial',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('x¹:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='ponto_inicial', size=(25,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaGradiente1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaGradiente2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaGradiente3', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaGradiente4', text_color = 'black')]
            ]
    return sg.Window('Gradiente', layout, size=(400, 400), finalize=True, resizable=True)

def window_fletcherReeves():
    layout = [[sg.Text('FLETCHER & REEVES', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(35,1))],
            [sg.Text('Exemplo: x¹ = (0, 0) para R² o ponto inicial',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('x¹:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='ponto_inicial', size=(25,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaFletcher1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaFletcher2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaFletcher3', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaFletcher4', text_color = 'black')]
            ]
    return sg.Window('Fletcher & Reeves', layout, size=(400, 400), finalize=True, resizable=True)

def window_davidonFletcherPowell():
    layout = [[sg.Text('DAVIDON-FLETCHER-POWELL', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(35,1))],
            [sg.Text('Exemplo: x¹ = (0, 0) para R² o ponto inicial',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('x¹:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='ponto_inicial', size=(25,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaDavidon1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaDavidon2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaDavidon3', text_color = 'black')]
            ]
    return sg.Window('Davidon-Fletcher-Powell', layout, size=(400, 400), finalize=True, resizable=True)

def window_newton():
    layout = [[sg.Text('NEWTON', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(35,1))],
            [sg.Text('Exemplo: x¹ = (0, 0) para R² o ponto inicial',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('x¹:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='ponto_inicial', size=(25,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaNewton1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaNewton2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaNewton3', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaNewton4', text_color = 'black')]
            ]
    return sg.Window('Newton', layout, size=(400, 400), finalize=True, resizable=True)

# Janela Inicial Principal
def main_window():
    layout = [[sg.Text(' ', size = (10, 1))],
            [sg.Text('Selecione a rotina que deseja utilizar:', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text(' ', size = (4, 1))],
            [sg.Button('Hooke & Jeeves', size=(20,1))],
            [sg.Button('Newton', size=(20,1))],
            [sg.Button('Gradiente', size=(20,1))],
            [sg.Button('Fletcher & Reeves', size=(20,1))],
            [sg.Button('Davidon-Fletcher-Powell', size=(20,1))],
            [sg.Text(' ', size = (4, 1))],
            [sg.Button('Sair')]]
    return sg.Window('PO II - Trabalho 2', layout, size=(400, 400), element_justification='center', finalize=True, resizable=True)


### Funções ###

#função que retorna uma lista com as variáveis, o número de variáveis, o número de pontos iniciais e os pontos
def determinaVariaveisPontos(funcao, ponto_inicial):
    variaveis = []
    pontos_string = []
    pontos = []
    variaveis = parser.parse(funcao).variables() #Pega a função e retorna em uma lista as variaveis
    num_variaveis = len(variaveis) #Retorna o numero de variaveis
    ponto_inicial = ponto_inicial.replace('(', '') #removendo ) e ( da string de pontos
    ponto_inicial = ponto_inicial.replace(')', '')   
    pontos_string = ponto_inicial.split(",") #separando os numeros pela virgula (,)
    num_pontos = len(pontos_string) #conta o numero de pontos que foi colocado
    pontos = [float(i) for i in pontos_string] #tranforma a lista de string em float

    return (variaveis, num_variaveis, pontos, num_pontos)

# def HookeJeeves ():

# Rotina - Fletcher & Reeves
def FletcherReeves(funcao, ponto_inicial, epsilon):
    epsilon = float(epsilon)
    var_pontos = determinaVariaveisPontos(funcao, ponto_inicial)
    variaveis = var_pontos[0]
    num_variaveis = var_pontos[1]
    pontos = var_pontos[2]
    num_pontos = var_pontos[3]
    k = 0
    if (num_variaveis!=num_pontos):
        sg.popup_ok('Número de pontos de entrada não condiz com a quantidade de variáveis da função!')
        return

    entrada = {}
    for i in range(0,num_variaveis):
        entrada[variaveis[i]] = pontos[i]
    
    #Declarando matrizes
    x = [[0 for j in range(1) ] for i in range(num_variaveis)]
    gradiente = [[0 for j in range(1) ] for i in range(num_variaveis)]
    g_atual = [[0 for j in range(1) ] for i in range(num_variaveis)]
    g_atual = np.array(g_atual, float)
    g_prox = [[0 for j in range(1) ] for i in range(num_variaveis)]
    g_prox = np.array(g_prox, float)
    d = [[0 for j in range(1) ] for i in range(num_variaveis)]
    d_prox = [[0 for j in range(1) ] for i in range(num_variaveis)]
    min_f = [[0 for j in range(1) ] for i in range(num_variaveis)]
    novo_x = [[0 for j in range(1) ] for i in range(num_variaveis)]
    norma_grad = 0.0
    
    # Calculo do gradiente
    for i in range(0,num_variaveis):
        derivada = str(diff(funcao, variaveis[i]))
        gradiente[i][0] = derivada
    
    # Deixa matriz X como coluna
    x = np.reshape(pontos, (num_variaveis, 1))

    # Calcular o gradiente atual e a norma
    for i in range(0,num_variaveis):
        entrada[variaveis[i]] = x[i][0]

    for i in range(0,num_variaveis):
        resultado = np.longfloat(parser.parse(gradiente[i][0]).evaluate(entrada))
        g_atual[i][0] = resultado
        norma_grad += resultado**2
    norma_grad = math.sqrt(norma_grad)

    while(float(norma_grad) >= float(epsilon)):
        l = 0.0
        norma_grad = 0.0
        # Calcula direção
        for i in range(0,num_variaveis):
            d[i][0] = float(- g_atual[i][0])
        for k in range(0, num_variaveis):
            # Faz o formato da função de min f(x+lambda*d)
            for i in range(0,num_variaveis):
                min_f[i][0] = '(' + str(x[i][0]) + '+' + str(d[i][0]) + '*x' + ')'
            # Substituir na função os valores da função min f
            nova_funcao = str(funcao)
            for i in range(0,num_variaveis):
                nova_funcao = nova_funcao.replace(str(variaveis[i]), str(min_f[i][0]))
            # Determina o valor de lambda
            l = float(MetodoNewton(nova_funcao, x[0][0]))   
            print('lambda: ', l)           
            # Substituir x pelo valor de lambda e coloca o resultado na matriz novo_x
            for i in range(0,num_variaveis):
                novo_x[i][0] = min_f[i][0]
                novo_x[i][0] = min_f[i][0].replace('x', str(l))
                resultado = np.longfloat(parser.parse(novo_x[i][0]).evaluate(entrada))
                novo_x[i][0] = float(resultado)
            # Calcular o gradiente próximo
            for i in range(0,num_variaveis):
                entrada[variaveis[i]] = novo_x[i][0]
            for i in range(0,num_variaveis):
                resultado = np.longfloat(parser.parse(str(gradiente[i][0])).evaluate(entrada))
                g_prox[i][0] = resultado  
            if k < (num_variaveis - 1):
                g_atualTransposta = np.transpose(g_atual) 
                g_proxTransposta = np.transpose(g_prox)
                b = float(float(g_proxTransposta.dot(g_prox)) / float(g_atualTransposta.dot(g_atual)))
                # Calcula a nova direção
                for i in range(0,num_variaveis):
                    d[i][0] = float( - g_prox[i][0] + b*d[i][0])
            # Coloca os valores do novo_x na matrix x
            for i in range(0,num_variaveis):
                entrada[variaveis[i]] = novo_x[i][0]
                x[i][0] = novo_x[i][0]
        for i in range(0,num_variaveis):
            entrada[variaveis[i]] = x[i][0]
        for i in range(0,num_variaveis):
            resultado = np.longfloat(parser.parse(gradiente[i][0]).evaluate(entrada))
            g_atual[i][0] = resultado
            norma_grad += math.pow(resultado, 2)
        norma_grad = math.sqrt(norma_grad)

    print('x: ', x)
    # (x1-2)^4+(x1-2*x2)^2
    # x1^3-x1^2+2*x2^2-2*x2
    # x1^3-2*x1*x2+x2^2

# def DavidonFletcherPowell():
def DecomposicaoLU (A, X, B, ordem):
    L = [[0 for j in range(ordem) ] for i in range(ordem)]
    U = [[0 for j in range(ordem) ] for i in range(ordem)]
    Y = [[0 for j in range(1) ] for i in range(ordem)]
    for i in range (0, ordem):
        #linhas de U
        for j in range (i, ordem):
            soma = 0
            for k in range (0, i):
                soma += L[i][k]*U[k][j]
            U[i][j] = A[i][j] - soma
        #Colunas de L
        for j in range (i, ordem):
            soma = 0
            for k in range (0, i):
                soma += L[j][k]*U[k][i]
            L[j][i] = (A[j][i]-soma)/U[i][i]
    
    #resolvendo sistema triangular inferior
    Y[0][0] = B[0][0]/L[0][0]
    for i in range (1, ordem):
        Y[i][0] = B[i][0]
        for j in range (0, i):
            Y[i][0] -= L[i][j]*Y[j][0]
        Y[i][0] /= L[i][i]
    
    #SistemaTriangularInferior(ordem,L,b,y);
    #resolvendo sistema triangular superior
    X[ordem-1][0] = Y[ordem-1][0]/U[ordem-1][ordem-1]
    for i in range (ordem-2, -1, -1):
        X[i][0] = Y[i][0]
        for j in range (i+1, ordem):
            X[i][0] -= U[i][j]*X[j][0]
        X[i][0] /= U[i][i]
	#SistemaTriangularSuperior(ordem,U,y,x);

# Rotina - Newton
def Newton(funcao, ponto_inicial, epsilon):
    epsilon = float(epsilon)
    var_pontos = determinaVariaveisPontos(funcao, ponto_inicial)
    variaveis = var_pontos[0]
    num_variaveis = var_pontos[1]
    pontos = var_pontos[2]
    num_pontos = var_pontos[3]
    if (num_variaveis!=num_pontos):
        sg.popup_ok('Número de pontos de entrada não condiz com a quantidade de variáveis da função!')
        return

    entrada = {}
    for i in range(0,num_variaveis):
        entrada[variaveis[i]] = pontos[i]

    k=-1
    continua = true
    #Declarando matrizes
    w = [[0 for j in range(1) ] for i in range(num_variaveis)]
    x = [[0 for j in range(1) ] for i in range(num_variaveis)]
    gradiente = [[0 for j in range(1) ] for i in range(num_variaveis)]
    gradienteX = [[0 for j in range(1) ] for i in range(num_variaveis)]
    gradienteX = np.array(gradienteX, float)
    hessiana = [[0 for j in range(num_variaveis) ] for i in range(num_variaveis)]
    hessianaX = [[0 for j in range(num_variaveis) ] for i in range(num_variaveis)]
    hessianaX = np.array(hessianaX, float)
    
    #calculo gradiente
    for i in range(0,num_variaveis):
        derivada = str(diff(funcao, variaveis[i]))
        gradiente[i][0] = derivada
    
    #calculo hessiana
    for i in range(0,num_variaveis):
        for j in range(0,num_variaveis):
            derivada = str(diff(gradiente[i][0], variaveis[j]))
            hessiana[i][j] = derivada
    
    x = np.reshape(pontos, (num_variaveis, 1))

    while (continua):
        norma_grad = 0
        norma_x = 0

        #calcula gradiente(x)
        for i in range(0,num_variaveis):
            entrada[variaveis[i]] = x[i][0]

        for i in range(0,num_variaveis):
            resultado = np.longfloat(parser.parse(gradiente[i][0]).evaluate(entrada))
            gradienteX[i][0] = resultado
            norma_grad += resultado**2

        norma_grad = math.sqrt(norma_grad)
        if (norma_grad>=epsilon):
            k+=1
            #calcula hessiana(x)
            for i in range(0,num_variaveis):
                for j in range(0,num_variaveis):
                    resultado = float(parser.parse(hessiana[i][j]).evaluate(entrada))
                    hessianaX[i][j] = resultado
            #resolvendo sistema por decomposicao LU
            DecomposicaoLU(hessianaX, w, ((-1)*gradienteX), num_variaveis)
            x_anterior = x
            x = w + x_anterior
            for i in range (0, num_variaveis):
                norma_x += ((x[i][0]-x_anterior[i][0])**2)
            norma_x = math.sqrt(norma_x)
            if (norma_x<epsilon):
                continua = false
        else:
            continua=false
    
    for i in range(0,num_variaveis):
            entrada[variaveis[i]] = x[i][0]
    y = float(parser.parse(funcao).evaluate(entrada))
    return (k, x, y, num_variaveis)

    #Alguns testes:
    #(x1-2)^4+(x1-2*x2)^2 com (0,3) e e=0.1
    #(x1+3)^2+(x2-1)^3 com (0,2) e e=0.01 ==> x = (-3, 1,0313)

# Rotina - Gradiente
def Gradiente (funcao, ponto_inicial, epsilon):
    var_pontos = determinaVariaveisPontos(funcao, ponto_inicial)
    variaveis = var_pontos[0]
    num_variaveis = var_pontos[1]
    pontos = var_pontos[2]
    num_pontos = var_pontos[3]
    norma_grad = 0.0
    k = 0

    if (num_variaveis!=num_pontos):
        sg.popup_ok('Número de pontos de entrada não condiz com a quantidade de variáveis da função!')
        return

    entrada = {}
    for i in range(0,num_variaveis):
        entrada[variaveis[i]] = pontos[i]

    #Declarando matrizes
    x = [[0 for j in range(1) ] for i in range(num_variaveis)]
    gradiente = [[0 for j in range(1) ] for i in range(num_variaveis)]
    gradienteF = [[0 for j in range(1) ] for i in range(num_variaveis)]
    gradienteF = np.array(gradienteF, float)
    d = [[0 for j in range(1) ] for i in range(num_variaveis)]
    min_f = [[0 for j in range(1) ] for i in range(num_variaveis)]
    novo_x = [[0 for j in range(1) ] for i in range(num_variaveis)]

    # Calculo do gradiente
    for i in range(0,num_variaveis):
        derivada = str(diff(funcao, variaveis[i]))
        gradiente[i][0] = derivada

    # Deixa matriz X como coluna
    x = np.reshape(pontos, (num_variaveis, 1))
 
    if float(epsilon) > 0.0:
        k = 1
    # fazer um else caso não precise entrar no algoritmo

    
    # Calcular o gradiente de F
    for i in range(0,num_variaveis):
        entrada[variaveis[i]] = x[i][0]

    for i in range(0,num_variaveis):
        resultado = np.longfloat(parser.parse(gradiente[i][0]).evaluate(entrada))
        gradienteF[i][0] = resultado
        norma_grad += resultado**2
    norma_grad = math.sqrt(norma_grad)


    while(float(norma_grad) > float(epsilon)):
        # zera a variavel da norma
        norma_grad = 0.0

        # Calcula direção
        for i in range(0,num_variaveis):
            d[i][0] = - gradienteF[i][0]

        # Calcula a função de min f(x+lambda*d)
        for i in range(0,num_variaveis):
            min_f[i][0] = '(' + str(x[i][0]) + '+' + str(d[i][0]) + '*x' + ')'

        # Substituir na função os valores da função min f
        nova_funcao = funcao
        for i in range(0,num_variaveis):
            nova_funcao = nova_funcao.replace(str(variaveis[i]), str(min_f[i][0]))
     
        # Determina o valor de lambda
        l = float(MetodoNewton(nova_funcao, x[0][0]))
        
        # Substituir x pelo valor de lambda
        for i in range(0,num_variaveis):
            novo_x[i][0] = min_f[i][0]
            novo_x[i][0] = min_f[i][0].replace('x', str(l))
            resultado = np.longfloat(parser.parse(novo_x[i][0]).evaluate(entrada))
            novo_x[i][0] = float(resultado)
        
        # Calcular o gradiente de F e coloca o novo x na matrix x
        for i in range(0,num_variaveis):
            entrada[variaveis[i]] = novo_x[i][0]
            x[i][0] = novo_x[i][0]

        # Calcula a norma para a condição do while
        for i in range(0,num_variaveis):
            resultado = np.longfloat(parser.parse(gradiente[i][0]).evaluate(entrada))
            gradienteF[i][0] = resultado
            norma_grad += resultado**2
        norma_grad = math.sqrt(norma_grad)
        
        # incrementa o número de iterações
        k = k + 1    

    #Determina valor de f(x)
    for i in range(0,num_variaveis):
            entrada[variaveis[i]] = x[i][0]
    y = float(parser.parse(funcao).evaluate(entrada))
    return (k, x, y, num_variaveis)

    # (x1-2)^4+(x1-2*x2)^2 0,3 0.1 ==> (2.2680, 1.1433) k = 10
    # x1^2-2*x1*x2+4*x2^2 1, 0.25 0.1 ==> (0.0625, 0.015625) k = 5
    # 2*x1^2+(x2-1)^2  0, 0 0.1 ==> (0, 1) k = 2
    # 4*x1^2+2*x1*x2+2*x2^2+x1+x2  1,1  0.01 ==> (-0.0716, -0,2139) k = 6

#Função para busca na reta (Newton):
def MetodoNewton(funcao, a):
    x = a
    deriv1 = str(diff(funcao))
    d1 = float(parser.parse(deriv1).evaluate({'x' : x}))    
    k = []
    k.append(x)
    l = 0
    
    while abs(float(d1)) >= 0.00001:
        deriv2 = str(diff(deriv1))
        d2 = float(parser.parse(deriv2).evaluate({'x' : x}))
        if d2 != 0.0:
            x = float(k[len(k)-1] - (d1 / d2))
            k.append(x)

            if(float((abs(k[len(k)-1] - k[len(k)-2]) / max(1, abs(k[len(k)-2])))) < 0.00001):         
                break
            else:
                d1 = float(parser.parse(deriv1).evaluate({'x' : x}))
        else:
            break
        
        l = l + 1
    return (k[len(k)-1])

window1, window2, window3, window4, window5, window6, window7 = main_window(), None, None, None, None, None, None
parser = Parser()

while True:
    window, event, valores = sg.read_all_windows()
    if event == 'Sair'or event == sg.WIN_CLOSED:
        window.close()

    if window== window1 and event == 'Hooke & Jeeves':
        window2 = window_hookeJeeves()
        window2.move(window1.current_location()[0] + 50, window1.current_location()[1] + 50)

    if window== window1 and event == 'Newton':
        window3 = window_newton()
        window3.move(window1.current_location()[0] + 50, window1.current_location()[1] + 50)

    if window== window1 and event == 'Gradiente':
        window4 = window_gradiente()
        window4.move(window1.current_location()[0] + 50, window1.current_location()[1] + 50)

    if window== window1 and event == 'Fletcher & Reeves':
        window5 = window_fletcherReeves()
        window5.move(window1.current_location()[0] + 50, window1.current_location()[1] + 50)

    if window== window1 and event == 'Davidon-Fletcher-Powell':
        window6 = window_davidonFletcherPowell()
        window6.move(window1.current_location()[0] + 50, window1.current_location()[1] + 50)

    if window == window2 and event == 'Calcular':
       print ("Hooke & Jeeves"); 
    
    if window == window3 and event == 'Calcular': 
        funcao = str(parser.parse(valores['expressao']))
        resultado = Newton(funcao, valores['ponto_inicial'], valores['epsilon'])
        window3['respostaNewton1'].update('RESULTADO: ')
        window3['respostaNewton2'].update('Com K variando de 0 a %d' % resultado[0])
        saida = '('
        for i in range (0, resultado[3]):
            #(x1+3)^2+(x2-1)^3
            valor = "{:.4f}".format(float(resultado[1][i]))
            saida += str(valor)
            if (i!=resultado[3]-1):
                saida += ', '
        saida += ')^t'
        window3['respostaNewton3'].update('x* = ' + saida)
        window3['respostaNewton4'].update('f(x*) = %.4f' % resultado[2])

    if window == window4 and event == 'Calcular':
        funcao = str(parser.parse(valores['expressao']))
        resultado = Gradiente(funcao, valores['ponto_inicial'], valores['epsilon'])
        window4['respostaGradiente1'].update('RESULTADO: ')
        window4['respostaGradiente2'].update('Com K variando de 0 a %d' % resultado[0])
        saida = '('
        for i in range (0, resultado[3]):
            #(x1+3)^2+(x2-1)^3
            valor = "{:.4f}".format(float(resultado[1][i]))
            saida += str(valor)
            if (i!=resultado[3]-1):
                saida += ', '
        saida += ')^t'
        window4['respostaGradiente3'].update('x* = ' + saida)
        window4['respostaGradiente4'].update('f(x*) = %.4f' % resultado[2])
    if window == window5 and event == 'Calcular':
        funcao = str(parser.parse(valores['expressao']))
        FletcherReeves(funcao, valores['ponto_inicial'], valores['epsilon'])
        #window5['respostaFletcher1'].update('RESULTADO: ')
        #window5['respostaFletcher2'].update('Com K variando de 0 a %d' % resultado[0])
        #saida = '('
        #for i in range (0, resultado[3]):
            #(x1+3)^2+(x2-1)^3
        #    valor = "{:.4f}".format(float(resultado[1][i]))
        #    saida += str(valor)
        #    if (i!=resultado[3]-1):
        #        saida += ', '
        #saida += ')^t'
       # window5['respostaFletcher3'].update('x* = ' + saida)
        #window5['respostaFletcher4'].update('f(x*) = %.4f' % resultado[2])
    if window == window6 and event == 'Calcular':
        print ("Davidon-Fletcher-Powell"); 
