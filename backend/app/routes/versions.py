from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.version import Version, VersionCreate, VersionUpdate, VersionHistory
from app.services.version_service import VersionService

router = APIRouter()
service = VersionService()

@router.post("/", response_model=Version, status_code=status.HTTP_201_CREATED)
async def create_version(version: VersionCreate):
    """Create a new mod version"""
    # Validate version number format
    if not await service.validate_version_number(version.version_number):
        raise HTTPException(
            status_code=400,
            detail="Invalid version number format. Use format: X.Y.Z or X.Y.Z-alpha/beta/rc"
        )
    return await service.create_version(version)

@router.get("/mod/{mod_id}/", response_model=VersionHistory)
async def list_versions_by_mod(mod_id: str):
    """List all versions for a specific mod"""
    versions = await service.list_versions_by_mod(mod_id)
    return VersionHistory(
        mod_id=mod_id,
        versions=versions,
        total_count=len(versions)
    )

@router.get("/mod/{mod_id}/latest", response_model=Version)
async def get_latest_version(mod_id: str):
    """Get latest version of a mod"""
    version = await service.get_latest_version(mod_id)
    if not version:
        raise HTTPException(status_code=404, detail="No versions found for this mod")
    return version

@router.get("/{version_id}", response_model=Version)
async def get_version(version_id: str):
    """Get a specific version"""
    version = await service.get_version(version_id)
    if not version:
        raise HTTPException(status_code=404, detail="Version not found")
    return version

@router.put("/{version_id}", response_model=Version)
async def update_version(version_id: str, version: VersionUpdate):
    """Update a version"""
    updated = await service.update_version(version_id, version)
    if not updated:
        raise HTTPException(status_code=404, detail="Version not found")
    return updated

@router.delete("/{version_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_version(version_id: str):
    """Delete a version"""
    success = await service.delete_version(version_id)
    if not success:
        raise HTTPException(status_code=404, detail="Version not found")
    return None

@router.post("/{version_id}/download")
async def download_version(version_id: str):
    """Download a version (increments download count)"""
    version = await service.increment_download_count(version_id)
    if not version:
        raise HTTPException(status_code=404, detail="Version not found")
    return {"message": "Download counted", "download_count": version.download_count}
