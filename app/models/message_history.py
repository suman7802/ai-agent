from typing import Optional
from pydantic import BaseModel


class Message_history(BaseModel):
    role: str
    content: str
    tool: Optional[str]
    input: Optional[str]
