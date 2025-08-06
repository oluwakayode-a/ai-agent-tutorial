from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from .models import ChatMessagePayload, ChatMessage, ChatMessageList
from typing import List
from api.db import get_session
from api.ai.services import generate_email_message
from api.ai.schemas import EmailMessageSchema

router = APIRouter()


@router.get("/")
def chat_health():
    return {"hello": "world"}


@router.post("/", response_model=EmailMessageSchema)
def create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)
):
    data = payload.model_dump()
    
    try:
        obj = ChatMessage.model_validate(data)
    except Exception as e:
        print(e)

    session.add(obj)
    session.commit()
    # session.refresh(obj)

    response = generate_email_message(payload.message)
    return response


@router.get("/recent/", response_model=List[ChatMessageList])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]

    return results

