# AGENTS.md

Instruções para agentes de código que trabalharem neste repositório.

## O que é

Uma apresentação de slides em HTML único, interativa, para um seminário acadêmico (PUC-SP, TIDD) sobre o cap. 6 de *Semiótica da IA* (Santaella & Cruz, 2026). Ela é projetada em sala e operada ao vivo pelo apresentador. Publicada via GitHub Pages a partir da raiz da `main`.

## Regra principal: edite a fonte, não o build

- **Edite `src/template.html`.** Nunca edite `index.html` à mão.
- Depois de qualquer mudança, rode `python3 build.py` e commite **os dois** arquivos (`src/template.html` e `index.html`).
- O build injeta dois marcadores no template, que precisam continuar aparecendo exatamente uma vez:
  - `/*D3_LIB*/`: substituído por `vendor/d3-7.8.5.min.js`
  - `/*RASTROS_DATA*/`: substituído pelo trecho de `src/rastros-da-cibernetica.html` entre `const TYPES=` e `const byId=` (constantes `TYPES`, `CONTRO`, `N`, `E`)
- `index.html` deve continuar funcionando **offline**, aberto direto do disco (`file://`). Não adicione dependências de CDN, `fetch` de arquivos locais nem módulos ES separados. A única dependência externa tolerada é o Google Fonts, que tem fallback.

## Arquitetura (dentro de `src/template.html`)

- **Palco fixo 1600×900** (`#stage`), escalado via `--s` para caber na janela. Mede e posicione tudo nesse sistema de coordenadas.
- **Slides** são `<section class="slide" data-id="…" data-title="…">`. A ordem no DOM é a ordem da apresentação.
- **Passos**: elementos `.frag` aparecem em sequência. `data-f="n"` fixa o passo de um fragmento. `data-steps="n"` na seção define o total de passos quando há passos sem fragmento visível (animações).
- **Hooks por slide** no objeto `H[data-id]`:
  - `init(s)`: uma vez, na primeira entrada
  - `enter(s)` / `leave(s)`
  - `step(s, n, jump)`: renderiza o estado do passo `n`. **Precisa ser idempotente**: o engine chama com `jump=true` ao voltar ou pular, e aí nada deve animar.
  - `tick(t)`: chamado a cada frame só enquanto o slide está ativo
- **Animações assíncronas** usam tokens de geração em `G[chave]` para serem canceladas ao trocar de passo. Siga o padrão de `typeText(el, txt, speed, g, key)`.
- **Console**: `tc(name, args)` registra uma ação como `<tool_call>`, `conLog(html, cls)` escreve uma linha, e os comandos ficam em `runCmd`. Toda nova interação relevante deve chamar `tc(...)`, porque o console encena o harness, que é parte do argumento da apresentação.
- **Notas do apresentador**: objeto `NOTES[data-id]`.
- **Modo curto**: o array `SHORT` (lista de `data-id`) define a versão curta, ativada pelo comando `short` e desfeita por `full`. A navegação segue `order()`; ao renomear ou remover um slide, atualize `SHORT`.

## Estética

- Terminal / matrix: fundo `--bg` preto, grade neon, fontes monoespaçadas (`--mono`, `--disp`).
- Cores: `--g` verde (padrão), `--c` ciano, `--y` amarelo (citações), `--m` magenta, `--r` vermelho (erros).
- **Magenta tem significado**: marca as contribuições do apresentador (selo `// leitura do apresentador`, classe `.mine`) e os nós "este seminário" no grafo. Não use magenta como decoração.
- Títulos de slide são comandos: `<h1 class="cmd">`.
- Atenção: a classe `.cur` é o cursor piscante global. Não reutilize esse nome para outra coisa.

## Conteúdo acadêmico

- Citações diretas são **literais** do fichamento do autor e trazem página no formato `(Autor, ano, p. X)`. Não parafraseie dentro de aspas nem invente páginas.
- Distinga sempre a voz da Santaella & Cruz das leituras do apresentador (selo magenta).
- Referências em ABNT, no slide `refs`. Autores citados apenas via apud não entram na lista.

## Verificação

Antes de commitar, abra `index.html` num navegador (ou Playwright/Chromium headless), percorra todos os slides e passos com `→` e `←` e confirme que não há erros no console nem texto sobreposto ao rodapé, onde ficam o console (canto inferior esquerdo) e a barra de progresso (canto inferior direito).
