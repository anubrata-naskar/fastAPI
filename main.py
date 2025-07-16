"""
Main FastAPI application entry point.
This file serves as the main entry point for the entire FastAPI project.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="FastAPI Project",
    description="A comprehensive FastAPI project with multiple applications",
    version="1.0.0",
    contact={
        "name": "Administrator",
        "email": "admin@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Root endpoint that provides an overview of available applications.
    """
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI Project</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 800px; margin: 0 auto; }
            .app-card { border: 1px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 8px; }
            .app-title { color: #2c3e50; }
            .link { color: #3498db; text-decoration: none; }
            .link:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>FastAPI Project</h1>
            <p>Welcome to the FastAPI project! This project contains multiple applications:</p>
            
            <div class="app-card">
                <h2 class="app-title">1. Demo Application</h2>
                <p>A basic FastAPI application with simple endpoints.</p>
                <p><strong>Run command:</strong> <code>uvicorn 1.Demo.try:app --reload --port 8001</code></p>
                <p><strong>Features:</strong> Basic routing, Hello World endpoint</p>
            </div>
            
            <div class="app-card">
                <h2 class="app-title">2. Patient Management System</h2>
                <p>A complete CRUD application for managing patient data.</p>
                <p><strong>Run command:</strong> <code>cd 2.PatientMangement && uvicorn try:app --reload --port 8002</code></p>
                <p><strong>Features:</strong> CRUD operations, Data validation, BMI calculation, Health assessment</p>
            </div>
            
            <div class="app-card">
                <h2 class="app-title">Getting Started</h2>
                <ol>
                    <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
                    <li>Run any of the applications using the commands above</li>
                    <li>Access the interactive API documentation at <code>/docs</code></li>
                </ol>
            </div>
            
            <div class="app-card">
                <h2 class="app-title">API Documentation</h2>
                <p>Each application provides interactive API documentation:</p>
                <ul>
                    <li><a class="link" href="/docs">Swagger UI</a> - Interactive API documentation</li>
                    <li><a class="link" href="/redoc">ReDoc</a> - Alternative API documentation</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy", "message": "FastAPI project is running"}

@app.get("/info")
async def project_info():
    """
    Project information endpoint.
    """
    return {
        "project": "FastAPI Project",
        "version": "1.0.0",
        "description": "A comprehensive FastAPI project with multiple applications",
        "applications": [
            {
                "name": "Demo Application",
                "path": "1.Demo",
                "description": "Basic FastAPI demo with simple endpoints"
            },
            {
                "name": "Patient Management System",
                "path": "2.PatientMangement",
                "description": "Complete CRUD operations for patient data management"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
