"""
siu_analysis.py
---------------
Reproduces the methodology used to analyse the SIU-Guaraní course catalogue
and identify materias where a "cambio de curso" is meaningful/relevant.

NOTE: The real SIU records cannot be published (institutional access only).
This script uses the real materia names from materias_cursos.json (which are
public information) paired with synthetic/example values for the fields that
were derived from the actual SIU data, so the analysis logic can be inspected
and verified independently.

Criteria used to define "es_relevante" (mirrors the real report):
  A course-change request is considered relevant for a materia when BOTH of
  the following conditions hold across its available cursos:
    1. Attendance IS taken (toma_asistencia = True) — if no curso records
       attendance, switching doesn't affect the student's standing.
    2. The evaluation method DIFFERS between at least two cursos
       (modalidad_evaluacion varies) — if all cursos evaluate identically,
       changing comisión has no practical impact on the student's grade path.
  A materia with only one curso is never relevant (nothing to change to).
"""

# ---------------------------------------------------------------------------
# 1. Synthetic dataset
#    Columns mirror the real SIU extract:
#      materia            — official name as it appears in the system
#      cantidad_cursos    — number of available cursos/comisiones
#      toma_asistencia    — whether any curso records attendance (bool)
#      modalidad_evaluacion_variable — whether evaluation method differs
#                          across cursos (bool); only meaningful if > 1 curso
#      es_relevante       — derived flag (computed below, not hardcoded)
# ---------------------------------------------------------------------------

DATA = [
    # materia                                                        cursos  asist   modal_var
    {"materia": "ÁLGEBRA LINEAL (CB002)",                            "cantidad_cursos": 22, "toma_asistencia": True,  "modalidad_evaluacion_variable": False},
    {"materia": "DESARROLLO ECONÓMICO (TC011)",                      "cantidad_cursos": 3,  "toma_asistencia": True,  "modalidad_evaluacion_variable": True },
    {"materia": "ECONOMÍA (TC010)",                                  "cantidad_cursos": 3,  "toma_asistencia": False, "modalidad_evaluacion_variable": False},
    {"materia": "ELECTRICIDAD Y MAGNETISMO (CB022)",                 "cantidad_cursos": 10, "toma_asistencia": True,  "modalidad_evaluacion_variable": True },
    {"materia": "ELECTROTECNIA, MÁQUINAS E INSTALACIONES (TB015)",   "cantidad_cursos": 6,  "toma_asistencia": True,  "modalidad_evaluacion_variable": False},
    {"materia": "EQUIPOS Y SISTEMAS PARA AUTOMATIZACIÓN (TB016)",    "cantidad_cursos": 3,  "toma_asistencia": True,  "modalidad_evaluacion_variable": True },
    {"materia": "ESTADÍSTICA APLICADA (TB014)",                      "cantidad_cursos": 3,  "toma_asistencia": True,  "modalidad_evaluacion_variable": True },
    {"materia": "ESTÁTICA Y RESISTENCIA DE MATERIALES (TB011)",      "cantidad_cursos": 5,  "toma_asistencia": True,  "modalidad_evaluacion_variable": False},
    {"materia": "FÍSICA DE LOS SISTEMAS DE PARTÍCULAS (CB020)",      "cantidad_cursos": 14, "toma_asistencia": True,  "modalidad_evaluacion_variable": True },
    {"materia": "GESTIÓN INTEGRAL DE LA CADENA DE VALOR (TA011)",    "cantidad_cursos": 4,  "toma_asistencia": True,  "modalidad_evaluacion_variable": True },
    {"materia": "HIGIENE Y SEGURIDAD (TC003)",                       "cantidad_cursos": 6,  "toma_asistencia": False, "modalidad_evaluacion_variable": False},
    {"materia": "INDUSTRIAS EXTRACTIVAS (TA016)",                    "cantidad_cursos": 2,  "toma_asistencia": True,  "modalidad_evaluacion_variable": False},
    {"materia": "INGENIERÍA AMBIENTAL, SUSTENTABILIDAD (TC004)",     "cantidad_cursos": 3,  "toma_asistencia": True,  "modalidad_evaluacion_variable": True },
    {"materia": "INVESTIGACIÓN OPERATIVA (TA012)",                   "cantidad_cursos": 2,  "toma_asistencia": True,  "modalidad_evaluacion_variable": True },
    {"materia": "LEGISLACIÓN Y EJERCICIO PROFESIONAL (TC002)",       "cantidad_cursos": 6,  "toma_asistencia": False, "modalidad_evaluacion_variable": False},
    {"materia": "MATERIALES Y APLICACIONES I (TB012)",               "cantidad_cursos": 1,  "toma_asistencia": True,  "modalidad_evaluacion_variable": False},
    {"materia": "ORGANIZACIÓN Y DIRECCIÓN EMPRESARIA (TA010)",       "cantidad_cursos": 5,  "toma_asistencia": True,  "modalidad_evaluacion_variable": True },
    {"materia": "PRINCIPIOS DE INGENIERÍA INDUSTRIAL (TB010)",       "cantidad_cursos": 3,  "toma_asistencia": True,  "modalidad_evaluacion_variable": False},
    {"materia": "QUÍMICA BÁSICA (CB040)",                            "cantidad_cursos": 10, "toma_asistencia": True,  "modalidad_evaluacion_variable": True },
    {"materia": "SISTEMAS CONTABLES Y GESTIÓN DE COSTOS (TA013)",    "cantidad_cursos": 3,  "toma_asistencia": True,  "modalidad_evaluacion_variable": True },
]

# ---------------------------------------------------------------------------
# 2. Apply relevance criteria (mirrors real methodology)
# ---------------------------------------------------------------------------
for row in DATA:
    row["es_relevante"] = (
        row["cantidad_cursos"] > 1
        and row["toma_asistencia"]
        and row["modalidad_evaluacion_variable"]
    )

# ---------------------------------------------------------------------------
# 3. Calculate summary statistics and report
# ---------------------------------------------------------------------------
total_materias       = len(DATA)
multi_curso          = [r for r in DATA if r["cantidad_cursos"] > 1]
relevantes           = [r for r in DATA if r["es_relevante"]]
pct_relevantes       = len(relevantes) / total_materias * 100

print("=" * 60)
print("  SIU-Guaraní catalogue — cambio de curso relevance analysis")
print("  (synthetic data — real SIU records not published)")
print("=" * 60)
print(f"  Total materias analysed          : {total_materias}")
print(f"  Materias with more than 1 curso  : {len(multi_curso)}")
print(f"  Materias with cambio relevante   : {len(relevantes)}")
print(f"  Percentage relevant              : {pct_relevantes:.1f} %")
print("=" * 60)

print("\nMaterias flagged as relevant:")
for r in relevantes:
    print(f"  ✓  {r['materia']}  ({r['cantidad_cursos']} cursos)")

print("\nMaterias NOT relevant (and reason):")
for r in DATA:
    if not r["es_relevante"]:
        if r["cantidad_cursos"] <= 1:
            reason = "solo 1 curso"
        elif not r["toma_asistencia"]:
            reason = "no toma asistencia"
        else:
            reason = "modalidad de evaluación uniforme"
        print(f"  ✗  {r['materia']}  → {reason}")
