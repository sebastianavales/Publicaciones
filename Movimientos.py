#!/usr/bin/env python
# coding: utf-8

# # Importación archivo Movimientos.

# In[1]:


#Importar librerias para trabajar con DataFrames

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[2]:


#Importar y ajustar archivo de Movimientos

Movimientos = pd.read_csv('Movimientos.csv', dtype = {'Documento': 'str', 'Codigo Entidad Orgien': 'int'}, sep=',')

Movimientos = pd.DataFrame(Movimientos)

Movimientos.loc[(Movimientos['Codigo Entidad Orgien'] == 105) & (Movimientos['Nombre Canal'] == 'Corresponsal Cooperativo'), 'Nombre Canal'] = 'Oficinas'

Movimientos.loc[(Movimientos['Codigo Entidad Orgien'] == 105) & (Movimientos['ID. Canal'] == 6), 'ID. Canal'] = 0

Movimientos['Concatenar'] = Movimientos['Documento'] + Movimientos['Tarjeta']


# # Interbancarias recibidas.

# In[ ]:


Interbancarias = Movimientos.loc[(Movimientos['ID. Transaccion'] == '46') & ((Movimientos['Nombre Canal'] == 'Banca Movil') | (Movimientos['Nombre Canal'] == 'Portal transaccional (Web)'))]

Interbancarias.to_excel('Interbancarias.xlsx')


# # PSE.

# In[ ]:


#PSE = Movimientos.loc[(Movimientos['ID. Terminal'] == 'W1')]

PSE = Movimientos.loc[((Movimientos['ID. Transaccion'] == '01') | (Movimientos['ID. Transaccion'] == 'PSE3')) & ((Movimientos['Nombre Canal'] == 'Banca Movil') | (Movimientos['Nombre Canal'] == 'Portal transaccional (Web)'))]

PSE.to_excel('PSE.xlsx')


# # Portal Transando.

# In[3]:


Portaltrans = Movimientos.loc[(Movimientos['ID. Transaccion'] == '40') | (Movimientos['ID. Transaccion'] == '41') | (Movimientos['ID. Transaccion'] == '44') | (Movimientos['ID. Transaccion'] == '48') | (Movimientos['ID. Transaccion'] == '50') | (Movimientos['ID. Transaccion'] == '52') | (Movimientos['ID. Transaccion'] == 'PG') | (Movimientos['ID. Transaccion'] == 'RC') | (Movimientos['ID. Transaccion'] == 'TCAD') | (Movimientos['ID. Transaccion'] == 'TCPD')]

Portaltrans.to_excel('Portaltrans.xlsx')


# # Liquidación EFECTY.

# In[ ]:


Efecty = Movimientos.loc[(Movimientos['ID. Terminal'] == 'W7') & (Movimientos['Error'] == 0)]

Efecty.to_excel('Efecty.xlsx')


# # Liquidación TRANSFIYA.

# In[ ]:


Transfiya = Movimientos.loc[(Movimientos['ID. Transaccion'] == '50') & ((Movimientos['Error'] == 0) | (Movimientos['Error'] == 900))]

Transfiya.to_excel('Transfiya.xlsx')


# # Recaudo Terceros.

# In[ ]:


Recaudos = Movimientos.loc[((Movimientos['ID. Transaccion'] == 'RT') | (Movimientos['ID. Transaccion'] == 'RTTJ')) & (Movimientos['Error'] == 0)]

Recaudos.to_excel('Recaudos.xlsx')


# # Intercooperativas.

# In[ ]:


#Identificar si una trx es Intercooperativa o no

Movimientos['Intercooperativas'] = ''

intercooperativa = [
    (Movimientos['Codigo Entidad Orgien']) == (Movimientos['Cooperativa Terminal']),
    (Movimientos['Codigo Entidad Orgien']) != (Movimientos['Cooperativa Terminal'])
]

interlist = ['NO','SI']
Movimientos['Intercooperativas'] = np.select(intercooperativa, interlist, default='-' )
Intercooperativas = pd.DataFrame(Movimientos)

Intercooperativas.to_excel('Intercooperativas.xlsx')

