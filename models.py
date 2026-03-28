from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class JobPost(Base):
    __tablename__ = 'job_posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class Candidate(Base):
    __tablename__ = 'candidates'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String)


class CandidateInteraction(Base):
    __tablename__ = 'candidate_interactions'

    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey('candidates.id'), nullable=False)
    job_post_id = Column(Integer, ForeignKey('job_posts.id'), nullable=False)
    interaction_date = Column(DateTime, nullable=False)
    notes = Column(String)

    candidate = relationship("Candidate")
    job_post = relationship("JobPost")


class Interview(Base):
    __tablename__ = 'interviews'

    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey('candidates.id'), nullable=False)
    job_post_id = Column(Integer, ForeignKey('job_posts.id'), nullable=False)
    interview_date = Column(DateTime, nullable=False)
    interviewers = Column(String)
    feedback = Column(String)

    candidate = relationship("Candidate")
    job_post = relationship("JobPost")