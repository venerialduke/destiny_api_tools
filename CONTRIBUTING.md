# Contributing to Destiny API Tools

Thank you for your interest in contributing to Destiny API Tools! This document provides guidelines and information for contributors.

## Code of Conduct

This project follows a Code of Conduct that we expect all contributors to adhere to. Please read and follow these guidelines to help maintain a welcoming and inclusive environment.

## How to Contribute

### Reporting Bugs

1. **Check existing issues** first to avoid duplicates
2. **Use the bug report template** when creating new issues
3. **Include detailed information**:
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, browser, etc.)
   - Screenshots or error messages

### Suggesting Features

1. **Check existing feature requests** to avoid duplicates
2. **Use the feature request template**
3. **Provide detailed information**:
   - Use case and motivation
   - Proposed solution
   - Alternative solutions considered
   - Additional context

### Pull Requests

1. **Fork the repository** and create a new branch
2. **Follow the development setup** in README.md
3. **Make your changes** with clear, focused commits
4. **Add tests** for new functionality
5. **Update documentation** as needed
6. **Run the test suite** to ensure nothing is broken
7. **Create a pull request** with a clear description

## Development Guidelines

### Code Style

**Python (Backend):**
- Follow PEP 8 style guidelines
- Use `black` for code formatting
- Use `isort` for import sorting
- Use `flake8` for linting
- Maximum line length: 88 characters

**JavaScript/React (Frontend):**
- Use ESLint configuration provided
- Follow React best practices
- Use functional components and hooks
- Use meaningful variable and function names
- Maximum line length: 100 characters

### Commit Messages

Use clear, descriptive commit messages:

```
feat: add inventory transfer functionality
fix: resolve authentication token refresh issue
docs: update API documentation for loadouts
test: add unit tests for stats service
refactor: improve error handling in auth service
```

Prefix types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test-related changes
- `refactor`: Code refactoring
- `style`: Code style changes
- `chore`: Maintenance tasks

### Branch Naming

Use descriptive branch names:
- `feature/inventory-management`
- `bugfix/auth-token-refresh`
- `hotfix/critical-security-issue`
- `docs/api-documentation-update`

### Testing

**Backend Tests:**
- Write unit tests for services and utilities
- Write integration tests for API endpoints
- Use pytest framework
- Maintain test coverage above 80%

**Frontend Tests:**
- Write unit tests for components and hooks
- Write integration tests for user flows
- Use React Testing Library
- Test accessibility and responsive design

### Documentation

**API Documentation:**
- Update endpoint documentation for new APIs
- Include request/response examples
- Document authentication requirements
- Update the API summary guides

**Code Documentation:**
- Add docstrings to Python functions and classes
- Add JSDoc comments for complex JavaScript functions
- Include inline comments for complex logic
- Update README.md for new features

## Development Environment

### Prerequisites

- Python 3.8+
- Node.js 16+
- Git
- Code editor (VS Code recommended)

### Setup

1. **Clone your fork:**
   ```bash
   git clone https://github.com/your-username/destiny_api_tools.git
   cd destiny_api_tools
   ```

2. **Set up backend:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Configure your .env file
   ```

3. **Set up frontend:**
   ```bash
   cd frontend
   npm install
   cp .env.example .env
   # Configure your .env file
   ```

4. **Run development servers:**
   ```bash
   # Terminal 1 - Backend
   cd backend
   python app.py

   # Terminal 2 - Frontend
   cd frontend
   npm start
   ```

### Development Tools

**Recommended VS Code Extensions:**
- Python
- ES7+ React/Redux/React-Native snippets
- Prettier - Code formatter
- ESLint
- Tailwind CSS IntelliSense
- Thunder Client (for API testing)

**Environment Configuration:**
- Use the provided `.env.example` files
- Never commit actual API keys or secrets
- Use environment variables for configuration

## Project Structure

Understanding the project structure helps with contributions:

```
destiny_api_tools/
├── backend/                 # Flask backend
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── services/       # Business logic
│   │   ├── utils/          # Utility functions
│   │   └── config.py       # Configuration
│   └── tests/              # Backend tests
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # UI components
│   │   ├── services/       # API services
│   │   ├── hooks/          # Custom hooks
│   │   └── utils/          # Utility functions
│   └── tests/              # Frontend tests
├── references/             # API documentation
└── docs/                   # Project documentation
```

## Bungie API Guidelines

### Authentication
- Always use proper OAuth scopes
- Handle token refresh gracefully
- Respect rate limits
- Never expose API keys in frontend code

### Data Handling
- Cache manifest data appropriately
- Handle API errors gracefully
- Respect user privacy
- Follow Bungie's Terms of Service

### Best Practices
- Use the provided API documentation
- Test with different account types
- Handle cross-platform scenarios
- Consider offline functionality

## Release Process

1. **Version Bumping**: Update version numbers in relevant files
2. **Changelog**: Update CHANGELOG.md with new features and fixes
3. **Testing**: Ensure all tests pass and manual testing is complete
4. **Documentation**: Update documentation for new features
5. **Release**: Create a new release with proper tags and notes

## Getting Help

- **Documentation**: Check the `references/` directory
- **Issues**: Search existing issues on GitHub
- **Discussions**: Use GitHub Discussions for questions
- **Discord**: Join our community Discord (link coming soon)

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation
- Special contributor badges

## License

By contributing to Destiny API Tools, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Destiny API Tools! Your help makes this project better for the entire Destiny 2 community.