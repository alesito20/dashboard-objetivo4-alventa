import streamlit as st
import plotly.express as px
from data.objetivo4_data import df_heijunka

st.set_page_config(page_title="Heijunka | Objetivo 4", page_icon="📅", layout="wide")
st.title("02 | Implementación de Heijunka")
st.caption("Nivelación de la programación diaria por presentación")

programado = int(df_heijunka["Total programado"].sum())
preparado = int(df_heijunka["Preparado"].sum())
despachado = int(df_heijunka["Despachado"].sum())

a, b, c = st.columns(3)
a.metric("Total programado", f"{programado:,} unidades")
b.metric("Total preparado", f"{preparado:,} unidades")
c.metric("Total despachado", f"{despachado:,} unidades")

st.subheader("Tablero de producción diaria")
st.dataframe(df_heijunka, use_container_width=True, hide_index=True)

fig = px.bar(
    df_heijunka, x="Día",
    y=["900 mL programado", "1 L programado"],
    barmode="stack",
    title="Distribución diaria programada por presentación"
)
st.plotly_chart(fig, use_container_width=True)

fig = px.line(
    df_heijunka, x="Día",
    y=["Total programado", "Preparado", "Despachado"],
    markers=True,
    title="Seguimiento diario: programado, preparado y despachado"
)
st.plotly_chart(fig, use_container_width=True)

cumplimiento = despachado / programado * 100 if programado else 0
st.metric("Cumplimiento de despacho frente a programación", f"{cumplimiento:.2f}%")
st.warning(
    "Este porcentaje compara unidades despachadas con unidades programadas "
    "durante la semana simulada. No representa el OTIF por pedido."
)
