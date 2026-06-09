---
title: Runbook — Ciclo de vida del conocimiento en la Living Library
aliases:
- Knowledge lifecycle
- Ciclo de vida conocimiento
created: '2026-06-10'
updated: '2026-06-10'
type: runbook
status: active
area: bmo-ops
subarea: living-library-ops
knowledge_layer: compiled-wiki
canonical_status: curated_output
tags:
- runbook
- curation
- living-library
- knowledge-lifecycle
related:
- '[[karpathy-hardening]]'
- '[[library-preflight]]'
- '[[Claims/Index]]'
- '[[Contradictions/Index]]'
confidence: high
---

# Ciclo de vida del conocimiento

Cada pieza de conocimiento en la Living Library sigue este ciclo. El objetivo es que nada se pudra: todo output se absorbe, se verifica o se declara obsoleto.

## Las 5 fases

```
INGESTA → CURACIÓN → CONOCIMIENTO → PROMOCIÓN → ARCHIVO
  ↑                                                ↓
  └────────── REVISIÓN PERIÓDICA ←─────────────────┘
```

### Fase 1: INGESTA (fuente → raw)

**Entrada:** Una fuente externa (transcripción, URL, PDF, handoff de agente)  
**Acción:** Se copia a `raw/` con un `.source-card.md` que registra provenance, fecha, licencia  
**Output:** Archivo(s) en `raw/` + entrada en `wiki/Sources.md`  
**Agente:** Scout o import manual  
**Regla:** No más de 5 MB por fuente. Si es más grande, resumir primero.

### Fase 2: CURACIÓN (raw → wiki)

**Entrada:** Fuente(s) en `raw/`  
**Acción:** Se extraen afirmaciones, patrones, decisiones. Se crea un output en `wiki/Outputs/` con frontmatter completo y `canonical_status: curated_output`  
**Output:** Página en `wiki/Outputs/YYYY-MM-DD-*.md`  
**Agente:** Librero o BMO (bajo supervisión)  
**Regla:** Un output debe citar sus fuentes raw. Si no hay fuentes, `confidence: low`.

### Fase 3: CONOCIMIENTO ESTRUCTURADO (output → runbook/decision/failure/claim)

**Entrada:** Output curado con `canonical_status: curated_output`  
**Acción:** Se promueve a tipo canónico:
- Si es un procedimiento repetible → `Runbooks/`
- Si es una decisión tomada → `Decisions/`
- Si es un error del que aprender → `Failures/`
- Si es una afirmación verificable → `Claims/`
- Si es una idea arquitectónica → `Concepts/`

El output original se marca `canonical_status: absorbed` con `absorbed_by: [[../Decisions/signal-delivery-ladder]]`.  
**Agente:** Librero (revisión semanal)  
**Regla:** Un output no debe vivir más de 14 días sin ser absorbido o marcado como `ledger`.

### Fase 4: PROMOCIÓN (wiki → Obsidian)

**Entrada:** Runbook, decisión o concepto marcado `status: verified`  
**Acción:** Se copia a Obsidian (vault de the user) como página curada. En la wiki se marca `promoted: true`.  
**Agente:** the user (humano) o BMO con aprobación explícita  
**Regla:** NUNCA promocionar automáticamente. Requiere aprobación humana.

### Fase 5: ARCHIVO (conocimiento obsoleto)

**Entrada:** Claim expirada, runbook superseded, decisión revocada  
**Acción:** Se marca `status: archived` o `canonical_status: superseded`. Se añade `superseded_by` si hay reemplazo.  
**Agente:** Librero (detección automática) + the user (confirmación)  
**Regla:** Nunca borrar. Todo conocimiento obsoleto se archiva, no se elimina.

## Gatillos automáticos

| Evento | Acción |
|--------|--------|
| Nuevo output sin canonical_status tras 7 días | Librero asigna `curated_output` o `ledger` |
| Claim con `expires` pasada de fecha | Librero marca `status: review` y notifica |
| Contradicción detectada entre claims | Librero crea entrada en `Contradictions/` |
| Output sin absorber tras 14 días | Librero evalúa: ¿promover a runbook/decision o marcar `ledger`? |
| `raw/` supera 80 MB | Librero poda fuentes no referenciadas |

## Ejecución semanal del Librero

```bash
python3 ~/.hermes/libraries/bmo-ops/scripts/librarian_weekly.py
```

Este script:
1. Ejecuta `lint_editorial_karpathy.py`
2. Ejecuta `build_knowledge_map.py`
3. Ejecuta `detect_contradictions.py`
4. Detecta claims expiradas
5. Detecta outputs sin absorber tras 14 días
6. Hace git commit si hay cambios
7. Reporta a the user solo si hay decisiones necesarias

## Navegación humana

- [[karpathy-hardening]]
- [[Claims/Index]]
- [[Contradictions/Index]]
