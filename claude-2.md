# Task: Destiny Account Authentication and Character Display

## Objective
Create a full-stack feature that allows a user to authenticate with their Bungie.net account via OAuth, and then displays their Destiny 2 characters on the landing page. This involves a client-side component to initiate the flow and display data, and a backend component to securely handle the OAuth token exchange and API calls to Bungie.

## Project Context
This is the core authentication and user data retrieval feature for the "Destiny API Tools" application. It builds upon the existing static `index.html` to create the first dynamic, user-facing functionality.

## Required Resources

### API Endpoints
#### Authentication
- **Authorization URL**: `https://www.bungie.net/en/OAuth/Authorize`
  - **Description**: Redirects the user to Bungie.net to approve the application's access.
- **Token URL**: `https://www.bungie.net/Platform/App/OAuth/token/`
  - **Description**: Used on the backend to securely exchange an authorization code for access and refresh tokens.

#### Data Retrieval
- **GET /User/GetMembershipsForCurrentUser/**
  - **Description**: Gets the Bungie.net and related platform memberships for the authenticated user.
  - **Reference**: `c:\Users\monte\GitHub\destiny_api_tools\references\bungie_new.html` (See endpoint `/User/GetMembershipsForCurrentUser/`)

- **GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/**
  - **Description**: Gets the Destiny 2 profile, including character data.
  - **Reference**: `c:\Users\monte\GitHub\destiny_api_tools\references\bungie_new.html` (See endpoint `/Destiny2/{membershipType}/Profile/{destinyMembershipId}/`)

### Entities/Schemas
- **User.UserMembershipData**: The response from `GetMembershipsForCurrentUser`. Contains `destinyMemberships` and `primaryMembershipId`.
  - **Reference**: `c:\Users\monte\GitHub\destiny_api_tools\references\bungie_new.html` (See entity `User.UserMembershipData`)
- **Destiny.Responses.DestinyProfileResponse**: The response from `GetProfile`. Contains the `characters` component.
  - **Reference**: `c:\Users\monte\GitHub\destiny_api_tools\references\bungie_new.html` (See entity `Destiny.Responses.DestinyProfileResponse`)
- **Destiny.Entities.Characters.DestinyCharacterComponent**: The data for a single character.
  - **Reference**: `c:\Users\monte\GitHub\destiny_api_tools\references\bungie_new.html` (See entity `Destiny.Entities.Characters.DestinyCharacterComponent`)

### Authentication
- **OAuth Scopes**: `ReadBasicUserProfile`
- **API Key**: Required for all requests in the `X-API-Key` header.
- **Token Management**: The backend must securely handle the `client_id` and `client_secret` for the token exchange. The frontend will handle the access token for subsequent authenticated requests.

## Implementation Requirements

### Phase 1: Client-Side Authentication Flow
**File to modify**: `main.js`

1.  **Login Initiation**:
    -   Attach a click handler to the `#login-button`.
    -   When clicked, generate a secure random `state` string for CSRF protection.
    -   Store the `state` string in `localStorage`.
    -   Construct the Bungie.net authorization URL with your `client_id`, `response_type=code`, and the generated `state`.
    -   Redirect the user to this URL using `window.location.href`.
2.  **Callback Handling**:
    -   On page load, check if the URL contains `code` and `state` query parameters. This indicates a return from Bungie.net.
    -   Retrieve the stored `state` from `localStorage` and verify it matches the one in the URL. If they don't match, show an error and stop.
    -   If they match, make a `POST` request to a new backend endpoint (e.g., `/api/auth/callback`) and send the `code` from the URL in the request body.
    -   Clear the `code` and `state` from the URL to clean up the address bar.
3.  **Data Display**:
    -   Upon a successful response from `/api/auth/callback`, receive the access token and character data.
    -   Store the access token securely in `localStorage`.
    -   Hide the login button and show a "Logged In" status.
    -   Render the character data in the `#character-display` div. For each character, display their emblem, class, race, and light level.

### Phase 2: Backend OAuth and Data Proxy
**File to create**: `server.py` (or similar backend entry point)

1.  **Create a simple web server** (e.g., using Flask or another framework). It should be able to serve the static `index.html`, `main.js`, and `style.css` files.
2.  **Implement the `/api/auth/callback` endpoint**:
    -   This endpoint should accept a `POST` request with the authorization `code`.
    -   It must securely store your `client_id` and `client_secret` as environment variables or in a secure config.
    -   Make a `POST` request to the Bungie.net Token URL (`https://www.bungie.net/Platform/App/OAuth/token/`).
    -   The request body must be `application/x-www-form-urlencoded` and contain `grant_type=authorization_code`, `code`, `client_id`, and `client_secret`.
    -   On a successful response, you will receive an `access_token` and `membership_id`.
3.  **Fetch User and Character Data**:
    -   Using the newly acquired `access_token`, make a `GET` request to the `/User/GetMembershipsForCurrentUser/` endpoint. Include your `X-API-Key` and the `Authorization: Bearer <access_token>` headers.
    -   From the response, parse the `destinyMemberships` array to find the primary Destiny 2 account (use `primaryMembershipId` to identify it if available, otherwise pick the first one).
    -   Using the `membershipType` and `destinyMembershipId` from the previous step, make a `GET` request to the `/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=200` endpoint.
    -   Parse the `characters.data` object from the response. This will be a dictionary of characters, keyed by character ID.
4.  **Return Data to Frontend**:
    -   Structure a JSON response containing the `access_token` and a simplified list of character data (emblem path, class, race, light level).
    -   Send this JSON back to the frontend client.

### File Structure
Create the following new files in the project's root directory:
- `main.js`
- `style.css` (This file can be empty).
- `server.py` (Or your preferred backend language equivalent).

## Success Criteria

### Functional Requirements
1.  A user can click the "Log In" button and be successfully redirected to Bungie.net to authorize the application.
2.  After authorization, the user is redirected back to the application.
3.  The application securely exchanges the authorization code for an access token on the backend.
4.  The backend uses the token to fetch the user's Destiny 2 characters.
5.  The character list is rendered on the page, showing each character's emblem, class, and light level.
6.  The UI updates to reflect the logged-in state (e.g., login button is hidden).

### Technical and Security Requirements
1.  The OAuth `client_secret` is never exposed to the frontend.
2.  The `state` parameter is used correctly to prevent CSRF attacks.
3.  Access tokens are stored on the client-side for subsequent API calls (though we are not making any yet beyond this initial flow).
4.  The backend correctly handles headers (`X-API-Key`, `Authorization`, `Content-Type`) for all API calls.

## Testing Requirements
1.  **Full Auth Flow**: Perform a complete login flow and verify that characters are displayed.
2.  **CSRF Test**: Manually change the `state` parameter on the callback URL to ensure the application rejects the request.
3.  **Backend Endpoint Test**: Use a tool like Postman or curl to test the `/api/auth/callback` endpoint with a valid and an invalid/expired `code`.
4.  **UI State**: Verify the UI correctly shows loading states during API calls and updates correctly after login.
5.  **Error Handling**: Test what happens if the Bungie.net API is down or returns an error during the token exchange or data fetching steps. The user should see a friendly error message.

## Reference Materials
- `c:\Users\monte\GitHub\destiny_api_tools\references\bungie_new.html`: Primary reference for OAuth URLs and all endpoint/entity structures for this task.
- `c:\Users\monte\GitHub\destiny_api_tools\index.html`: The HTML file to be served and manipulated.

## Notes
- For this task, we will not implement token refresh logic. The user will need to re-authenticate if their session expires.
- The backend should be simple. A single-file Flask application is sufficient to proxy the requests.
- Remember to add your application's callback URL (e.g., `http://localhost:5000/`) to your Bungie.net application settings.
- For subsequent tasks that involve fetching data (e.g., user profiles, characters), we will use the more specific documentation found in `c:\Users\monte\GitHub\destiny_api_tools\references\endpoints\` and `c:\Users\monte\GitHub\destiny_api_tools\references\entities\`.
- For future tasks, we will use the more specific documentation found in `c:\Users\monte\GitHub\destiny_api_tools\references\endpoints\` and `c:\Users\monte\GitHub\destiny_api_tools\references\entities\`.