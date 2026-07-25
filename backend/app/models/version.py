from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class VersionBase(BaseModel):
    version_number: str  # e.g., "1.0.0"
    description: Optional[str] = None
    release_notes: Optional[str] = None
    minecraft_versions: List[str] = []  # e.g., ["1.20", "1.20.1"]
    is_beta: bool = False
    is_release: bool = True

class VersionCreate(VersionBase):
    mod_id: str

class VersionUpdate(BaseModel):
    version_number: Optional[str] = None
    description: Optional[str] = None
    release_notes: Optional[str] = None
    minecraft_versions: Optional[List[str]] = None
    is_beta: Optional[bool] = None
    is_release: Optional[bool] = None

class Version(VersionBase):
    id: str
    mod_id: str
    created_at: datetime
    updated_at: datetime
    download_count: int = 0
    
    class Config:
        from_attributes = True

class VersionHistory(BaseModel):
    mod_id: str
    versions: List[Version]
    total_count: int
