# Atividade - Refinamento de Prompts

> **Objetivo:** analisar como o refinamento de prompts pode melhorar a qualidade, clareza e adequação das respostas de uma IA para uma atividade de extensão.

## 📋 Identificação
 **Data:** 10/09/2026
- **Integrantes:**
  - Leandro Alcântara Morais (RGM: 41160291)
  - Leidson Arthur Santana Almeida (RGM: 38222345)
  - Leandro Santos Duque da Silva (RGM: 40456005)
- Ferramenta de IA utilizada: Microsoft Copilot

---

## 🎯 Problema escolhido

### Contexto
Explicar conceitos de programação para alunos da educação básica como parte do Itinerário Extensionista.

### Problema
Como tornar o conceito de Aprendizado de Máquina acessível e empolgante para estudantes do ensino fundamental II e médio.

### Objetivo
Produzir uma explicação clara, didática e motivadora sobre Aprendizado de Máquina, usando analogias simples, exemplos do cotidiano e pequenos trechos de código ilustrativos.

---

## 🤖 Prompt 1

### Prompt
```
Explique o que é aprendizado de máquina.
```

### Resultado
Vamos começar com um conceito bem fundamental: variáveis.
🔑 O que é uma variável?
Uma variável é como uma “caixa” onde você guarda informações para usar depois.
•  Imagine que você tem uma caixa com uma etiqueta chamada idade.
•  Dentro dela, você coloca o número 25.
•  Sempre que precisar saber a idade, você olha dentro dessa caixa.
Em programação, isso seria escrito assim (em Python, por exemplo):

```python
idade = 25
```
Aqui:
•  idade é o nome da variável (a etiqueta da caixa).
•  = significa que você está atribuindo um valor.
•  25 é o valor guardado.
📦 Por que isso é útil?
•  Você pode mudar o valor sem precisar reescrever tudo.
•  Pode usar a mesma variável em cálculos, comparações ou exibir na tela.
Exemplo:

```python
idade = 25
print("Minha idade é", idade)

idade = idade + 1
print("Agora tenho", idade, "anos")
```
Saída:

```text
Minha idade é 25
Agora tenho 26 anos
```
✨ Pensando de forma simples
Variáveis são como apelidos para valores. Em vez de escrever o número 25 em todo lugar, você usa o nome idade. Isso deixa o código mais organizado e fácil de entender.

### Análise
- Funcionou: trouxe uma definição básica.
- Faltou: público-alvo, exemplos do cotidiano, linguagem acessível.
- Ficou genérico: não houve analogias.
- Poderia ser melhor: incluir contexto, público e formato estruturado.

---

## 🔧 Prompt 2 — Primeiro refinamento

  Atue como estudante de Sistema da Informação da UDF no 6° semestre da graduação

Você devera explicar um conceito de programação para alunos da educação básica com objetivo de realizar o Itinerário Extensionista

Apresente:
1. uma definição;
2. como funciona;
3. três exemplos de aplicações no cotidiano;
4. uma comparação entre aprendizado supervisionado
   e não supervisionado.

Utilize linguagem acessível e limite a resposta
a aproximadamente 500 palavras.

### Resultado
1. O que é (Definição)
Aprendizado de Máquina é como ensinar um computador a aprender sozinho. Imagine uma criança que vê várias vezes um cachorro e um gato. No começo, ela não sabe diferenciar. Mas, depois de ouvir várias vezes “isso é um gato” ou “isso é um cachorro”, ela começa a reconhecer sozinha. O computador faz algo parecido: aprende com exemplos.

2. Como funciona
O processo é como treinar para um jogo:

O computador recebe muitos exemplos (dados).

Ele analisa e procura padrões.

Testamos para ver se aprendeu.

Se erra, ajustamos e ele melhora.

Assim, ele vai ficando cada vez mais “experiente”.

3. Machine Learning no seu dia a dia

O feed do TikTok ou Instagram aprende o que você gosta e mostra mais vídeos parecidos.

A Netflix recomenda filmes e séries com base no que você já assistiu.

O corretor de texto do celular sugere palavras porque aprendeu como você escreve.

4. Aprendizado Supervisionado vs. Não Supervisionado

Supervisionado: é como estudar com um professor. Você faz exercícios e ele corrige, mostrando o que está certo ou errado. O computador aprende com dados que já têm respostas.

Não supervisionado: é como brincar sozinho de separar objetos. Você não sabe os nomes, mas percebe que alguns são redondos e outros quadrados. O computador organiza os dados sem respostas prontas, apenas pelos padrões que encontra.

---

## 📊 Comparação

| Critério | Prompt 1 | Prompt 2 |
| ------------------------- | ---------: | ---------: |
| Clareza | 3 | 5 |
| Precisão | 3 | 4 |
| Relevância | 3 | 5 |
| Organização | 2 | 5 |
| Adequação ao público | 2 | 5 |
| Atendimento ao objetivo | 3 | 5 |

---

## 🚀 Prompt 3 — Segundo refinamento

Atue como um estudante de Sistemas de Informação da UDF, cursando o 6º semestre da graduação. Você está desenvolvendo uma atividade para o Itinerário Extensionista.

Seu objetivo é explicar o conceito de Aprendizado de Máquina (Machine Learning) para alunos da educação básica (ensino fundamental II / médio). O tom deve ser empolgante, didático, acolhedor e totalmente livre de jargões técnicos complexos. Sempre que usar um termo técnico, explique-o com uma metáfora simples.

Apresente a resposta dividida estritamente nos seguintes tópicos:

1. O que é (Definição): Explique como se fosse uma criança aprendendo a reconhecer objetos, usando uma metáfora divertida.
2. Como funciona: Mostre o passo a passo como se fosse um treino esportivo ou um jogo de videogame.
3. Machine Learning no seu dia a dia: Traga três exemplos práticos que os alunos conhecem bem (TikTok/Instagram, Netflix, celular com corretor de texto ou filtros de foto).
4. Aprendizado Supervisionado vs. Não Supervisionado: Compare com situações escolares (professor corrigindo exercícios vs. aluno organizando objetos sozinho).

Restrições: limite de aproximadamente 500 palavras, frases curtas, linguagem acessível e tom motivador.

### Resultado
1. O que é (Definição)
Aprendizado de Máquina é como ensinar um computador a aprender sozinho. Imagine uma criança que vê várias vezes um cachorro e um gato. No começo, ela erra. Mas, depois de ouvir “isso é um gato” ou “isso é um cachorro”, ela começa a acertar. O computador faz o mesmo: aprende com exemplos até reconhecer sozinho.

2. Como funciona
Funciona como treinar para um jogo de videogame:

O computador recebe muitos exemplos, como fases do jogo.

Ele pratica e tenta descobrir padrões.

Testamos para ver se aprendeu.

Se erra, ele ajusta e joga de novo.
Com o tempo, fica cada vez melhor, como um jogador que treina até dominar o jogo.

3. Machine Learning no seu dia a dia

O TikTok ou Instagram aprendem o que você gosta e mostram mais vídeos parecidos.

A Netflix recomenda séries e filmes com base no que você já assistiu.

O celular sugere palavras ou aplica filtros de foto porque aprendeu com o seu jeito de escrever e com as imagens que reconhece.

4. Aprendizado Supervisionado vs. Não Supervisionado

Supervisionado: é como ter um professor corrigindo seus exercícios. Você aprende com as respostas certas e erradas. O computador também aprende com dados que já têm respostas.

Não supervisionado: é como quando você organiza objetos sozinho. Você não sabe os nomes, mas percebe que alguns são redondos e outros quadrados. O computador faz o mesmo: agrupa dados sem respostas prontas, apenas pelos padrões que encontra.
📌 **Exemplo em código (supervisionado):**
```python
# Lista de imagens já identificadas
dados = [
    ("imagem1.jpg", "gato"),
    ("imagem2.jpg", "cachorro"),
    ("imagem3.jpg", "gato"),
]

# O computador "aprende" com os exemplos
for imagem, etiqueta in dados:
    print("Aprendendo que", imagem, "é um", etiqueta)
```

---

**3. Machine Learning no seu dia a dia**
- O TikTok ou Instagram aprendem o que você gosta e mostram mais vídeos parecidos.
- A Netflix recomenda séries e filmes com base no que você já assistiu.
- O celular sugere palavras ou aplica filtros de foto porque aprendeu com o seu jeito de escrever e com as imagens que reconhece.

📌 **Exemplo em código (recomendação simples):**
```python
# O aluno assistiu a dois filmes
assistidos = ["Filme de ação", "Filme de aventura"]

# O sistema sugere algo parecido
if "Filme de ação" in assistidos:
    print("Sugestão: Você pode gostar de 'Missão Impossível'")
```

---

**4. Aprendizado Supervisionado vs. Não Supervisionado**
- **Supervisionado:** é como ter um professor corrigindo seus exercícios. Você aprende com as respostas certas e erradas. O computador também aprende com dados que já têm respostas.
- **Não supervisionado:** é como quando você organiza objetos sozinho. Você não sabe os nomes, mas percebe que alguns são redondos e outros quadrados. O computador faz o mesmo: agrupa dados sem respostas prontas, apenas pelos padrões que encontra.

📌 **Exemplo em código (não supervisionado):**
```python
# Lista de objetos sem nome
objetos = ["⚽", "🟦", "🏀", "⬛"]

# O computador tenta separar por formato
grupo_redondo = ["⚽", "🏀"]
grupo_quadrado = ["🟦", "⬛"]

print("Grupo redondo:", grupo_redondo)
print("Grupo quadrado:", grupo_quadrado)
```

---

## 📊 Comparação final

| Critério | Prompt 1 | Prompt 2 | Prompt 3 |
| ------------------------- | ---------: | ---------: | ---------: |
| Clareza | 3 | 5 | 5 |
| Precisão | 3 | 4 | 5 |
| Relevância | 3 | 5 | 5 |
| Organização | 2 | 5 | 5 |
| Adequação ao público | 2 | 5 | 5 |
| Atendimento ao objetivo | 3 | 5 | 5 |
| Utilidade prática | 3 | 5 | 5 |
| **Total** | 19 | 34 | 35 |

---

## ✅ Validação

Checklist aplicado:
- Conceitos corretos e confirmáveis.
- Termos técnicos reais (supervisionado e não supervisionado).
- Sem dados inventados.
- Faltaram referências explícitas.
- Simplificações aceitáveis para o público.
- Resposta clara e reexplicável.

---

## 💭 Reflexão Individual
1. Qual foi a principal diferença entre o prompt inicial e o prompt refinado?
O inicial era genérico e sem público definido. O refinado trouxe contexto, papel, objetivo e público-alvo, tornando a resposta muito mais direcionada.

2. Quais elementos tiveram maior impacto no resultado?
A definição clara do público (alunos da educação básica) e a exigência de exemplos práticos do cotidiano. Isso mudou totalmente o tom e a utilidade da resposta.

3. Um prompt mais longo necessariamente produz uma resposta melhor? Justifique.
Não. O que importa não é o tamanho, mas a clareza e a relevância das instruções. Um prompt longo pode até atrapalhar se tiver detalhes desnecessários.

4. O que acontece quando o objetivo solicitado à IA não está claramente definido?
A resposta tende a ser genérica, superficial e pouco útil, porque a IA não sabe exatamente o que priorizar.

5. Quais informações você considera indispensáveis para elaborar um bom prompt?

Papel (quem está falando).

Público-alvo.

Objetivo da explicação.

Formato da resposta.

Restrições (como linguagem simples ou limite de palavras).

6. Como o refinamento de prompts pode ser útil para um profissional de Ciência da Computação?
Ajuda a obter respostas mais precisas e aplicáveis, economizando tempo e melhorando a comunicação com sistemas de IA em projetos acadêmicos ou profissionais.

7. Que riscos podem surgir quando confiamos em uma resposta da IA sem avaliar sua qualidade?
Podemos reproduzir informações incorretas, generalizações ou conceitos mal explicados, comprometendo a credibilidade do trabalho.

8. Houve alguma situação em que o Prompt 3 ficou pior que o Prompt 2? Se sim, explique.
Não. O Prompt 3 manteve a clareza do Prompt 2 e adicionou mais empolgação e acolhimento, sem perder precisão.

9. Existe um ponto em que adicionar mais instruções começa a prejudicar a resposta?
Sim. Quando o prompt fica excessivamente detalhado ou confuso, a IA pode se perder ou gerar respostas muito rígidas.

10. O que você faria para verificar se a resposta tecnicamente está correta?
Consultaria livros, artigos acadêmicos ou sites confiáveis sobre aprendizado de máquina, comparando os conceitos apresentados com fontes oficiais.

---

## 💡 Take Away

> Um bom prompt não é simplesmente um prompt longo. Ele precisa ser claro, objetivo e trazer as informações certas para orientar a IA.

---

## ⭐ Cinco recomendações

1. Defina o público-alvo.
2. Explique o objetivo.
3. Use formato estruturado.
4. Inclua restrições úteis.
5. Valide sempre em fontes confiáveis.

---

## 🏁 Desafio final

Cinco perguntas para diagnosticar problemas em prompts:
1. O objetivo estava claro?
2. O público foi definido?
3. O formato foi especificado?
4. Havia restrições úteis?
5. Você validou a resposta?

**Pergunta final:** O problema está no prompt, na resposta da IA, nas informações utilizadas ou na forma como o usuário avaliou o resultado?
