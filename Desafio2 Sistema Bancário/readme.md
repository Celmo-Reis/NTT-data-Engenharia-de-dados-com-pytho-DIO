
# Objetivo geral :

1) Separar as função de saque, deposito, extrato.

2) Criar 2 funções: cadastrar usuários(cliente) e cadastrar conta bancaria.

## Cada função vai ter uma regra na passagem de argumento

- **Saque** 
Deve receber argumentos apenas por nome(keyword only). sugestão de argumentos: saldo, valor, extrato, limite, numero saques, limite saques. Sugestao de retorno: saldo e extrado.

- **Deposito** 
Deve receber apenas por posição. saldo, valor, extrato. sugestão de retorno saldo, extrato.

- **Extrato** 
Posicionais : saldo.  nomeado= extrato

- **Criar usuário (cliente)** 
Armazerar o usuário em uma lista. Usuário composto por nome, data de nascimento, cpf e endereço. endereto é uma string com o formato: logradouto - nro - bairro - cidade/sigla estado. apenas armazenar os números de cpf. não pode cadastrar 2 usuários iguais

- **Criar conta corrente** 
O programa deve armazenar uma conta em uma lista, uma conta é composta por agencia, numero da conta e usuário. numero da conta sequencial, iniciada em 1. o numero da agencia é fixo 0001. o usuário pode ter mais de uma conta, mas uma conta pertente somente a 1 usuario







