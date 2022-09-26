from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class RoleChangeAudit(Base):
    __tablename__ = "role_change_audit_log"

    id = Column(Integer, primary_key=True)

    discord_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role_change_time = Column(DateTime(timezone=True), server_default=func.now())
    old_roles = Column(String(512))
    new_roles = Column(String(512))

    user = relationship("User", back_populates="audit_entries")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    role_description = Column(String(4096))
    user_create_time = Column(DateTime(timezone=True), server_default=func.now())
    discord_id = Column(Integer)
    discord_name = Column(String(38))

    audit_entries = relationship(
        "RoleChangeAudit",
        back_populates="user",
        cascade="all, delete-orphan"
    )
