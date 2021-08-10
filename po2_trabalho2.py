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
            [sg.Text(size=(40,1), key='respostaHookeJeeves1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaHookeJeeves2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaHookeJeeves3', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaHookeJeeves4', text_color = 'black')]
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
            [sg.Text(size=(40,1), key='respostaDavidon3', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaDavidon4', text_color = 'black')]
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

# Rotina - Hooke & Jeeves
def HookeJeeves(funcao, ponto_inicial, epsilon):
    epsilon = float(epsilon)
    var_pontos = determinaVariaveisPontos(funcao, ponto_inicial)
    variaveis = var_pontos[0]
    num_variaveis = var_pontos[1]
    pontos = var_pontos[2]
    num_pontos = var_pontos[3]
    
    entrada = {}
    for i in range(0,num_variaveis):
        entrada[variaveis[i]] = pontos[i]
        
    if (num_variaveis!=num_pontos):
        k = -1
        sg.popup_ok('Número de pontos de entrada não condiz com a quantidade de variáveis da função!')
        return (k, k, k, k)
    if (epsilon <= 0.0):
        k = -1
        sg.popup_ok('Epsilon inválido!')
        return (k, k, k, k)
    
    y = [[0 for j in range(1) ] for i in range(num_variaveis)]
    x = [[0 for j in range(1) ] for i in range(num_variaveis)]
    x_anterior = [[0 for j in range(1) ] for i in range(num_variaveis)]
    d = [[0 for j in range(1) ] for i in range(num_variaveis)]
    d = np.array(d, float)
    min_f = [[0 for j in range(1) ] for i in range(num_variaveis)]
    
    for i in range(0,num_variaveis):
        entrada[variaveis[i]] = x[i][0]

    # Deixa matriz y e x como coluna
    y = np.reshape(pontos, (num_variaveis, 1))
    x = np.reshape(pontos, (num_variaveis, 1))

    k = 1
    j = 0
    continua = True
    
    while(continua and k < 100):
        # Passo 1: Busca exploratória
        # Para j = 0 até j = num_variaveis-1
        for j in range(0,num_variaveis):
            nova_funcao = funcao
            for i in range(0,num_variaveis):
                # Atualiza direção
                d[i][0] = i==j
                min_f[i][0] = '(' + str(y[i][0]) + '+(' + str(d[i][0]) + ')*(x))'
                # Substituir na função os valores da função min f
                nova_funcao = nova_funcao.replace(str(variaveis[i]), str(min_f[i][0]))
            
            # Determina o valor de lambda ---> Aceita lambda negativo
            l = float(MetodoNewton(nova_funcao, x[0][0]))
            
            # Substituir y pelo valor de lambda e atualizar y
            for i in range(0,num_variaveis):
                nova_funcao = min_f[i][0].replace('x', str(l))
                resultado = np.longfloat(parser.parse(nova_funcao).evaluate(entrada))
                y[i][0] = float(resultado)
                entrada[variaveis[i]] = y[i][0]
            if(j == num_variaveis-1):
                soma = 0.0
                for i in range(0,num_variaveis):
                    x_anterior[i][0] = x[i][0]
                    x[i][0] = y[i][0]
                    soma += (x[i][0] - x_anterior[i][0])**2
                if(math.sqrt(soma) < epsilon):
                    continua = False
                else:
                    # Passo 2: Busca conjugada
                    nova_funcao = funcao
                    for i in range(0,num_variaveis):
                        # Atualiza direção
                        d[i][0] = x[i][0] - x_anterior[i][0]
                        
                        min_f[i][0] = '(' + str(x[i][0]) + '+(' + str(d[i][0]) + ')*(x))'
                    
                        # Substituir na função os valores da função min f
                        nova_funcao = nova_funcao.replace(str(variaveis[i]), str(min_f[i][0]))
                    # Determina o valor de lambda ---> Aceita lambda negativo
                    l = float(MetodoNewton(nova_funcao, x[0][0]))
                    # y^(j+1) = y^j + l_j * d^j
                    # Substituir y pelo valor de lambda e atualizar y
                    for i in range(0,num_variaveis):
                        nova_funcao = min_f[i][0].replace('x', str(l))
                        resultado = np.longfloat(parser.parse(nova_funcao).evaluate(entrada))
                        y[i][0] = float(resultado)
                        entrada[variaveis[i]] = y[i][0]
                    j = 0
                    k = k + 1

    for i in range(0,num_variaveis):
            entrada[variaveis[i]] = x[i][0]
    y = float(parser.parse(funcao).evaluate(entrada))
    
    return (k, x, y, num_variaveis)

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
        k = -1
        sg.popup_ok('Número de pontos de entrada não condiz com a quantidade de variáveis da função!')
        return (k, k, k, k)
    if (epsilon <= 0.0):
        k = -1
        sg.popup_ok('Epsilon inválido!')
        return (k, k, k, k)

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
    m = 1

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
            
            # Determina o valor de lambda ---> Se lambda negativo não pode continuar
            l = float(FiltraMetodoNewton(nova_funcao, x[0][0]))
            if(l < 0):
                sg.popup_ok('Não foi encontrado um lambda positivo! Insira um novo ponto inicial.')
                m = -1
                return (m, m, m, m)
            
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

        # Determina o gradiente e a norma para testar na condição de parada do while
        for i in range(0,num_variaveis):
            entrada[variaveis[i]] = x[i][0]
        for i in range(0,num_variaveis):
            resultado = np.longfloat(parser.parse(gradiente[i][0]).evaluate(entrada))
            g_atual[i][0] = resultado
            norma_grad += math.pow(resultado, 2)
        norma_grad = math.sqrt(norma_grad)
        m = m + 1

    #Determina valor de f(x)
    for i in range(0,num_variaveis):
            entrada[variaveis[i]] = x[i][0]
    y = float(parser.parse(funcao).evaluate(entrada))
    return (m, x, y, num_variaveis)

# Rotina - Davidon, Fletcher & Powell
def simetrica(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)
def definida_positiva(a):
    return np.all(np.linalg.eigvals(a) > 0)
def DavidonFletcherPowell(funcao, ponto_inicial, epsilon):
    epsilon = float(epsilon)
    var_pontos = determinaVariaveisPontos(funcao, ponto_inicial)
    variaveis = var_pontos[0]
    num_variaveis = var_pontos[1]
    pontos = var_pontos[2]
    num_pontos = var_pontos[3]
    
    if (num_variaveis!=num_pontos):
        k = -1
        sg.popup_ok('Número de pontos de entrada não condiz com a quantidade de variáveis da função!')
        return (k, k, k, k)
    if (epsilon <= 0.0):
        k = -1
        sg.popup_ok('Epsilon inválido!')
        return (k, k, k, k)

    entrada = {}
    for i in range(0,num_variaveis):
        entrada[variaveis[i]] = pontos[i]
    
    #Declarando matrizes
    x = [[0 for j in range(1) ] for i in range(num_variaveis)]
    gradiente = [[0 for j in range(1) ] for i in range(num_variaveis)]
    g = [[0 for j in range(1) ] for i in range(num_variaveis)]
    g = np.array(g, float)
    p = [[0 for j in range(1) ] for i in range(num_variaveis)]
    p = np.array(p, float)
    q = [[0 for j in range(1) ] for i in range(num_variaveis)]
    q = np.array(q, float)
    d = [[0 for j in range(1) ] for i in range(num_variaveis)]
    d = np.array(d, float)
    novo_g = [[0 for j in range(1) ] for i in range(num_variaveis)]
    novo_g = np.array(novo_g, float)
    min_f = [[0 for j in range(1) ] for i in range(num_variaveis)]
    norma_grad = 0.0
    
    i = 0
    k = 0
    # Calculo do gradiente
    for c in range(0,num_variaveis):
        derivada = str(diff(funcao, variaveis[c]))
        gradiente[c][0] = derivada
        
    # Deixa matriz X como coluna
    x = np.reshape(pontos, (num_variaveis, 1))

    for c in range(0,num_variaveis):
        entrada[variaveis[c]] = x[c][0]
            
    # Matriz simétrica definida positiva inicial
    s = [[0 for j in range(num_variaveis) ] for i in range(num_variaveis)]
    
    for c in range(0,num_variaveis):
        for c1 in range(0,num_variaveis):
            s[c][c1] = (c == c1)

    # Calcula novo gradiente
    norma_grad = 0.0
    for c in range(0,num_variaveis):
        g[c][0] = np.longfloat(parser.parse(gradiente[c][0]).evaluate(entrada))
        norma_grad += g[c][0]**2
    norma_grad = math.sqrt(norma_grad)
    
    while(i < 100):        
        if(float(norma_grad) < float(epsilon)):
            break
        
        # Calcula direção
        for c in range(0,num_variaveis):
            soma = 0.0
            for c1 in range(0,num_variaveis):
                soma += s[c][c1] * g[c1][0]
            d[c][0] = - soma
        
        # Faz o formato da função de min f(x+lambda*d)
        nova_funcao = funcao
        for c in range(0,num_variaveis):
            min_f[c][0] = '(' + str(x[c][0]) + '+(' + str(d[c][0]) + ')*x)'
        
            # Substituir na função os valores da função min f
            nova_funcao = nova_funcao.replace(str(variaveis[c]), str(min_f[c][0]))

        # Determina o valor de lambda ---> Se lambda negativo não pode continuar
        l = float(FiltraMetodoNewton(nova_funcao, x[0][0]))
        if(l < 0):
            sg.popup_ok('Não foi encontrado um lambda positivo! Insira um novo ponto inicial.')
            m = -1
            return (m, m, m, m) 
        
        # Substituir x pelo valor de lambda e atualizar x
        for c in range(0,num_variaveis):
            nova_funcao = min_f[c][0].replace('x', str(l))
            resultado = np.longfloat(parser.parse(nova_funcao).evaluate(entrada))
            x[c][0] = float(resultado)
            entrada[variaveis[c]] = x[c][0]
            
        # Atualiza gradiente
        norma_grad = 0.0
        for c in range(0,num_variaveis):
            novo_g[c][0] = np.longfloat(parser.parse(gradiente[c][0]).evaluate(entrada))
            norma_grad += novo_g[c][0]**2
        norma_grad = math.sqrt(norma_grad)
        
        if(k < num_variaveis-1):
            
            for c in range(0,num_variaveis):
                # qk = g^(k+1)
                q[c][0] = novo_g[c][0] - g[c][0]
                # atualiza gradiente
                g[c][0] = novo_g[c][0]
                # pk = l_kd^k
                p[c][0] = l * d[c][0]
            
            auxa = np.dot(s,q)
            auxb = np.dot(auxa,q.T)
            auxa = np.dot(auxb,s)
            
            auxb = np.dot(q.T,s)
            auxc = np.dot(auxb,q)
            
            auxb = np.dot(p.T,q)
                              
            s = s + (p.dot(p.T))/(auxb[0][0]) - (auxa)/(auxc[0][0])
            
            # simetrica
            if(not simetrica(s)):
                return -1
            # definida positiva
            if(not definida_positiva(s)):
                return -1
            k = k + 1
        else:
            # Atualiza x, i, g, k
            # x já atualizado
            # Matriz simétrica definida positiva inicial
            for c in range(0,num_variaveis):
                # atualiza gradiente
                g[c][0] = novo_g[c][0]
                for c1 in range(0,num_variaveis):
                    # Atualliza matriz inicial
                    s[c][c1] = (c == c1)
            i = i + 1
            k = 0
    # Determina valor de f(x*)
    for c in range(0,num_variaveis):
            entrada[variaveis[c]] = x[c][0]
    y = float(parser.parse(funcao).evaluate(entrada))
    
    return (i, x, y, num_variaveis)
        
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
        k = -1
        sg.popup_ok('Número de pontos de entrada não condiz com a quantidade de variáveis da função!')
        return (k, k, k, k)
    if (epsilon <= 0.0):
        k = -1
        sg.popup_ok('Epsilon inválido!')
        return (k, k, k, k)

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
        k = -1
        sg.popup_ok('Número de pontos de entrada não condiz com a quantidade de variáveis da função!')
        return (k, k, k, k)
    if (float(epsilon) <= 0.0):
        k = -1
        sg.popup_ok('Epsilon inválido!')
        return (k, k, k, k)

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

#Filtra o método de Newton:
def FiltraMetodoNewton(funcao, x):
    retorna = float(MetodoNewton(funcao, x))
    if(retorna < 0):
        return float(MetodoNewton(funcao, 0))
    return retorna

#Função para busca na reta (Newton):
def MetodoNewton(funcao, x):
    k = []
    x = float(x)
    deriv1 = str(diff(funcao))
    d1 = float(parser.parse(deriv1).evaluate({'x' : x}))    
    j = 0
    k.append(x)
    l = 0
    
    while abs(d1) >= 0.00001:
        deriv2 = str(diff(deriv1))
        d2 = float(parser.parse(deriv2).evaluate({'x' : x}))
        if d2 != 0.0:
            x = float(k[len(k)-1] - (d1 / d2))
            k.append(x)

            if float(abs(k[len(k)-1] - k[len(k)-2]) / max(1, abs(k[len(k)-1]))) < 0.00001:         
                break
            else:
                d1 = float(parser.parse(deriv1).evaluate({'x' : x}))
        else:
            break
        j = j + 1
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
       funcao = str(parser.parse(valores['expressao']))
       resultado = HookeJeeves(funcao, valores['ponto_inicial'], valores['epsilon'])
       if(resultado[0] != -1):
           window2['respostaHookeJeeves1'].update('RESULTADO: ')
           saida = 'Com K variando de 1 a %d' % resultado[0]
           if(resultado[0]==100):
               saida += ' (máximo de iterações)'
           window2['respostaHookeJeeves2'].update(saida)
           saida = '('
           for i in range (0, resultado[3]):
               valor = "{:.4f}".format(float(resultado[1][i]))
               saida += str(valor)
               if (i!=resultado[3]-1):
                   saida += ', '
           saida += ')^t'
           window2['respostaHookeJeeves3'].update('x* = ' + saida)
           window2['respostaHookeJeeves4'].update('f(x*) = %.4f' % resultado[2])
    
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
        resultado = FletcherReeves(funcao, valores['ponto_inicial'], valores['epsilon'])
        if(resultado[0] != -1):
            window5['respostaFletcher1'].update('RESULTADO: ')
            window5['respostaFletcher2'].update('Com K variando de 0 a %d' % resultado[0])
            saida = '('
            for i in range (0, resultado[3]):
                #(x1+3)^2+(x2-1)^3
                valor = "{:.4f}".format(float(resultado[1][i]))
                saida += str(valor)
                if (i!=resultado[3]-1):
                    saida += ', '
            saida += ')^t'
            window5['respostaFletcher3'].update('x* = ' + saida)
            window5['respostaFletcher4'].update('f(x*) = %.4f' % resultado[2])
    if window == window6 and event == 'Calcular':
        funcao = str(parser.parse(valores['expressao']))
        resultado =  DavidonFletcherPowell(funcao, valores['ponto_inicial'], valores['epsilon'])
        if(resultado[0] != -1):
            window6['respostaDavidon1'].update('RESULTADO: ')
            saida = 'Com I variando de 0 a %d' % resultado[0]
            if(resultado[0]==100):
                saida += ' (máximo de iterações)'
            window6['respostaDavidon2'].update(saida)
            saida = '('
            for i in range (0, resultado[3]):
                valor = "{:.4f}".format(float(resultado[1][i]))
                saida += str(valor)
                if (i!=resultado[3]-1):
                    saida += ', '
            saida += ')^t'
            window6['respostaDavidon3'].update('x* = ' + saida)
            window6['respostaDavidon4'].update('f(x*) = %.4f' % resultado[2])
