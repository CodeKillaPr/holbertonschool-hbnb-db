from persistence.IPersistenceManager import IPersistenceManager


class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}

    def save(self, entity):
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity.id] = entity
        entity.save()

    def get(self, entity_id, entity_type):
        if entity_type in self.storage:
            for entity in self.storage[entity_type].values():
                if entity.id == entity_id or entity.code == entity_id:
                    return entity
        return None

    def update(self, entity):
        entity_type = type(entity).__name__
        if entity_type in self.storage and entity.id in self.storage[entity_type]:
            self.storage[entity_type][entity.id] = entity
            entity.save()
        else:
            raise ValueError("Entity not found in storage")

    def delete(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
        else:
            raise ValueError("Entity not found in storage")
