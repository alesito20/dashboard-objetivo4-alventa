import streamlit as st
import plotly.express as px
from data.objetivo4_data import (
    df_otif, df_heijunka, df_kanban, df_inventario,
    df_costos, pedidos_total, pedidos_conformes, pedidos_no_conformes,
    otif_inicial, gasto_antes, gasto_despues, ahorro_mensual,
    reduccion_costos, inversion_inicial, beneficio_neto_anual
)

st.set_page_config(
    page_title="Objetivo 4 | Alventa S.A.C.",
    page_icon="📦",
    layout="wide"
)

st.markdown("""
<style>
.stApp {background: #F4F7FA;}
.block-container {padding-top: 1.4rem; padding-bottom: 2rem;}
[data-testid="stMetric"] {
    background: white; border: 1px solid #E2E8F0;
    padding: 14px; border-radius: 12px;
}
h1, h2, h3 {color: #123C52;}
</style>
""", unsafe_allow_html=True)

st.title("Dashboard de Gestión – Objetivo 4")
st.caption("Corporación Alventa S.A.C. | Cumplimiento de entregas | Heijunka + Kanban")

st.sidebar.title("OBJETIVO 4")
st.sidebar.caption("Corporación Alventa S.A.C.")
st.sidebar.info(
    "Utiliza las secciones del menú para revisar el diagnóstico, "
    "las herramientas implementadas y la evaluación económica."
)

st.subheader("Vista ejecutiva")
st.write(
    "Panel de seguimiento del escenario de mejora propuesto para reducir "
    "incidencias de abastecimiento y fortalecer la planificación de despachos."
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Pedidos evaluados", f"{pedidos_total}")
c2.metric("OTIF inicial", f"{otif_inicial:.2f}%")
c3.metric("Pedidos no conformes", f"{pedidos_no_conformes}")
c4.metric("Ahorro mensual estimado", f"S/ {ahorro_mensual:,.2f}")

st.divider()
left, right = st.columns(2)

with left:
    st.markdown("### Situación inicial de los pedidos")
    fig = px.pie(
        names=["Conformes", "No conformes"],
        values=[pedidos_conformes, pedidos_no_conformes],
        hole=0.55
    )
    fig.update_traces(textinfo="label+percent")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### Evolución mensual del OTIF")
    fig = px.line(df_otif, x="Mes", y="OTIF (%)", markers=True)
    fig.update_yaxes(range=[0, 100], ticksuffix="%")
    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.markdown("### Resultado económico mensual")
fig = px.bar(
    x=["Antes de la mejora", "Después de la mejora"],
    y=[gasto_antes, gasto_despues],
    text=[f"S/ {gasto_antes:,.0f}", f"S/ {gasto_despues:,.0f}"],
    labels={"x": "Escenario", "y": "Gasto mensual (S/)"}
)
fig.update_traces(textposition="outside")
st.plotly_chart(fig, use_container_width=True)

k1, k2, k3 = st.columns(3)
k1.metric("Reducción de costos", f"{reduccion_costos:.2f}%")
k2.metric("Inversión inicial", f"S/ {inversion_inicial:,.2f}")
k3.metric("Beneficio neto anual proyectado", f"S/ {beneficio_neto_anual:,.2f}")

st.warning(
    "Nota metodológica: los resultados de implementación y los costos son "
    "supuestos de simulación académica. El OTIF inicial y el cumplimiento de "
    "unidades programadas son indicadores distintos; no deben compararse como equivalentes."
)

st.caption("Para abrir los detalles, selecciona una sección en el menú lateral.")
