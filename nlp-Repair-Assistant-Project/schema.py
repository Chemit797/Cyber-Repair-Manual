import json
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field, field_validator
from collections import defaultdict

class AskQuestion(BaseModel):
    q: str
    yes: str
    no: str

class FaultEntry(BaseModel):
    id: str
    device: str = Field(..., description="Device Category")
    fault_category: str = Field(..., description="Fault Category")
    symptom_text: List[str] = Field(..., min_length=1)
    severity: str = Field(..., description="Severity Level")
    possible_causes: List[str] = Field(..., min_length=1)
    ask_questions: List[AskQuestion] = []
    solution_steps: List[str] = Field(..., min_length=1)
    tools: List[str] = []
    est_time_min: int
    safety_notes: List[str] = []

    @field_validator('device')
    def validate_device(cls, v):
        allowed = {'Flashlight', 'Kettle', 'Coffee Machine', 'Fan'}
        if v not in allowed:
            raise ValueError(f"device must be one of {allowed}")
        return v

    @field_validator('severity')
    def validate_severity(cls, v):
        allowed = {'DIY Repair', 'Requires Professional Service'}
        if v not in allowed:
            raise ValueError(f"severity must be one of {allowed}")
        return v

def load_corpus(file_path: str) -> List[FaultEntry]:
    entries = []
    stats = defaultdict(lambda: defaultdict(int))
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            entry = FaultEntry(**data)
            entries.append(entry)
            stats[entry.device][entry.fault_category] += len(entry.symptom_text)
            
    return entries
