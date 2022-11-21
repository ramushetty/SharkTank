from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from uuid import UUID
import uuid
from database import Base


def generate_uuid():
    return str(uuid.uuid4())
class Pitch(Base):
    __tablename__ = "pitches"

    id = Column(String, name="uuid", primary_key=True, default=generate_uuid)
    entrepreneur = Column(String,nullable=False)
    pitchTitle = Column(String,nullable=False)
    pitchIdea = Column(String,nullable=False)
    askAmount = Column(Float,nullable=False)
    equity = Column(Float,nullable=False)

class Pitch_Offer(Base):
    __tablename__ = "pitches_offers"

    id = Column(String, name="uuid", primary_key=True, default=generate_uuid)
    pitch_id = Column(String, nullable=False )
    investor = Column(String,nullable=False)
    amount = Column(Float,nullable=False)
    equity = Column(Float,nullable=False)
    comment = Column(String,nullable=False)