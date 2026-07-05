import streamlit as st

st.set_page_config(
    page_title="Cambio de Curso - FIUBA",
    page_icon="🎓",
    layout="centered",
)

import pandas as pd
import os
import base64
from datetime import datetime, timedelta

def _logo_b64(height_px=None):
    logo_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "attached_assets",
        "logo_fiuba_1783172752615.png",
    )
    try:
        with open(logo_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        h = f"height:{height_px}px;" if height_px else ""
        return f'<img src="data:image/png;base64,{b64}" style="{h}vertical-align:middle;">'
    except Exception:
        return ""

LOGO_LG = _logo_b64(48)
LOGO_SM = _logo_b64(30)

MATERIAS = [
    "ÁLGEBRA LINEAL (CB002)",
    "DESARROLLO ECONÓMICO (TC011)",
    "ECONOMÍA (TC010)",
    "ELECTRICIDAD Y MAGNETISMO (CB022)",
    "ELECTROTECNIA, MÁQUINAS E INSTALACIONES ELÉCTRICAS (TB015)",
    "EQUIPOS Y SISTEMAS PARA AUTOMATIZACIÓN INDUSTRIAL (TB016)",
    "ESTADÍSTICA APLICADA (TB014)",
    "ESTÁTICA Y RESISTENCIA DE MATERIALES (TB011)",
    "FÍSICA DE LOS SISTEMAS DE PARTÍCULAS (CB020)",
    "GESTIÓN INTEGRAL DE LA CADENA DE VALOR (TA011)",
    "HIGIENE Y SEGURIDAD (TC003)",
    "INDUSTRIAS EXTRACTIVAS (TA016)",
    "INGENIERÍA AMBIENTAL, SUSTENTABILIDAD Y CUIDADO DEL PLANETA (TC004)",
    "INVESTIGACIÓN OPERATIVA (TA012)",
    "LEGISLACIÓN Y EJERCICIO PROFESIONAL (TC002)",
    "MATERIALES Y APLICACIONES I (TB012)",
    "ORGANIZACIÓN Y DIRECCIÓN EMPRESARIA (TA010)",
    "PRINCIPIOS DE INGENIERÍA INDUSTRIAL (TB010)",
    "QUÍMICA BÁSICA (CB040)",
    "SISTEMAS CONTABLES Y GESTIÓN DE COSTOS (TA013)",
]

CURSOS_POR_MATERIA = {
    "FÍSICA DE LOS SISTEMAS DE PARTÍCULAS (CB020)": [
        "01 - CORSINI (lun y mie)", "02 - SACCONE (lun y mie)", "04 - AGUIRRE (mar y jue)",
        "05 - CORACH (mar y jue)", "06 - VIÑALES (mie y vie)", "07 - CHIABRANDO (mie y vie)",
        "09 - CORNEJO (lun y mie)", "10 - TOSCANI (lun y mie)", "11 - SOLA (mar y jue)",
        "12 - ROSSI (mar y jue)", "15 - CAMUYRANO (lun y mie)", "16 - RACERO (lun y mie)",
        "17 - FERRINI (mar y jue)", "18 - MORENO (mar y jue)",
    ],
    "PRINCIPIOS DE INGENIERÍA INDUSTRIAL (TB010)": [
        "1 - SABELLI - LOPEZ CONDE (lun y mie)", "2 - PINCHETE (lunes)", "3 - PINCHETE (jueves)",
    ],
    "ÁLGEBRA LINEAL (CB002)": [
        "01A - VARGAS - PALACIOS (lun y mie)", "01B - VARGAS - PERALTA (lu y mie)",
        "02A - VIBRENTIS - FAGES (mar y jue)", "02B - VIBRENTIS - CASTILLO (mar y jue)",
        "04A - LOPEZ - ORECCHIA (mar y jue)", "04B - LOPEZ - ALONSO (mar y jue)",
        "05 - PALACIOS PATRICIA ELIZABETH (mie y vie)", "06A - BOGGI - VENTURIELLO (lu y mie)",
        "06B - BOGGI - DOMINGUEZ (lu y mie)", "07A - CENTENO - ALVAREZ (mar y jue)",
        "07B - CENTENO - KLINGER (mar y jue)", "10 - GIRIBET JUAN IGNACIO (mie y vie)",
        "13A - CABANA - ALONSO (mie y vie)", "13B - CABANA - PRESENZA (mie y vie)",
        "15A - PALAU - CATUOGNO (lu y mie)", "15B - PALAU - GRÖER (lun y mie)",
        "17 - MENDIETA JULIO ANTONIO (mar y jue)", "19 - GARCIA SERRANO SILVINA AIDA (lu y mie)",
        "23A - GRYNBERG - CASSANI (lu y mie)", "23B - GRYNBERG - PEREYRA (lu y mie)",
        "24 - PERALTA NORA BEATRIZ (lu y mie)", "25 - ORECCHIA MONICA INES (mar y jue)",
    ],
    "QUÍMICA BÁSICA (CB040)": [
        "01 - IRIANNI JORGE LUIS (lunes y viernes)", "01B - DIZ VIRGINIA EMILSE (miércoles y viernes)",
        "02 - PORTA GUSTAVO ROBERTO (jueves y viernes)", "03 - SARALEGUI ANDREA BEATRIZ (viernes)",
        "04 - ANDRONIKOV ANDRES (martes y viernes)", "06 - GOBBI MIÑONES ALEJANDRO RICARDO (viernes)",
        "07 - CARACCIOLO NESTOR (lunes y viernes)", "07B - CARACCIOLO NESTOR (martes y viernes)",
        "08 - PORTA GUSTAVO ROBERTO (miércoles y viernes)", "09 - ROMERO ADRIANA MARCELA (jueves y viernes)",
    ],
    "ESTÁTICA Y RESISTENCIA DE MATERIALES (TB011)": [
        "1 - CORRAL (martes y jueves)", "2 - CORRAL (miércoles y viernes)",
        "3 - HARGAIN (miércoles y jueves)",
        "4 - HARGAIN (martes 8:30 a 11:30 y jueves 9:00 a 12:00)",
        "5 - HARGAIN (martes 19:00 a 22:00 y jueves 9:00 a 12:00)",
    ],
    "ORGANIZACIÓN Y DIRECCIÓN EMPRESARIA (TA010)": [
        "CONDE COMISIÓN 1", "CONDE COMISIÓN 2", "LIBSTER", "MOREY COMISIÓN 1", "MOREY COMISIÓN 2",
    ],
    "ECONOMÍA (TC010)": [
        "1 - BOTTA", "2 - SURACE", "3 - MONTALBANO",
    ],
    "ELECTRICIDAD Y MAGNETISMO (CB022)": [
        "01 - FONTANA MARCELO RAUL", "02 - APARICIO RODOLFO RUBEN", "03 - ZALDIVAR ESCOLA FACUNDO",
        "04 - PIVA MARCELO FABIAN", "05 - REDIN EDUARDO GABRIEL", "06 - ROHT YANINA LUCRECIA",
        "07 - SILVEYRA JOSEFINA MARIA", "08 - BINDA LEONARDO DAVID", "09 - PAMPILLO LAURA GABRIELA",
        "10 - PAGNOLA MARCELO RUBEN",
    ],
    "DESARROLLO ECONÓMICO (TC011)": [
        "1 - CIVALLERO", "2 - BOTTA", "3 - CHAVES",
    ],
    "ESTADÍSTICA APLICADA (TB014)": [
        "1 (lunes y jueves)", "2 (lunes y miércoles)", "3 (lunes, jueves y viernes)",
    ],
    "GESTIÓN INTEGRAL DE LA CADENA DE VALOR (TA011)": [
        "GUIDA 1 (martes y jueves de 14 a 19 hrs)", "GUIDA 2 (martes y jueves de 16 a 21 hrs)",
        "KOLL", "LEITER",
    ],
    "ELECTROTECNIA, MÁQUINAS E INSTALACIONES ELÉCTRICAS (TB015)": [
        "2", "3", "4", "5", "6", "7",
    ],
    "INVESTIGACIÓN OPERATIVA (TA012)": [
        "1 RIGOU", "2 GONZALEZ",
    ],
    "SISTEMAS CONTABLES Y GESTIÓN DE COSTOS (TA013)": [
        "1 ZANCHETTI (lunes)", "2 ZANCHETTI (viernes)", "3 CHAVES",
    ],
    "INGENIERÍA AMBIENTAL, SUSTENTABILIDAD Y CUIDADO DEL PLANETA (TC004)": [
        "01 SOLANA (martes 15 a 19 hrs)", "02 BIANUCCI", "03 SOLANA (martes 17 a 21 hrs)",
    ],
    "EQUIPOS Y SISTEMAS PARA AUTOMATIZACIÓN INDUSTRIAL (TB016)": [
        "1 (lunes y jueves)", "2", "3",
    ],
    "HIGIENE Y SEGURIDAD (TC003)": [
        "CHENLO - RIZZO", "BRIOZZO - BENAVIDES", "MARENSI - LEYBOVICH", "LEYBOVICH - MARENSI",
        "D´ELIA - BATTAN", "BELTRAMINI - DI MEGLIO",
    ],
    "INDUSTRIAS EXTRACTIVAS (TA016)": [
        "1 (jueves 19 a 23 hrs)", "2 (miércoles 19 a 23 hrs)",
    ],
    "LEGISLACIÓN Y EJERCICIO PROFESIONAL (TC002)": [
        "1 STEPANIK (miércoles 19 a 21 hrs)", "2 CASSIN (martes 19 a 21 hrs)",
        "3 LOPEZ (miércoles 17 a 19 hrs)", "4 NOREMBERG (jueves 17 a 19 hrs)",
        "5 RAIDEN I (lunes 16 a 18 hrs)", "6 RAIDEN II (lunes 19 a 21 hrs)",
    ],
}

_TODOS = "(todos los cursos)"
_PLACEHOLDER_MATERIA = "— Seleccioná una materia —"
_PLACEHOLDER_CURSO = "— Seleccioná un curso —"

ARCHIVO = "pedidos.csv"
COLUMNAS = [
    "padron", "iniciales", "nombre", "mail", "telefono",
    "materia", "curso_actual", "curso_deseado", "genero",
    "fecha", "vencimiento", "activo",
]
DIAS_VENCIMIENTO = 15

if not os.path.exists(ARCHIVO):
    pd.DataFrame(columns=COLUMNAS).to_csv(ARCHIVO, index=False)


def cargar_datos():
    df = pd.read_csv(ARCHIVO)
    if len(df) > 0:
        df["vencimiento"] = pd.to_datetime(df["vencimiento"], format="mixed")
        vencidos = df["vencimiento"] < pd.Timestamp.now()
        df.loc[vencidos, "activo"] = False
        df.to_csv(ARCHIVO, index=False)
    return df


st.markdown("""
<style>
.block-container { padding-top: 3.75rem !important; }
.fiuba-header, .fiuba-footer {
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    box-sizing: border-box;
}
.fiuba-header {
    background: #0A2A5E;
    padding: 1rem 3rem;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 1.8rem;
}
.fiuba-header-text .title {
    font-weight: 700;
    color: #ffffff;
    font-size: 1.05rem;
    line-height: 1.2;
}
.fiuba-header-text .subtitle {
    color: rgba(255,255,255,0.7);
    font-size: 0.82rem;
    line-height: 1.2;
}
.fiuba-footer {
    background: #f3f4f6;
    padding: 1.2rem 3rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 3rem;
    flex-wrap: wrap;
    gap: 12px;
    border-top: 1px solid #e5e7eb;
}
.fiuba-footer .footer-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #374151;
    font-size: 0.85rem;
}
.fiuba-footer .footer-contact {
    font-size: 0.85rem;
    color: #374151;
}
.fiuba-footer a { color: #E8743B; text-decoration: none; font-weight: 600; }
.fiuba-footer a:hover { text-decoration: underline; }
.section-head {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 0.6rem;
}
.section-icon {
    background: #EAF2FB;
    border-radius: 10px;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
}
.section-title-wrap h2 {
    margin: 0;
    font-size: 1.35rem;
    font-weight: 700;
    color: #111827;
    line-height: 1.2;
}
.section-accent {
    height: 3px;
    width: 56px;
    background: #E8743B;
    border-radius: 2px;
    margin-top: 4px;
}
[data-testid="stForm"] {
    background: #ffffff;
    border-radius: 14px;
    padding: 1.4rem 1.6rem !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    border: 1px solid #e9ecef;
    margin-top: 0.5rem;
}
.stTextInput > div > div > input {
    background-color: #f8f9fa !important;
    border: 1.5px solid #dee2e6 !important;
    border-radius: 8px !important;
    color: #1a1a1a !important;
}
.stTextInput > div > div > input:focus {
    border-color: #E8743B !important;
    box-shadow: 0 0 0 2px rgba(232,116,59,0.15) !important;
}
.stSelectbox > div > div {
    background-color: #f8f9fa !important;
    border: 1.5px solid #dee2e6 !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="fiuba-header">
    {LOGO_LG}
    <div class="fiuba-header-text">
        <div class="title">Facultad de Ingeniería</div>
        <div class="subtitle">Universidad de Buenos Aires</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    "<p style='color:#E8743B;font-size:0.72rem;font-weight:700;"
    "letter-spacing:2.5px;margin-bottom:2px;'>SERVICIOS ACADÉMICOS</p>",
    unsafe_allow_html=True,
)
st.title("Cambio de Curso")
st.markdown(
    "Esta herramienta te permite encontrar compañeros que quieran hacer el intercambio inverso "
    "de curso en la misma materia ([podés consultar la oferta de comisiones acá]"
    "(https://guaraniautogestion.fi.uba.ar/g3w/oferta_comisiones)). "
    "**Empezá buscando** si ya hay alguien con quien intercambiar — "
    "no necesitás registrarte para buscar. "
    "Si encontrás a alguien, contactalos directamente por mail o teléfono para coordinar el cambio con la secretaría. "
    "Si no hay resultados todavía, publicá tu pedido para que otros te encuentren — "
    "los pedidos se publican por 15 días y podés darte de baja en cualquier momento "
    "ingresando tu **Padrón** e **Iniciales de tu nombre** en la sección correspondiente."
)

_df_contador = cargar_datos()
_activos_count = int((_df_contador["activo"] == True).sum()) if len(_df_contador) > 0 else 0
st.markdown(f"📊 Hay **{_activos_count}** pedidos activos en este momento")

st.divider()
st.markdown("""
<div class="section-head">
    <div class="section-icon">🔍</div>
    <div class="section-title-wrap">
        <h2>Buscar cambios compatibles</h2>
        <div class="section-accent"></div>
    </div>
</div>
""", unsafe_allow_html=True)

buscar_materia_sel = st.selectbox(
    "Materia que querés buscar",
    [_PLACEHOLDER_MATERIA] + MATERIAS,
    key="buscar_materia",
)
buscar_materia = "" if buscar_materia_sel == _PLACEHOLDER_MATERIA else buscar_materia_sel

with st.form("form_busqueda"):
    col_bact, col_bdes = st.columns(2)
    with col_bact:
        if buscar_materia in CURSOS_POR_MATERIA:
            buscar_curso_actual_sel = st.selectbox(
                "Tu curso actual",
                [_TODOS] + CURSOS_POR_MATERIA[buscar_materia],
                key="bca_sel",
            )
            buscar_curso_actual = "" if buscar_curso_actual_sel == _TODOS else buscar_curso_actual_sel
        else:
            buscar_curso_actual = st.text_input("Tu curso actual", key="bca_txt")

    with col_bdes:
        if buscar_materia in CURSOS_POR_MATERIA:
            buscar_curso_deseado_sel = st.selectbox(
                "Curso al que querés inscribirte",
                [_TODOS] + CURSOS_POR_MATERIA[buscar_materia],
                key="bcd_sel",
            )
            buscar_curso_deseado = "" if buscar_curso_deseado_sel == _TODOS else buscar_curso_deseado_sel
        else:
            buscar_curso_deseado = st.text_input("Curso al que querés inscribirte", key="bcd_txt")

    buscar = st.form_submit_button("🔍 Buscar", use_container_width=True)

if buscar:
    if not buscar_materia:
        st.error("Por favor seleccioná una materia para buscar.")
    else:
        df = cargar_datos()
        activos = df[df["activo"] == True].copy()

        resultado = activos[
            activos["materia"].str.lower().str.contains(buscar_materia.strip().lower(), regex=False)
        ]

        if buscar_curso_deseado.strip():
            resultado = resultado[
                resultado["curso_actual"]
                .str.lower()
                .str.contains(buscar_curso_deseado.strip().lower(), regex=False)
            ]

        if buscar_curso_actual.strip():
            resultado = resultado[
                resultado["curso_deseado"]
                .str.lower()
                .str.contains(buscar_curso_actual.strip().lower(), regex=False)
            ]

        if resultado.empty:
            st.info(
                "No hay nadie todavía con ese pedido. "
                "¿Querés publicar el tuyo para que te encuentren cuando aparezca alguien?"
            )
        else:
            st.success(f"Se encontraron {len(resultado)} pedido(s):")
            for _, row in resultado.iterrows():
                with st.expander(f"{row['nombre']} — {row['materia']}"):
                    st.markdown(f"**Curso actual:** {row['curso_actual']}")
                    st.markdown(f"**Curso deseado:** {row['curso_deseado']}")
                    st.markdown(f"**Género:** {row['genero']}")
                    st.markdown(f"**Mail:** {row['mail']}")
                    if row["telefono"]:
                        st.markdown(f"**Teléfono:** {row['telefono']}")
                    st.markdown(
                        f"**Publicado:** {row['fecha']} — Vence: {str(row['vencimiento'])[:16]}"
                    )

st.divider()
st.markdown("""
<div class="section-head">
    <div class="section-icon">📋</div>
    <div class="section-title-wrap">
        <h2>Cargar mi pedido de cambio</h2>
        <div class="section-accent"></div>
    </div>
</div>
""", unsafe_allow_html=True)

materia_sel = st.selectbox(
    "Materia",
    [_PLACEHOLDER_MATERIA] + MATERIAS,
    key="cargar_materia",
)
materia = "" if materia_sel == _PLACEHOLDER_MATERIA else materia_sel

with st.form("form_pedido"):
    nombre = st.text_input("Nombre")

    col_padron, col_iniciales = st.columns([2, 1])
    with col_padron:
        padron = st.text_input("Padrón")
    with col_iniciales:
        iniciales = st.text_input("Iniciales de tu nombre (ej: JP)")

    col_mail, col_tel = st.columns([3, 2])
    with col_mail:
        mail = st.text_input("Mail")
    with col_tel:
        telefono = st.text_input("Teléfono (opcional)")

    col_actual, col_deseado = st.columns(2)
    with col_actual:
        if materia in CURSOS_POR_MATERIA:
            curso_actual_sel = st.selectbox(
                "Curso actual",
                [_PLACEHOLDER_CURSO] + CURSOS_POR_MATERIA[materia],
                key="ca_sel",
            )
            curso_actual = "" if curso_actual_sel == _PLACEHOLDER_CURSO else curso_actual_sel
        else:
            curso_actual = st.text_input(
                "Curso actual (tal como figura en SIU-Guaraní)",
                key="ca_txt",
            )
    with col_deseado:
        if materia in CURSOS_POR_MATERIA:
            curso_deseado_sel = st.selectbox(
                "Curso deseado",
                [_PLACEHOLDER_CURSO] + CURSOS_POR_MATERIA[materia],
                key="cd_sel",
            )
            curso_deseado = "" if curso_deseado_sel == _PLACEHOLDER_CURSO else curso_deseado_sel
        else:
            curso_deseado = st.text_input(
                "Curso deseado (tal como figura en SIU-Guaraní)",
                key="cd_txt",
            )

    genero = st.selectbox(
        "Género", ["Prefiero no decir", "Femenino", "Masculino", "Otro"]
    )
    acepto = st.checkbox(
        "Acepto que mis datos de contacto sean visibles para otros usuarios que busquen cambio de curso"
    )

    enviado = st.form_submit_button("📨 Enviar mi pedido de cambio", use_container_width=True)

    if enviado:
        if (
            not nombre
            or not padron
            or not iniciales
            or not mail
            or not materia
            or not curso_actual
            or not curso_deseado
        ):
            st.error("Por favor completá todos los campos obligatorios (incluida materia y curso).")
        elif not padron.strip().isdigit():
            st.error("El Padrón debe contener solo números.")
        elif not acepto:
            st.error("Debés aceptar que tus datos sean visibles para continuar.")
        else:
            df = cargar_datos()
            fecha = datetime.now()
            vencimiento = fecha + timedelta(days=DIAS_VENCIMIENTO)
            nueva_fila = pd.DataFrame([{
                "padron": padron.strip(),
                "iniciales": iniciales.strip().upper(),
                "nombre": nombre,
                "mail": mail,
                "telefono": telefono,
                "materia": materia,
                "curso_actual": curso_actual,
                "curso_deseado": curso_deseado,
                "genero": genero,
                "fecha": fecha.strftime("%Y-%m-%d %H:%M"),
                "vencimiento": vencimiento.strftime("%Y-%m-%d %H:%M"),
                "activo": True,
            }])
            df = pd.concat([df, nueva_fila], ignore_index=True)
            df.to_csv(ARCHIVO, index=False)
            st.success(
                "¡Pedido enviado! Para darte de baja cuando quieras, usá tu Padrón e Iniciales."
            )
            with st.container(border=True):
                st.markdown("**Resumen de tu pedido:**")
                st.markdown(f"- **Nombre:** {nombre}")
                st.markdown(f"- **Materia:** {materia}")
                st.markdown(f"- **Curso actual:** {curso_actual}")
                st.markdown(f"- **Curso deseado:** {curso_deseado}")
                st.markdown(f"- **Mail:** {mail}")
                if telefono:
                    st.markdown(f"- **Teléfono:** {telefono}")

st.divider()
st.markdown("""
<div class="section-head">
    <div class="section-icon">🗑️</div>
    <div class="section-title-wrap">
        <h2>Dar de baja mi pedido</h2>
        <div class="section-accent"></div>
    </div>
</div>
""", unsafe_allow_html=True)

with st.form("form_baja"):
    col_bp, col_bi = st.columns(2)
    with col_bp:
        baja_padron = st.text_input("Padrón")
    with col_bi:
        baja_iniciales = st.text_input("Iniciales de tu nombre")
    baja = st.form_submit_button("🗑️ Dar de baja", use_container_width=True)

    if baja:
        if not baja_padron.strip() or not baja_iniciales.strip():
            st.error("Ingresá tu Padrón e Iniciales.")
        else:
            df = cargar_datos()
            mask = (
                (df["padron"].astype(str) == baja_padron.strip())
                & (df["iniciales"].str.upper() == baja_iniciales.strip().upper())
                & (df["activo"] == True)
            )
            if mask.sum() == 0:
                st.error(
                    "No se encontró un pedido activo con ese Padrón e Iniciales. "
                    "Revisá que no haya espacios de más o errores de tipeo."
                )
            else:
                df.loc[mask, "activo"] = False
                df.to_csv(ARCHIVO, index=False)
                st.success("Tu pedido fue dado de baja correctamente.")

st.markdown(f"""
<div class="fiuba-footer">
    <div class="footer-brand">
        {LOGO_SM}
        <span>Facultad de Ingeniería / Universidad de Buenos Aires</span>
    </div>
    <div class="footer-contact">
        ¿Necesitás ayuda? <a href="mailto:mcaffoz@fi.uba.ar">Contactanos</a>
    </div>
</div>
""", unsafe_allow_html=True)
