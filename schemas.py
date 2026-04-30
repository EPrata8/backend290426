from pydantic import BaseModel
from typing import Optional

#Entrada: criação de uma tarefa
class TarefaCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None

#Saída: Tarefa lida do banco
class TarefaResponse(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    concluida: bool

class Config:
    from_attributes = True #lê do ORM