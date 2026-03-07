class DataModel:
    """
    Represents a data record used in the application
    """

    def __init__(self, id, value):
        self.id = id
        self.value = value

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value
        }

    def __str__(self):
        return f"DataModel(id={self.id}, value={self.value})"