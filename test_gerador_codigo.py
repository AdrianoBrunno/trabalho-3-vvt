import pytest
from unittest.mock import patch, MagicMock
from app import inserir_novo_produto

# Intercepta a conexão com o banco de dados no arquivo 'app'
@patch('app.mysql.connector.connect')
def test_gerador_codigo_grupo_existente(mock_connect):
    """
    Testa o cenário onde o grupo já existe. 
    Se a última sequência for 3, o novo código deve usar 4 (0004).
    """
    mock_conexao = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conexao
    mock_conexao.cursor.return_value = mock_cursor
    
    # Simula que o banco respondeu 3 para o MAX(sec)
    mock_cursor.fetchone.return_value = (3,)
    
    # Roda a função
    resultado = inserir_novo_produto(grupo='C', tipo_alimento='A', pais='BR')
    
    # Verifica a formatação
    assert resultado == 'BRC0004A'

@patch('app.mysql.connector.connect')
def test_gerador_codigo_grupo_novo(mock_connect):
    """
    Testa o cenário onde o grupo é novo (retorno None do banco).
    Deve começar a sequência no número 1.
    """
    mock_conexao = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conexao
    mock_conexao.cursor.return_value = mock_cursor
    
    # Simula que o grupo não tem registros ainda
    mock_cursor.fetchone.return_value = (None,)
    
    resultado = inserir_novo_produto(grupo='Z', tipo_alimento='K', pais='BR')
    
    assert resultado == 'BRZ0001K'

@patch('app.mysql.connector.connect')
def test_tratamento_letras_minusculas(mock_connect):
    """
    Testa se o sistema converte corretamente letras minúsculas para maiúsculas.
    """
    mock_conexao = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conexao
    mock_conexao.cursor.return_value = mock_cursor
    
    mock_cursor.fetchone.return_value = (15,)
    
    # Passando os parâmetros em minúsculo de propósito
    resultado = inserir_novo_produto(grupo='f', tipo_alimento='b', pais='br')
    
    # Deve converter tudo para maiúsculo (BRF0016B)
    assert resultado == 'BRF0016B'