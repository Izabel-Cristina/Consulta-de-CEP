
import json
import requests
import PySimpleGUI as sg

layout = [
    [sg.Text('Informe o número do CEP que deseja consultar: ')],
    [sg.InputText(key= 'numero_CEP')],
    [sg.Button('Consultar'), sg.Button('Cancelar')],
    [sg.Text('', key = 'texto_CEP')]
]

janela = sg.Window('Consulta de CEP', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    try:
        if evento == 'Consultar':
            codigo_cep = valores['numero_CEP']
            codigo_cep = codigo_cep.replace('-', '').replace('.', '').replace(' ', '')
            len('numero_CEP')==8
            link = f'https://viacep.com.br/ws/{codigo_cep}/json/'
            requisicao = requests.get(link)
            dic_requisicao = requisicao.json()
            cep_endereco = dic_requisicao['cep']
            logradouro = dic_requisicao['logradouro']
            complemento = dic_requisicao['complemento']
            uf = dic_requisicao['uf']
            cidade = dic_requisicao['localidade']
            bairro = dic_requisicao['bairro']
            resultado = f'''
            
                        CEP: {cep_endereco}
                        Logradouro: {logradouro}
                        Complemento:{complemento}
                        Cidade: {cidade}
                        Bairro: {bairro}
                        UF: {uf}'''
        janela['texto_CEP'].update(f'Consultando {codigo_cep}: {resultado}')  
          
    except:
       cep = 'CEP INVALIDO'
       janela['texto_CEP'].update(f'{cep}')
janela.close()







