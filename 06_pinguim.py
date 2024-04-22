#
#
# Base de dados de pinguins do Ártico:
# Estudo Dra. Palmer, 2001
# Base de Dados no Github:
# https://gist.github.com/slopp/ce3b90b9168f2f921784de84fa445651
#
# Artigo:
# https://lauranavarroviz.wordpress.com/2020/08/01/palmer-penguins/

#v6: acréscimos em relação a versão v6:
# 1: Analisar por cada sexo, coluna 'sex'

# Importando bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título
st.title('Análise de dados de pinguins do Ártico')

# Subtítulo
st.markdown("Utilize este App e construa suas próprias análises de dados!")

selecao_especies = st.sidebar.multiselect('Selecione as espécies de pinguins', ['Adelie', 'Chinstrap', 'Gentoo'], default='Adelie')

print(type(selecao_especies), selecao_especies)
selecao_var_x = st.selectbox('Selecione a variável para o eixo X', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

selecao_var_y = st.selectbox('Selecione a variável para o eixo Y', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

# selecionando o sexo
selecao_sexo = st.selectbox('Selecione o sexo', ['Ambos os sexos', 'Macho', 'Fêmea'])

visualizar_toda_escala = st.checkbox('Visualizar toda a escala do gráfico')

pinguim_arq = st.file_uploader('Carregue o arquivo de dados pinguins . csv', type='csv')

if pinguim_arq is not None:
    df = pd.read_csv(pinguim_arq)
else:
    df = pd.read_csv('penguins.csv')

if selecao_sexo == 'Macho':
    df = df[df['sex'] == 'male']
elif selecao_sexo == 'Fêmea':
    df = df[df['sex'] == 'female']
# A função plt.subplots () sem parâmetros retorna uma figura e um eixo. A fig e o ax retornados são atribuídos a variáveis fig e ax, respectivamente.

# A variável figé um objeto de figura. A figura é a imagem final que pode conter um ou mais eixos. Você pode pensar na figura como um contêiner que contém esses eixos.

# A variável ax é um objeto de eixos. Um objeto de eixos é um gráfico individual com um eixo x, um eixo y e o espaço onde você pode desenhar linhas ou pontos.

# Após essa linha, você pode usar o objeto ax para desenhar gráficos, definir rótulos, etc. e usar o objeto fig para salvar a figura em um arquivo, alterar o tamanho da figura e assim por diante.


# criando um gráfico de dispersão
fig, ax = plt.subplots()
for sel_epc in selecao_especies:
    df1 = df[df.species == sel_epc]
    ax.scatter(df1[selecao_var_x], df1[selecao_var_y], alpha=0.8)
if visualizar_toda_escala:
    ax.set_xlim(0, 1.1*df[selecao_var_x].max())
    ax.set_ylim(0, 1.1*df[selecao_var_y].max())
ax.set_xlabel(selecao_var_x)
ax.set_ylabel(selecao_var_y) 
ax.legend(selecao_especies)   
ax.grid(True)

ax.set_title(f'Dispersão {selecao_var_x} x {selecao_var_y} para a(s) espécie(s):'+' '.join(selecao_especies))
# Fixed the issue by closing the opening parenthesis in the set_title function call.
st.pyplot(fig)