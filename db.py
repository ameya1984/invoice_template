from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
import logging
import os

if os.environ.get('ENVIRONMENT') == 'qa':
    from environment.qa import DEBUG, SQLALCHEMY_DATABASE_URI, echo
elif os.environ.get('ENVIRONMENT') == 'production':
    from environment.production import DEBUG, SQLALCHEMY_DATABASE_URI, echo
else:
    from environment.development import DEBUG, SQLALCHEMY_DATABASE_URI, echo

logger = logging.getLogger('invoice')

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=echo)


def get_session():
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    return Session()


