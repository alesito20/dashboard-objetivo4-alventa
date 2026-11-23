import streamlit as st
import plotly.express as px
from data.objetivo4_data import df_kanban, df_inventario

st.set_page_config(page_title="Kanban | Objetivo 4", page_icon="🗂️", layout="wide")
st.title("03 | Implementación de Kanban")
st.caption("Control visual de existencias y activación de reposición")

st.subheader("Parámetros de inventario")
st.dataframe(df_kanban, use_container_width=True, hide_index=True)

fig = px.bar(
    df_kanban,
    x="Presentación",
    y=["Inventario inicial", "Punto de reposición"],
    barmode="group",
    title="Inventario inicial frente al punto de reposición"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Comportamiento del inventario durante la semana")
st.dataframe(df_inventario, use_container_width=True, hide_index=True)

fig = px.line(
    df_inventario, x="Día",
    y=["Aceite 900 mL", "Aceite 1 L"],
    markers=True,
    title="Existencias al cierre de cada día"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Resumen de tarjetas Kanban")
st.metric("Tarjetas definidas", int(df_kanban["Tarjetas Kanban"].sum()))
st.info(
    "El diseño final considera dos tarjetas por presentación. "
    "Validar los movimientos diarios de entradas y salidas antes de afirmar "
    "que el inventario permaneció constante por reposiciones reales."
)
