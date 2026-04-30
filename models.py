from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean
from database import Base

class Tarefa(Base):
    __tablename__ = "tarefas"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    titulo: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    descricao: Mapped[str] = mapped_column(
        String(300), nullable=True
    )
    concluida: Mapped[bool] = mapped_column(
        Boolean, default=False
    )