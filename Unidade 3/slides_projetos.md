# Sistema de Lançamento de Nota Fiscal

## Slide 1 — Visão Geral do Projeto

- Projeto desenvolvido como solução de baixa complexidade orientada a processo.
- Objetivo: acelerar e padronizar o lançamento de notas fiscais.
- O sistema foi pensado para reduzir erros manuais e facilitar o trabalho de usuários e administradores.
- A proposta combina cadastro automatizado, validação de dados e controle de acesso.

---

## Slide 2 — Objetivo do Sistema

- Simplificar o lançamento de notas fiscais em um processo mais rápido e prático.
- Evitar retrabalho com entrada manual de dados.
- Automatizar o cadastro de fornecedores e produtos.
- Gravidade do problema: muitas empresas ainda operam com processos fragmentados e pouco integrados.
- Resultado esperado: maior agilidade, menor erro humano e melhor rastreabilidade.

### Objetivo principal

> Transformar a entrada de dados de notas fiscais em um fluxo mais inteligente, seguro e eficiente.

---

## Slide 3 — Funcionalidades Principais

- Tela de login com diferentes perfis de acesso.
- Administrador: cadastra usuários, define permissões e acessa todas as funções.
- Lançamento da nota por:
  - chave de acesso
  - importação de XML
  - arquivo PDF
  - foto da nota
- Extração automática de informações relevantes da nota.
- Cadastro automático de fornecedor e produtos.
- Edição de dados antes da confirmação final.
- Verificação de duplicidade e consistência de informações.

---

## Slide 4 — Arquitetura do Fluxo de Trabalho

### Fluxo principal

1. Acesso ao sistema via login.
2. Usuário seleciona a forma de entrada da nota.
3. O sistema recebe a nota em XML, PDF ou imagem.
4. Dados são extraídos e estruturados.
5. O sistema identifica fornecedor, produtos e campos relevantes.
6. Dados são validados e comparados com o banco.
7. O usuário revisa e confirma as informações.
8. O registro é salvo e disponibilizado para consultas.

### Visão de arquitetura

- Camada de autenticação e autorização
- Camada de entrada de documentos
- Camada de extração/interpretacão de dados
- Camada de validação e cruzamento de informações
- Camada de persistência de fornecedores, produtos e usuários
- Camada de interface para consulta e manutenção

```text
Login -> Entrada da Nota -> Leitura/Extração -> Validação -> Edição -> Confirmação -> Persistência
```

---

## Slide 5 — Regras de Negócio e Validação

- Cadastro automático do fornecedor com:
  - razão social
  - nome fantasia
  - CNPJ
  - CEP
  - endereço
  - telefone
- Cadastro automático dos produtos com:
  - código
  - descrição
  - NCM
  - unidade de medida
  - quantidade
  - valor unitário
- Verificação se o dado já existe no sistema.
- Identificação de produtos duplicados ou já cadastrados.
- Alerta para correção de inconsistências entre fornecedores.
- Validação cruzada de informações para reduzir erros de cadastro.

---

## Slide 6 — Estrutura da Interface

- Menu principal com acesso às áreas do sistema:
  - cadastro de nota
  - visualização de fornecedores
  - visualização de produtos
  - administração de usuários
- Interface orientada a operação simples e com pouco treinamento.
- Processo visual em etapas, com foco em usabilidade.
- Permite revisão antes do arquivamento final das informações.

### Telas esperadas no projeto

- Login
- Cadastro de nota
- Tela de validação de dados
- Tela de fornecedores
- Tela de produtos
- Administração de usuários

---

## Slide 7 — Aprendizados

- Low code pode acelerar a criação de soluções práticas e úteis.
- O processo de identificação e captura de dados é tão importante quanto a interface.
- A validação cruzada e o controle de qualidade reduzem erros de negócio.
- A organização por perfis de usuário melhora segurança e governança.
- A automação de cadastro reduz trabalho manual e aumenta produtividade.
- A experiência do usuário precisa ser simples, sem perder controle de regras e exceções.

---

## Slide 8 — Próximos Passos

- Integrar com ERP ou sistema de gestão da empresa.
- Melhorar a extração de dados com OCR e inteligência artificial.
- Criar dashboards para acompanhamento de lançamentos e inconsistências.
- Implementar auditoria de alterações e histórico de processos.
- Expandir a validação de dados com regras mais robustas.
- Evoluir a solução para uso em múltiplos usuários e departamentos.
- Adicionar testes automatizados e melhoria contínua da experiência.

---

## Slide 9 — Conclusão

O projeto demonstra como uma solução de baixo código pode resolver um problema real de operação empresarial: o lançamento de notas fiscais. A proposta central é reduzir tempo, aumentar qualidade e simplificar a rotina do usuário, mantendo controle de regras de negócio, acesso e validação de dados.

### Mensagem final

> Com automação, validação e organização, o processo de nota fiscal deixa de ser uma operação manual e passa a ser uma rotina mais ágil e confiável.
