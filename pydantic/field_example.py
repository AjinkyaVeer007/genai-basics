from pydantic import BaseModel
from typing import List, Dict, Optional

class cart(BaseModel):
    user_id : str
    items : List[str]
    quantities: Dict[str, int]

class blog(BaseModel):
    id: int
    content: str
    image_url: Optional[str] = None 