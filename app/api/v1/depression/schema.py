from pydantic import BaseModel, Field

class DepressionRequest(BaseModel):
    query: str
    type: str
    top_k: int

class DepressionUpdate(BaseModel):
    id: int = Field(..., description="The ID of the depression record to update")
    query: str = Field(None, description="The updated query text")
    type: str = Field(None, description="The updated type")
    top_k: int = Field(None, description="The updated top_k value")