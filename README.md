# Cambio de Curso — FIUBA

Herramienta web para que estudiantes de la Facultad de Ingeniería (UBA) encuentren compañeros con quienes intercambiar comisiones en una misma materia.

## Enlaces

- 🌐 **Aplicación web:** https://starter-script--Facucaffo.replit.app
- 🎥 **Video demo:** https://drive.google.com/file/d/1tX7o3FTPmIP75D_19qJvbzupdylODS5t/view?usp=drive_link
- 📄 **Informe completo (PDF):** [docs/Informe - Cambios de Curso (1).pdf](docs/Informe%20-%20Cambios%20de%20Curso%20(1).pdf)

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

Los pedidos se guardan en una base de datos SQLite (pedidos.db), creada automáticamente en el primer uso y excluida del repositorio. El uso de SQLite (en lugar de CSV) permite manejar correctamente el acceso concurrente de múltiples usuarios.

## Estructura

app.py                       # Aplicación principal
materias_cursos.json         # Materias y cursos disponibles (editable sin tocar el código)
requirements.txt             # Dependencias
LICENSE                      # Licencia MIT
pedidos.db                   # Base de datos SQLite (creada automáticamente, excluida del repo)
.streamlit/
  config.toml                 # Tema y configuración de Streamlit
attached_assets/
  logo_fiuba_*.png            # Logo FIUBA (embebido en header y footer)
docs/
  Informe - Cambios de Curso (1).pdf   # Informe de diagnóstico y justificación del proyecto
analysis/
  whatsapp_analysis.py         # Reproduce el análisis de WhatsApp con datos sintéticos
  siu_analysis.py               # Reproduce el análisis de SIU con datos sintéticos
  README.md                     # Explica la metodología y por qué los datos son sintéticos


## Contacto

¿Consultas o problemas? Escribí a [mcaffoz@fi.uba.ar](mailto:mcaffoz@fi.uba.ar)
