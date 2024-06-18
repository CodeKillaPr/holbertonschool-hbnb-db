from model.BaseModel import BaseModel


class Country(BaseModel):
    def __init__(self, name, code, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.code = code

    def __str__(self):
        return f"[Country] ({self.id}) {self.to_dict()}"
