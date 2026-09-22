# Aula 06 – Programação Assistida por Inteligência Artificial
### Atividades: Leitura orientada, discussão em grupo e estudo de caso

**Texto-base:** *Vibe coding: programming through conversation with artificial intelligence* — Advait Sarkar e Ian Drosos (PPIG 2025)
**Disciplina:** Tendências em Ciência da Computação | Unidade II — Programação Assistida
**Centro Universitário UDF**

---

## 0. Códigos da pesquisa (identificação das evidências)

O artigo de Sarkar e Drosos (2025) analisou uma lista inicial de 35 vídeos do YouTube e Twitch sobre "vibe coding", dos quais **5 vídeos (8h27min)** passaram por análise detalhada completa segundo o framework metodológico (framework analysis). Os códigos usados como identificadores dessas evidências ao longo do artigo — e citados nas respostas deste documento — são:

| Código | Vídeo / Contexto | Plataforma | Duração |
|---|---|---|---|
| **TW1** | *!foony \| VIP \| Vibe Coding \| !idea* — desenvolvimento de funcionalidades exclusivas para membros em site de games já existente | Twitch | 05:30:50 |
| **YT15** | *VIBE CODING with CURSOR – Draw w/ HTML and JS* — criação de diagrama animado explicando o workflow de um agente de código | YouTube | 00:17:45 |
| **YT21** | *Vibe Coding with AI: Watch me fix a chat interface in real-time* — aplicação de chat com base de código integrada ao GitHub | YouTube | 01:29:37 |
| **YT22 / YT22b** | *Vibe Coding Startup Using Most Advanced AI — Phase 1 e 2* — aplicativo web para auxiliar estudantes internacionais em candidaturas a emprego | YouTube | 00:32:05 + 00:37:02 |

Esses quatro códigos (TW1, YT15, YT21, YT22) são as fontes primárias de evidência citadas nas questões norteadoras e no estudo de caso a seguir, conforme a metodologia de **framework analysis** (Ritchie e Spencer, 2002) empregada pelos pesquisadores, que organizou os achados em 9 categorias: goals, intentions, workflow, prompting, debugging, challenges, expertise, trust, e definition and performance.

---

## 1. Trechos/ideias registrados durante a leitura individual

**Trecho 1 — sobre confiança na IA**

O artigo mostra que a confiança na IA durante a "vibe coding" não é um cheque em branco, mas sim algo **granular, dinâmico e contingente**. O programador do vídeo **[YT21]** resume bem essa postura: consegue avançar rapidamente com a IA, mas revisa as mudanças porque isso o ajuda "a permanecer no controle". Já no **[YT22]**, o criador afirma categoricamente que não acredita em "seguir cegamente a IA" e reforça que "IA é apenas uma ferramenta".

**Trecho 2 — sobre expertise**

Um dos achados mais importantes é que a IA não elimina a necessidade de conhecimento técnico — ela **redistribui** essa expertise. Em vez de escrever código linha a linha, o desenvolvedor passa a atuar como diretor, revisor e avaliador, aplicando seu conhecimento para escolher ferramentas, avaliar rapidamente o código gerado ("leitura por varredura/impressionista", Seção 3.5.1 do artigo, exemplificada em **[YT21]** e **[YT15]**) e decidir quando transicionar para o trabalho manual.

---

## 2. Respostas às questões norteadoras

### 2.1 Até que ponto podemos confiar no código produzido pela IA?

O artigo indica que a confiança deve ser **construída por verificação iterativa, não por aceitação em bloco**. Antes de aceitar e usar um código gerado por IA, é importante:

- **Testar a aplicação** na prática (rodar, verificar comportamento real) — estratégia usada em todos os vídeos analisados no estudo (**TW1, YT15, YT21, YT22**).
- **Ler os diffs**, mesmo que rapidamente, buscando padrões, nomes de funções e chamadas de API corretas (leitura "gestalt"/por varredura — **YT21**).
- **Cruzar o código com documentação** e outras partes do sistema, como o desenvolvedor do **[YT21]** fazia ao verificar se a IA usava o endpoint correto.
- **Formular hipóteses e verificar erros** com ferramentas tradicionais (console do navegador, terminal — **YT21, YT22**), em vez de simplesmente colar mensagens de erro de volta para a IA sem entender a causa.

**Riscos de aceitar código sem revisão, testes ou compreensão:**

- Uso de APIs inexistentes (alucinações do modelo);
- Dependências não verificadas;
- Vulnerabilidades de segurança (injeção de SQL, XSS, bibliotecas desatualizadas);
- Código "difícil demais" de manter — como alertado em **[TW1]**, "o vibe coder médio talvez não conseguisse consertar isso";
- Perda de compreensão do próprio sistema, o que compromete manutenção futura.

O guia de boas práticas da UDF reforça esse ponto citando Lee, Goldberg e Kohane (2024): **a responsabilidade legal pelo código aceito é sempre do desenvolvedor**, nunca da ferramenta.

### 2.2 A IA reduz a necessidade de conhecimento em programação ou transforma o tipo de conhecimento necessário?

O artigo é enfático: a IA **transforma**, não elimina, a expertise necessária. Surgem três domínios de conhecimento essenciais:

1. **Expertise técnica tradicional** — necessária para depuração manual, leitura de código e arquitetura de sistemas (o que o guia da UDF classifica como "Liderança Humana": arquitetura, trade-offs, lógica de negócio, segurança).
2. **Expertise em IA** — entender modelos, janelas de contexto, estratégias de prompting e limitações de cada ferramenta.
3. **Expertise de produto** — traduzir metas de negócio em funcionalidades, decidir o que manter ou descartar do que a IA sugere.

O desenvolvedor passa a atuar como **orientador, avaliador e revisor**. Isso exige competências críticas novas: avaliação rápida de qualidade (sem ler linha a linha), formação de hipóteses de causa-e-efeito diante de erros, e saber quando aprofundar a revisão em vez de confiar no julgamento rápido inicial.

### 2.3 Quando é melhor utilizar a IA e quando é melhor assumir o controle manualmente?

Cruzando o artigo com o guia de boas práticas da UDF:

| Delegar à IA | Trabalhar manualmente |
|---|---|
| Código boilerplate, tarefas repetitivas | Arquitetura de sistemas e decisões de trade-off |
| Tarefas onde prompting é mais rápido que digitar | Edições pontuais simples (ex: "autocomplete da IDE é mais rápido que a IA" — **[TW1]**) |
| Geração de testes unitários (casos felizes e de falha) | Lógica de negócio central |
| Documentação e explicação de código legado | Revisão de segurança e ética |
| Exploração inicial/prototipagem (**YT15**) | Depuração de bugs complexos com hipóteses causais profundas (**YT21, YT22**) |

**Critério transversal:** quando o esforço de formular um prompt supera o esforço da edição direta, vale mais a pena editar manualmente (**TW1, YT21**).

---

## 3. Estudo de caso

**Situação:** uma equipe aceita a implementação completa de uma funcionalidade gerada por IA, testada apenas superficialmente, sem revisão de dependências, segurança, manutenibilidade ou impactos em outras partes do sistema.

### Ações recomendadas antes de incorporar o código ao projeto

1. Aplicar o **checklist de QA crítico**: o código faz exatamente o que foi pedido? Há edge cases não tratados? Há vulnerabilidades óbvias? Segue os padrões de estilo do projeto? Está comentado adequadamente?
2. Rodar ferramentas de análise estática/dinâmica (SAST/DAST) e sanitizar dados de entrada.
3. Gerar testes de regressão e cobertura antes de mesclar ao projeto principal.
4. Verificar licenciamento de bibliotecas incluídas (risco de código GPL em produto fechado, por exemplo).
5. Realizar **revisão por pares** — tratar o código da IA com o mesmo rigor (ou maior) que código escrito por humanos.
6. Documentar a justificativa da abordagem escolhida, não apenas descrever o que o código faz.

### Responsabilidades que permanecem humanas

- Decisões de arquitetura de sistemas;
- Avaliação final de segurança;
- Responsabilidade legal pelo commit;
- Julgamento sobre impacto em outras partes do sistema;
- Decisão final de aceitar ou rejeitar o código gerado.

Nenhuma dessas responsabilidades pode ser delegada à IA.

---

## 4. Três boas práticas para a colaboração humano-IA

1. **Nunca aceitar código sem compreendê-lo** — se a IA gerar algo que você não entende totalmente, pare e aprenda antes de prosseguir (princípio da Transparência).
2. **Testar e verificar sempre, nunca confiar cegamente** — validar o comportamento prático do código, não apenas sua aparência.
3. **Separar claramente o papel humano do papel da IA** — arquitetura, trade-offs e decisões críticas de segurança ficam com o humano; código repetitivo/boilerplate pode ser delegado.

---

## 5. Síntese final

> "Programar com IA de maneira responsável não significa apenas saber pedir código; significa também **manter a compreensão ativa sobre o que está sendo construído**, mesmo quando a IA acelera a produção. Significa desenvolver uma nova forma de expertise — a de avaliar rapidamente, questionar resultados e saber quando assumir o controle manual. Significa tratar a confiança como algo que se conquista a cada iteração, por meio de testes e revisão, e não como algo concedido de antemão. Acima de tudo, significa lembrar que a responsabilidade técnica, ética e legal pelo código permanece sempre humana — a IA participa da criação, mas não da prestação de contas."

---

*Documento elaborado com base em: Sarkar, A. & Drosos, I. (2025). Vibe coding: programming through conversation with artificial intelligence. PPIG 2025; e Guia de Boas Práticas na Colaboração Humano-IA (UDF, Prof.ª Kadidja Valéria).*
