import mysql.connector

class BancoDeDados:
  _conexao = None

  def __init__(self, host, nomeDoBancoDeDados, usuario, senha):
    self._host = host
    self._nomeDoBancoDeDados = nomeDoBancoDeDados
    self._usuario = usuario
    self._senha = senha
  
  def getConexao(self):
    return self._conexao

  def conectar(self):
    resultado = False

    if (self.getConexao() is None):
      try:
        self._conexao = mysql.connector.connect(
          host=self._host,
          user=self._usuario,
          password=self._senha,
          database=self._nomeDoBancoDeDados
        )
      
        print("\nBanco de dados conectado com sucesso!")

        resultado = True

      except Exception as erro:
        print("\nHouve um erro na conexão com o banco dados.")
        print(erro)
    
    return resultado
    
  def fecharConexao(self):
    if self._conexao and self._conexao.is_connected():
      self._conexao.close()
      self._conexao = None
      print("\nConexão com o banco de dados foi fechada!")
