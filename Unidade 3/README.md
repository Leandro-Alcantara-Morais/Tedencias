# Sistema de Lançamento de Nota Fiscal

Criamos um sistema para atender algumas necessidades que outros têm uma certa deficiência em operar, visando um processo mais rápido e prático para o usuário.

## 1. Tela de Login

O primeiro login é para o administrador do sistema, que possui autonomia para registrar novos usuários, definir quais campos eles podem acessar e utilizar, além de utilizar todas as funções do sistema.

## 2. Sistema

O lançamento de notas poderá ser feito via chave de acesso, importação de XML, arquivo PDF ou foto.

### 2.1. Informações obtidas da nota fiscal

#### 2.1.1. Cadastro automático do fornecedor
O sistema fará o cadastro automático do fornecedor pegando as informações de razão social, nome fantasia (se houver), CNPJ, CEP, endereço, telefone.

#### 2.1.2. Cadastro automático dos produtos
O sistema cadastrará automaticamente os produtos da nota, com código, descrição do produto, NCM, unidade de medida (UND), quantidade (QTD), valor unitário (V. UN.).

#### 2.1.3. Edição das informações
Será possível editar as informações obtidas a partir do momento em que forem obtidas, com botão de confirmação após as alterações.

## 3. Verificações

Ao lançar as informações da nota, o sistema deverá verificar se o que foi obtido já possui no sistema, podendo indicar os produtos que já possui e os que serão adicionados ao banco de dados do sistema.

### 3.1. Verificação de informação cruzada

O sistema irá verificar se as informações obtidas de um fornecedor se repetem em outro, criando um alerta para o usuário editar o erro mostrado.

## 4. Interface

O sistema possui menu para cadastro de nota, visualização de fornecedores, visualização de produtos, administração de usuários.
