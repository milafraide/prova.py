class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.__idade = idade

    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, novo_idade):
        self.__idade = novo_idade

class Endereco:
    def __init__(self, estado, cidade):
        self.estado = estado
        self.__cidade = cidade

    def get_estado(self):
        return self.estado
    
    def set_estado(self, novo_estado):
        self.estado = novo_estado

    def get_cidade(self):
        return self.__cidade
    
    def set_cidade(self, novo_cidade):
        self.__cidade = novo_cidade

print("Faça seu cadastro:")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite a sua cidade: ")
estado = input("Digite o seu estado: ")

print("Seu cadastro foi concluído!")

pessoa = Pessoa(nome, idade)
endereco = Endereco(estado, cidade)

print(f"nome:{pessoa.get_nome()}")
pessoa.set_nome(input("Digite um novo nome: "))
print(f"nome atualizado:{pessoa.get_nome()}")

print(f"idade:{pessoa.get_idade()}")
pessoa.set_idade(int(input("Digite uma nova idade: ")))
print(f"idade atualizada:{pessoa.get_idade()}")

print(f"estado:{endereco.get_estado()}")
endereco.set_estado(input("Digite um novo estado: "))
print(f"estado atualizado:{endereco.get_estado()}")

print(f"cidade:{endereco.get_cidade()}")
endereco.set_cidade(input("Digite uma nova cidade: "))
print(f"cidade atualizada:{endereco.get_cidade()}")

print("Seu cadastro foi atualizado com sucesso!")


print("O que é pipeline? um processo de construção automatizado, envolvendo várias etapas para desenvolver e testar um código")
print("O que são requisitos funcionais e não funcionais? Requisitos não funcionais são as coisas usada na segurança e usabilidade que não são vísiveis para as pessoas que usam Exemplo: O site suportar 500 pessoas ao mesmo tempo, criptografar a senha dos usuários. Requisitos funcionais é tudo quando o usuários consegue acessar/mexer Ex: o usuário fazer login, acessar o site  ")
print("Quais são os pilares do modelo cascata? 1-satisfação do cliente, 2-ser receptivo a alterações, 3- efetuar entregas frequenetes de valor, 4-Colaboração diária, 5- Motivação individual, 6- Comunicação ativa, 7- Corresponder a medida de progresso, 8- Promover sustentabilidade, 9- Atenção frequente na excelencia, 10-Simpicidade é essencial, 11- equipe auto-organizadas 12-Reflexão regular de melhoria")