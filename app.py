import mysql.connector

def inserir_novo_produto(grupo, tipo_alimento, pais="BR"):
    """
    Busca a última sequência na tabela codigos_sequenciais, 
    gera o novo código com zerofill (4 dígitos) e insere no banco.
    """
    grupo = grupo.upper()
    tipo_alimento = tipo_alimento.upper()
    pais = pais.upper()

    try:
        # Configuração da conexão
        # Atenção: Se no seu PC a senha for vazia "", troque aqui na hora de testar local.
        # Para o GitHub Actions (CI/CD), a senha será "root".
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",  # Altere para a sua senha local se necessário
            database="db_produtos"
        )
        cursor = conexao.cursor()

        # 1. Busca a última sequência na NOVA tabela (codigos_sequenciais)
        query_max = "SELECT MAX(sec) FROM codigos_sequenciais WHERE Grupo = %s"
        cursor.execute(query_max, (grupo,))
        resultado = cursor.fetchone()

        # 2. Calcula a nova sequência
        nova_sec = resultado[0] + 1 if resultado[0] is not None else 1

        # 3. Formata o código (ex: BRC0004A)
        codigo_gerado = f"{pais}{grupo}{str(nova_sec).zfill(4)}{tipo_alimento}"

        # 4. Insere o novo registro na NOVA tabela
        query_insert = """
            INSERT INTO codigos_sequenciais (codigo, sec, Grupo, Tipo_Alimento, Pais) 
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query_insert, (codigo_gerado, nova_sec, grupo, tipo_alimento, pais))
        conexao.commit()

        print(f"Sucesso! Código gerado: {codigo_gerado}")
        return codigo_gerado

    except mysql.connector.Error as erro:
        print(f"Erro no banco de dados: {erro}")
        return None
    finally:
        # Fecha a conexão com segurança
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

# --- Área de Teste Local ---
if __name__ == "__main__":
    print("Testando a inserção de novos códigos...")
    inserir_novo_produto(grupo="C", tipo_alimento="K", pais="BR")