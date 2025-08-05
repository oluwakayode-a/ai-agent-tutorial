from sqlmodel import Field, SQLModel, DateTime
from datetime import datetime, timezone



def get_utc_now():
    return datetime.now().replace(tzinfo=timezone.utc)

class ChatMessagePayload(SQLModel):
    message: str

class ChatMessage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    message: str
    created_at: datetime = Field(
        default_factory=get_utc_now, 
        sa_type=DateTime(timezone=True),
        primary_key=False,
        nullable=False
    )


class ChatMessageList(SQLModel):
    id: int | None = Field(default=None)
    message: str
    created_at: datetime = Field(default=None)

