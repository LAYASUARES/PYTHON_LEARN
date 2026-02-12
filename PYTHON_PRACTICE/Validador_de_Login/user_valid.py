
#lista de usuarios validos
usuarios = [
    {"username": "alice", "senha": "alice@example.com"},
    {"username": "bob", "senha": "bob@example.com"},
    {"username": "charlie", "senha": "charlie@example.com"}
]    

try:
     usuarios_input = input("Insira o nome do usuario: ")
     usuarios_senha = input("Insira a senha do usuario: ")

     if usuarios_input == "" or usuarios_senha == "":
          print("Erro: Email ou senha nao podem ser vazios.")

     usuario_encontrado = False
     senha_correta = False     
     
     #percorre a lista de usuarios para validar as credenciais
     for usuario in usuarios:
          if usuario["username"] == usuarios_input:
               usuario_encontrado = True
               if usuario["senha"] == usuarios_senha:
                    senha_correta = True
                    break

     #Resultado da validacao
     if usuario_encontrado and senha_correta:
          print("Login bem-sucedido!")
     elif usuario_encontrado and not senha_correta:
          print("Erro: Senha incorreta.")
     else:
          print("Erro: Usuario nao encontrado.")

except Exception as erro:
     print(f"Ocorreu um erro: {erro}")