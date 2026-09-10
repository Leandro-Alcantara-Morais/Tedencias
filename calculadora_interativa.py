#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Interativa
Uma aplicação de linha de comando que funciona como uma calculadora
com suporte a operações matemáticas básicas e tratamento de erros.
"""


def exibir_menu():
    """
    Exibe o menu de operações disponíveis.
    """
    print("\n" + "=" * 50)
    print("         CALCULADORA INTERATIVA")
    print("=" * 50)
    print("\nEscolha uma operação:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Sair")
    print("-" * 50)


def obter_numeros():
    """
    Solicita e valida dois números do usuário.
    
    Returns:
        tuple: Uma tupla contendo dois números float (num1, num2)
        
    Raises:
        ValueError: Se os valores inseridos não forem números válidos
    """
    while True:
        try:
            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            return num1, num2
        except ValueError:
            print("\n❌ Erro! Por favor, digite valores numéricos válidos.")
            print("   Exemplo: 5 ou 3.14")


def adicionar(num1, num2):
    """
    Realiza a adição de dois números.
    
    Args:
        num1 (float): Primeiro número
        num2 (float): Segundo número
        
    Returns:
        float: Resultado da adição
    """
    return num1 + num2


def subtrair(num1, num2):
    """
    Realiza a subtração de dois números.
    
    Args:
        num1 (float): Primeiro número
        num2 (float): Segundo número
        
    Returns:
        float: Resultado da subtração
    """
    return num1 - num2


def multiplicar(num1, num2):
    """
    Realiza a multiplicação de dois números.
    
    Args:
        num1 (float): Primeiro número
        num2 (float): Segundo número
        
    Returns:
        float: Resultado da multiplicação
    """
    return num1 * num2


def dividir(num1, num2):
    """
    Realiza a divisão de dois números com validação de divisão por zero.
    
    Args:
        num1 (float): Dividendo
        num2 (float): Divisor
        
    Returns:
        float: Resultado da divisão
        
    Raises:
        ZeroDivisionError: Se o divisor for zero
    """
    if num2 == 0:
        raise ZeroDivisionError("❌ Erro! Não é possível dividir por zero.")
    return num1 / num2


def executar_operacao(opcao, num1, num2):
    """
    Executa a operação matemática selecionada.
    
    Args:
        opcao (str): Opção selecionada pelo usuário
        num1 (float): Primeiro número
        num2 (float): Segundo número
        
    Returns:
        tuple: (sucesso: bool, resultado: float ou None, mensagem: str)
    """
    operacoes = {
        '1': (adicionar, "Adição"),
        '2': (subtrair, "Subtração"),
        '3': (multiplicar, "Multiplicação"),
        '4': (dividir, "Divisão"),
    }
    
    if opcao not in operacoes:
        return False, None, "❌ Opção inválida! Escolha entre 1 e 5."
    
    try:
        funcao, nome_operacao = operacoes[opcao]
        resultado = funcao(num1, num2)
        return True, resultado, nome_operacao
    except ZeroDivisionError as e:
        return False, None, str(e)


def formatar_resultado(num1, num2, operacao, resultado):
    """
    Formata e exibe o resultado da operação de forma clara.
    
    Args:
        num1 (float): Primeiro número
        num2 (float): Segundo número
        operacao (str): Nome da operação
        resultado (float): Resultado da operação
    """
    simbolos = {
        "Adição": "+",
        "Subtração": "-",
        "Multiplicação": "*",
        "Divisão": "/"
    }
    
    simbolo = simbolos.get(operacao, "?")
    
    print("\n" + "-" * 50)
    print(f"✓ {operacao} realizada com sucesso!")
    print(f"\n  {num1} {simbolo} {num2} = {resultado}")
    
    # Formata o resultado se for inteiro
    if isinstance(resultado, float) and resultado.is_integer():
        print(f"  Resultado: {int(resultado)}")
    else:
        print(f"  Resultado: {resultado:.4f}")
    print("-" * 50)


def continuar_calculando():
    """
    Pergunta ao usuário se deseja continuar calculando.
    
    Returns:
        bool: True se o usuário deseja continuar, False caso contrário
    """
    while True:
        resposta = input("\nDeseja fazer outra operação? (s/n): ").strip().lower()
        if resposta in ('s', 'sim', 'yes'):
            return True
        elif resposta in ('n', 'não', 'nao', 'no'):
            return False
        else:
            print("❌ Opção inválida! Digite 's' para sim ou 'n' para não.")


def main():
    """
    Função principal que controla o fluxo da calculadora.
    """
    print("\n" + "=" * 50)
    print("         BEM-VINDO À CALCULADORA INTERATIVA!")
    print("=" * 50)
    
    continuar = True
    
    while continuar:
        exibir_menu()
        opcao = input("Digite sua escolha (1-5): ").strip()
        
        # Verificar se o usuário quer sair
        if opcao == '5':
            print("\n" + "=" * 50)
            print("        Obrigado por usar a calculadora!")
            print("=" * 50)
            print("👋 Até logo!\n")
            break
        
        # Validar opção de operação
        if opcao not in ('1', '2', '3', '4'):
            print("\n❌ Opção inválida! Por favor, escolha entre 1 e 5.")
            continue
        
        # Obter números
        num1, num2 = obter_numeros()
        
        # Executar operação
        sucesso, resultado, mensagem = executar_operacao(opcao, num1, num2)
        
        if sucesso:
            formatar_resultado(num1, num2, mensagem, resultado)
            continuar = continuar_calculando()
        else:
            print(f"\n{mensagem}")
            continuar = continuar_calculando()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + "=" * 50)
        print("        Programa interrompido pelo usuário")
        print("=" * 50)
        print("👋 Até logo!\n")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("Por favor, reinicie o programa.")
