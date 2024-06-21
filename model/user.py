from model.BaseModel import BaseModel


class User(BaseModel):
    def __init__(self, email, first_name="", last_name="", **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"[User] ({self.id}) {self.to_dict()}"
