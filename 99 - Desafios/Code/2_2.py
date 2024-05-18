class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.nome = nome
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
          
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
        saldo = self.plano.saldo
        mensagem = ""
        if saldo < 10:
            mensagem = "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo >= 50:
            mensagem = "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            mensagem = "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        return [saldo, mensagem]

# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)