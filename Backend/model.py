from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class TeamMember(Base):
    __tablename__ = "team_members"
    id = Column(Integer, primary_key=True, index=True)
    Name: Column(String, index=True)
    Role: Column(String, index=True)
    Email: Column(String, unique=True, index=True)
    contact:  Column(String)
    TechStack: Column(String)
    Hobbies: Column(String, nullable=True)
    team = relationship("Team", back_populates="members")
    teamSize: Column(String, index=True)
    members: List[TeamMember]

    