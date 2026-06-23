# COMS Location Service

A simple FastAPI service for checking whether a point lies inside a stored constituency polygon.

## Features

- `POST /check-location` accepts latitude and longitude
- Checks the coordinates against constituency polygons stored in PostgreSQL
- Returns whether the point is inside a constituency and the constituency details
- Includes health and root endpoints for status checks

## Requirements

- Python 3.11+ (recommended)
- PostgreSQL with a table for constituency polygons
- `poetry` or `pip` for dependency installation

## Installation

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root with the following values:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=YOUR_DB_NAME
DB_USER=YOUR_DB_USER
DB_PASSWORD=YOUR_DB_PASSWORD
```

## Run

```bash
uvicorn app.main:app --reload
```

## API

### Health

`GET /health`

Returns service health status.

### Location check

`POST /check-location`

Body:

```json
{
  "latitude": 12.345,
  "longitude": 67.890
}
```

Response when inside a constituency:

```json
{
  "inside": true,
  "constituency_id": 1,
  "constituency_name": "Example Constituency"
}
```

Response when outside all constituencies:

```json
{
  "inside": false
}
```

## Notes

- The app uses `shapely` to evaluate whether a point is contained in a polygon.
- `app/model.py` defines `TblConstituency` with a JSONB polygon field.
- The project assumes the constituency geometry is stored as GeoJSON in PostgreSQL.
