# Task: Destiny Account Authentication and Character Display

## Objective
Create a landing page that allows users to authenticate with their Destiny account via Bungie OAuth and display their characters. This will serve as the foundation authentication system for the Destiny API Tools application.

## Project Context
We are building the core authentication and user onboarding flow for the Destiny API Tools web application. The project structure is already established with a Flask backend and React frontend. This implementation will create the first functional user flow: login and character display.

## Required Resources

### API Endpoints
Based on the authentication workflow analysis, we need these specific endpoints:

#### Authentication Flow
- **Authorization URL**: `https://www.bungie.net/en/OAuth/Authorize` - Bungie OAuth authorization
- **Token Exchange**: `https://www.bungie.net/Platform/App/OAuth/token/` - Exchange auth code for tokens

#### User Data Retrieval
- **GET /User/GetMembershipsForCurrentUser/** - Get current user's platform memberships
  - **Reference**: `references/endpoint-details/get--User-GetMembershipsForCurrentUser.md`
  - **Authentication**: OAuth required
  - **Scopes**: ReadBasicUserProfile

#### Character Data Retrieval  
- **GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/** - Get player profile and characters
  - **Reference**: `references/endpoint-details/get--Destiny2-membershipType-Profile-destinyMembershipId.md`
  - **Authentication**: OAuth required
  - **Scopes**: ReadDestinyInventoryAndVault
  - **Components**: 200 (Characters component)

#### Fallback Search (if needed)
- **POST /Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/** - Search for player by Bungie name
  - **Reference**: `references/endpoint-details/post--Destiny2-SearchDestinyPlayerByBungieName-membershipType.md`
  - **Authentication**: API Key only

### Entities/Schemas
Key data structures to handle:

- **User.UserMembershipData** - User membership information
  - **Reference**: `references/entity-details/User-UserMembershipData.md`
  - Contains: bungieNetUser, destinyMemberships, primaryMembershipId

- **Destiny.Responses.DestinyProfileResponse** - Complete profile response
  - **Reference**: `references/entity-details/Destiny-Responses-DestinyProfileResponse.md`
  - Contains: profile, characters, profileInventory, etc.

- **Destiny.Entities.Characters.DestinyCharacterComponent** - Individual character data
  - **Reference**: `references/entity-details/Destiny-Entities-Characters-DestinyCharacterComponent.md`
  - Contains: membershipId, membershipType, characterId, classType, raceType, genderType, emblemPath, etc.

### Authentication Requirements
- **OAuth Scopes Needed**:
  - `ReadBasicUserProfile` - To get user membership information
  - `ReadDestinyInventoryAndVault` - To access character and profile data
- **API Key**: Required for all requests
- **Token Management**: Handle access token and refresh token storage

## Implementation Requirements

### Backend Implementation (Flask)

#### Step 1: Enhance Authentication Service
**Files to modify/create**:
- `backend/app/services/auth_service.py` - Enhance existing OAuth implementation
- `backend/app/api/auth/__init__.py` - Add character retrieval after auth

**Key functionality**:
1. **OAuth Flow Management**:
   - Generate authorization URL with correct scopes
   - Handle callback and token exchange
   - Store tokens securely
   - Implement token refresh logic

2. **User Data Retrieval**:
   - Get user memberships after successful authentication
   - Identify primary Destiny membership
   - Retrieve character data for the user

#### Step 2: Create User Profile Service
**Files to create**:
- `backend/app/services/user_service.py` - User data management
- `backend/app/api/core/user.py` - User-related endpoints

**Key functionality**:
1. Get current user's memberships
2. Fetch Destiny profile with characters component
3. Parse and structure character data
4. Handle multiple platform memberships

#### Step 3: Backend API Endpoints
**Endpoints to implement**:
1. **GET /api/auth/login** - Start OAuth flow
2. **POST /api/auth/callback** - Handle OAuth callback, return tokens + user data
3. **GET /api/user/profile** - Get user profile and characters (authenticated)
4. **POST /api/auth/refresh** - Refresh access token

### Frontend Implementation (React)

#### Step 4: Enhanced Landing Page
**Files to modify**:
- `frontend/src/pages/HomePage.js` - Update with authentication CTA
- `frontend/src/components/layout/Header.js` - Add login state management

**Key features**:
1. **Welcome Section**: Introduction to Destiny API Tools
2. **Login CTA**: Prominent "Connect your Destiny Account" button
3. **Feature Preview**: Show what's available after login
4. **User State**: Show different content for logged-in vs logged-out users

#### Step 5: Authentication Pages
**Files to create/modify**:
- `frontend/src/pages/auth/LoginPage.js` - Dedicated login page
- `frontend/src/pages/auth/CallbackPage.js` - OAuth callback handler
- `frontend/src/contexts/AuthContext.js` - Enhance with character data

**Key functionality**:
1. **Login Flow**: Initiate OAuth with Bungie
2. **Callback Handling**: Process OAuth response and store tokens
3. **State Management**: Manage authentication state across app
4. **Error Handling**: Handle authentication failures gracefully

#### Step 6: Character Display Components
**Files to create**:
- `frontend/src/pages/CharacterDashboard.js` - Main character display page
- `frontend/src/components/shared/CharacterCard.js` - Individual character display
- `frontend/src/components/shared/CharacterList.js` - Character grid/list
- `frontend/src/services/userService.js` - User data API calls

**Key features**:
1. **Character Grid**: Display all user's characters
2. **Character Details**: Show class, level, light level, emblem
3. **Platform Indicators**: Show which platform each character is on
4. **Character Selection**: Allow users to select primary character
5. **Responsive Design**: Work on desktop and mobile

### Frontend Services

#### Step 7: API Service Layer
**Files to enhance/create**:
- `frontend/src/services/authService.js` - Enhanced OAuth handling
- `frontend/src/services/userService.js` - User data management
- `frontend/src/services/apiClient.js` - Centralized API client with auth

**Key functionality**:
1. **Auth Service**: OAuth flow, token management, refresh logic
2. **User Service**: Profile and character data fetching
3. **API Client**: Centralized HTTP client with automatic auth headers
4. **Error Handling**: Standardized error handling across services

## Implementation Steps

### Phase 1: Backend Foundation (Steps 1-3)
1. **Enhance OAuth Service** - Complete OAuth flow with character retrieval
2. **Create User Service** - Profile and character data management  
3. **Implement API Endpoints** - Authentication and user data endpoints

### Phase 2: Frontend Authentication (Steps 4-5)
4. **Update Landing Page** - Add authentication call-to-action
5. **Create Auth Pages** - Login page and OAuth callback handling

### Phase 3: Character Display (Steps 6-7)
6. **Build Character Components** - Character display and selection
7. **Complete Service Layer** - API integration and state management

## Success Criteria

### Functional Requirements
1. **User can click "Login" and be redirected to Bungie OAuth**
2. **After approval, user is returned to app with valid tokens**
3. **App automatically fetches and displays user's Destiny characters**
4. **Characters show correct class, level, and emblem images**
5. **Multiple platform characters are handled correctly**
6. **Authentication state persists across browser sessions**
7. **Token refresh works seamlessly when tokens expire**

### Technical Requirements
1. **Secure token storage** - Tokens stored securely in localStorage
2. **Error handling** - Graceful handling of auth failures and API errors
3. **Loading states** - Appropriate loading indicators during API calls
4. **Responsive design** - Works on desktop and mobile devices
5. **Cross-platform support** - Handles Xbox, PlayStation, Steam, etc.

### User Experience Requirements
1. **Clear onboarding** - User understands what connecting their account does
2. **Visual character representation** - Characters are visually appealing and informative
3. **Fast loading** - Character data loads quickly after authentication
4. **Error messaging** - Clear error messages if something goes wrong

## Testing Requirements

### Backend Testing
1. **OAuth flow testing** - Verify complete authentication flow
2. **API endpoint testing** - Test all auth and user endpoints
3. **Token management testing** - Verify token refresh and expiration handling
4. **Error scenario testing** - Test invalid tokens, API failures, etc.

### Frontend Testing
1. **Authentication flow testing** - End-to-end login process
2. **Character display testing** - Verify character data rendering
3. **Responsive testing** - Test on various screen sizes
4. **Error handling testing** - Test error states and recovery

### Integration Testing
1. **Full user flow testing** - Complete login to character display flow
2. **Cross-browser testing** - Verify compatibility across browsers
3. **Token persistence testing** - Verify auth state across sessions

## Reference Materials

### Authentication Documentation
- `references/api-summary/authentication-guide.md` - Complete OAuth implementation guide
- `references/api-summary/common-workflows.md` - User authentication workflow patterns

### API Endpoint Details
- `references/endpoint-details/get--User-GetMembershipsForCurrentUser.md` - User membership data
- `references/endpoint-details/get--Destiny2-membershipType-Profile-destinyMembershipId.md` - Character data
- `references/endpoint-details/post--Destiny2-SearchDestinyPlayerByBungieName-membershipType.md` - Player search

### Entity Schema References
- `references/entity-details/User-UserMembershipData.md` - User membership structure
- `references/entity-details/Destiny-Responses-DestinyProfileResponse.md` - Profile response format
- `references/entity-details/Destiny-Entities-Characters-DestinyCharacterComponent.md` - Character data structure

### Project Architecture
- `GEMINI.md` - Project management guidelines
- `references/api-summary/quick-reference.md` - Quick API reference
- `NEXT_STEPS.md` - Development setup instructions

## Notes

### OAuth Scopes Strategy
Start with minimal scopes (`ReadBasicUserProfile`, `ReadDestinyInventoryAndVault`) and add more as features are implemented.

### Character Data Caching
Consider implementing client-side caching for character data to improve performance.

### Multi-Platform Handling
Users may have characters on multiple platforms (Xbox, PlayStation, Steam). The UI should clearly indicate platform and allow selection.

### Error Recovery
Implement robust error recovery for common scenarios:
- Expired tokens
- API rate limiting  
- Network connectivity issues
- Invalid character data

### Future Extensibility
Design the authentication and character system to support future features like inventory management, loadouts, and statistics.