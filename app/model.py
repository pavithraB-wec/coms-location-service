from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB

from app.database import Base


class TblConstituency(Base):
    __tablename__ = "tbl_constituency"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    constituency_name = Column(
        String(50),
        nullable=False
    )

    geo_json = Column(
        JSONB,
        nullable=False
    )