import sqlite3

# Função para conectar ao banco de dados (arquivo SQLite)
def conectar():
    return sqlite3.connect('agenda.db')

# Criar a tabela contatos (se não existir) com os campos extras: endereco e cpf
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT,
            cpf TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar um contato
def adicionar_contato():
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    endereco = input('Endereço: ')
    cpf = input('CPF: ')
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contatos (nome, telefone, endereco, cpf)
        VALUES (?, ?, ?, ?)
    ''', (nome, telefone, endereco, cpf))
    conn.commit()
    conn.close()
    print('Contato adicionado com sucesso!')

# Função para listar todos os contatos
def listar_contatos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()
    conn.close()
    
    if contatos:
        for c in contatos:
            print(f"ID: {c[0]}, Nome: {c[1]}, Telefone: {c[2]}, Endereço: {c[3]}, CPF: {c[4]}")
    else:
        print('Nenhum contato encontrado.')

# Função para buscar contato por nome
def buscar_contato():
    nome_busca = input('Digite o nome para buscar: ')
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contatos WHERE nome LIKE ?', ('%' + nome_busca + '%',))
    contatos = cursor.fetchall()
    conn.close()
    
    if contatos:
        for c in contatos:
            print(f"ID: {c[0]}, Nome: {c[1]}, Telefone: {c[2]}, Endereço: {c[3]}, CPF: {c[4]}")
    else:
        print('Contato não encontrado.')

# Função para remover contato por ID
def remover_contato():
    listar_contatos()
    try:
        id_remover = int(input('Digite o ID do contato para remover: '))
    except ValueError:
        print('ID inválido.')
        return
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contatos WHERE id = ?', (id_remover,))
    conn.commit()
    if cursor.rowcount > 0:
        print('Contato removido com sucesso.')
    else:
        print('ID não encontrado.')
    conn.close()

# Menu simples para usar as funções
def menu():
    criar_tabela()
    while True:
        print('\n--- AGENDA DE CONTATOS ---')
        print('1 - Adicionar contato')
        print('2 - Listar contatos')
        print('3 - Buscar contato')
        print('4 - Remover contato')
        print('0 - Sair')
        
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '4':
            remover_contato()
        elif opcao == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    menu()
