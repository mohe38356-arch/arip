from fastapi import FastAPI

app = FastAPI(
title="ARIP Backend",
description="Backend API for ARIP — Autonomous Reliability Intelligence Platform",
version="0.1.1-alpha",
)

@app.get("/")
def root():
return {
"name": "ARIP Backend",
"description": "Autonomous Reliability Intelligence Platform backend service",
"status": "running",
"version": "0.1.1-alpha",
}

@app.get("/health")
def health_check():
return {
"status": "healthy",
"service": "arip-backend",
"version": "0.1.1-alpha",
}

@app.get("/api/v1/health")
def api_health_check():
return {
"status": "healthy",
"service": "arip-backend",
"api_version": "v1",
"version": "0.1.1-alpha",
}
