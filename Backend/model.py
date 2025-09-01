from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship 

from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, index=True, nullable=False)
    team_size = Column(Integer, nullable=False)
    members = relationship("TeamMember", back_populates="team")

class TeamMember(Base):
    __tablename__ = "team_members"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    role = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True)
    contact = Column(String, index=True)
    tech_stack = Column(String)
    hobbies = Column(String, nullable=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="members")