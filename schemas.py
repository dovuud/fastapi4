from pydantic import BaseModel
from typing import Optional,List

class ExpirienceBase(BaseModel):
    title: str
    company: str
    start_date:str
    end_date:str

class ExpirienceCreate(ExpirienceBase):
    pass

class Expirience(ExpirienceBase):
    id: int

    class Config:
        orm_mode = True

class EducationBase(BaseModel):
    title: str
    institution: str
    degree: str
    start_date:str
    end_date:str

class EducationCreate(EducationBase):
    pass

class Education(EducationBase):
    id: int
    class Config:
        orm_mode = True

class AboutBase(BaseModel):
    name: str
    bio: Optional[str]

class AboutCreate(AboutBase):
    pass

class About(AboutBase):
    id: int
    experiences: List[Expirience] = []
    educations: List[Education] = []

    class Config:
        orm_mode = True