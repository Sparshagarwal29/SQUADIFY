from pydantic import BaseModel,field
from typing import List, Optional

def employ(basemodel):
    id = int
    name = str = Field(...,min_length = 3)  #if Field(...) this three dot means required 
    department = Optional[str] = "general"
    salary = float = Field(...,ge=10000)

    