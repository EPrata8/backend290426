from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Tarefa
from schemas import TarefaCreate, TarefaResponse

app = FastAPI(title="API de Tarefas", version="1.0.0")


# ── CREATE ──────────────────────────────────────────────────────────────────

@app.post(
    "/tarefas",
    response_model=TarefaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar nova tarefa",
)
def criar_tarefa(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    nova_tarefa = Tarefa(
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        concluida=False,
    )
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa


# ── READ ALL ─────────────────────────────────────────────────────────────────

@app.get(
    "/tarefas",
    response_model=List[TarefaResponse],
    summary="Listar todas as tarefas",
)
def listar_tarefas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    tarefas = db.query(Tarefa).offset(skip).limit(limit).all()
    return tarefas


# ── READ ONE ─────────────────────────────────────────────────────────────────

@app.get(
    "/tarefas/{tarefa_id}",
    response_model=TarefaResponse,
    summary="Buscar tarefa por ID",
)
def buscar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com id {tarefa_id} não encontrada.",
        )
    return tarefa


# ── UPDATE ───────────────────────────────────────────────────────────────────

@app.put(
    "/tarefas/{tarefa_id}",
    response_model=TarefaResponse,
    summary="Atualizar tarefa",
)
def atualizar_tarefa(
    tarefa_id: int,
    dados: TarefaCreate,
    db: Session = Depends(get_db),
):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com id {tarefa_id} não encontrada.",
        )
    tarefa.titulo = dados.titulo
    tarefa.descricao = dados.descricao
    db.commit()
    db.refresh(tarefa)
    return tarefa


# ── PATCH concluída ───────────────────────────────────────────────────────────

@app.patch(
    "/tarefas/{tarefa_id}/concluir",
    response_model=TarefaResponse,
    summary="Marcar/desmarcar tarefa como concluída",
)
def concluir_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com id {tarefa_id} não encontrada.",
        )
    tarefa.concluida = not tarefa.concluida
    db.commit()
    db.refresh(tarefa)
    return tarefa


# ── DELETE ───────────────────────────────────────────────────────────────────

@app.delete(
    "/tarefas/{tarefa_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletar tarefa",
)
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com id {tarefa_id} não encontrada.",
        )
    db.delete(tarefa)
    db.commit()
