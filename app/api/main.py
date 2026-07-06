from fastapi import FastAPI

from app.api.routes.jobs import router as jobs_router

app = FastAPI(
    title="Job Hunter API",
    version="0.1.0",
)

app.include_router(jobs_router)


@app.get("/")
def root():
    return {
        "message": "Job Hunter API is running 🚀"
    }