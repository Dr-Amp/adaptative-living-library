---
title: Índice de Contradicciones
aliases: [Contradictions Index, Knowledge conflicts]
created: '2026-06-10'
updated: '2026-06-10'
type: index
status: active
area: bmo-ops
subarea: living-library-ops
knowledge_layer: human-navigation
tags: [contradictions, curation, integrity]
related:
- '[[Claims/Index]]'
- '[[../Questions/open-questions]]'
confidence: high
---

# Índice de Contradicciones

Las contradicciones son pares de claims o afirmaciones en la biblioteca que parecen inconsistentes entre sí. No son errores — son **señales** de que el conocimiento evolucionó, hay matiz, o una de las afirmaciones está obsoleta.

## Contradicciones activas

| ID | Claim A | Claim B | Estado | Detección |
|----|---------|---------|--------|-----------|
| — | — | — | — | Poblar en próxima pasada del Librero |

## Cómo se detectan

El script `scripts/detect_contradictions.py` compara pares de claims por similitud semántica en el mismo área y marca pares con alta similitud pero confidence divergente como candidatos a contradicción.

## Cómo se resuelven

1. El Librero detecta un par candidato
2. Se crea una entrada en esta página con ambas claims enlazadas
3. Se evalúa: ¿una es obsoleta? ¿Ambas son válidas en contextos distintos? ¿Una tiene confidence incorrecta?
4. Se resuelve: `superseded`, `both_valid`, `old_value_correct`, `new_value_correct`

## Navegación humana

- [[Claims/Index]]
- [[../Questions/open-questions]]
