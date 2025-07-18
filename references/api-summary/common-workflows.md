# Common API Workflows

This document outlines common task workflows using the Bungie API, providing step-by-step guidance for accomplishing typical developer scenarios.

## Table of Contents

1. [User Authentication Flow](#user-authentication-flow)
2. [Getting Player Data](#getting-player-data)
3. [Inventory Management](#inventory-management)
4. [Clan Operations](#clan-operations)
5. [Social Interactions](#social-interactions)
6. [Fireteam Finding](#fireteam-finding)
7. [Statistics and Reporting](#statistics-and-reporting)
8. [Content Discovery](#content-discovery)

---

## User Authentication Flow

### OAuth 2.0 Authentication Setup

**Purpose**: Authenticate users to access their private data and perform actions on their behalf.

**Steps**:
1. **Register Application**: Register your app at https://www.bungie.net/en/Application to get API key and OAuth credentials
2. **Redirect for Authorization**: Direct user to authorization URL with your client ID and desired scopes
3. **Handle Authorization Code**: Receive authorization code from redirect
4. **Exchange for Access Token**: Exchange authorization code for access token
5. **Make Authenticated Requests**: Use access token in Authorization header

**Endpoints Used**:
- Authorization URL: `https://www.bungie.net/en/OAuth/Authorize`
- Token URL: `https://www.bungie.net/Platform/App/OAuth/token/`
- Refresh URL: `https://www.bungie.net/Platform/App/OAuth/token/`

**Example Flow**:
```
1. User clicks "Login with Bungie"
2. Redirect to: https://www.bungie.net/en/OAuth/Authorize?client_id=YOUR_CLIENT_ID&response_type=code&scope=ReadBasicUserProfile,ReadDestinyInventoryAndVault
3. User approves, redirected back with code
4. POST to token URL with code to get access token
5. Use access token for authenticated requests
```

**Common Scopes**:
- `ReadBasicUserProfile`: Basic user info
- `ReadDestinyInventoryAndVault`: Destiny inventory access
- `MoveEquipDestinyItems`: Item management
- `ReadUserData`: User social data
- `ReadGroups`: Group membership info

---

## Getting Player Data

### Basic Player Profile Lookup

**Purpose**: Find and retrieve basic information about a Destiny 2 player.

**Steps**:
1. **Search by Bungie Name**: Use player's display name to find their membership
2. **Get Linked Profiles**: Retrieve all platform accounts linked to the player
3. **Get Profile Data**: Fetch detailed profile information with desired components

**Endpoints Used**:
```
POST /Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/
GET /Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/
GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=Profiles,Characters,CharacterInventories
```

**Example Workflow**:
```
1. Search for player "Guardian#1234"
   POST /Destiny2/SearchDestinyPlayerByBungieName/All/
   Body: {"displayName": "Guardian", "displayNameCode": 1234}

2. Get linked profiles for cross-platform data
   GET /Destiny2/3/Profile/4611686018467260757/LinkedProfiles/

3. Get full profile with characters and inventory
   GET /Destiny2/3/Profile/4611686018467260757/?components=100,200,201,205
```

### Character-Specific Data

**Purpose**: Get detailed information about specific characters.

**Steps**:
1. **Get Profile**: Retrieve profile to get character list
2. **Get Character Details**: Fetch specific character information
3. **Get Character Inventory**: Retrieve character-specific inventory

**Endpoints Used**:
```
GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=Characters
GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/?components=CharacterInventories,CharacterEquipment
```

---

## Inventory Management

### Item Transfer Workflow

**Purpose**: Move items between characters and vault.

**Prerequisites**: OAuth authentication with `MoveEquipDestinyItems` scope

**Steps**:
1. **Get Current Inventory**: Retrieve current inventory state
2. **Identify Item**: Find the item to transfer (requires both item hash and instance ID)
3. **Transfer Item**: Execute the transfer operation
4. **Verify Transfer**: Confirm the transfer was successful

**Endpoints Used**:
```
GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=CharacterInventories,ProfileInventory
POST /Destiny2/Actions/Items/TransferItem/
```

**Example Workflow**:
```
1. Get current inventory state
   GET /Destiny2/3/Profile/4611686018467260757/?components=102,103

2. Transfer item from character to vault
   POST /Destiny2/Actions/Items/TransferItem/
   Body: {
     "itemReferenceHash": 1234567890,
     "stackSize": 1,
     "transferToVault": true,
     "itemId": "6917529047958703104",
     "characterId": "2305843009265042115",
     "membershipType": 3
   }

3. Verify transfer by checking inventory again
   GET /Destiny2/3/Profile/4611686018467260757/?components=102,103
```

### Equipment Management

**Purpose**: Equip items on characters.

**Prerequisites**: OAuth authentication with `MoveEquipDestinyItems` scope

**Steps**:
1. **Get Equipment State**: Check current equipped items
2. **Equip Item**: Equip the desired item
3. **Verify Equipment**: Confirm item is equipped

**Endpoints Used**:
```
GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=CharacterEquipment
POST /Destiny2/Actions/Items/EquipItem/
```

**Example Workflow**:
```
1. Get current equipment
   GET /Destiny2/3/Profile/4611686018467260757/?components=205

2. Equip weapon
   POST /Destiny2/Actions/Items/EquipItem/
   Body: {
     "itemId": "6917529047958703104",
     "characterId": "2305843009265042115",
     "membershipType": 3
   }
```

### Loadout Management

**Purpose**: Create and manage character loadouts.

**Prerequisites**: OAuth authentication with `MoveEquipDestinyItems` scope

**Steps**:
1. **Create Loadout Snapshot**: Capture current equipment as loadout
2. **Store Loadout**: Save loadout configuration
3. **Apply Loadout**: Equip saved loadout on character

**Endpoints Used**:
```
POST /Destiny2/Actions/Loadouts/SnapshotLoadout/
POST /Destiny2/Actions/Loadouts/EquipLoadout/
```

---

## Clan Operations

### Joining a Clan

**Purpose**: Find and join a clan.

**Prerequisites**: OAuth authentication with appropriate group scopes

**Steps**:
1. **Search Clans**: Find clans matching criteria
2. **Get Clan Details**: Review clan information
3. **Request to Join**: Submit join request
4. **Monitor Status**: Check application status

**Endpoints Used**:
```
POST /GroupV2/Search/
GET /GroupV2/{groupId}/
POST /GroupV2/{groupId}/Members/Apply/
GET /GroupV2/User/{membershipType}/{membershipId}/0/1/
```

### Clan Management (Admin)

**Purpose**: Manage clan members and settings.

**Prerequisites**: OAuth authentication with `AdminGroups` scope and appropriate clan permissions

**Steps**:
1. **Get Pending Members**: Review join requests
2. **Approve/Deny Members**: Process applications
3. **Manage Members**: Set roles and permissions
4. **Update Clan Settings**: Modify clan configuration

**Endpoints Used**:
```
GET /GroupV2/{groupId}/Members/Pending/
POST /GroupV2/{groupId}/Members/Approve/{membershipType}/{membershipId}/
POST /GroupV2/{groupId}/Members/SetMembershipType/{memberType}/
POST /GroupV2/{groupId}/Edit/
```

### Clan Statistics

**Purpose**: Get clan performance data.

**Steps**:
1. **Get Weekly Rewards**: Check clan reward status
2. **Get Clan Stats**: Retrieve aggregate statistics
3. **Get Leaderboards**: View clan rankings

**Endpoints Used**:
```
GET /Destiny2/Clan/{groupId}/WeeklyRewardState/
GET /Destiny2/Stats/AggregateClanStats/{groupId}/
GET /Destiny2/Stats/Leaderboards/Clans/{groupId}/
```

---

## Social Interactions

### Friend Management

**Purpose**: Manage friend relationships.

**Prerequisites**: OAuth authentication with `ReadUserData` scope

**Steps**:
1. **Get Friend List**: Retrieve current friends
2. **Get Friend Requests**: Check pending requests
3. **Send Friend Request**: Add new friend
4. **Manage Requests**: Accept/decline requests

**Endpoints Used**:
```
GET /Social/Friends/
GET /Social/Friends/Requests/
POST /Social/Friends/Add/{membershipId}/
POST /Social/Friends/Requests/Accept/{membershipId}/
POST /Social/Friends/Requests/Decline/{membershipId}/
```

**Example Workflow**:
```
1. Get current friends
   GET /Social/Friends/

2. Get pending friend requests
   GET /Social/Friends/Requests/

3. Send friend request
   POST /Social/Friends/Add/4611686018467260757/

4. Accept friend request
   POST /Social/Friends/Requests/Accept/4611686018467260757/
```

---

## Fireteam Finding

### Using Fireteam Finder

**Purpose**: Find or create groups for activities.

**Prerequisites**: OAuth authentication with appropriate scopes

**Steps**:
1. **Check Character Access**: Verify character can access desired activity
2. **Search Fireteams**: Find available groups
3. **Apply to Fireteam**: Submit application
4. **Monitor Application**: Track application status

**Endpoints Used**:
```
GET /FireteamFinder/CharacterActivityAccess/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
POST /FireteamFinder/Search/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
POST /FireteamFinder/Listing/{listingId}/Apply/{applicationType}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
GET /FireteamFinder/PlayerApplications/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
```

### Creating a Fireteam

**Purpose**: Host a fireteam for others to join.

**Prerequisites**: OAuth authentication with appropriate scopes

**Steps**:
1. **Host Lobby**: Create fireteam lobby
2. **Configure Settings**: Set activity and requirements
3. **Manage Applications**: Review and approve players
4. **Start Activity**: Launch the activity

**Endpoints Used**:
```
POST /FireteamFinder/Lobby/Host/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
POST /FireteamFinder/Lobby/UpdateSettings/{lobbyId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
GET /FireteamFinder/Lobby/{lobbyId}/Applications/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
POST /FireteamFinder/Application/Respond/{applicationId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
```

---

## Statistics and Reporting

### Player Performance Analysis

**Purpose**: Analyze player performance across activities.

**Steps**:
1. **Get Account Stats**: Retrieve overall account statistics
2. **Get Character Stats**: Get character-specific performance
3. **Get Activity History**: Review recent activity performance
4. **Generate Reports**: Create carnage reports for specific activities

**Endpoints Used**:
```
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/
GET /Destiny2/Stats/PostGameCarnageReport/{activityId}/
```

### Leaderboard Tracking

**Purpose**: Compare player performance against others.

**Steps**:
1. **Get Personal Leaderboards**: Check player's rankings
2. **Get Clan Leaderboards**: Compare within clan
3. **Get Global Leaderboards**: View top performers

**Endpoints Used**:
```
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/
GET /Destiny2/Stats/Leaderboards/Clans/{groupId}/
GET /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/
```

---

## Content Discovery

### News and Updates

**Purpose**: Stay current with game news and updates.

**Steps**:
1. **Get News Articles**: Retrieve latest news
2. **Search Content**: Find specific content types
3. **Get Trending**: Check what's popular
4. **RSS Integration**: Subscribe to news feeds

**Endpoints Used**:
```
GET /Content/Search/{locale}/
GET /Content/GetContentByTagAndType/{tag}/{type}/{locale}/
GET /Trending/Categories/
GET /Content/Rss/NewsArticles/{pageToken}/
```

### Community Content

**Purpose**: Discover community-generated content.

**Steps**:
1. **Browse Community Content**: View user submissions
2. **Filter by Type**: Find specific content types
3. **Get Trending Community**: Popular community content

**Endpoints Used**:
```
GET /CommunityContent/Get/{sort}/{mediaFilter}/{page}/
GET /Trending/Categories/{categoryId}/{pageNumber}/
```

---

## Error Handling and Best Practices

### Common Error Scenarios

1. **Rate Limiting**: Monitor `ThrottleSeconds` in responses
2. **Authentication Errors**: Handle expired tokens
3. **Permission Errors**: Verify OAuth scopes
4. **Data Validation**: Check required parameters

### Best Practices

1. **Cache Responses**: Cache static data like manifest definitions
2. **Batch Requests**: Group related operations when possible
3. **Handle Throttling**: Respect rate limits and retry after delays
4. **Error Recovery**: Implement proper error handling and user feedback
5. **Token Management**: Refresh tokens before expiration

### Response Format

All API responses follow this standard format:
```json
{
  "Response": {}, // Actual response data
  "ErrorCode": 1, // Error code (1 = success)
  "ThrottleSeconds": 0, // Seconds to wait before next request
  "ErrorStatus": "Success", // Error status text
  "Message": "Ok", // Response message
  "MessageData": {}, // Additional message data
  "DetailedErrorTrace": "" // Detailed error information
}
```

For more detailed information about specific endpoints, see the [Endpoint Reference](endpoint-by-function.md) and individual endpoint documentation in the `endpoint-details` directory.