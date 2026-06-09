---
title: "Runbook — Ecosystem: Scout, Librarian, Oracle, Architect"
aliases:
- Ecosystem integration
- Scout Librarian Oracle Architect
created: '2026-06-10'
updated: '2026-06-10'
type: runbook
status: active
area: bmo-ops
subarea: living-library-ops
knowledge_layer: compiled-wiki
canonical_status: curated_output
tags:
- scout
- librero
- relic
- autonomous
- living-library
- ecosystem
- integration
related:
- '[[../Concepts/scout-librarian-oracle-architect-architecture]]'
- '[[knowledge-lifecycle]]'
- '[[scout-coyote-swarm]]'
- '[[oracle-pattern-review]]'
confidence: high
---

# Ecosistema BMO — Integración Scout → Librero → Relic → Autonomous

## Los 4 especialistas y la Living Library

```
                    ┌──────────────────┐
                    │   LIVING LIBRARY  │
                    │  (conocimiento    │
                    │   estructurado)    │
                    └──────┬───────┬────┘
                           ↑       ↑
              ┌────────────┘       └────────────┐
              │                                 │
    ┌─────────┴──────────┐          ┌──────────┴──────────┐
    │      SCOUT          │          │      LIBRERO        │
    │  (coyote multi-     │          │  (Wan Shi Tong —     │
    │   frente: señales   │──────────│   curador silencioso)│
    │   externas → inbox) │  inbox   │                      │
    └─────────────────────┘          └──────────┬───────────┘
                                                │
                               ┌────────────────┼────────────────┐
                               ↓                ↓                ↓
                    ┌──────────┴──────┐ ┌──────┴──────┐ ┌───────┴───────┐
                    │     RELIC       │ │ AUTONOMOUS  │ │   BMO (chat)  │
                    │ (oráculo longi- │ │ (arquitecto │ │ (respuestas   │
                    │  tudinal: patro-│ │ de mejora:  │ │  informadas)  │
                    │  nes → gates)   │ │ propuestas) │ │               │
                    └─────────────────┘ └─────────────┘ └───────────────┘
```

## Scout → Living Library

**Scout encuentra señales externas.** Su trabajo es ser un coyote multi-frente que rastrea fuentes (RSS, web, GitHub, YouTube, Reddit, OpenTabs) y clasifica señales por utilidad temporal.

**Flujo:**
1. Scout detecta una señal
2. La clasifica según la escalera: `raw_silencioso` → `knowledge_candidate` → `oportunidad_autonomous` → `alert_user`
3. Las señales `knowledge_candidate` se depositan en `wiki/Inbox/` de la Living Library
4. Las señales `raw_silencioso` se registran en logs internos de Scout, no en la Library
5. Las `alert_user` van por Telegram solo si son urgentes

**Regla:** Scout NUNCA escribe directamente en `wiki/Areas/`, `wiki/Runbooks/`, `wiki/Decisions/` o `wiki/Claims/`. Solo en `wiki/Inbox/` o `wiki/Outputs/` con `canonical_status: raw_signal`.

_Ver: [[scout-coyote-swarm]], [[../Decisions/signal-delivery-ladder]]_

## Librero → Curador de la Living Library

**El Librero es Wan Shi Tong:** no caza, no actúa. Solo organiza el conocimiento. Su trabajo es silencioso: curar, deduplicar, detectar contradicciones, absorber outputs, mantener la integridad editorial.

**Tareas semanales (cron domingo 12:00):**
1. Ejecuta `lint_editorial_karpathy.py` — detecta frontmatter roto, canonical faltante
2. Reconstruye `Knowledge Map` desde frontmatter
3. Detecta contradicciones entre claims con `detect_contradictions.py`
4. Encuentra claims expiradas y las marca para revisión
5. Detecta outputs sin absorber tras 14 días
6. Hace `git commit` con los cambios
7. Reporta a the user SOLO si hay decisiones necesarias

**El Librero NO hace:**
- Escribir en Obsidian, FRAME, Mnemosyne, Stash
- Modificar config, crons, gateway, modelos
- Tomar decisiones unilaterales sobre claims en conflicto
- Notificar a the user por cada minucia

_Ver: [[knowledge-lifecycle]], cron `<your-cron-id>`_

## Relic → Patrones longitudinales desde la Library

**Relic detecta patrones a lo largo del tiempo.** No mira señales individuales — mira tendencias: ¿qué decisiones se repiten? ¿qué fallos son recurrentes? ¿qué claims se contradicen sistemáticamente?

**Flujo:**
1. Relic lee la Living Library (read-only): claims, failures, decisions, outputs
2. Detecta patrones cross-session: mismos errores, decisiones revertidas, claims que cambiaron de confidence
3. Propone gates: "antes de hacer X, verifica que no estés repitiendo el failure Y"
4. Deposita hallazgos en `wiki/Promotions/relic-pattern-review-manifest.md`

**Regla:** Relic no modifica la Library directamente. Sus hallazgos van a `wiki/Inbox/relic/` para que el Librero los promueva.

_Ver: [[oracle-pattern-review]], [[scout-to-oracle-notes]]_

## Autonomous Drive → Propuestas desde la Library

**Autonomous es el arquitecto de mejora.** Lee el estado actual de la Library (gaps, claims pendientes, failures sin resolver) y propone acciones concretas: ¿falta un runbook? ¿hay que actualizar una decisión? ¿un failure revela un bug que hay que arreglar?

**Flujo:**
1. Autonomous lee la Living Library: gaps, preguntas abiertas, claims `medium`/`low`, failures
2. Cruza con el estado real del sistema (config, skills, memoria)
3. Propone mejoras: nuevas skills, runbooks, decisiones, correcciones
4. Deposita propuestas en `wiki/Inbox/relic/` o crea tarjetas Kanban (solo si the user autoriza)

**Regla:** Autonomous NUNCA ejecuta cambios sin aprobación. Solo propone.

## Estados de la integración

| Especialista | Cron/Trigger | Output | ¿Autónomo? |
|-------------|-------------|--------|------------|
| **Scout** | Diario (coyote swarm) | `wiki/Inbox/`, señales raw | ✅ Sí — solo lectura externa |
| **Librero** | Semanal (domingo 12:00) | Lint + claims + git | ✅ Sí — solo escribe en Library |
| **Relic** | Bajo demanda / semanal | `wiki/Inbox/relic/` | ✅ Sí — solo lectura + propuesta |
| **Autonomous** | Bajo demanda | `wiki/Inbox/`, Kanban | ⚠️ Propone, no ejecuta |

## Verificación de salud del ecosistema

```bash
# ¿Está el Librero funcionando?
hermes cronjob list | grep librarian

# ¿Está la Library sana?
python3 ~/.hermes/libraries/bmo-ops/scripts/lint_editorial_karpathy.py | python3 -c "import sys,json; d=json.load(sys.stdin); print('OK' if d['ok'] else 'FAIL')"

# ¿Scout está produciendo?
ls ~/.hermes/autonomous-drive/bmo-scout/briefing/morning/

# ¿Relic tiene patrones pendientes?
cat ~/.hermes/libraries/bmo-ops/wiki/Promotions/relic-pattern-review-manifest.md
```

## Navegación humana

- [[../Concepts/scout-librarian-oracle-architect-architecture]]
- [[scout-coyote-swarm]]
- [[knowledge-lifecycle]]
- [[oracle-pattern-review]]
- [[../Decisions/signal-delivery-ladder]]
