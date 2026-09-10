# tests/evaluation/

AI output evaluation harnesses (scoring rubrics, LLM-graded checks, quality thresholds) — distinct from `tests/golden/`'s fixed expected-output datasets; this is the harness that would compare live output *against* those datasets, or apply a rubric where there's no single correct answer.

Empty at `PHASE-0.8` — same reason as `tests/golden/`: no AI runtime exists yet to evaluate.
