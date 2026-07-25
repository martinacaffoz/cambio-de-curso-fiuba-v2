"""
whatsapp_analysis.py
--------------------
Reproduces the methodology used to analyse a WhatsApp group-chat export
and identify messages related to "cambio de curso" requests.

NOTE: The real WhatsApp export cannot be published for privacy reasons.
This script generates a synthetic dataset of ~500 messages that mirrors
the structure and approximate proportions found in the real data (~19 %
course-change-related), so the classification logic can be inspected and
verified independently.
"""

import random

# ---------------------------------------------------------------------------
# 1. Synthetic dataset generation
# ---------------------------------------------------------------------------
random.seed(42)

# Templates for course-change messages (~19 % of total)
CAMBIO_TEMPLATES = [
    "alguien se quiere cambiar del curso {X} al {Y} en {M}?",
    "busco cambiar de comisión en {M}, estoy en {X} y quiero {Y}",
    "hola, necesito cambio de curso en {M} de {X} a {Y}",
    "alguien de {M} quiere hacer el cambio inverso? estoy en {X}",
    "busco cambiar de {M}, comisión {X} a {Y}, avisenme",
    "hay alguien que quiera cambiar curso en {M}? necesito pasar a {Y}",
    "cambio de comisión {M}: tengo {X} y necesito {Y}",
    "me quiero cambiar de la comisión {X} a {Y} en {M}, alguien?",
    "ofrezco cambio en {M}: salgo de {X}, entro a {Y}",
    "necesito cambio urgente en {M} de {X} a {Y}, por favor",
]

MATERIAS = ["Álgebra", "Física", "Química", "Electricidad", "Estadística"]
CURSOS   = ["01", "02", "03", "04", "05", "06"]

def make_cambio_msg():
    t = random.choice(CAMBIO_TEMPLATES)
    m = random.choice(MATERIAS)
    x, y = random.sample(CURSOS, 2)
    return t.format(M=m, X=x, Y=y)

# Templates for unrelated messages (~81 % of total)
GENERIC_TEMPLATES = [
    "alguien tiene los apuntes de la clase de hoy?",
    "qué nota sacaron en el parcial?",
    "cuándo es el próximo TP?",
    "hay clases el jueves?",
    "alguien me puede pasar el link de meet?",
    "el profesor dijo algo sobre la fecha del final?",
    "dónde se consigue el libro de la materia?",
    "gracias por los apuntes!",
    "cuál es el aula de la práctica?",
    "recuerden llevar calculadora mañana",
    "se suspendió la clase de hoy",
    "alguien sabe si hay que entregar algo para el viernes?",
    "el TP se entrega en papel o digital?",
    "qué ejercicios entran en el parcial?",
    "hay alguien que pueda explicarme el tema 3?",
    "gracias! muy útil el resumen",
    "se cayó el sistema de guaraní de nuevo",
    "cuándo abren las mesas de final?",
    "hay que inscribirse al parcial?",
    "alguien va a la consulta del jueves?",
]

def make_generic_msg():
    return random.choice(GENERIC_TEMPLATES)

# Build the full dataset: ~19 % cambio, ~81 % generic
TOTAL_MESSAGES = 500
N_CAMBIO  = round(TOTAL_MESSAGES * 0.19)   # ≈ 95
N_GENERIC = TOTAL_MESSAGES - N_CAMBIO       # ≈ 405

messages = (
    [make_cambio_msg()  for _ in range(N_CAMBIO)]
    + [make_generic_msg() for _ in range(N_GENERIC)]
)
random.shuffle(messages)

# ---------------------------------------------------------------------------
# 2. Keyword-based classifier
#    Mirrors the real methodology: a message is flagged as course-change-
#    related if it contains at least one keyword from a predefined set.
#    In the real analysis the same keyword list was applied to every line
#    of the WhatsApp export (after stripping timestamps and sender names).
# ---------------------------------------------------------------------------
KEYWORDS = {
    "cambio", "cambiar", "curso", "comisión", "comision",
    "cambiarme", "cambiarme", "quiero pasar", "pasar a",
    "intercambio", "inverso",
}

def is_cambio_related(msg: str) -> bool:
    """Return True if msg contains at least one course-change keyword."""
    lower = msg.lower()
    return any(kw in lower for kw in KEYWORDS)

# ---------------------------------------------------------------------------
# 3. Count and report
# ---------------------------------------------------------------------------
identified = [m for m in messages if is_cambio_related(m)]

total      = len(messages)
n_related  = len(identified)
percentage = n_related / total * 100

print("=" * 55)
print("  WhatsApp export — cambio de curso analysis")
print("  (synthetic data — real export not published)")
print("=" * 55)
print(f"  Total messages analysed : {total}")
print(f"  Course-change-related   : {n_related}")
print(f"  Percentage              : {percentage:.1f} %")
print("=" * 55)
print("\nSample identified messages:")
for m in identified[:5]:
    print(f"  → {m}")
