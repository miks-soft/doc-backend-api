from sqlalchemy.ext.declarative import (
    declared_attr,
    as_declarative,
)


@as_declarative()
class Base:
    id: any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
