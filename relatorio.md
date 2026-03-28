# Relatório Técnico: Implementação de Pipeline CI/CD para VV&T

## 1. Arquitetura da Solução e Ferramentas Utilizadas
Para atender aos requisitos de automação e provisionamento, a solução foi construída baseada no **GitHub Actions**. A escolha se justifica pela sua integração nativa com o repositório de código, facilidade de provisionamento de containers e ampla documentação.

* **Ambiente Operacional:** Ubuntu Linux (provisionado pela tag `ubuntu-latest`).
* **Banco de Dados:** MySQL Server 8.0, provisionado como um `service` dockerizado diretamente na pipeline, rodando na porta padrão 3306.
* **Linguagem e Testes:** Python 3.10 gerenciando a lógica de negócio, com testes unitários executados pela biblioteca `pytest`.

## 2. Automação das Etapas
A pipeline `.github/workflows/main.yml` foi orquestrada nas seguintes etapas:
1. **Provisionamento:** Levanta a máquina Linux e o container do MySQL.
2. **Setup:** Instala o Python e as bibliotecas (`mysql-connector-python` e `pytest`).
3. **Database Injection:** Executa o script `schema.sql` via linha de comando para criar o banco `db_produtos` e a tabela `codigos_sequenciais`, injetando os dados de teste.
4. **Validação:** Executa o `pytest test_gerador_codigo.py -v` para garantir que a lógica de zerofill, regras de negócio e incremento funcionem no novo ambiente.
5. **Integração Real:** Executa o `app.py` para provar que a conexão entre a aplicação Python e o banco MySQL configurado na nuvem ocorre com sucesso.

## 3. Desafios Encontrados e Soluções
* **Desafio de Conexão CI/CD:** Garantir que o Python conseguisse acessar o MySQL na nuvem, visto que localmente as credenciais eram diferentes. **Solução:** O `app.py` foi parametrizado para usar o host `127.0.0.1` e a senha `root`, que foram declarados nas variáveis de ambiente (`env`) do serviço MySQL no GitHub Actions.
* **Isolamento de Testes:** Evitar que os testes unitários alterassem a base de dados real provisionada. **Solução:** O uso rigoroso da biblioteca `unittest.mock` (Mocking) no arquivo de testes garantiu que a lógica matemática fosse avaliada sem depender da camada física do banco.