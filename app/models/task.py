from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.backend.db import Base
from app.models.user import *


class Task(Base):
    __table__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, idex=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'), index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates='task')


from sqlalchemy.schema import CreateTable

print(CreateTable(Task.__table__))
