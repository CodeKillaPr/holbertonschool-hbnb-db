from persistence.IPersistenceManager import IPersistenceManager
from collections import defaultdict


class DataManager(IPersistenceManager):
    def __init__(self):
        # Usaremos un diccionario para almacenar las entidades en memoria.
        self.storage = defaultdict(dict)

    def save(self, entity):
        entity_type = type(entity).__name__
        self.storage[entity_type][entity.id] = entity

    def get(self, entity_id, entity_type):
        return self.storage[entity_type].get(entity_id, None)

    def update(self, entity):
        entity_type = type(entity).__name__
        if entity.id in self.storage[entity_type]:
            self.storage[entity_type][entity.id] = entity
        else:
            raise ValueError(
                f"Entity of type {entity_type} with ID {entity.id} does not exist.")

    def delete(self, entity_id, entity_type):
        if entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
        else:
            raise ValueError(
                f"Entity of type {entity_type} with ID {entity_id} does not exist.")
