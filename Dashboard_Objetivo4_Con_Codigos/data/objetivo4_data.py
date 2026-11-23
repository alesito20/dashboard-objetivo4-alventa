import pandas as pd

# ==========================================================
# BASE CENTRAL DE DATOS – OBJETIVO 4
# Valores tomados del escenario de trabajo conversado.
# Los datos de mejora y costos son simulados/proyectados.
# ==========================================================

# Diagnóstico inicial: 100 pedidos
pedidos_total = 100
pedidos_conformes = 85
pedidos_no_conformes = 15
otif_inicial = 85.00

df_otif = pd.DataFrame({
    "Mes": ["Marzo", "Abril", "Mayo", "Junio", "Julio"],
    "Pedidos recibidos": [15, 15, 25, 25, 20],
    "Pedidos conformes": [14, 13, 20, 19, 19],
    "Pedidos no conformes": [1, 2, 5, 6, 1],
    "OTIF (%)": [93.33, 86.67, 80.00, 76.00, 95.00]
})

# Heijunka: programación y seguimiento simulado de la primera semana
df_heijunka = pd.DataFrame({
    "Día": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
    "900 mL programado": [145, 145, 145, 145, 145],
    "1 L programado": [90, 90, 90, 90, 90],
    "Total programado": [235, 235, 235, 235, 235],
    "Preparado": [235, 235, 225, 235, 235],
    "Despachado": [235, 220, 225, 235, 230]
})

# Kanban
df_kanban = pd.DataFrame({
    "Presentación": ["Aceite 900 mL", "Aceite 1 L"],
    "Inventario inicial": [300, 180],
    "Demanda diaria": [145, 90],
    "Punto de reposición": [290, 180],
    "Stock de seguridad": [145, 90],
    "Tarjetas Kanban": [2, 2],
    "Plazo de reposición (días)": [1, 1]
})

df_inventario = pd.DataFrame({
    "Día": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
    "Aceite 900 mL": [155, 155, 155, 155, 155],
    "Aceite 1 L": [90, 90, 90, 90, 90]
})

# Economía mensual simulada
df_costos = pd.DataFrame({
    "Concepto": [
        "Compras urgentes y transporte adicional",
        "Horas extras por retrasos",
        "Reprogramación de despachos",
        "Segundos viajes",
        "Seguimiento de herramientas"
    ],
    "Antes (S/)": [480, 240, 135, 140, 0],
    "Después (S/)": [160, 60, 45, 0, 120]
})

df_inversion = pd.DataFrame({
    "Actividad": [
        "Diseño del tablero Heijunka",
        "Capacitación Heijunka",
        "Materiales y formatos Heijunka",
        "Tarjetas Kanban",
        "Señalización y organización visual",
        "Capacitación Kanban"
    ],
    "Herramienta": ["Heijunka", "Heijunka", "Heijunka",
                    "Kanban", "Kanban", "Kanban"],
    "Inversión (S/)": [100, 150, 50, 80, 120, 50]
})

gasto_antes = 995
gasto_despues = 385
inversion_inicial = 550
ahorro_mensual = 610
reduccion_costos = 61.31
roi_primer_mes = 10.91
ahorro_operativo_anual = 7320
beneficio_neto_anual = 6770
