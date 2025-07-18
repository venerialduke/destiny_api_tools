# Destiny API Tools

A comprehensive web application for Destiny 2 players to manage inventory, track statistics, find fireteams, and more using the Bungie.net API.

## Features

### 🎒 Inventory Manager
- Transfer items between characters and vault
- View all characters' inventory in one place
- Quick equip and unequip items
- Vault management tools

### ⚙️ Loadout Manager
- Create and save custom loadouts
- Quick loadout switching
- Build optimization tools
- Loadout sharing capabilities

### 📊 Stats Tracker
- Comprehensive player statistics
- Activity history and performance metrics
- Leaderboard comparisons
- Progress tracking

### 👥 Fireteam Finder
- Looking for Group (LFG) system
- Activity-based matchmaking
- Team coordination tools
- Clan integration

### 🛒 Vendor Tracker
- Real-time vendor inventory monitoring
- Weapon and armor roll notifications
- Vendor rotation tracking
- Wishlist integration

## Tech Stack

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Requests** - HTTP library for Bungie API calls
- **Gunicorn** - WSGI HTTP server

### Frontend
- **React** - JavaScript library for building UIs
- **React Router** - Client-side routing
- **React Query** - Data fetching and caching
- **Tailwind CSS** - Utility-first CSS framework
- **Lucide React** - Icon library

### API Integration
- **Bungie.net API** - Official Destiny 2 API
- **OAuth 2.0** - Authentication flow
- **Real-time updates** - Live data synchronization

## Project Structure

```
destiny_api_tools/
├── backend/                 # Flask backend application
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   │   ├── auth/       # Authentication routes
│   │   │   ├── core/       # Core API routes
│   │   │   └── tools/      # Tool-specific routes
│   │   ├── models/         # Data models
│   │   ├── services/       # Business logic services
│   │   ├── utils/          # Utility functions
│   │   └── config.py       # Configuration settings
│   ├── tests/              # Backend tests
│   ├── requirements.txt    # Python dependencies
│   └── app.py             # Application entry point
├── frontend/               # React frontend application
│   ├── src/
│   │   ├── components/     # React components
│   │   │   ├── layout/     # Layout components
│   │   │   ├── shared/     # Shared components
│   │   │   └── tools/      # Tool-specific components
│   │   ├── contexts/       # React contexts
│   │   ├── hooks/          # Custom hooks
│   │   ├── pages/          # Page components
│   │   ├── services/       # API services
│   │   └── utils/          # Utility functions
│   ├── public/             # Static assets
│   └── package.json        # Node.js dependencies
├── references/             # API documentation
│   ├── api-summary/        # API usage guides
│   ├── endpoint-details/   # Endpoint documentation
│   └── entity-details/     # Entity schemas
├── tests/                  # Integration tests
└── docs/                   # Project documentation
```

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