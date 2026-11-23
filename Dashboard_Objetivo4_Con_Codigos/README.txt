DASHBOARD OBJETIVO 4 – VERSIÓN CON CÓDIGOS

ESTRUCTURA:
Dashboard_Objetivo4_Con_Codigos/
├── app.py
├── requirements.txt
├── data/
│   ├── __init__.py
│   └── objetivo4_data.py
├── pages/
│   ├── 1_Diagnostico.py
│   ├── 2_Heijunka.py
│   ├── 3_Kanban.py
│   └── 4_Analisis_Economico.py
└── assets/

INSTALACIÓN:
1. Descomprime la carpeta.
2. En VS Code abre la carpeta completa (Archivo > Abrir carpeta).
3. Abre Terminal > New Terminal.
4. Ejecuta:
   py -m pip install -r requirements.txt
5. Ejecuta:
   py -m streamlit run app.py

NOTAS:
- Los archivos de páginas aparecen en el menú lateral de Streamlit.
- Los datos están centralizados en data/objetivo4_data.py.
- Para actualizar valores, modifica ese archivo de datos.
- Los datos de implementación y economía se presentan como escenario simulado.
- El 97.45% es cumplimiento de unidades despachadas/programadas en la semana
  simulada, no OTIF posterior.
- Revisar la consistencia del registro de reposiciones e inventario antes de
  presentar esos movimientos como resultados verificados.
