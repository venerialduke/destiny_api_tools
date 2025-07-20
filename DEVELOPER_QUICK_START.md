# Developer Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Prerequisites
- Python 3.8+ and Node.js 16+
- Git and a code editor
- Bungie API credentials

### Setup Steps

1. **Clone & Install**:
```bash
git clone <repository-url>
cd destiny_api_tools

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install
```

2. **Environment Configuration**:
```bash
# Backend .env
BUNGIE_API_KEY=your_api_key
BUNGIE_CLIENT_ID=your_client_id
BUNGIE_CLIENT_SECRET=your_client_secret
FLASK_ENV=development

# Frontend .env
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_BUNGIE_CLIENT_ID=your_client_id
```

3. **Run Development Servers**:
```bash
# Backend (Terminal 1)
cd backend
python app.py

# Frontend (Terminal 2)
cd frontend
npm start
```

## 🛠️ Creating a New Tool - Quick Steps

### 1. Backend Service (5 minutes)
```python
# File: backend/app/services/your_tool_service.py
from .bungie_api import BungieAPIService
from .cache_service import get_cache

class YourToolService:
    def __init__(self, access_token: str):
        self.bungie_api = BungieAPIService(access_token)
        self.cache = get_cache()
    
    def your_method(self, param):
        # Your business logic here
        return {"data": "result"}
```

### 2. API Endpoints (5 minutes)
```python
# File: backend/app/api/core/your_tool.py
from flask import Blueprint, request
from ...services.your_tool_service import YourToolService
from ...utils.response import APIResponse

your_tool_bp = Blueprint('your_tool', __name__)

@your_tool_bp.route('/your-endpoint', methods=['GET'])
def your_endpoint():
    # Get access token
    access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
    
    service = YourToolService(access_token)
    result = service.your_method()
    
    return APIResponse.success(data=result)
```

### 3. Register Blueprint (1 minute)
```python
# File: backend/app/api/core/__init__.py
from .your_tool import your_tool_bp
core_bp.register_blueprint(your_tool_bp, url_prefix='/your-tool')
```

### 4. Frontend Service (5 minutes)
```javascript
// File: frontend/src/services/yourToolService.js
import BaseService from './base/BaseService';
import apiClient from './apiClient';

class YourToolService extends BaseService {
  constructor() {
    super(apiClient);
  }

  async yourMethod() {
    const operation = () => this.apiClient.get('/core/your-tool/your-endpoint');
    return this.withErrorHandling(operation);
  }
}

export default new YourToolService();
```

### 5. React Component (10 minutes)
```javascript
// File: frontend/src/components/tools/YourTool.js
import React, { useState, useEffect } from 'react';
import yourToolService from '../../services/yourToolService';

const YourTool = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    setLoading(true);
    try {
      const result = await yourToolService.yourMethod();
      setData(result.data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading...</div>;

  return (
    <div className="bg-gray-800 rounded-lg p-6">
      <h2 className="text-xl font-bold text-white mb-4">Your Tool</h2>
      {/* Your tool UI here */}
    </div>
  );
};

export default YourTool;
```

### 6. Add Route (2 minutes)
```javascript
// File: frontend/src/App.js
import YourToolPage from './pages/tools/YourToolPage';

// Add to routes
<Route path="/tools/your-tool" element={<YourToolPage />} />
```

## 📋 Development Checklists

### ✅ Backend Checklist
- [ ] Service follows dependency injection pattern
- [ ] All methods have proper error handling
- [ ] Caching is implemented where appropriate
- [ ] API endpoints use standardized responses
- [ ] Request validation is implemented
- [ ] Authentication is required where needed
- [ ] Logging is added for important operations

### ✅ Frontend Checklist
- [ ] Service extends BaseService
- [ ] Components use proper loading states
- [ ] Error handling displays user-friendly messages
- [ ] Performance monitoring is included
- [ ] Responsive design works on mobile
- [ ] Accessibility attributes are included
- [ ] Component is properly tested

### ✅ Testing Checklist
- [ ] Unit tests for service methods
- [ ] API endpoint tests
- [ ] Component rendering tests
- [ ] Error scenario tests
- [ ] Integration tests for full workflow

## 🔧 Common Patterns

### Error Handling Pattern
```javascript
// Frontend
try {
  setLoading(true);
  const result = await service.method();
  setData(result.data);
} catch (error) {
  setError(error.message);
  performanceMonitor.recordError(error, { context: 'ComponentName' });
} finally {
  setLoading(false);
}
```

### Caching Pattern
```python
# Backend
def get_data(self, key):
    cache_key = f"data:{key}"
    cached = self.cache.get(cache_key)
    if cached:
        return cached
    
    data = self.fetch_from_api(key)
    self.cache.set(cache_key, data, ttl=300)
    return data
```

### Authentication Pattern
```python
# Backend API
access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
if not access_token:
    return APIResponse.error(message="Authentication required"), 401
```

## 🐛 Debugging Tips

### Backend Issues
- Check Flask logs in terminal
- Use `logger.debug()` for detailed tracing
- Verify environment variables are set
- Test API endpoints with curl/Postman

### Frontend Issues
- Check browser console for errors
- Use React Developer Tools
- Check Network tab for API call failures
- Verify service imports and exports

### Common Issues
1. **CORS Errors**: Check API URL configuration
2. **Authentication Failures**: Verify token format and expiration
3. **Import Errors**: Check file paths and exports
4. **Cache Issues**: Clear browser cache and restart servers

## 📚 Key Files to Know

### Backend Core Files
- `app/__init__.py` - Application factory
- `app/config.py` - Configuration management
- `app/utils/response.py` - Standardized responses
- `app/services/bungie_api.py` - Bungie API integration

### Frontend Core Files
- `src/App.js` - Main application and routing
- `src/services/base/BaseService.js` - Service base class
- `src/contexts/AuthContext.js` - Authentication state
- `src/utils/performanceMonitor.js` - Performance tracking

### Configuration Files
- `backend/.env` - Backend environment variables
- `frontend/.env` - Frontend environment variables
- `backend/requirements.txt` - Python dependencies
- `frontend/package.json` - Node.js dependencies

## 🔍 Testing Commands

```bash
# Backend tests
cd backend
python -m pytest tests/ -v

# Frontend tests
cd frontend
npm test

# Specific test file
python -m pytest tests/test_your_service.py -v
npm test -- YourComponent.test.js
```

## 📦 Adding Dependencies

```bash
# Backend
pip install new-package
pip freeze > requirements.txt

# Frontend
npm install new-package
# Dependencies automatically added to package.json
```

## 🚀 Deployment Quick Commands

```bash
# Build for production
cd frontend
npm run build

# Run production backend
cd backend
FLASK_ENV=production python app.py
```

This quick start guide should have you up and running with new tools in under 30 minutes!