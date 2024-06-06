from model.BaseModel import BaseModel


class City(BaseModel):
    def __init__(self, country_id, name, **kwargs):
        super().__init__(**kwargs)
        self.country_id = country_id
        self.name = name

    def __str__(self):
        return f"[City] ({self.id}) {self.to_dict()}"
