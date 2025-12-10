from pydantic import BaseModel, Field
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = True

    model_config = {
        "from_attributes": True,  
        "json_schema_extra": {    
            "example": {
                "username": "john_doe",
                "email": "johndoe@gmail.com",
                "password": "password123",
                "is_staff": False,
                "is_active": True
            }
        }
    }
