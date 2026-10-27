import os
from datetime import datetime, timezone
import json
from typing import Any

from fastapi import FastAPI
from fastapi.responses import JSONResponse


class PrettyJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return json.dumps(content, indent=2).encode("utf-8")


app = FastAPI(
    title="Cloud Run Showcase API",
    description="A lightweight FastAPI service demonstrating deployment on Google Cloud Run.",
    version=os.getenv("API_VERSION", "1.0.0"),
    default_response_class=PrettyJSONResponse,
)


def project_info() -> dict[str, str]:
    return {
        "description": "A lightweight FastAPI service deployed on Google Cloud Run.",
        "api_version": app.version,
        "repository_url": os.getenv(
            "GITHUB_REPOSITORY_URL",
            "https://github.com/prakhar-thecoder/cloud-run-showcase",
        ),
        "github_profile_url": os.getenv(
            "GITHUB_PROFILE_URL", "https://github.com/prakhar-thecoder"
        ),
        "commit_sha": os.getenv("COMMIT_SHA", "local"),
        "commit_url": os.getenv("COMMIT_URL", ""),
        "built_at": os.getenv("BUILD_TIME", datetime.now(timezone.utc).isoformat()),
    }


@app.get("/", summary="Project information")
def root() -> dict:
    return {
        "name": "Cloud Run Showcase API",
        "message": "A portfolio project demonstrating FastAPI on Google Cloud Run.",
        "info": project_info(),
        "health_url": "/health",
        "docs_url": "/docs",
    }


@app.get("/health", summary="Health check")
def health() -> dict[str, str]:
    return {"status": "ok"}
