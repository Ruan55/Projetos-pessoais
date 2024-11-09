from models.tarefas import Tarefas
from sqlalchemy.orm import Session

class TarefasRepositorio:
    def __init__(self, session: Session) -> None:
        self.session = session

    def salvar_tarefa(self, tarefas: Tarefas):
        self.session.add(tarefas)
        self.session.commit()

    def buscar_tarefa_pela_data(self, data:str):
        return self.session.query(Tarefas).filter_by(data=data).first()
    
    def deletar_tarefa(self, tarefas: Tarefas):
        self.session.delete(tarefas)
        self.session.commit()

    def listar_tarefas(self):
        return self.session.query(Tarefas).all()