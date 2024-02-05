from app.repositories.city import CityRepository
from db.config import session as db_session
from app.models.city import City


class CityService:
    @staticmethod
    def list_cities():
        with db_session.begin() as session:
            result = CityRepository(session).get_all()
        return result

    @staticmethod
    def create(city: dict):
        with db_session.begin() as session:
            city = CityRepository(session).create(city)
            session.commit()
        return city

    @staticmethod
    def get_city(city_id: int):
        with db_session.begin() as session:
            city = CityRepository(session).get_by_id(city_id)
        return city


    @staticmethod
    def delete_city(city_id: int):
        with db_session.begin() as session:
            city = CityService.get_city(city_id)
            CityRepository(session).delete(city)
            session.commit()
        return city


    @staticmethod
    def update_city(city_id: int, updated_city: dict):
        with db_session.begin() as session:
            city = CityRepository(session).get_by_id(city_id)
            result = CityRepository(session).update(city, updated_city)
        return result
