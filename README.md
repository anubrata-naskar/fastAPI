# FastAPI Applications Suite (demo project)

A comprehensive collection of FastAPI applications demonstrating various use cases, from basic API development to machine learning model deployment and enterprise-level applications.

## 🚀 Overview

This repository contains multiple FastAPI applications showcasing different aspects of modern web API development:

- **Demo Application**: Basic FastAPI setup and routing
- **Patient Management System**: Complete CRUD operations with data validation
- **Machine Learning API**: ML model deployment and prediction services
- **Insurance Application**: Enterprise-grade insurance management system

## 📁 Project Structure

```
FastAPI/
├── 1.Demo/                          # Basic FastAPI demo application
│   └── try.py                      # Simple endpoints and routing examples
├── 2.PatientMangement/             # Healthcare patient management system
│   ├── try.py                      # Patient CRUD operations
│   └── patients.json               # Patient data storage
├── 3.ML/                           # Machine Learning API application
│   ├── try.py                      # ML model serving endpoints
│   ├── frontend.py                 # Frontend interface
│   ├── fastapi_ml_model.ipynb      # ML model development notebook
│   ├── insurance.csv               # Training dataset
│   └── model.pkl                   # Trained ML model
├── Insurance/                      # Enterprise insurance application
│   ├── app.py                      # Main application entry point
│   ├── Dockerfile                  # Container configuration
│   ├── requirements.txt            # Application dependencies
│   ├── config/                     # Configuration files
│   │   └── city_tier.py           # City tier configuration
│   ├── model/                      # ML model components
│   │   ├── model.pkl              # Trained model
│   │   └── predict.py             # Prediction logic
│   └── schema/                     # Data validation schemas
│       ├── user_input.py          # Input validation
│       └── prediction_response.py  # Response schemas
├── main.py                         # Main application orchestrator
├── requirements.txt                # Global dependencies
├── pyproject.toml                  # Project configuration
└── README.md                       # This documentation
```

## 🔧 Applications Overview

### 1. Demo Application
**Purpose**: Introduction to FastAPI fundamentals
- Basic HTTP endpoints (GET, POST, PUT, DELETE)
- Path parameters and query parameters
- Request/response handling
- FastAPI automatic documentation

### 2. Patient Management System
**Purpose**: Healthcare data management
- Complete CRUD operations for patient records
- Pydantic models for data validation
- BMI calculation and health assessment
- JSON file-based data persistence
- Patient search and filtering

### 3. Machine Learning API
**Purpose**: ML model deployment and serving
- Model training and prediction endpoints
- Data preprocessing pipelines
- Real-time prediction services
- Frontend interface for model interaction
- Insurance premium prediction model

### 4. Insurance Application
**Purpose**: Enterprise-grade insurance management
- Dockerized application deployment
- Microservices architecture
- Advanced data validation schemas
- City-based tier configuration
- Production-ready model serving
- Comprehensive error handling

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager
- Git

### Global Setup
1. **Clone the repository**:
```powershell
git clone <repository-url>
cd FastAPI
```

2. **Create virtual environment**:
```powershell
python -m venv venv
venv\Scripts\activate
```

3. **Install global dependencies**:
```powershell
pip install -r requirements.txt
```

### Insurance Application Setup
For the Insurance application with its own environment:
```powershell
cd Insurance
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Running Applications

### Demo Application
```powershell
uvicorn 1.Demo.try:app --reload --port 8001
```

### Patient Management System
```powershell
uvicorn 2.PatientMangement.try:app --reload --port 8002
```

### Machine Learning API
```powershell
uvicorn 3.ML.try:app --reload --port 8003
```

### Insurance Application
```powershell
cd Insurance
uvicorn app:app --reload --port 8004
```

### All Applications (using main.py)
```powershell
python main.py
```

## 📚 API Documentation

Each application provides interactive API documentation:

| Application | Swagger UI | ReDoc |
|-------------|------------|-------|
| Demo | http://localhost:8001/docs | http://localhost:8001/redoc |
| Patient Management | http://localhost:8002/docs | http://localhost:8002/redoc |
| ML API | http://localhost:8003/docs | http://localhost:8003/redoc |
| Insurance | http://localhost:8004/docs | http://localhost:8004/redoc |

## 🐳 Docker Deployment

### Insurance Application
```powershell
cd Insurance
docker build -t insurance-app .
docker run -p 8004:8004 insurance-app
```

## 🔥 Key Features

### Framework & Architecture
- **FastAPI**: High-performance, modern Python web framework
- **Async/Await**: Asynchronous request handling
- **Type Hints**: Full type annotation support
- **Dependency Injection**: Clean architecture patterns

### Data & Validation
- **Pydantic Models**: Robust data validation and serialization
- **JSON Schema**: Automatic schema generation
- **Input Validation**: Request/response validation
- **Error Handling**: Comprehensive HTTP exception handling

### Machine Learning
- **Model Deployment**: Production-ready ML model serving
- **Prediction APIs**: Real-time inference endpoints
- **Data Processing**: Preprocessing pipelines
- **Model Versioning**: Pickle-based model storage

### Development Tools
- **Auto-Documentation**: Swagger UI and ReDoc integration
- **Hot Reload**: Development server with auto-reload
- **Testing**: Built-in testing framework support
- **Logging**: Structured logging capabilities

## 🧪 Testing

Run tests for individual applications:
```powershell
# Demo application tests
python -m pytest 1.Demo/

# Patient management tests
python -m pytest 2.PatientMangement/

# ML API tests
python -m pytest 3.ML/

# Insurance application tests
cd Insurance
python -m pytest
```

## 🔐 Security Features

- Input validation and sanitization
- SQL injection prevention
- CORS configuration
- Rate limiting capabilities
- Authentication middleware ready

## 📊 Performance

- Async request handling
- Connection pooling
- Response caching
- Optimized JSON serialization
- Database query optimization

## 🤝 Contributing

1. **Fork the repository**
2. **Create feature branch**:
   ```powershell
   git checkout -b feature/amazing-feature
   ```
3. **Commit changes**:
   ```powershell
   git commit -m "Add amazing feature"
   ```
4. **Push to branch**:
   ```powershell
   git push origin feature/amazing-feature
   ```
5. **Open Pull Request**

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in this repository
- Check the API documentation
- Review the code examples

## 🔄 Version History

- **v1.0.0**: Initial release with basic applications
- **v1.1.0**: Added ML API and enhanced patient management
- **v1.2.0**: Enterprise insurance application
- **v1.3.0**: Docker support and production optimizations

---

**Built with ❤️ using FastAPI**
