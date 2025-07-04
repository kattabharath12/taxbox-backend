
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Dependent(BaseModel):
    name: str
    age: int
    relation: str

class TaxProfile(BaseModel):
    filing_status: str
    dependents: List[Dependent]

@router.post("/")
def save_profile(profile: TaxProfile):
    return {"message": "Profile saved", "data": profile}
