from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DECIMAL

class Base(DeclarativeBase):
    pass


class City(Base):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    region: Mapped[str] = mapped_column(String(256))
    municipality: Mapped[str] = mapped_column(String(256))
    settlement: Mapped[str] = mapped_column(String(256))
    oktmo: Mapped[str] = mapped_column(String(32))
    latitude_dd: Mapped[DECIMAL] = mapped_column(DECIMAL(15, 2), nullable=True)
    longitude_dd: Mapped[DECIMAL] = mapped_column(DECIMAL(15, 2), nullable=True)
    year: Mapped[int] = mapped_column(Integer, nullable=True)
    birth: Mapped[DECIMAL] = mapped_column(DECIMAL(5, 1), nullable=True)
    crimes: Mapped[int] = mapped_column(DECIMAL(6, 1), nullable=True)
    death: Mapped[DECIMAL] = mapped_column(DECIMAL(5, 1), nullable=True)
    doctors: Mapped[int] = mapped_column(Integer, nullable=True)
    doctors_per10: Mapped[DECIMAL] = mapped_column(DECIMAL(5, 1), nullable=True)
    hospitals: Mapped[int] = mapped_column(Integer, nullable=True)
    job_regist: Mapped[int] = mapped_column(DECIMAL(6, 1), nullable=True)
    n_companies: Mapped[int] = mapped_column(Integer, nullable=True)
    pens: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 1), nullable=True)
    pop_work: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 1), nullable=True)
    wage: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 1), nullable=True)







