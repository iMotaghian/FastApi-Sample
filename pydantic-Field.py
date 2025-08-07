from pydantic import BaseModel

class Example(BaseModel):
    integer: int
    floating_point: float
    boolean: bool
    string: str

#################################################################################

from typing import List, Tuple, Set, Dict
from pydantic import BaseModel

class Example(BaseModel):
    list_field: List[int]
    tuple_field: Tuple[str, int]
    set_field: Set[str]
    dict_field: Dict[str, int]

#################################################################################    
    
from typing import Optional, Union
from pydantic import BaseModel

class Example(BaseModel):
    optional_field: Optional[str] # Can be str or None
    union_field: Union[int, str] # Can be int or str
    
#################################################################################   
    
from pydantic import BaseModel, EmailStr, HttpUrl
from uuid import UUID

class Example(BaseModel):
    uuid_field: UUID
    email_field: EmailStr
    url_field: HttpUrl
    
#################################################################################

from pydantic import BaseModel, FilePath, DirectoryPath

class Example(BaseModel):
    file_path: FilePath
    directory_path: DirectoryPath
    
#################################################################################

from datetime import date, time, datetime, timedelta
from pydantic import BaseModel

class Example(BaseModel):
    date_field: date
    time_field: time
    datetime_field: datetime
    timedelta_field: timedelta
    
  
#################################################################################

from pydantic import BaseModel, StrictStr, StrictInt, StrictFloat, StrictBool

class Example(BaseModel):
    strict_string: StrictStr
    strict_int: StrictInt
    strict_float: StrictFloat
    strict_bool: StrictBool
    
#################################################################################   

from enum import Enum
from pydantic import BaseModel

class Color(str, Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

class Example(BaseModel):
    color: Color
    
#################################################################################

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zipcode: str

class User(BaseModel):
    name: str
    address: Address
    
#################################################################################

from pydantic import BaseModel

class CustomType:
    def __init__(self, value):
        self.value = value

class Example(BaseModel):
    custom_field: CustomType
    
    
#################################################################################

from typing import Annotated
from pydantic import BaseModel, Field

class Example(BaseModel):
    age: Annotated[int, Field(gt=0, description="Age must be greater than 0")]
    
#################################################################################


from typing import Literal
from pydantic import BaseModel

class Example(BaseModel):
    status: Literal["active", "inactive"]
    
    
#################################################################################

from decimal import Decimal
from pydantic import BaseModel

class Example(BaseModel):
    price: Decimal
    
 #################################################################################
   
    
from pydantic import BaseModel, Field

class Example(BaseModel):
    name: str = Field(default="John Doe")

example = Example()
print(example.name) # Output: "John Doe"

#################################################################################


from pydantic import BaseModel, Field

class Example(BaseModel):
    name: str = Field(default="John Doe", description="The user's name", example="Alice")

print(Example.model_json_schema())

# Includes metadata in the schema:
# {
#     "title": "Example",
#     "properties": {
#         "name": {
#             "title": "Name",
#             "default": "John Doe",
#             "description": "The user's name",
#             "examples": ["Alice"]
#         }
#     }
# }    

#################################################################################

from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    id: int = Field(..., gt=0, description="The unique ID of the user")
    username: str = Field(..., min_length=3, max_length=15, regex=r'^\w+$')
    email: str = Field(..., alias="userEmail", regex=r'^\S+@\S+\.\S+$')
    age: int = Field(default=None, gt=0, lt=120, description="User's age (optional)")
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Note that 'userEmail' is used here because of the alias in the email field.
user = User(userEmail="test@example.com", id=1, username="JohnDoe")

print(user.model_dump())

# Output:
# {
#     'id': 1,
#     'username': 'JohnDoe',
#     'email': 'test@example.com',
#     'age': None,
#     'created_at': datetime.datetime(2025, 8, 7, 9, 34, 41, 123456) # زمان دقیق متفاوت خواهد بود
# }