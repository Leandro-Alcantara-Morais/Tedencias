#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Interativa - Versão Refatorada com Orientação a Objetos

Uma aplicação de linha de comando que funciona como uma calculadora
com suporte a operações matemáticas básicas, tratamento de erros robusto
e arquitetura orientada a objetos.
"""

from typing import Tuple, Optional, Callable, Dict


class OperacaoMatematica:
    """Representa uma operação matemática com seu símbolo e função."""

    def __init__(
        self,
        nome: str,
        simbolo: str,
        funcao: Callable[[float, float], float]
    ):
        """
        Inicializa uma operação matemática.

        Args:
            nome: Nome descritivo da operação (ex: "Adição")
            simbolo: Símbolo da operação (ex: "+")
            funcao: Função que implementa a operação
        """
        self.nome = nome
        self.simbolo = simbolo
        self.funcao = funcao

    def executar(self, num1: float, num2: float) -> float:
        """
        Executa a operação.

        Args:
            num1: Primeiro operando
            num2: Segundo operando

        Returns:
            Resultado da operação

        Raises:
            ZeroDivisionError: Se a operação envolver divisão por zero
            ValueError: Se houver erro na operação
        """
        return self.funcao(num1, num2)


class Calculadora:
    """
    Calculadora interativa com suporte a operações matemáticas básicas.

    Attributes:
        operacoes: Dicionário com as operações disponíveis
        historico: Lista com histórico de operações realizadas
    """

    def __init__(self):
        """Inicializa a calculadora e suas operações."""
        self.historico: list = []
        self.operacoes: Dict[str, OperacaoMatematica] = self._inicializar_operacoes()

    @staticmethod
    def _inicializar_operacoes() -> Dict[str, OperacaoMatematica]:
        """
        Inicializa o dicionário de operações disponíveis.

        Returns:
            Dicionário com as operações mapeadas por código
        """
        return {
            '1': OperacaoMatematica('Adição', '+', lambda a, b: a + b),
            '2': OperacaoMatematica('Subtração', '-', lambda a, b: a - b),
            '3': OperacaoMatematica('Multiplicação', '*', lambda a, b: a * b),
            '4': OperacaoMatematica(
                'Divisão',
                '/',
                Calculadora._dividir
            ),
        }

    @staticmethod
    def _dividir(num1: float, num2: float) -> float:
        """
        Realiza a divisão com validação de divisão por zero.

        Args:
            num1: Dividendo
            num2: Divisor

        Returns:
            Resultado da divisão

        Raises:
            ZeroDivisionError: Se o divisor for zero
        """
        if num2 == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return num1 / num2

    def obter_numeros(self) -> Tuple[float, float]:
        """
        Solicita e valida dois números do usuário.

        Returns:
            Tupla contendo dois números float (num1, num2)

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

    def validar_opcao(self, opcao: str) -> bool:
        """
        Valida se a opção escolhida existe.

        Args:
            opcao: Código da operação

        Returns:
            True se a opção é válida, False caso contrário
        """
        return opcao in self.operacoes

    def calcular(
        self,
        opcao: str,
        num1: float,
        num2: float
    ) -> Tuple[bool, Optional[float], str]:
        """
        Executa a operação selecionada.

        Args:
            opcao: Código da operação
            num1: Primeiro número
            num2: Segundo número

        Returns:
            Tupla contendo (sucesso, resultado, mensagem)
            - sucesso: bool indicando se a operação foi bem-sucedida
            - resultado: float com o resultado ou None em caso de erro
            - mensagem: string com descrição da operação ou erro
        """
        if not self.validar_opcao(opcao):
            return False, None, "Opção inválida! Escolha entre 1 e 4."

        try:
            operacao = self.operacoes[opcao]
            resultado = operacao.executar(num1, num2)
            self._adicionar_ao_historico(num1, num2, operacao, resultado)
            return True, resultado, operacao.nome
        except ZeroDivisionError:
            return False, None, "Divisão por zero não é permitida."
        except Exception as e:
            return False, None, f"Erro ao calcular: {str(e)}"

    def _adicionar_ao_historico(
        self,
        num1: float,
        num2: float,
        operacao: OperacaoMatematica,
        resultado: float
    ) -> None:
        """
        Adiciona a operação ao histórico.

        Args:
            num1: Primeiro número
            num2: Segundo número
            operacao: Objeto da operação realizada
            resultado: Resultado obtido
        """
        entrada = {
            'operacao': operacao.nome,
            'num1': num1,
            'num2': num2,
            'resultado': resultado,
            'simbolo': operacao.simbolo
        }
        self.historico.append(entrada)

    def obter_historico(self) -> list:
        """
        Retorna o histórico de operações.

        Returns:
            Lista com todas as operações realizadas
        """
        return self.historico.copy()

    def limpar_historico(self) -> None:
        """Limpa o histórico de operações."""
        self.historico.clear()


class InterfaceCalculadora:
    """
    Interface de linha de comando para a calculadora.

    Gerencia a interação com o usuário e a apresentação de informações.
    """

    def __init__(self, calculadora: Calculadora):
        """
        Inicializa a interface.

        Args:
            calculadora: Instância da calculadora a usar
        """
        self.calculadora = calculadora

    @staticmethod
    def limpar_tela() -> None:
        """Limpa a tela do console."""
        print("\n" * 2)

    def exibir_menu_principal(self) -> None:
        """Exibe o menu principal de operações."""
        self.limpar_tela()
        print("=" * 50)
        print("         CALCULADORA INTERATIVA")
        print("=" * 50)
        print("\nEscolha uma operação:")
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("5 - Ver histórico")
        print("6 - Limpar histórico")
        print("7 - Sair")
        print("-" * 50)

    def exibir_boas_vindas(self) -> None:
        """Exibe mensagem de boas-vindas."""
        print("\n" + "=" * 50)
        print("    BEM-VINDO À CALCULADORA INTERATIVA!")
        print("=" * 50)

    def exibir_despedida(self) -> None:
        """Exibe mensagem de despedida."""
        print("\n" + "=" * 50)
        print("    Obrigado por usar a calculadora!")
        print("=" * 50)
        print("👋 Até logo!\n")

    def exibir_resultado(
        self,
        num1: float,
        num2: float,
        operacao: str,
        simbolo: str,
        resultado: float
    ) -> None:
        """
        Exibe o resultado de uma operação de forma formatada.

        Args:
            num1: Primeiro número
            num2: Segundo número
            operacao: Nome da operação
            simbolo: Símbolo da operação
            resultado: Resultado obtido
        """
        print("\n" + "-" * 50)
        print(f"✓ {operacao} realizada com sucesso!")
        print(f"\n  {num1} {simbolo} {num2} = {resultado}")

        if isinstance(resultado, float) and resultado.is_integer():
            print(f"  Resultado: {int(resultado)}")
        else:
            print(f"  Resultado: {resultado:.4f}")
        print("-" * 50)

    def exibir_erro(self, mensagem: str) -> None:
        """
        Exibe mensagem de erro.

        Args:
            mensagem: Texto do erro a exibir
        """
        print(f"\n❌ Erro! {mensagem}")

    def exibir_historico(self) -> None:
        """Exibe o histórico de operações realizadas."""
        historico = self.calculadora.obter_historico()

        if not historico:
            print("\n📋 Histórico vazio. Nenhuma operação foi realizada ainda.")
            return

        print("\n" + "=" * 50)
        print("              HISTÓRICO DE OPERAÇÕES")
        print("=" * 50)

        for idx, entrada in enumerate(historico, 1):
            resultado = entrada['resultado']
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            else:
                resultado = f"{resultado:.4f}"

            print(
                f"{idx}. {entrada['num1']} {entrada['simbolo']} "
                f"{entrada['num2']} = {resultado}"
            )

        print("=" * 50)

    def obter_confirmacao(self, mensagem: str) -> bool:
        """
        Solicita confirmação do usuário (sim/não).

        Args:
            mensagem: Mensagem a exibir

        Returns:
            True se o usuário confirmar, False caso contrário
        """
        while True:
            resposta = input(f"\n{mensagem} (s/n): ").strip().lower()
            if resposta in ('s', 'sim', 'yes'):
                return True
            elif resposta in ('n', 'não', 'nao', 'no'):
                return False
            else:
                print("❌ Opção inválida! Digite 's' para sim ou 'n' para não.")

    def obter_opcao(self) -> str:
        """
        Obtém a opção do usuário no menu.

        Returns:
            String com a opção digitada
        """
        return input("Digite sua escolha (1-7): ").strip()


class AplicacaoCalculadora:
    """
    Aplicação principal que coordena a calculadora e sua interface.

    Gerencia o fluxo principal e a interação entre componentes.
    """

    def __init__(self):
        """Inicializa a aplicação."""
        self.calculadora = Calculadora()
        self.interface = InterfaceCalculadora(self.calculadora)

    def processar_opcao(self, opcao: str) -> bool:
        """
        Processa a opção selecionada pelo usuário.

        Args:
            opcao: Código da opção

        Returns:
            False se o usuário quer sair, True caso contrário
        """
        if opcao == '7':
            self.interface.exibir_despedida()
            return False

        elif opcao == '5':
            self.interface.exibir_historico()
            return True

        elif opcao == '6':
            if self.interface.obter_confirmacao(
                "Deseja limpar todo o histórico?"
            ):
                self.calculadora.limpar_historico()
                print("✓ Histórico limpo com sucesso!")
            return True

        elif opcao in ('1', '2', '3', '4'):
            return self._processar_calculo(opcao)

        else:
            self.interface.exibir_erro("Opção inválida! Escolha entre 1 e 7.")
            return True

    def _processar_calculo(self, opcao: str) -> bool:
        """
        Processa um cálculo matemático.

        Args:
            opcao: Código da operação

        Returns:
            True para continuar, False para sair
        """
        num1, num2 = self.calculadora.obter_numeros()
        sucesso, resultado, mensagem = self.calculadora.calcular(
            opcao,
            num1,
            num2
        )

        if sucesso:
            operacao = self.calculadora.operacoes[opcao]
            self.interface.exibir_resultado(
                num1,
                num2,
                operacao.nome,
                operacao.simbolo,
                resultado
            )
        else:
            self.interface.exibir_erro(mensagem)

        return self.interface.obter_confirmacao(
            "Deseja fazer outra operação?"
        )

    def executar(self) -> None:
        """Executa o loop principal da aplicação."""
        self.interface.exibir_boas_vindas()

        continuar = True
        while continuar:
            self.interface.exibir_menu_principal()
            opcao = self.interface.obter_opcao()
            continuar = self.processar_opcao(opcao)


def main() -> None:
    """Função principal de entrada da aplicação."""
    try:
        app = AplicacaoCalculadora()
        app.executar()
    except KeyboardInterrupt:
        print("\n\n" + "=" * 50)
        print("    Programa interrompido pelo usuário")
        print("=" * 50)
        print("👋 Até logo!\n")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("Por favor, reinicie o programa.")


if __name__ == "__main__":
    main()
