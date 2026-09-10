from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.devops_sre_incident_responder.schemas import AgenticDevopsSreIncidentResponderSessionCreate, AgenticDevopsSreIncidentResponderSessionResponse
from app.domain.devops_sre_incident_responder.service import AgenticDevopsSreIncidentResponderService

router = APIRouter(prefix="/api/v1/devops_sre_incident_responder", tags=["Agentic Devops Sre Incident Responder Domain"])

@router.post("/sessions", response_model=AgenticDevopsSreIncidentResponderSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticDevopsSreIncidentResponderSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Devops Sre Incident Responder.
    """
    return AgenticDevopsSreIncidentResponderService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticDevopsSreIncidentResponderSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticDevopsSreIncidentResponderService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
