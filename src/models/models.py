from pydantic import BaseModel

class ButtonModel(BaseModel):
    id: str
    on: bool