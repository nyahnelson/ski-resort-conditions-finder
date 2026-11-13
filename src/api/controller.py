
from src.api.model import Resort
from src.services.database import db


def get_all_resorts():
    resorts = db.session.execute(
        db.select(Resort).order_by(Resort.id)
    ).scalars().all()

    return [resort.to_dict() for resort in resorts]


def get_resort_by_id(resort_id):
    resort = db.session.get(Resort, resort_id)

    if resort is None:
        return None

    return resort.to_dict()
