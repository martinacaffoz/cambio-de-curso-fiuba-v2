analysis/
These scripts reproduce the analysis methodology described in the project report, using synthetic example data.

The real source data — a WhatsApp group-chat export and SIU-Guaraní course records — cannot be published for privacy and institutional-access reasons respectively. The synthetic datasets are designed to mirror the structure and approximate proportions of the real data so that the classification and filtering logic can be read, run, and verified independently. Because these are synthetic datasets, the percentages produced by running these scripts (e.g. ~19 % for WhatsApp, ~55 % for SIU) are illustrative of the methodology only and are not expected to exactly match the specific figures reported in the PDF (19.25 % and 64.29 %), which were calculated from the real, non-published data.

Scripts
whatsapp_analysis.py
Generates ~500 example WhatsApp-style messages (~19 % course-change-related) and applies a keyword-based classifier to identify which messages are about "cambio de curso" requests. Prints total messages, identified messages, and the percentage.

siu_analysis.py
Uses the real materia names from materias_cursos.json (public information) paired with synthetic values for attendance and evaluation-method fields. Applies the same two-condition relevance criteria used in the report (attendance is taken and evaluation method differs between cursos) to classify each materia, then prints summary counts and per-materia results.

Running
python analysis/whatsapp_analysis.py
python analysis/siu_analysis.py

No external dependencies — both scripts use only the Python standard library.
