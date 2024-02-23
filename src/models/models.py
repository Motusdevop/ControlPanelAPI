from pydantic import BaseModel

class ButtonModel(BaseModel):
    id: str
    on: bool

class ButtonsStage(BaseModel):
    one: bool
    two: bool