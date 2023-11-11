#------------------------------------------------------------------------------------
# Passo a Passo de solução:
# Abrir os 6 arquivos em Excel
# Para cada arquivo:
# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000
# Se for maior que 55k -> Envia um SMS com o nome, o mês e as vendas do vendedor
# Caso não seja maior que 55k, não faça nada.
#------------------------------------------------------------------------------------
#Para fazer o programa será necessário instalar: #Pandas (integração do pyhton com excel), #openpyxl (integração do pyhton com excel), #twilio (integração Python com sms)

import pandas as pd 
from twilio.rest import Client
import certifi

#conta Twilio
account_sid = 'ACc0811a1d0db1ca912adaf0c3d2b9264d'
#token twilio
auth_token = '61e64975f2c0afb968b6ec8d1a2c6016'
client = Client(account_sid, auth_token)


# Abrir os 6 arquivos em Excel

lista_meses = ['janeiro', 'fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    

# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000    
    
    if (tabela_vendas ['Vendas'] > 55000).any():

        vendedor = tabela_vendas.loc[tabela_vendas ['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas ['Vendas'] > 55000,'Vendas'].values[0]
        print (f' No mês de {mes} alguém bateu a meta!!!  vendedor: {vendedor}, Valor de vendas: R$ {vendas:.2f} ')
        message = client.messages.create(
                     from_='xxxxxxxxxx', #numero gerado no twilio
                     to='+xxxxxxxxx', #seu numero
                     body=f' No mês de {mes} alguém bateu a meta!!!  vendedor: {vendedor}, Valor de vendas: R$ {vendas:.2f} '                   
                 )

        print(message.sid)


#Dica, caso dê erro de certificado quando rodar, vá no terminal e digite "pip install python-certifi-win32"




