#!/usr/bin/env python
# coding: utf-8

# In[7]:


from validate_docbr import CPF, CNPJ
import pandas as pd


# In[13]:


def validar_documento(documento):
    cpf = CPF()
    cnpj = CNPJ()

    documento = documento.replace(".", "").replace("-", "").replace("/", "")

    if len(documento) == 11 and cpf.validate(documento):
        return 'FISICA'
    elif len(documento) == 14 and cnpj.validate(documento):
        return 'JURIDICA'
    else:
        return "Documento inválido"


# # Insira o nome da Planilha aqui

# In[17]:


df1 = pd.read_excel('Planilha de Recepção de Votos.xlsx')
df1


# In[20]:


df2 = pd.DataFrame()

# Transferindo os dados de df1 para df2 com base na lógica
df2['NOME'] = df1['Razão Social do Participante']
df2['TIPO_PESSOA'] = df1['Documento do Participante'].apply(validar_documento)
df2['CPF_CNPJ'] = df1['Documento do Participante']
df2['ON'] = df1['Quantidade']

# Adicionando uma coluna 'PN' vazia (caso necessário)
df2['PN'] = 0  # ou df1['PN'] se houver uma coluna correspondente no df1


# In[23]:


df2


# In[22]:


df2.to_csv('base_votos.csv', index=False, sep=',')

