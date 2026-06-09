---
title: Federation Template — Creating new Living Libraries
aliases:
- Federation template
- New library template
created: '2026-06-10'
updated: '2026-06-10'
type: runbook
status: active
area: ops
subarea: library-governance
knowledge_layer: compiled-wiki
tags:
- template
- federation
- living-library
confidence: high
---
# BMO Living Library — Federation Template

Este directorio contiene los archivos mínimos necesarios para crear una nueva Living Library
federada para otro dominio (FRAME/VideoEdit, Homestead, GameDev, Finance, etc.).

## Cómo crear una nueva biblioteca

```bash
# 1. Crear directorio
mkdir -p ~/.hermes/libraries/<nombre>/

# 2. Copiar estos archivos
cp ~/.hermes/libraries/bmo-ops/SCHEMA.md ~/.hermes/libraries/<nombre>/
cp ~/.hermes/libraries/bmo-ops/AGENTS.md ~/.hermes/libraries/<nombre>/
cp ~/.hermes/libraries/bmo-ops/scripts/lint_library.py ~/.hermes/libraries/<nombre>/scripts/
cp ~/.hermes/libraries/bmo-ops/scripts/lint_editorial_karpathy.py ~/.hermes/libraries/<nombre>/scripts/
cp ~/.hermes/libraries/bmo-ops/scripts/build_knowledge_map.py ~/.hermes/libraries/<nombre>/scripts/
cp ~/.hermes/libraries/bmo-ops/scripts/librarian_weekly.py ~/.hermes/libraries/<nombre>/scripts/

# 3. Crear estructura inicial
mkdir -p ~/.hermes/libraries/<nombre>/{wiki/{Mapas,Areas,Runbooks,Decisions,Failures,Concepts,Outputs,Claims,Contradictions,Logs,Inbox},raw,scripts}

# 4. Personalizar SCHEMA.md con el área específica

# 5. Crear index.md, README.md, state.md, log.md iniciales

# 6. git init && git add -A && git commit -m "Initial commit"
```

## Archivos requeridos por biblioteca

| Archivo | Función |
|---------|---------|
| `SCHEMA.md` | Taxonomía, frontmatter, reglas de la biblioteca |
| `AGENTS.md` | Reglas para agentes que escriben en la biblioteca |
| `README.md` | Descripción humana |
| `index.md` | Índice raíz (apunta a wiki/Index.md) |
| `state.md` | Estado actual + checklist de fases |
| `log.md` | Log cronológico de operaciones |
| `wiki/Index.md` | Índice principal de la wiki |
| `wiki/Knowledge Map.md` | Mapa de conocimiento (auto-generado) |
| `wiki/Mapas/` | Mapas humanos de navegación |
| `wiki/Areas/` | Páginas de dominio |
| `wiki/Runbooks/` | Procedimientos |
| `wiki/Decisions/` | Decisiones tomadas |
| `wiki/Failures/` | Lecciones aprendidas |
| `wiki/Outputs/` | Informes y síntesis |

## Scripts compartidos (simlinks recomendados)

```bash
# En lugar de copiar, crear symlinks a los scripts de bmo-ops:
ln -s ~/.hermes/libraries/bmo-ops/scripts/lint_library.py scripts/
ln -s ~/.hermes/libraries/bmo-ops/scripts/lint_editorial_karpathy.py scripts/
ln -s ~/.hermes/libraries/bmo-ops/scripts/build_knowledge_map.py scripts/
# El librarian_weekly.py debe ser específico de cada biblioteca
```

## Bibliotecas candidatas a federación

| Dominio | Ruta sugerida | Estado |
|---------|---------------|--------|
| FRAME/VideoEdit | `~/.hermes/libraries/frame-videoedit/` | Planificar |
| BMO Homestead | `~/.hermes/libraries/bmo-homestead/` | Planificar |
| GameDev / Neon Crusade | `~/.hermes/libraries/neon-crusade/` | Planificar |
| BMO Finanzas | `~/.hermes/libraries/bmo-finanzas/` | Planificar |
| WebDev / STANDARDIEGO | `~/.hermes/libraries/standariego/` | Planificar |
