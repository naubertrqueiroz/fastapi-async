from typing import Optional

from pydantic import BaseModel, HttpUrl


class ArtigoSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: str = HttpUrl
    usuario_id: Optional[int] = None

    class Config:
        from_attributes = True
