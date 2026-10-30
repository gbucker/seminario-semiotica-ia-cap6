# O agenciamento cognitivo entre humano e máquina

Apresentação interativa para um seminário sobre o capítulo 6 de *Semiótica da IA: cognições híbridas entre humano e máquina* (Santaella & Cruz, 2026).

**Gustavo Bonassa Bucker**, doutorando em Tecnologias da Inteligência e Design Digital (PUC-SP). Outubro de 2026. Coautoria híbrida com Claude Opus 5.5.

▶ **[Abrir a apresentação](https://gbucker.github.io/seminario-semiotica-ia-cap6/)**

## Como usar

| Tecla | Ação |
|---|---|
| `→` `espaço` `PageDown` | avança (item por item, depois slide) |
| `←` `PageUp` | volta |
| `F` | tela cheia |
| `N` | notas do apresentador (citações completas e páginas) |
| `O` | índice de slides |
| `:` | console (`goto 7`, `flip`, `help`) |
| `C` | mostra/oculta o console |

**Versão curta:** na abertura, aperte `:` e digite `short`. A apresentação passa a seguir só orquestração → Deleuze & Guattari → Latour → rastros → Murray → causalidade → uso de IA → fim. `full` volta à versão completa.

O `index.html` é um arquivo único e roda offline. Sem internet, só as fontes caem para a monoespaçada do sistema.

## Roteiro

00 abertura · 01 harness · 02 generativa × agêntica · 03 orquestração agêntica · 04 limite da autonomia · 05 Deleuze & Guattari · 06 Latour · 07 rastros da cibernética · 08 Peirce · 09 da extensão à reversão · 10 Murray · 11 agenciamento misto · 12 causalidade · 13 o pássaro em pleno voo · 14 uso de IA · 15 referências · 16 debate

## Estrutura

- `index.html`: a apresentação gerada (é o que o GitHub Pages serve)
- `src/template.html`: fonte editável da apresentação
- `src/rastros-da-cibernetica.html`: página de origem dos dados do grafo do slide 06
- `vendor/d3-7.8.5.min.js`: d3, embutido no build (licença em `vendor/d3-LICENSE`)
- `build.py`: gera `index.html` (`python3 build.py`)
- `ai_usage_log.yaml`: inventário de uso de IA na produção da apresentação (resumido no slide 14)

## Uso de IA

Esta apresentação foi feita em coautoria híbrida com o Claude Opus 5.5 (Anthropic). O inventário completo, etapa por etapa, com o que foi feito pela IA e o que é autoria do apresentador, está em [`ai_usage_log.yaml`](ai_usage_log.yaml).

## Contato

gustavo@gbucker.com
