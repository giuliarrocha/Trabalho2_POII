import PySimpleGUI as sg
from sympy.polys.polyoptions import Symbols
from py_expression_eval import Expression, Parser
from sympy import *
from decimal import Decimal
import math

from sympy.solvers.diophantine.diophantine import length

sg.theme('LightBrown13')

## Janelas
def window_hookeJeeves():
    layout = [[sg.Text('HOOKE & JEEVES', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(30,1))],
            [sg.Text('Exemplo: x¹ = (0, 0) para R² o ponto inicial',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('x¹:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='ponto_inicial', size=(10,1))],
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
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(30,1))],
            [sg.Text('Exemplo: x¹ = (0, 0) para R² o ponto inicial',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('x¹:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='ponto_inicial', size=(10,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaGradiente1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaGradiente2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaGradiente3', text_color = 'black')]
            ]
    return sg.Window('Gradiente', layout, size=(400, 400), finalize=True, resizable=True)

def window_fletcherReeves():
    layout = [[sg.Text('FLETCHER & REEVES', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(30,1))],
            [sg.Text('Exemplo: x¹ = (0, 0) para R² o ponto inicial',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('x¹:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='ponto_inicial', size=(10,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaFletcher1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaFletcher2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaFletcher3', text_color = 'black')]
            ]
    return sg.Window('Fletcher & Reeves', layout, size=(400, 400), finalize=True, resizable=True)

def window_davidonFletcherPowell():
    layout = [[sg.Text('DAVIDON-FLETCHER-POWELL', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(30,1))],
            [sg.Text('Exemplo: x¹ = (0, 0) para R² o ponto inicial',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('x¹:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='ponto_inicial', size=(10,1))],
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
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(30,1))],
            [sg.Text('Exemplo: x¹ = (0, 0) para R² o ponto inicial',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('x¹:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='ponto_inicial', size=(10,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaNewton1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaNewton2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaNewton3', text_color = 'black')]
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
# Pegar resultado da função dada
def Resultado(funcao, ponto):
    if len(ponto) == 1:
        print("até x1")
        resultado = float(parser.parse(funcao).evaluate({'x1' : float(ponto[0])}))
        pass
    if len(ponto) == 2:
        print("até x2")
        resultado = float(parser.parse(funcao).evaluate({'x1' : float(ponto[0]), 'x2' : float(ponto[1])}))
        pass
    if len(ponto) == 3:
        print("até x3")
        resultado = float(parser.parse(funcao).evaluate({'x1' : float(ponto[0]), 'x2' : float(ponto[1]), 'x3' : float(ponto[2])}))
        pass
    if len(ponto) == 4:
        print("até x4")
        resultado = float(parser.parse(funcao).evaluate({'x1' : float(ponto[0]), 'x2' : float(ponto[1]), 'x3' : float(ponto[2]), 'x4' : float(ponto[3])}))
        pass
    return resultado

# def HookeJeeves ():

# def Newton():


# Rotina - Gradiente
def Gradiente (funcao, ponto_inicial, epsilon):
    x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
    init_printing(use_unicode=True)
    ponto = []
    fx = []
    
    # Pega os números da string ponto_inicial e coloca num vetor
    for i in ponto_inicial:
        if i.isdigit():
            ponto.append(i)

    resultado = Resultado(funcao, ponto)
    print(resultado)

    if float(epsilon) > 0.0:
        k = 1
        # derivada parcial

        #for j in ponto+1:
        #    print(j)
        #    x = 'x' + str(j)
        #    derivada = str(diff(funcao, x))
        #    fx.append(derivada)
        
        #print(fx)


# def FletcherPowell():
# def DavidonFletcherPowell():

#Função para busca na reta (Newton):
def MetodoNewton(funcao, a, b, epsilon):
    x, y, z = symbols('x y z')
    init_printing(use_unicode=True)

    x = a
    deriv1 = str(diff(funcao))
    d1 = float(parser.parse(deriv1).evaluate({'x' : x}))    
    k = []
    k.append(x)
    l = 0
    
    while abs(float(d1)) >= epsilon:
    
        deriv2 = str(diff(deriv1))
        d2 = float(parser.parse(deriv2).evaluate({'x' : x}))
        
        if d2 != 0.0:
            x = k[len(k)-1] - (d1 / d2)
            k.append(x)
            if((abs(k[len(k)-1] - k[len(k)-2]) / max(1, abs(k[len(k)-2]))) < epsilon):         
                break
            else:
                d1 = float(parser.parse(deriv1).evaluate({'x' : x}))
        else:
            break
        l = l + 1
    return (k[len(k)-1], l)

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
        print ("Newton"); 

    if window == window4 and event == 'Calcular':
        funcao = str(parser.parse(valores['expressao']))
        Gradiente(funcao, valores['ponto_inicial'], valores['epsilon'])

    if window == window5 and event == 'Calcular':
        print ("Fletcher & Reeves"); 
    
    if window == window6 and event == 'Calcular':
        print ("Davidon-Fletcher-Powell"); 
