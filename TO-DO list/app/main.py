from models.tarefas import Tarefas
from services.task_services import TarefasServices
from repositories.task_repository import TarefasRepositorio
from config.connection import Session
import os

def main():
    session = Session()
    repositorio = TarefasRepositorio(session)
    service = TarefasServices(repositorio)

    while True:

        print("=== TO-DO List ===")
        print("1 - Adicionar tarefas")
        print("2 - Mostrar tarefas")
        print("3 - Atualizar tarefas")
        print("4 - Excluir tarefas")
        print("0 - Sair")
        menu_opcoes = int(input("Escolha uma das opções acima: "))

        match menu_opcoes:

            case 1:
                os.system("cls || clear")
                nome = str(input("Digite o nome da tarefa: "))
                data = str(input("Digite a data que ela foi criada: "))

                tarefa = Tarefas(nome=nome, data=data)
                session.add(tarefa)
                session.commit()
                print()
            case 2:
                os.system("cls || clear")
                print("\nListando as tarefas")
                listar_tarefas = session.query(Tarefas).all()
                for tarefa in listar_tarefas:
                    print(f"{tarefa.nome} - {tarefa.data}")
            case 3:
                os.system("cls || clear")
                data_tarefa = str(input("Digite a data que a tarefa foi criada: "))
                tarefa = session.query(Tarefas).filter_by(data=data_tarefa).first()
                if tarefa:
                    tarefa.nome = str(input("Digite o nome da tarefa: "))
                    tarefa.data = str(input("Digite a data que a tarefa foi criada: "))
                    session.commit()
                else:
                    print("Tarefa não encontrada!")
            case 4:
                os.system("cls || clear")
                data_tarefa = str(input("Digite a data que a tarefa foi criada: "))
                tarefa = session.query(Tarefas).filter_by(data=data_tarefa).first()
                if tarefa:
                    session.delete(tarefa)
                    session.commit()
                    print("Tarefa deletada com sucesso!")
                else:
                    print("Tarefa não encontrada!")
            case 0:
                break

if __name__ == "__main__":
    os.system("cls || clear")
    main()