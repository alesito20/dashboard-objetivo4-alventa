import streamlit as st
import plotly.express as px
from data.objetivo4_data import (
    df_costos, df_inversion, gasto_antes, gasto_despues,
    inversion_inicial, ahorro_mensual, reduccion_costos,
    roi_primer_mes, beneficio_neto_anual, ahorro_operativo_anual
)

st.set_page_config(page_title="Análisis económico | Objetivo 4", page_icon="💰", layout="wide")
st.title("04 | Análisis económico")
st.caption("Comparación mensual antes y después de Heijunka + Kanban")

a, b, c, d = st.columns(4)
a.metric("Gasto antes", f"S/ {gasto_antes:,.2f}")
b.metric("Gasto después", f"S/ {gasto_despues:,.2f}")
c.metric("Ahorro mensual", f"S/ {ahorro_mensual:,.2f}")
d.metric("Inversión inicial", f"S/ {inversion_inicial:,.2f}")

st.subheader("Desglose de costos mensuales")
st.dataframe(df_costos, use_container_width=True, hide_index=True)

fig = px.bar(
    df_costos,
    x="Concepto",
    y=["Antes (S/)", "Después (S/)"],
    barmode="group",
    title="Comparación de gastos por concepto"
)
fig.update_layout(xaxis_tickangle=-25)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Inversión de implementación")
st.dataframe(df_inversion, use_container_width=True, hide_index=True)
inversion_herramienta = df_inversion.groupby("Herramienta", as_index=False)["Inversión (S/)"].sum()
fig = px.pie(
    inversion_herramienta,
    names="Herramienta",
    values="Inversión (S/)",
    hole=0.5,
    title="Distribución de la inversión inicial"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Indicadores económicos")
x, y, z = st.columns(3)
x.metric("Reducción de costos", f"{reduccion_costos:.2f}%")
y.metric("ROI del primer mes", f"{roi_primer_mes:.2f}%")
z.metric("Beneficio neto anual proyectado", f"S/ {beneficio_neto_anual:,.2f}")

st.write(f"**Ahorro operativo anual:** S/ {ahorro_operativo_anual:,.2f}")
st.write(f"**Beneficio neto del primer año:** S/ {ahorro_operativo_anual:,.2f} − S/ {inversion_inicial:,.2f} = S/ {beneficio_neto_anual:,.2f}")

st.warning(
    "Los costos por incidencia, el nivel de reducción y los costos de seguimiento "
    "son supuestos del escenario simulado; no son registros contables verificados."
)
