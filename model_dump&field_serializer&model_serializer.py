from pydantic import BaseModel, EmailStr,field_serializer,model_serializer

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

# Pydantic automatically converts the string "123" to an integer for account_id.
user = User(name="ali bigdeli", email="bigdeli.ali3@gmail.com", account_id="123")

# --- Interactive Session Examples ---

user.model_dump() # as dictionary (.dict is deprecated)
# Output: {'name': 'ali bigdeli', 'email': 'bigdeli.ali3@gmail.com', 'account_id': 123}

user.model_dump_json() # as json (.json is deprecated)
# Output: '{"name":"ali bigdeli","email":"bigdeli.ali3@gmail.com","account_id":123}'

user.model_dump_json(indent=2)
# Output:
# {
#   "name": "ali bigdeli",
#   "email": "bigdeli.ali3@gmail.com",
#   "account_id": 123
# }


###############################################

# --- Behavior without a custom serializer ---

# m = Model(number=1/3)
# print(m.model_dump())
# Output: {'number': 0.3333333333333333}


# --- Now with the custom serializer ---

class Model(BaseModel):
    number: float

    @field_serializer("number")
    def serialize_float(self, value):
        return round(value, 2)

    # @field_serializer(name,when_used="json-unless-none")
    # will be applied only to json serializer and will be affected only if its none

# --- Instantiating and dumping the model with the serializer ---

m = Model(number=1/3)
print(m.model_dump())
# Output: {'number': 0.33}



#####################################################

class User(BaseModel):
    id: int
    name: str
    is_active: bool

    # Custom serializer to modify the output format
    @model_serializer
    def custom_serializer(self) -> dict:
        # Customizing the output
        return {
            "user_id": self.id,
            "full_name": self.name.upper(), # Convert name to uppercase
            "status": "active" if self.is_active else "inactive",
        }

# Example usage
user = User(id=1, name="John Doe", is_active=True)

# Serialize the model (e.g., for JSON output)
print(user.model_dump_json()) # Output: {"user_id": 1, "full_name": "JOHN DOE", "status": "active"}