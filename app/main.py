from fastapi import FastAPI
from app.routes import insights, anomaly

app = FastAPI(title="ThingsEye AI Service Layer")

app.include_router(insights.router, prefix="/insights")
app.include_router(anomaly.router, prefix="/anomaly")

@app.get("/")
def home():
    return {"message": "ThingsEye AI Service Layer is running"}
