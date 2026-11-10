
from src.api.model import Resort

RESORTS = [
    Resort(1, "Bogus Basin", "Boise, Idaho"),
    Resort(2, "Brundage Mountain", "McCall, Idaho"),
    Resort(3, "Tamarack Resort", "Donnelly, Idaho"),
    Resort(4, "Sun Valley Resort", "Sun Valley, Idaho")
]

def get_all_resorts():
    return [resort.to_dict() for resort in RESORTS]

def get_resort_by_id(resort_id):
    for resort in RESORTS:
        if resort.id == resort_id:
            return resort.to_dict()

    return None
