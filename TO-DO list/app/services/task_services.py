from models.tarefas import Tarefas
from repositories.task_repository import TarefasRepositorio

class TarefasServices:
    def __init__(self, repositorio: TarefasRepositorio) -> None:
        self.repositorio = repositorio

    def criar_tarefa(self, nome: str, data: str):
        try:
            tarefa = Tarefas(nome=nome, data=data)

            registrado = self.repositorio.buscar_tarefa_pela_data(data=tarefa.data)

            if registrado:
                print("Tarefa criada com sucesso!")
                return
        
            self.repositorio.salvar_tarefa(tarefas=tarefa)
            print("Tarefa registrada com sucesso!")
        except TypeError as error:
            print(f"Erro ao salvar tarefa: {error}")
        except Exception as error:
            print(f"Ocorreu um erro inesperado: {error}")

    def listar_todas_as_tarefas(self):
        return self.repositorio.listar_tarefas()