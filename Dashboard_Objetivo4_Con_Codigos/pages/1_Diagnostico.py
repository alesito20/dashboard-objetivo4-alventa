import streamlit as st
import plotly.express as px
from data.objetivo4_data import df_otif, pedidos_total, pedidos_conformes, pedidos_no_conformes, otif_inicial

st.set_page_config(page_title="Diagnóstico | Objetivo 4", page_icon="📊", layout="wide")
st.title("01 | Diagnóstico inicial")
st.caption("Incumplimiento de entregas a clientes – situación previa a la mejora")

a, b, c = st.columns(3)
a.metric("Pedidos evaluados", pedidos_total)
b.metric("Pedidos conformes", pedidos_conformes)
c.metric("Pedidos no conformes", pedidos_no_conformes)

left, right = st.columns(2)
with left:
    st.subheader("Composición de pedidos")
    fig = px.pie(
        names=["Pedidos conformes", "Pedidos no conformes"],
        values=[pedidos_conformes, pedidos_no_conformes],
        hole=0.55
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Evolución mensual del OTIF")
    fig = px.line(df_otif, x="Mes", y="OTIF (%)", markers=True)
    fig.update_yaxes(range=[0, 100], ticksuffix="%")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Registro mensual")
st.dataframe(df_otif, use_container_width=True, hide_index=True)
st.info("Mayo y junio suman 11 de los 15 pedidos no conformes (73.33%).")
