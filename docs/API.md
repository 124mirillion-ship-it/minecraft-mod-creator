## Version Endpoints

### Create Version
```
POST /versions/
Content-Type: application/json

{
  "mod_id": "uuid",
  "version_number": "1.0.0",
  "description": "Initial release",
  "release_notes": "## Features\n- First release\n- Basic functionality",
  "minecraft_versions": ["1.20", "1.20.1"],
  "is_beta": false,
  "is_release": true
}
```

**Response:**
```json
{
  "id": "version-uuid",
  "mod_id": "mod-uuid",
  "version_number": "1.0.0",
  "description": "Initial release",
  "release_notes": "## Features\n- First release",
  "minecraft_versions": ["1.20", "1.20.1"],
  "is_beta": false,
  "is_release": true,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00",
  "download_count": 0
}
```

### List Versions by Mod
```
GET /versions/mod/{mod_id}/
```

**Response:**
```json
{
  "mod_id": "mod-uuid",
  "versions": [
    {
      "id": "version-uuid",
      "mod_id": "mod-uuid",
      "version_number": "1.0.0",
      "description": "Initial release",
      "release_notes": "...",
      "minecraft_versions": ["1.20"],
      "is_beta": false,
      "is_release": true,
      "created_at": "2024-01-01T00:00:00",
      "updated_at": "2024-01-01T00:00:00",
      "download_count": 42
    }
  ],
  "total_count": 1
}
```

### Get Latest Version
```
GET /versions/mod/{mod_id}/latest
```

### Get Specific Version
```
GET /versions/{version_id}
```

### Update Version
```
PUT /versions/{version_id}
Content-Type: application/json

{
  "version_number": "1.0.1",
  "release_notes": "Bug fixes"
}
```

### Delete Version
```
DELETE /versions/{version_id}
```

### Download Version (Increment Count)
```
POST /versions/{version_id}/download
```

**Response:**
```json
{
  "message": "Download counted",
  "download_count": 43
}
```

## Version Number Format

Supported formats:
- `X.Y.Z` (e.g., `1.0.0`)
- `X.Y.Z-alpha` (e.g., `1.0.0-alpha`)
- `X.Y.Z-beta` (e.g., `1.0.0-beta`)
- `X.Y.Z-rc` (e.g., `1.0.0-rc`)
- `X.Y.Z-alpha.1` (e.g., `1.0.0-alpha.1`)
