from fastapi import APIRouter,Depends,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db
import Schema
import model
router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/team",tags=["Team"])
def allTeam(db:db_dependency):
    teamDetails= db.query(model.Team).all()
    return teamDetails

@router.get("/team/{id}",tags=["Team"])
def teamuser(id:int, db:db_dependency):
    team = db.query(model.Team).filter(model.User.id == id).first()
    if not team:
        raise HTTPException(status_code=404, detail=f"team with id {id} not found")
    return team

@router.post("/team",status_code=201,tags=["Team"]) 
def create_User(team: Schema.CreateTeam,db: db_dependency):
    newTeam = model.Team(teamname = team.teamname , teamSize = team.teamSize,members = team.members) # type: ignore
    db.add(newTeam)
    db.commit()
    db.refresh(newTeam)
    return newTeam

@router.delete("/team/{id}",status_code=204,tags=["Team"])
def delete_team(id:int,db: db_dependency):
    deleteCount = db.query(model.Team).filter(model.Team.id == id).delete(synchronize_session=False)
    if deleteCount == 0:
        raise HTTPException(status_code=404, detail=f"Team with id {id} not found")
    db.commit()    
    return "deleted"

@router.put("/Team/{id}",tags=["Team"])
def update(id:int , team: Schema.CreateTeam , db: db_dependency):
    updateTeam = db.query(model.Team).filter(model.Team.id == id)
    if not updateTeam.first():
        raise HTTPException(status_code=404, detail=f"team with id {id} not found")
    updateTeam.update(team.dict()) # type: ignore
    db.commit()
    updated_Team = db.query(model.Team).filter(model.Team.id == id).first()
    return updated_Team