# Cloud Run Showcase

A lightweight FastAPI project demonstrating a production-style service deployed to Google Cloud Run.

## API

- `GET /` — project message and deployment information
- `GET /health` — health check
- `GET /docs` — interactive OpenAPI documentation
- `GET /redoc` — ReDoc documentation

The root response includes the commit SHA, GitHub commit URL, repository URL, GitHub profile URL, API version, and build timestamp. Deployment metadata is supplied through environment variables so the same image works locally and in Cloud Run.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Then visit <http://127.0.0.1:8000/docs>.

## Test

```bash
pytest
```

## Run with Docker

```bash
docker build -t cloud-run-showcase:local .
docker run --rm -p 8080:8080 cloud-run-showcase:local
```

The API is then available at <http://localhost:8080>.

## Planned deployment

The service will be containerized and deployed to Google Cloud Run in `us-central1`, using request-based billing, no minimum instances, and GitHub Actions for build and deployment automation.
