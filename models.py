from sqlalchemy import Column, Integer, String,Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class About(Base):
    __tablename__ = "about"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(255))
    bio = Column(Text,index=True)

class Expirience(Base):
    __tablename__ = "expirience"

    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(255))
    company = Column(String(255))
    start_date = Column(String)
    end_date = Column(String)
    about_id = Column(Integer, ForeignKey("about.id"))

    about = relationship("About",back_populates="expiriences")

class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(255))
    institution = Column(String(255))
    degree = Column(String(255))
    start_date = Column(String)
    end_date = Column(String)

    about = relationship("About",back_populates="educations")

About.expiriences = relationship("Expirience",back_populates="about", order_by=Expirience.id)
About.educations = relationship("Education",back_populates="about", order_by=Education.id)