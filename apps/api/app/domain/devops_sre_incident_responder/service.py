from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.devops_sre_incident_responder.models import AgenticDevopsSreIncidentResponderSession, AgenticDevopsSreIncidentResponderItem
from app.domain.devops_sre_incident_responder.schemas import AgenticDevopsSreIncidentResponderSessionCreate, AgenticDevopsSreIncidentResponderItemCreate

class AgenticDevopsSreIncidentResponderService:
    @staticmethod
    def create_session(db: Session, data: AgenticDevopsSreIncidentResponderSessionCreate) -> AgenticDevopsSreIncidentResponderSession:
        db_obj = AgenticDevopsSreIncidentResponderSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticDevopsSreIncidentResponderSession:
        return db.query(AgenticDevopsSreIncidentResponderSession).filter(AgenticDevopsSreIncidentResponderSession.id == session_id).first()
