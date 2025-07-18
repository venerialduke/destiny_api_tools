# Authentication Guide

This guide provides comprehensive information about authenticating with the Bungie API, including OAuth 2.0 implementation, scopes, and best practices.

## Table of Contents

1. [API Key Requirements](#api-key-requirements)
2. [OAuth 2.0 Implementation](#oauth-20-implementation)
3. [OAuth Scopes](#oauth-scopes)
4. [Authentication Flow Examples](#authentication-flow-examples)
5. [Endpoint Authorization Requirements](#endpoint-authorization-requirements)
6. [Token Management](#token-management)
7. [Common Authentication Patterns](#common-authentication-patterns)
8. [Troubleshooting](#troubleshooting)

---

## API Key Requirements

### Basic API Key

**All** API requests require an API key, regardless of whether they need OAuth authentication.

- **Header**: `X-API-Key`
- **Required**: Yes, for every request
- **How to get**: Register an application at https://www.bungie.net/en/Application

**Example**:
```http
GET /Destiny2/Manifest/
X-API-Key: YOUR_API_KEY_HERE
```

### Application Registration

1. Visit https://www.bungie.net/en/Application
2. Create a new application
3. Provide required information:
   - Application name
   - Website URL
   - OAuth Client Type (Confidential for server apps, Public for client apps)
   - Redirect URL (for OAuth)
   - Application description
4. Receive your API key and OAuth credentials

---

## OAuth 2.0 Implementation

### OAuth Endpoints

- **Authorization URL**: `https://www.bungie.net/en/OAuth/Authorize`
- **Token URL**: `https://www.bungie.net/Platform/App/OAuth/token/`
- **Refresh URL**: `https://www.bungie.net/Platform/App/OAuth/token/`

### Authorization Flow

#### Step 1: Authorization Request

Redirect the user to the authorization URL:

```
https://www.bungie.net/en/OAuth/Authorize?client_id=YOUR_CLIENT_ID&response_type=code&scope=ReadBasicUserProfile,ReadDestinyInventoryAndVault
```

**Parameters**:
- `client_id`: Your application's client ID
- `response_type`: Always `code`
- `scope`: Space-separated list of requested scopes
- `state`: (Optional) Random string to prevent CSRF attacks

#### Step 2: Authorization Response

User approves and is redirected back to your app:

```
https://your-app.com/callback?code=AUTHORIZATION_CODE&state=STATE_VALUE
```

#### Step 3: Access Token Request

Exchange the authorization code for an access token:

```http
POST /Platform/App/OAuth/token/
Content-Type: application/x-www-form-urlencoded
X-API-Key: YOUR_API_KEY

grant_type=authorization_code&code=AUTHORIZATION_CODE&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET
```

#### Step 4: Access Token Response

```json
{
  "access_token": "ACCESS_TOKEN",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "REFRESH_TOKEN",
  "scope": "ReadBasicUserProfile ReadDestinyInventoryAndVault",
  "membership_id": "USER_MEMBERSHIP_ID"
}
```

#### Step 5: Using the Access Token

```http
GET /Destiny2/3/Profile/4611686018467260757/?components=200
Authorization: Bearer ACCESS_TOKEN
X-API-Key: YOUR_API_KEY
```

---

## OAuth Scopes

### Available Scopes

| Scope | Description | Use Cases |
|-------|-------------|-----------|
| `ReadBasicUserProfile` | Read basic user profile information | User identification, display names, avatars |
| `ReadGroups` | Read group/clan information | Clan membership, group details |
| `WriteGroups` | Write group/clan information | Posting in clan forums, group messages |
| `AdminGroups` | Administer groups/clans | Managing clan members, settings |
| `BnetWrite` | Elevated Bungie.net actions | Creating groups, advanced forum actions |
| `MoveEquipDestinyItems` | Move or equip Destiny items | Item transfers, equipment changes, loadouts |
| `ReadDestinyInventoryAndVault` | Read Destiny inventory and vault | Inventory viewing, item details |
| `ReadUserData` | Read user data | Social features, notifications, memberships |
| `EditUserData` | Edit user data | Profile updates, preferences |
| `ReadDestinyVendorsAndAdvisors` | Read vendor data (Destiny 1 only) | Legacy Destiny 1 support |
| `ReadAndApplyTokens` | Read and apply tokens | Bungie Rewards, partner offers |
| `AdvancedWriteActions` | Advanced write actions | Actions requiring user prompts |
| `PartnerOfferGrant` | Partner offer API | Partner reward claiming |
| `DestinyUnlockValueQuery` | Query unlock values | Sensitive progression data |
| `UserPiiRead` | Read user PII | Email addresses, personal info |

### Scope Combinations by App Type

#### Destiny 2 Item Manager App
```
ReadBasicUserProfile
ReadDestinyInventoryAndVault
MoveEquipDestinyItems
ReadUserData
```

#### Clan Management App
```
ReadBasicUserProfile
ReadGroups
WriteGroups
AdminGroups
ReadUserData
```

#### Social App
```
ReadBasicUserProfile
ReadUserData
ReadGroups
```

#### Statistics App
```
ReadBasicUserProfile
ReadDestinyInventoryAndVault
```

---

## Authentication Flow Examples

### Complete OAuth Flow (JavaScript)

```javascript
// Step 1: Redirect to authorization
function initiateAuth() {
    const clientId = 'YOUR_CLIENT_ID';
    const redirectUri = 'https://your-app.com/callback';
    const scopes = 'ReadBasicUserProfile ReadDestinyInventoryAndVault MoveEquipDestinyItems';
    const state = generateRandomString();
    
    localStorage.setItem('oauth_state', state);
    
    const authUrl = `https://www.bungie.net/en/OAuth/Authorize?client_id=${clientId}&response_type=code&scope=${encodeURIComponent(scopes)}&state=${state}`;
    
    window.location.href = authUrl;
}

// Step 2: Handle callback
function handleCallback() {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');
    const state = urlParams.get('state');
    
    if (state !== localStorage.getItem('oauth_state')) {
        throw new Error('Invalid state parameter');
    }
    
    return exchangeCodeForToken(code);
}

// Step 3: Exchange code for token
async function exchangeCodeForToken(code) {
    const response = await fetch('https://www.bungie.net/Platform/App/OAuth/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-API-Key': 'YOUR_API_KEY'
        },
        body: new URLSearchParams({
            grant_type: 'authorization_code',
            code: code,
            client_id: 'YOUR_CLIENT_ID',
            client_secret: 'YOUR_CLIENT_SECRET'
        })
    });
    
    const tokenData = await response.json();
    
    // Store tokens securely
    localStorage.setItem('access_token', tokenData.access_token);
    localStorage.setItem('refresh_token', tokenData.refresh_token);
    localStorage.setItem('token_expires', Date.now() + (tokenData.expires_in * 1000));
    
    return tokenData;
}

// Step 4: Make authenticated requests
async function makeAuthenticatedRequest(endpoint) {
    const accessToken = localStorage.getItem('access_token');
    
    const response = await fetch(`https://www.bungie.net/Platform${endpoint}`, {
        headers: {
            'Authorization': `Bearer ${accessToken}`,
            'X-API-Key': 'YOUR_API_KEY'
        }
    });
    
    return response.json();
}
```

### Token Refresh Flow

```javascript
async function refreshAccessToken() {
    const refreshToken = localStorage.getItem('refresh_token');
    
    const response = await fetch('https://www.bungie.net/Platform/App/OAuth/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-API-Key': 'YOUR_API_KEY'
        },
        body: new URLSearchParams({
            grant_type: 'refresh_token',
            refresh_token: refreshToken,
            client_id: 'YOUR_CLIENT_ID',
            client_secret: 'YOUR_CLIENT_SECRET'
        })
    });
    
    const tokenData = await response.json();
    
    // Update stored tokens
    localStorage.setItem('access_token', tokenData.access_token);
    localStorage.setItem('refresh_token', tokenData.refresh_token);
    localStorage.setItem('token_expires', Date.now() + (tokenData.expires_in * 1000));
    
    return tokenData;
}
```

---

## Endpoint Authorization Requirements

### No Authentication Required

These endpoints are publicly accessible with just an API key:

**User Information**:
- `GET /User/GetBungieNetUserById/{id}/`
- `GET /User/GetSanitizedPlatformDisplayNames/{membershipId}/`
- `GET /User/Search/Prefix/{displayNamePrefix}/{page}/`

**Destiny 2 Public Data**:
- `GET /Destiny2/Manifest/`
- `GET /Destiny2/Manifest/{entityType}/{hashIdentifier}/`
- `GET /Destiny2/Vendors/`
- `GET /Destiny2/Milestones/`
- `GET /Destiny2/Stats/Definition/`

**Content & Media**:
- All `/Content/` endpoints
- All `/CommunityContent/` endpoints
- All `/Trending/` endpoints

**System Information**:
- `GET /GetAvailableLocales/`
- `GET /Settings/`
- `GET /GlobalAlerts/`

### OAuth Authentication Required

#### ReadBasicUserProfile
- `GET /User/GetMembershipsForCurrentUser/`

#### ReadDestinyInventoryAndVault
- `GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/` (with private components)
- `GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/` (with private components)
- `GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/`

#### MoveEquipDestinyItems
- `POST /Destiny2/Actions/Items/TransferItem/`
- `POST /Destiny2/Actions/Items/EquipItem/`
- `POST /Destiny2/Actions/Items/EquipItems/`
- `POST /Destiny2/Actions/Items/PullFromPostmaster/`
- `POST /Destiny2/Actions/Items/SetLockState/`
- `POST /Destiny2/Actions/Items/SetTrackedState/`
- `POST /Destiny2/Actions/Items/InsertSocketPlug/`
- `POST /Destiny2/Actions/Items/InsertSocketPlugFree/`
- All `/Destiny2/Actions/Loadouts/` endpoints

#### ReadUserData
- All `/Social/` endpoints
- `GET /GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/`

#### ReadGroups
- `GET /GroupV2/{groupId}/Members/`
- `GET /GroupV2/{groupId}/` (for private groups)

#### WriteGroups
- `POST /GroupV2/{groupId}/OptionalConversations/Add/`
- Group messaging endpoints

#### AdminGroups
- `POST /GroupV2/{groupId}/Edit/`
- `POST /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/SetMembershipType/{memberType}/`
- `POST /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Kick/`
- `POST /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Ban/`
- All admin group management endpoints

#### AdvancedWriteActions
- `POST /Destiny2/Awa/Initialize/`
- `POST /Destiny2/Awa/AwaProvideAuthorizationResult/`
- `GET /Destiny2/Awa/GetActionToken/{correlationId}/`

#### ReadAndApplyTokens
- `POST /Tokens/Partner/ClaimOffer/`
- `POST /Tokens/Partner/ApplyMissingOffers/{partnerApplicationId}/{targetBnetMembershipId}/`

---

## Token Management

### Token Lifecycle

1. **Access Token**: Valid for 1 hour (3600 seconds)
2. **Refresh Token**: Valid for extended period (weeks/months)
3. **Automatic Refresh**: Implement automatic token refresh before expiration

### Best Practices

#### Token Storage
- **Server-side**: Store in secure session storage or encrypted database
- **Client-side**: Use secure storage (not localStorage for sensitive apps)
- **Never expose**: Don't include tokens in URLs or client-side code

#### Token Refresh Strategy
```javascript
class TokenManager {
    constructor(apiKey, clientId, clientSecret) {
        this.apiKey = apiKey;
        this.clientId = clientId;
        this.clientSecret = clientSecret;
        this.tokenRefreshPromise = null;
    }
    
    async getValidToken() {
        const token = this.getStoredToken();
        
        if (!token) {
            throw new Error('No token available');
        }
        
        if (this.isTokenExpired(token)) {
            return this.refreshToken();
        }
        
        return token.access_token;
    }
    
    async refreshToken() {
        // Prevent multiple simultaneous refresh attempts
        if (this.tokenRefreshPromise) {
            return this.tokenRefreshPromise;
        }
        
        this.tokenRefreshPromise = this.performTokenRefresh();
        const result = await this.tokenRefreshPromise;
        this.tokenRefreshPromise = null;
        
        return result;
    }
    
    async performTokenRefresh() {
        const refreshToken = this.getStoredRefreshToken();
        
        const response = await fetch('https://www.bungie.net/Platform/App/OAuth/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-API-Key': this.apiKey
            },
            body: new URLSearchParams({
                grant_type: 'refresh_token',
                refresh_token: refreshToken,
                client_id: this.clientId,
                client_secret: this.clientSecret
            })
        });
        
        if (!response.ok) {
            throw new Error('Token refresh failed');
        }
        
        const tokenData = await response.json();
        this.storeToken(tokenData);
        
        return tokenData.access_token;
    }
    
    isTokenExpired(token) {
        const now = Date.now();
        const expirationTime = token.expires_at || (token.created_at + (token.expires_in * 1000));
        
        // Refresh 5 minutes before expiration
        return now >= (expirationTime - 300000);
    }
}
```

---

## Common Authentication Patterns

### Pattern 1: Simple Read-Only App

**Use Case**: Display public player stats and information

**Required Scopes**: None (API key only)

**Implementation**:
```javascript
async function getPlayerStats(membershipType, membershipId) {
    const response = await fetch(`https://www.bungie.net/Platform/Destiny2/${membershipType}/Account/${membershipId}/Stats/`, {
        headers: {
            'X-API-Key': 'YOUR_API_KEY'
        }
    });
    
    return response.json();
}
```

### Pattern 2: Inventory Management App

**Use Case**: View and manage player inventory

**Required Scopes**: `ReadBasicUserProfile`, `ReadDestinyInventoryAndVault`, `MoveEquipDestinyItems`

**Implementation**:
```javascript
class InventoryManager {
    constructor(apiKey, accessToken) {
        this.apiKey = apiKey;
        this.accessToken = accessToken;
    }
    
    async getInventory(membershipType, membershipId) {
        const response = await fetch(`https://www.bungie.net/Platform/Destiny2/${membershipType}/Profile/${membershipId}/?components=102,103,201,205`, {
            headers: {
                'Authorization': `Bearer ${this.accessToken}`,
                'X-API-Key': this.apiKey
            }
        });
        
        return response.json();
    }
    
    async transferItem(itemId, itemHash, stackSize, transferToVault, characterId, membershipType) {
        const response = await fetch('https://www.bungie.net/Platform/Destiny2/Actions/Items/TransferItem/', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${this.accessToken}`,
                'X-API-Key': this.apiKey,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                itemId: itemId,
                itemReferenceHash: itemHash,
                stackSize: stackSize,
                transferToVault: transferToVault,
                characterId: characterId,
                membershipType: membershipType
            })
        });
        
        return response.json();
    }
}
```

### Pattern 3: Social/Clan App

**Use Case**: Manage social features and clan operations

**Required Scopes**: `ReadBasicUserProfile`, `ReadUserData`, `ReadGroups`, `WriteGroups`, `AdminGroups`

**Implementation**:
```javascript
class SocialManager {
    constructor(apiKey, accessToken) {
        this.apiKey = apiKey;
        this.accessToken = accessToken;
    }
    
    async getFriends() {
        const response = await fetch('https://www.bungie.net/Platform/Social/Friends/', {
            headers: {
                'Authorization': `Bearer ${this.accessToken}`,
                'X-API-Key': this.apiKey
            }
        });
        
        return response.json();
    }
    
    async getClanMembers(groupId) {
        const response = await fetch(`https://www.bungie.net/Platform/GroupV2/${groupId}/Members/`, {
            headers: {
                'Authorization': `Bearer ${this.accessToken}`,
                'X-API-Key': this.apiKey
            }
        });
        
        return response.json();
    }
}
```

---

## Troubleshooting

### Common Authentication Errors

#### Error: "ApiKeyMissingFromRequest"
**Cause**: Missing `X-API-Key` header
**Solution**: Include API key in all requests

#### Error: "ApiInvalidOrExpired"
**Cause**: Invalid or expired API key
**Solution**: Verify API key is correct and application is still active

#### Error: "AuthorizationCodeInvalid"
**Cause**: Invalid or expired authorization code
**Solution**: Restart OAuth flow with fresh authorization code

#### Error: "RefreshTokenInvalid"
**Cause**: Invalid or expired refresh token
**Solution**: Re-authenticate user through OAuth flow

#### Error: "AccessTokenInvalid"
**Cause**: Invalid or expired access token
**Solution**: Refresh the access token using refresh token

#### Error: "InsufficientPrivileges"
**Cause**: Missing required OAuth scope
**Solution**: Request additional scopes during OAuth flow

### Debugging Tips

1. **Check Response Headers**: Look for `X-RateLimit-*` headers for rate limit info
2. **Verify Token Expiration**: Check token expiration times
3. **Test with Postman**: Use API testing tools to isolate issues
4. **Monitor Network Requests**: Use browser dev tools to inspect requests
5. **Check API Status**: Verify Bungie API is operational

### Rate Limiting

The API implements rate limiting to prevent abuse:

- **Respect ThrottleSeconds**: Wait the specified time before retrying
- **Implement Exponential Backoff**: Increase wait times for repeated failures
- **Cache Responses**: Reduce API calls by caching static data
- **Batch Operations**: Group related requests when possible

For more information about specific endpoints and their requirements, see the [Endpoint Reference](endpoint-by-function.md) and [Common Workflows](common-workflows.md).