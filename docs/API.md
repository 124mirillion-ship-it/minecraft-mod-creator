# API Documentation

## Base URL
```
http://localhost:8000/api
```

## Dimensions Endpoints

### Create Dimension
```
POST /dimensions/
Content-Type: application/json

{
  "name": "Dimension Name",
  "description": "Optional description",
  "seed": 12345
}
```

**Response:**
```json
{
  "id": "uuid",
  "name": "Dimension Name",
  "description": "Optional description",
  "seed": 12345,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

### List Dimensions
```
GET /dimensions/
```

### Get Dimension
```
GET /dimensions/{dimension_id}
```

### Update Dimension
```
PUT /dimensions/{dimension_id}
Content-Type: application/json

{
  "name": "Updated Name",
  "description": "Updated description"
}
```

### Delete Dimension
```
DELETE /dimensions/{dimension_id}
```

### Merge Dimensions
```
POST /dimensions/merge/
Content-Type: application/json

{
  "source_dimension_id": "uuid1",
  "target_dimension_id": "uuid2",
  "merge_options": {}
}
```

## Translation Endpoints

### Translate Text
```
POST /translations/translate/
Content-Type: application/json

{
  "text": "Hello World",
  "source_language": "en",
  "target_languages": ["ja", "es", "fr"]
}
```

**Response:**
```json
{
  "original_text": "Hello World",
  "source_language": "en",
  "translations": {
    "ja": "こんにちは世界",
    "es": "Hola Mundo",
    "fr": "Bonjour le monde"
  }
}
```

### Get Supported Languages
```
GET /translations/languages/
```

### Get Language Info
```
GET /translations/languages/{language_code}
```

## Mods Endpoints

### Create Mod
```
POST /mods/
Content-Type: application/json

{
  "name": "My Mod",
  "description": "My custom mod",
  "version": "1.0.0",
  "dimension_ids": ["uuid1", "uuid2"]
}
```

### List Mods
```
GET /mods/
```

### Get Mod
```
GET /mods/{mod_id}
```

### Update Mod
```
PUT /mods/{mod_id}
Content-Type: application/json

{
  "name": "Updated Mod Name",
  "version": "2.0.0"
}
```

### Delete Mod
```
DELETE /mods/{mod_id}
```

### Export Mod
```
POST /mods/{mod_id}/export/?export_format=jar
```

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

## Health Check

### API Status
```
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "message": "Minecraft Mod Creator API is running"
}
```
