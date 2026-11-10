
from dataclasses import dataclass

@dataclass
class Resort:
    id: int
    name: str
    location: str

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location
        }
