import mysql.connector

class RepositorioCiente:
  _bancoDeDados = None
  _conexaoDoBancoDeDados = None
  _cursorDoBancoDeDados = None
  _nomeDaTabela = "cliente"

  def __init__(self, bancoDeDados):
    self._bancoDeDados = bancoDeDados
    self._conexaoDoBancoDeDados = bancoDeDados.getConexao()
    self._cursorDoBancoDeDados = bancoDeDados.getConexao().cursor()

  def criar(self, nome, cpf, senha):
    resultado = None
    sql = f"INSERT INTO {self._nomeDaTabela} (nome, cpf, senha) VALUES (%s, %s, %s)"

    try:
      self._cursorDoBancoDeDados.execute(sql, (nome, cpf, senha))
      self._conexaoDoBancoDeDados.commit()
      resultado = {"foiBemSucedido": True, "mensagem": "O cliente foi cadastrado com sucesso."}

    except mysql.connector.IntegrityError as erro:
      self._conexaoDoBancoDeDados.rollback()

      if erro.errno == 1062:
        resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_CLIENTE_01", "mensagem": f"O CPF '{cpf}' já está cadastrado."}
      else:
        resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": f"Houve um erro no banco de dados."}
      
    except Exception as erro:
      self._conexaoDoBancoDeDados.rollback()
      print(f"\n{erro}")
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": f"Houve um erro no banco de dados."}
    
    return resultado

  def listarTodos(self):
    resultado = None
    sql = f"SELECT * FROM {self._nomeDaTabela}"

    try:
      self._cursorDoBancoDeDados.execute(sql)
      registros = self._cursorDoBancoDeDados.fetchall()

      colunas = [desc[0] for desc in self._cursorDoBancoDeDados.description]
      clientes = [dict(zip(colunas, registro)) for registro in registros]

      resultado = {"foiBemSucedido": True, "dados": clientes}
    except Exception as erro:
      print(f"\n{erro}")
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": f"Houve um erro no banco de dados."}
    
    return resultado
