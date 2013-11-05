""" SQLAlchemy models """
from steward_sqlalchemy import declarative_base
from sqlalchemy import Column, Integer, UnicodeText, PickleType


Base = declarative_base() # pylint: disable=C0103

class Announcement(Base):
    """
    An announcement

    Parameters
    ----------
    text : str
        The text of the announcement
    **kwargs : dict
        Any additional metadata about the announcement

    Attributes
    ----------
    text : str
        The text of the announcement
    data : dict
        Metadata for the announcement

    """
    __tablename__ = 'announcements'
    id = Column(Integer, primary_key=True)
    text = Column(UnicodeText())
    data = Column(PickleType())

    def __init__(self, text, **kwargs):
        self.text = text
        self.data = kwargs

    def __json__(self, request=None):
        return {'id': self.id,
                'text': self.text,
                'data': self.data,
                }
