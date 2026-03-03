from database.connection import init_db
from services import task_service

def run_tests():
    # 1. Inicializa o banco (cria o arquivo sqlite e as tabelas)
    init_db()
    print("Banco de dados inicializado!\n")

    user_numero = "5511999999999"

    # 2. Testando CREATE
    print("Adicionando tarefas...")
    task_service.create_task(user_numero, "Estudar cálculo", "Estudos")
    task_service.create_task(user_numero, "Revisar código Python", "Trabalho")

    # 3. Testando READ
    print("\nListando pendências:")
    pendentes = task_service.get_pending_tasks(user_numero)
    for t in pendentes:
        print(f"[{t.id}] {t.title} ({t.category})")

    # 4. Testando UPDATE
    if pendentes:
        id_para_concluir = pendentes[0].id
        print(f"\nConcluindo a tarefa ID {id_para_concluir}...")
        task_service.complete_task(id_para_concluir, user_numero)

    # 5. Lendo novamente para confirmar
    print("\nListando pendências após conclusão:")
    pendentes_atualizadas = task_service.get_pending_tasks(user_numero)
    for t in pendentes_atualizadas:
        print(f"[{t.id}] {t.title} ({t.category})")

if __name__ == "__main__":
    run_tests()