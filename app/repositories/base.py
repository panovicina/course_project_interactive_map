from sqlalchemy import select, update
from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, session: Session):
        self.session = session

    def _create(self, instance):
        self.session.add(instance)
        self.session.flush()
        return instance

    def _get(self, model_cls, filter):
        result = self.session.execute(
            select(model_cls).filter_by(id=filter)
        )
        return result.scalar()

    def _get_all(self, model_cls):
        result = self.session.execute(select(model_cls))
        return result.scalars().all()

    def _update(self, model_csl, instance, values: dict):
        query = (
            update(model_csl)
            .where(model_csl.id == instance.id)
            .values(**values)
        )
        result = self.session.execute(query)
        self.session.flush()
        return result

    def delete(self, instance):
        self.session.delete(instance)
        self.session.flush()