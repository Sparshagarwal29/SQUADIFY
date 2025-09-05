from fastapi import APIRouter,Depends,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db
import Schema
import model
router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/team",response_model=list[Schema.showTeam],tags=["Team"])
def allTeam(db:db_dependency):
    teams= db.query(model.Team).all()
    return teams

@router.get("/team/{id}",response_model=Schema.showTeam,tags=["Team"])
def teamuser(id:int, db:db_dependency):
    team = db.query(model.Team).filter(model.Team.id == id).first()
    if not team:
        raise HTTPException(status_code=404, detail=f"team with id {id} not found")
    return team

@router.post("/team",status_code=201,response_model=Schema.showTeam,tags=["Team"]) 
def create_User(team: Schema.CreateTeam,db: db_dependency):
    newTeam = model.Team(team_name = team.team_name , team_size = team.team_size) 
    db.add(newTeam)
    db.flush()
    for member_data in team.members:
        member = model.TeamMember(
            name=member_data.name,
            role=member_data.role,
            email=member_data.email,
            contact=member_data.contact,
            tech_stack=member_data.tech_stack,
            hobbies=member_data.hobbies,
            team_id=newTeam.id
        )
        db.add(member)

    db.commit()
    db.refresh(newTeam)
    return newTeam


@router.delete("/team/{id}", status_code=204, tags=["Team"])
def delete_team(id: int, db: db_dependency):
    team = db.query(model.Team).filter(model.Team.id == id).first()
    if not team:
        raise HTTPException(status_code=404, detail=f"Team with id {id} not found")
    db.delete(team)  
    db.commit()   
    # return "deleted"

@router.put("/team/{id}",response_model=Schema.showTeam,tags=["Team"])
def update(id:int , team: Schema.CreateTeam , db: db_dependency):
    existing_team = db.query(model.Team).filter(model.Team.id == id).first()
    if not existing_team:
        raise HTTPException(status_code=404, detail=f"Team with id {id} not found")
    existing_team.team_name = team.team_name # type: ignore
    existing_team.team_size = team.team_size # type: ignore
    db.query(model.TeamMember).filter(model.TeamMember.team_id == id).delete()
    
    for member_data in team.members:
        member = model.TeamMember(
            name=member_data.name,
            role=member_data.role,
            email=member_data.email,
            contact=member_data.contact,
            tech_stack=member_data.tech_stack,
            hobbies=member_data.hobbies,
            team_id=id
        )
        db.add(member)
    
    db.commit()
    db.refresh(existing_team)
    return existing_team