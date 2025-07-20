# Destiny API Tools

A comprehensive, enterprise-grade web application for Destiny 2 players and developers. Features advanced character management, real-time data synchronization, intelligent search capabilities, and a robust toolkit for interacting with Bungie's Destiny 2 API.

## 🚀 Features

### 🔐 Authentication & User Management
- **OAuth Integration**: Secure Bungie.net authentication flow
- **Character Sync**: Automatic character data synchronization
- **Session Management**: Persistent authentication with token refresh
- **Multi-Platform Support**: Xbox, PlayStation, Steam, and Stadia

### 🔍 Advanced Search & Discovery
- **Full-Text Search**: Search across all Destiny content (weapons, armor, activities)
- **Smart Filtering**: Advanced filters with faceted search
- **Auto-Suggestions**: Real-time search suggestions and completions
- **Fuzzy Matching**: Typo-tolerant search with intelligent ranking

### ⚡ Real-Time Features
- **WebSocket Sync**: Live character and inventory updates
- **Background Processing**: Scheduled manifest updates and data sync
- **Performance Monitoring**: Real-time application health tracking
- **Push Notifications**: Activity and vendor alerts

### 🛠️ Developer Tools
- **Comprehensive API**: RESTful endpoints for all functionality
- **Health Monitoring**: Production-ready health checks and metrics
- **Structured Logging**: JSON-formatted logs with request tracing
- **Performance Analytics**: Client and server-side performance tracking

### 📊 Data Management
- **Manifest Processing**: Automated Destiny 2 manifest updates
- **Smart Caching**: Multi-tier caching with intelligent invalidation
- **Data Pipeline**: Background job processing for heavy operations
- **Search Indexing**: Full-text search with faceting and aggregations

## 🏗️ Architecture & Tech Stack

### Backend (Python/Flask)
- **Flask**: Modern Python web framework with blueprint organization
- **WebSocket Support**: Real-time bidirectional communication
- **Background Jobs**: Scheduled task processing with persistence
- **Caching Layer**: Multi-tier caching (Memory → Redis → Database)
- **Search Engine**: Full-text search with indexing and faceting
- **Health Monitoring**: Production-ready health checks and metrics
- **Structured Logging**: JSON logging with request tracing

### Frontend (React/TypeScript)
- **React 18+**: Modern React with hooks and concurrent features
- **Tailwind CSS**: Utility-first styling with component design system
- **Advanced Components**: Search, filtering, real-time updates
- **Performance Monitoring**: Client-side metrics and error tracking
- **Service Architecture**: Layered API integration with error handling
- **Responsive Design**: Mobile-first responsive layouts

### Infrastructure & DevOps
- **Docker Ready**: Container-based deployment
- **Health Endpoints**: Kubernetes-compatible health checks
- **Monitoring**: Prometheus metrics export
- **Testing**: Comprehensive test coverage (backend + frontend)
- **Documentation**: Complete API documentation and guides

### Security & Performance
- **OAuth 2.0**: Secure Bungie.net authentication
- **Token Management**: Automatic refresh and secure storage
- **Rate Limiting**: API protection and usage optimization
- **Error Handling**: Centralized error processing and logging
- **Performance Optimization**: Caching, connection pooling, request batching

## 📁 Project Structure

```
destiny_api_tools/
├── backend/                           # Flask backend application
│   ├── app/
│   │   ├── api/                      # API endpoints (Blueprint-based)
│   │   │   ├── auth/                 # Authentication & OAuth
│   │   │   └── core/                 # Core functionality
│   │   │       ├── health.py         # Health checks & monitoring
│   │   │       ├── search.py         # Advanced search endpoints
│   │   │       ├── user.py           # User management
│   │   │       └── performance.py    # Performance metrics
│   │   ├── services/                 # Business logic layer
│   │   │   ├── bungie_api.py         # Bungie API integration
│   │   │   ├── auth_service.py       # OAuth & authentication
│   │   │   ├── search_service.py     # Advanced search engine
│   │   │   ├── websocket_manager.py  # Real-time updates
│   │   │   ├── data_pipeline.py      # Background processing
│   │   │   ├── job_scheduler.py      # Scheduled tasks
│   │   │   ├── cache_service.py      # Multi-tier caching
│   │   │   └── health_monitor.py     # Application monitoring
│   │   ├── utils/                    # Utility modules
│   │   │   ├── response.py           # Standardized API responses
│   │   │   ├── validation.py         # Request validation
│   │   │   └── logging_config.py     # Structured logging
│   │   └── config.py                 # Configuration management
│   └── tests/                        # Comprehensive test suite
├── frontend/                         # React frontend application
│   ├── src/
│   │   ├── components/               # React components
│   │   │   ├── shared/               # Reusable UI components
│   │   │   │   ├── AdvancedSearch.js # Advanced search interface
│   │   │   │   ├── CharacterCard.js  # Character display
│   │   │   │   └── CharacterList.js  # Character management
│   │   │   └── layout/               # Layout components
│   │   ├── services/                 # API integration layer
│   │   │   ├── base/BaseService.js   # Common service patterns
│   │   │   ├── apiClient.js          # HTTP client with interceptors
│   │   │   ├── authService.js        # Authentication service
│   │   │   └── userService.js        # User data management
│   │   ├── utils/                    # Utility functions
│   │   │   └── performanceMonitor.js # Client-side monitoring
│   │   ├── contexts/                 # React state management
│   │   └── pages/                    # Page components
│   └── package.json                  # Dependencies & scripts
├── references/                       # Bungie API documentation
│   ├── api-summary/                  # Usage guides & workflows
│   ├── endpoint-details/             # Complete endpoint docs
│   └── entity-details/               # Data structure schemas
├── PROJECT_ARCHITECTURE.md          # Detailed architecture guide
├── DEVELOPER_QUICK_START.md         # Quick development guide
└── CLAUDE.md                         # Development instructions
```

## 📖 Documentation

- **[Project Architecture](PROJECT_ARCHITECTURE.md)**: Detailed system design and component overview
- **[Developer Quick Start](DEVELOPER_QUICK_START.md)**: Get up and running in 5 minutes
- **[API Reference](references/)**: Complete Bungie API documentation
- **[Development Guide](CLAUDE.md)**: Project-specific development instructions

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Bungie.net API key and OAuth application

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/destiny_api_tools.git
   cd destiny_api_tools
   ```

2. **Set up Python environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your Bungie API credentials
   ```

4. **Run the backend**
   ```bash
   python app.py
   ```

### Frontend Setup

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Run the frontend**
   ```bash
   npm start
   ```

### Bungie API Setup

1. **Register your application**
   - Go to [Bungie.net Applications](https://www.bungie.net/en/Application)
   - Create a new application
   - Set the redirect URI to `http://localhost:3000/auth/callback`

2. **Get your credentials**
   - API Key: Required for all requests
   - Client ID: For OAuth authentication
   - Client Secret: For token exchange

3. **Configure OAuth scopes**
   - `ReadBasicUserProfile`: Basic user information
   - `ReadDestinyInventoryAndVault`: Inventory access
   - `MoveEquipDestinyItems`: Item management
   - Additional scopes based on features used

## Development

### Running Tests

**Backend tests:**
```bash
cd backend
pytest
```

**Frontend tests:**
```bash
cd frontend
npm test
```

### Code Quality

**Backend linting:**
```bash
cd backend
flake8 app/
black app/
isort app/
```

**Frontend linting:**
```bash
cd frontend
npm run lint
npm run lint:fix
```

### API Documentation

Detailed API documentation is available in the `references/` directory:
- **API Summary**: High-level guides and workflows
- **Endpoint Details**: Complete endpoint documentation
- **Entity Details**: Data model schemas

## Deployment

### Backend Deployment
- Configure production environment variables
- Use Gunicorn for production WSGI server
- Set up reverse proxy (nginx recommended)
- Configure SSL certificates

### Frontend Deployment
- Build production bundle: `npm run build`
- Serve static files with web server
- Configure environment variables for production API

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Bungie for providing the Destiny 2 API
- The Destiny 2 community for feedback and feature requests
- Open source contributors and maintainers

## Support

For support, please:
1. Check the documentation in `references/`
2. Search existing issues on GitHub
3. Create a new issue with detailed information
4. Join our community Discord (link coming soon)

---

**Note**: This application is not affiliated with or endorsed by Bungie, Inc. Destiny 2 is a trademark of Bungie, Inc.