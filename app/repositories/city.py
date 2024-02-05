from sqlalchemy.orm import Session
from app.models.city import City
from app.repositories.base import BaseRepository


class CityRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)

    def create(self, data: dict):
        city = City(**data)
        return self._create(city)

    def get_by_id(self, city_id):
        return self._get(City, city_id)

    def get_all(self):
        return self._get_all(City)

    async def update(self, instance: City, values: dict):
        return await self._update(City, instance, values)

