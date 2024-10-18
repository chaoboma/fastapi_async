from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, MetaData, Double, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from database import Base

class AllPoints(Base):
    __tablename__ = "all_points"
    metadata = MetaData()
    id = Column(Integer, primary_key=True)
    line_name = Column(String)
    line_code = Column(Integer)
    lng = Column(Float)
    lat = Column(Float)
    create_time = mapped_column(DateTime)
    update_time = mapped_column(DateTime)
    delete_flag = Column(Boolean)