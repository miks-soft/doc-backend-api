from sqlalchemy import (
    Text,
    ARRAY,
    Column,
    Integer,
    BigInteger,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from db.base_class import Base


class Field(Base):
    __tablename__ = 'fields'

    id = Column(BigInteger, primary_key=True, index=True)

    value = Column(Text)
    value_box = Column(ARRAY(Integer))
    description = Column(Text, nullable=False)

    page_id = Column(BigInteger, ForeignKey('pages.id'))
    document_id = Column(BigInteger, ForeignKey('documents.id'))

    page = relationship('Page', back_populates='fields')
