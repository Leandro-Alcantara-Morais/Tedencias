#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes unitários para a Calculadora Interativa

Módulo contendo testes abrangentes para todas as funcionalidades
da calculadora, incluindo operações matemáticas, validação de entrada
e tratamento de erros.
"""

import unittest
from io import StringIO
import sys
from calculadora_interativa import (
    Calculadora,
    OperacaoMatematica,
    InterfaceCalculadora,
    AplicacaoCalculadora
)


class TestOperacaoMatematica(unittest.TestCase):
    """Testes para a classe OperacaoMatematica."""

    def test_inicializacao_operacao(self):
        """Testa a inicialização de uma operação."""
        op = OperacaoMatematica('Teste', '+', lambda a, b: a + b)
        self.assertEqual(op.nome, 'Teste')
        self.assertEqual(op.simbolo, '+')
        self.assertEqual(op.executar(2, 3), 5)

    def test_execucao_operacao_simples(self):
        """Testa a execução de uma operação simples."""
        op = OperacaoMatematica('Adição', '+', lambda a, b: a + b)
        resultado = op.executar(5, 3)
        self.assertEqual(resultado, 8)


class TestCalculadora(unittest.TestCase):
    """Testes para a classe Calculadora."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.calculadora = Calculadora()

    def test_inicializacao(self):
        """Testa a inicialização da calculadora."""
        self.assertIsNotNone(self.calculadora.operacoes)
        self.assertEqual(len(self.calculadora.operacoes), 4)
        self.assertEqual(len(self.calculadora.historico), 0)

    def test_operacoes_disponíveis(self):
        """Testa se todas as operações estão disponíveis."""
        self.assertIn('1', self.calculadora.operacoes)  # Adição
        self.assertIn('2', self.calculadora.operacoes)  # Subtração
        self.assertIn('3', self.calculadora.operacoes)  # Multiplicação
        self.assertIn('4', self.calculadora.operacoes)  # Divisão

    def test_adicao(self):
        """Testa a operação de adição."""
        sucesso, resultado, mensagem = self.calculadora.calcular('1', 5, 3)
        self.assertTrue(sucesso)
        self.assertEqual(resultado, 8)
        self.assertEqual(mensagem, 'Adição')

    def test_subtracao(self):
        """Testa a operação de subtração."""
        sucesso, resultado, mensagem = self.calculadora.calcular('2', 10, 4)
        self.assertTrue(sucesso)
        self.assertEqual(resultado, 6)
        self.assertEqual(mensagem, 'Subtração')

    def test_multiplicacao(self):
        """Testa a operação de multiplicação."""
        sucesso, resultado, mensagem = self.calculadora.calcular('3', 7, 6)
        self.assertTrue(sucesso)
        self.assertEqual(resultado, 42)
        self.assertEqual(mensagem, 'Multiplicação')

    def test_divisao_valida(self):
        """Testa a operação de divisão com divisor válido."""
        sucesso, resultado, mensagem = self.calculadora.calcular('4', 20, 4)
        self.assertTrue(sucesso)
        self.assertEqual(resultado, 5.0)
        self.assertEqual(mensagem, 'Divisão')

    def test_divisao_por_zero(self):
        """Testa o tratamento de divisão por zero."""
        sucesso, resultado, mensagem = self.calculadora.calcular('4', 10, 0)
        self.assertFalse(sucesso)
        self.assertIsNone(resultado)
        self.assertIn('zero', mensagem.lower())

    def test_opcao_invalida(self):
        """Testa o tratamento de opção inválida."""
        sucesso, resultado, mensagem = self.calculadora.calcular('9', 5, 3)
        self.assertFalse(sucesso)
        self.assertIsNone(resultado)

    def test_validar_opcao_valida(self):
        """Testa a validação de opção válida."""
        self.assertTrue(self.calculadora.validar_opcao('1'))
        self.assertTrue(self.calculadora.validar_opcao('4'))

    def test_validar_opcao_invalida(self):
        """Testa a validação de opção inválida."""
        self.assertFalse(self.calculadora.validar_opcao('0'))
        self.assertFalse(self.calculadora.validar_opcao('5'))
        self.assertFalse(self.calculadora.validar_opcao('abc'))

    def test_historico_adicionado(self):
        """Testa se operação é adicionada ao histórico."""
        self.calculadora.calcular('1', 5, 3)
        self.assertEqual(len(self.calculadora.historico), 1)
        
        entrada = self.calculadora.historico[0]
        self.assertEqual(entrada['num1'], 5)
        self.assertEqual(entrada['num2'], 3)
        self.assertEqual(entrada['resultado'], 8)
        self.assertEqual(entrada['operacao'], 'Adição')

    def test_historico_multiplas_operacoes(self):
        """Testa o histórico com múltiplas operações."""
        self.calculadora.calcular('1', 5, 3)
        self.calculadora.calcular('2', 10, 4)
        self.calculadora.calcular('3', 7, 6)
        
        self.assertEqual(len(self.calculadora.historico), 3)

    def test_limpar_historico(self):
        """Testa a limpeza do histórico."""
        self.calculadora.calcular('1', 5, 3)
        self.calculadora.calcular('2', 10, 4)
        
        self.assertEqual(len(self.calculadora.historico), 2)
        self.calculadora.limpar_historico()
        self.assertEqual(len(self.calculadora.historico), 0)

    def test_obter_historico_copia(self):
        """Testa se obter_historico retorna uma cópia."""
        self.calculadora.calcular('1', 5, 3)
        
        historico1 = self.calculadora.obter_historico()
        historico2 = self.calculadora.obter_historico()
        
        self.assertEqual(historico1, historico2)
        self.assertIsNot(historico1, historico2)

    def test_numeros_negativos(self):
        """Testa operações com números negativos."""
        sucesso, resultado, _ = self.calculadora.calcular('1', -5, -3)
        self.assertTrue(sucesso)
        self.assertEqual(resultado, -8)

    def test_numeros_decimais(self):
        """Testa operações com números decimais."""
        sucesso, resultado, _ = self.calculadora.calcular('1', 3.5, 2.5)
        self.assertTrue(sucesso)
        self.assertEqual(resultado, 6.0)

    def test_divisao_resultado_decimal(self):
        """Testa divisão que resulta em número decimal."""
        sucesso, resultado, _ = self.calculadora.calcular('4', 10, 3)
        self.assertTrue(sucesso)
        self.assertAlmostEqual(resultado, 3.333333, places=5)


class TestInterfaceCalculadora(unittest.TestCase):
    """Testes para a classe InterfaceCalculadora."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.calculadora = Calculadora()
        self.interface = InterfaceCalculadora(self.calculadora)

    def test_inicializacao(self):
        """Testa a inicialização da interface."""
        self.assertIsNotNone(self.interface.calculadora)
        self.assertEqual(self.interface.calculadora, self.calculadora)

    def test_exibir_resultado_inteiro(self):
        """Testa a exibição de resultado inteiro."""
        with self.assertLogs(level='INFO') as cm:
            # Captura saída
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            
            self.interface.exibir_resultado(5, 3, 'Adição', '+', 8)
            
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout
            
            self.assertIn('8', output)

    def test_exibir_resultado_decimal(self):
        """Testa a exibição de resultado decimal."""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        self.interface.exibir_resultado(10, 3, 'Divisão', '/', 3.3333)
        
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        self.assertIn('3.3333', output)


class TestAplicacaoCalculadora(unittest.TestCase):
    """Testes para a classe AplicacaoCalculadora."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.app = AplicacaoCalculadora()

    def test_inicializacao(self):
        """Testa a inicialização da aplicação."""
        self.assertIsNotNone(self.app.calculadora)
        self.assertIsNotNone(self.app.interface)

    def test_processar_opcao_sair(self):
        """Testa o processamento da opção de sair."""
        resultado = self.app.processar_opcao('7')
        self.assertFalse(resultado)

    def test_processar_opcao_historico(self):
        """Testa o processamento da opção de ver histórico."""
        resultado = self.app.processar_opcao('5')
        self.assertTrue(resultado)

    def test_processar_opcao_invalida(self):
        """Testa o processamento de opção inválida."""
        resultado = self.app.processar_opcao('99')
        self.assertTrue(resultado)


class TestIntegracaCompleta(unittest.TestCase):
    """Testes de integração completa do sistema."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.calculadora = Calculadora()

    def test_fluxo_calculo_adicao(self):
        """Testa o fluxo completo de um cálculo de adição."""
        sucesso, resultado, mensagem = self.calculadora.calcular('1', 10, 5)
        
        self.assertTrue(sucesso)
        self.assertEqual(resultado, 15)
        self.assertEqual(mensagem, 'Adição')
        self.assertEqual(len(self.calculadora.historico), 1)

    def test_fluxo_multiplos_calculos(self):
        """Testa o fluxo com múltiplos cálculos."""
        operacoes = [
            ('1', 10, 5, 15, 'Adição'),
            ('2', 20, 8, 12, 'Subtração'),
            ('3', 6, 7, 42, 'Multiplicação'),
            ('4', 100, 5, 20.0, 'Divisão'),
        ]
        
        for opcao, num1, num2, resultado_esperado, msg_esperada in operacoes:
            sucesso, resultado, mensagem = self.calculadora.calcular(
                opcao,
                num1,
                num2
            )
            
            self.assertTrue(sucesso)
            self.assertEqual(resultado, resultado_esperado)
            self.assertEqual(mensagem, msg_esperada)
        
        self.assertEqual(len(self.calculadora.historico), 4)

    def test_tratamento_erros_completo(self):
        """Testa o tratamento de erros completo."""
        # Teste divisão por zero
        sucesso, _, _ = self.calculadora.calcular('4', 10, 0)
        self.assertFalse(sucesso)
        self.assertEqual(len(self.calculadora.historico), 0)
        
        # Teste com opção inválida
        sucesso, _, _ = self.calculadora.calcular('99', 5, 3)
        self.assertFalse(sucesso)
        self.assertEqual(len(self.calculadora.historico), 0)
        
        # Teste com cálculo válido depois de erros
        sucesso, resultado, _ = self.calculadora.calcular('1', 5, 3)
        self.assertTrue(sucesso)
        self.assertEqual(resultado, 8)
        self.assertEqual(len(self.calculadora.historico), 1)


class TestCasosExtremosEdge(unittest.TestCase):
    """Testes para casos extremos e edge cases."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.calculadora = Calculadora()

    def test_numeros_muito_grandes(self):
        """Testa operações com números muito grandes."""
        sucesso, resultado, _ = self.calculadora.calcular(
            '1',
            1e308,
            1e308
        )
        self.assertTrue(sucesso)

    def test_numeros_muito_pequenos(self):
        """Testa operações com números muito pequenos."""
        sucesso, resultado, _ = self.calculadora.calcular(
            '1',
            1e-308,
            1e-308
        )
        self.assertTrue(sucesso)

    def test_zero_como_operando(self):
        """Testa operações com zero como operando."""
        # Adição com zero
        sucesso, resultado, _ = self.calculadora.calcular('1', 0, 5)
        self.assertTrue(sucesso)
        self.assertEqual(resultado, 5)
        
        # Multiplicação por zero
        sucesso, resultado, _ = self.calculadora.calcular('3', 100, 0)
        self.assertTrue(sucesso)
        self.assertEqual(resultado, 0)

    def test_mesmos_numeros(self):
        """Testa operações com números iguais."""
        sucesso, resultado, _ = self.calculadora.calcular('2', 5, 5)
        self.assertTrue(sucesso)
        self.assertEqual(resultado, 0)


def suite_testes_basicos():
    """Retorna suite com testes básicos."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCalculadora))
    return suite


def suite_testes_completos():
    """Retorna suite com todos os testes."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestOperacaoMatematica))
    suite.addTest(unittest.makeSuite(TestCalculadora))
    suite.addTest(unittest.makeSuite(TestInterfaceCalculadora))
    suite.addTest(unittest.makeSuite(TestAplicacaoCalculadora))
    suite.addTest(unittest.makeSuite(TestIntegracaCompleta))
    suite.addTest(unittest.makeSuite(TestCasosExtremosEdge))
    return suite


if __name__ == '__main__':
    # Executa todos os testes com verbosidade
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite_testes_completos())
