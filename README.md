# Cambio de Curso — FIUBA

Herramienta web para que estudiantes de la Facultad de Ingeniería (UBA) encuentren compañeros con quienes intercambiar comisiones en una misma materia.

## ¿Cómo funciona?

1. **Buscá** si ya hay alguien que quiera el intercambio inverso al tuyo (sin necesidad de registrarte).
2. Si no hay resultados todavía, **publicá tu pedido** para que otros te encuentren.
3. Los pedidos se publican por **15 días** y podés darte de baja en cualquier momento con tu Padrón e Iniciales.
4. El contacto se coordina directamente entre los estudiantes (por mail o teléfono) y luego con la secretaría.

## Stack

- [Streamlit](https://streamlit.io/) — interfaz web
- [pandas](https://pandas.pydata.org/) — persistencia en CSV
- Python 3

## Instalación local

```bash
pip install streamlit pandas
streamlit run app.py
```

Los pedidos se guardan en `pedidos.csv` (creado automáticamente en el primer uso; excluido del repositorio).

## Estructura

```
app.py                  # Aplicación principal
requirements.txt        # Dependencias
.streamlit/
  config.toml           # Tema y configuración de Streamlit
attached_assets/
  logo_fiuba_*.png      # Logo FIUBA (embebido en header y footer)
start_streamlit.sh      # Script de arranque (suprime el prompt de email)
```

## Contacto

¿Consultas o problemas? Escribí a [mcaffoz@fi.uba.ar](mailto:mcaffoz@fi.uba.ar)
