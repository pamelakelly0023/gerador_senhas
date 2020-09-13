import random
import PySimpleGUI as sg 

class PassGen:
    def __init__(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('Nome do Site/Software: ', size=(10,1)),
            sg.Input(key='site', size=(20,1))],
            [sg.Text('Email: ', size=(10,1)),
            sg.Input(key='email', size=(20,1))],
            [sg.Text('Quantidade de caracteres: '), sg.Combo(values=list(
                range(30)), key='total', default_value=1, size=(3,1))],
            [sg.Output(size=(32,5))],
            [sg.Button('Gerar senha'), sg.Button('Cancelar'), sg.Button('Exibir')] 
        ]

        self.window = sg.Window('Gerador de senha', layout)

    def Start(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                break
            if event == 'Gerar senha':
                nova_senha = self.gerar_senha(values)
                print(nova_senha)
                self.salvar(nova_senha, values)
            if event == 'Exibir':
                arquivo = open('senhas.txt', 'r')
                info = arquivo.read()
                print(info)

    def gerar_senha(self, values):
        char_list= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@.-_'
        chars = random.choices(char_list, k=int(values['total']))
        new_pass = ''.join(chars)
        return new_pass
    
    def salvar(self, nova_senha, values):
        with open('senhas.txt','a', newline='') as arquivo:
            arquivo.write(
                f"info: {values['site']}, email: {values['email']}, nova senha: {nova_senha}"
            )
        print('Arquivo salvo')
    

gen = PassGen()
gen.Start()