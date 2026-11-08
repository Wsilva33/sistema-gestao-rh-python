funcionarios = []


def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    print()

    cargo = input("Qual o cargo do funcionário? ")
    print()

    horario = input("Qual o horário de trabalho desse funcionário? ")
    print()

    funcionario_ativo = input("O funcionário ainda está ativo? (Sim/Não): ")

    if funcionario_ativo.strip().lower() == "sim":
        ativo = True
    else:
        ativo = False

    print()

    salario = float(input("Qual o salário desse funcionário? "))
    print()

    horas_dias = float(input("Quantas horas por dia este funcionário trabalha? "))
    print()

    dias_semanas = float(input("Quantos dias da semana esse funcionário trabalha? "))

    # Cálculos
    horas_semanas = horas_dias * dias_semanas
    horas_mensais = horas_semanas * 4
    valor_hora = salario / horas_mensais if horas_mensais > 0 else 0

    print()
    print(f"Funcionário: {nome}")
    print(f"Cargo: {cargo}")
    print(f"Salário: R$ {salario:.2f}")
    print(f"Horas por semana: {horas_semanas}")
    print(f"Horas aproximadamente por mês: {horas_mensais}")
    print(f"Valor da hora: R$ {valor_hora:.2f}")

    # Dicionário do funcionário
    funcionario = {
        "nome": nome,
        "cargo": cargo,
        "horario": horario,
        "ativo": ativo,
        "salario": salario,
        "horas_dias": horas_dias,
        "registro_ponto": [],
        "dias_semanas": dias_semanas,
        "horas_semanas": horas_semanas,
        "horas_mensais": horas_mensais,
        "valor_hora": valor_hora,
    }

    # Adiciona na lista
    funcionarios.append(funcionario)

    print()
    print("Funcionário cadastrado com sucesso!\n")


def funcionarios_ativos():
    ativos = 0
    print("\n--- Funcionários Ativos ---")
    for funcionario in funcionarios:
        if funcionario["ativo"]:
            ativos += 1
            print(f"- {funcionario['nome']} ({funcionario['cargo']})")

    print(f"Total de funcionários ativos: {ativos}\n")


def funcionarios_desligados():
    desligados = 0
    print("\n--- Funcionários Desligados ---")
    for funcionario in funcionarios:
        # Verifica se 'ativo' é False (ou seja, está desligado)
        if not funcionario["ativo"]:
            desligados += 1
            print(f"- {funcionario['nome']} ({funcionario['cargo']})")

    print(f"Total de funcionários desligados: {desligados}\n")

    print()

def banco_de_horas():
    print("\n--- REGISTRO DE BANCO DE HORAS ---")
    nome_busca = input("Digite o nome do funcionário: ")
    print()

    # 1. Procurar o funcionário dentro da lista
    funcionario_encontrado = None
    for f in funcionarios:
        if f["nome"].strip().lower() == nome_busca.strip().lower():
            funcionario_encontrado = f
            break

def editar_funcionario():
    print("\n--- EDITAR / DESLIGAR FUNCIONÁRIO ---")
    nome_busca = input("Digite o nome do funcionário que deseja alterar: ")

    print()

    # 1. Busca o funcionário na lista
    funcionario_encontrado = None
    for f in funcionarios:
        if f["nome"].strip().lower() == nome_busca.strip().lower():
            funcionario_encontrado = f
            break

    if funcionario_encontrado is None:
        print("Funcionário não encontrado!\n")
        return

    # 2. Exibe as opções de edição
    print(f"Funcionário selecionado: {funcionario_encontrado['nome']}")
    print(
        f"Status atual: {'Ativo' if funcionario_encontrado['ativo'] else 'Desligado'}"
    )
    print("1 - Alterar Cargo")
    print("2 - Alterar Salário")
    print("3 - Alternar Status (Ativar / Desligar)")
    print("4 - Voltar")

    opcao_edicao = input("Escolha o que deseja alterar: ")

    if opcao_edicao == "1":
        novo_cargo = input("Digite o novo cargo: ")
        funcionario_encontrado["cargo"] = novo_cargo
        print("Cargo atualizado com sucesso!\n")

    elif opcao_edicao == "2":
        novo_salario = float(input("Digite o novo salário: R$ "))
        funcionario_encontrado["salario"] = novo_salario

        # Recalcula o valor da hora com o novo salário
        horas_mensais = funcionario_encontrado["horas_mensais"]
        funcionario_encontrado["valor_hora"] = (
            novo_salario / horas_mensais if horas_mensais > 0 else 0
        )
        print("Salário e valor da hora atualizados com sucesso!\n")

    elif opcao_edicao == "3":
        # Inverte o status atual (Se True vira False, se False vira True)
        funcionario_encontrado["ativo"] = not funcionario_encontrado["ativo"]
        novo_status = (
            "Ativo" if funcionario_encontrado["ativo"] else "Desligado"
        )
        print(
            f"Status de {funcionario_encontrado['nome']} alterado para: {novo_status}!\n"
        )

    elif opcao_edicao == "4":
        return

    # Se não encontrar ninguém com esse nome:
    if funcionario_encontrado is None:
        print("Funcionário não encontrado!")
        return  # Encerra a função e volta para o menu

    # 2. Guardar as respostas do usuário em variáveis
    entrada = input("1. Horário de entrada (HH:MM): ")
    saida_almoco = input("2. Horário de saída almoço (HH:MM): ")
    retorno_almoco = input("3. Horário de retorno do almoço (HH:MM): ")
    saida = input("4. Horário de saída (HH:MM): ")

    formato = "%H:%M"

    h_entrada = datetime.strptime(entrada, formato)
    h_saida_almoco = datetime.strptime(saida_almoco, formato)
    h_retorno_almoco = datetime.strptime(retorno_almoco, formato)
    h_saida = datetime.strptime(saida, formato)

    turno_manha = h_saida_almoco - h_entrada
    turno_tarde = h_saida - h_retorno_almoco
    tempo_total = turno_manha + turno_tarde

    horas_trabalhadas = tempo_total.total_seconds() / 3600
    saldo_dia = horas_trabalhadas - funcionario_encontrado["horas_dias"]

    # 4. Exibe o resultado na tela para o usuário
    print("\n--- Resultado do Dia ---")
    print(f"Horas trabalhadas: {horas_trabalhadas:.2f}h")
    print(f"Saldo do dia: {saldo_dia:.2f}h")

# MENU DO SISTEMA

while True:
    print("1 - Cadastro")
    print("2 - Funcionários ativos")
    print("3 - Funcionários desligados")
    print("4 - Banco de horas")
    print("5 - Horas extras")
    print("6 - Editar funcionario")
    print("7 - Sair")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        cadastrar_funcionario()

    elif opcao == "2":
        funcionarios_ativos()

    elif opcao == "3":
        # Chamada da função corrigida
        funcionarios_desligados()

    elif opcao == "4":
        print("Banco de horas")

    elif opcao == "5":
        print("Horas extras")

    elif opcao == "6":
        print("Editar funcionario")

    elif opcao == "7":
        print("Saindo...")
        print("Volte sempre")
        break
