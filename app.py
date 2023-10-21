import pandas as pd
import streamlit as st

df = pd.read_csv('historico_resultados_pruebas_saber_11.csv') 

df_comuna = df.sort_values('comuna')[['codigo_dane', 'comuna']]

df_registros =  df.loc[(df['registros'] >= 100) & (df['registros'] < 101)]

df_puntajeglobal = df.loc[df['puntaje_global'] >= 300, ['codigo_dane', 'puntaje_global']]
df_puntajelectura = df.loc[df['puntaje_lectura'] < 50, ['codigo_dane', 'puntaje_lectura']]
df_puntajesociales = df.loc[df['puntaje_sociales'] > 55, ['codigo_dane', 'puntaje_sociales']]



st.dataframe(df)

st.dataframe(df_comuna)

st.dataframe(df_registros)

st.dataframe(df_puntajeglobal)

st.dataframe(df_puntajelectura)

st.dataframe(df_puntajesociales)