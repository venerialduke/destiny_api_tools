# Applications.ApplicationScopes

## Entity Information
- **Entity Name**: Applications.ApplicationScopes
- **Entity Type**: Enumeration
- **Format**: int64
- **Base Type**: integer

## Description
Defines the various scopes/permissions that can be granted to applications accessing the Bungie API. These scopes determine what data and operations an application can access.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 1 | ReadBasicUserProfile | Read basic user profile information such as the user's handle, avatar icon, etc. |
| 2 | ReadGroups | Read Group/Clan Forums, Wall, and Members for groups and clans that the user has joined. |
| 4 | WriteGroups | Write Group/Clan Forums, Wall, and Members for groups and clans that the user has joined. |
| 8 | AdminGroups | Administer Group/Clan Forums, Wall, and Members for groups and clans that the user is a founder or an administrator. |
| 16 | BnetWrite | Create new groups, clans, and forum posts, along with other actions that are reserved for Bungie.net elevated scope: not meant to be used by third party applications. |
| 32 | MoveEquipDestinyItems | Move or equip Destiny items |
| 64 | ReadDestinyInventoryAndVault | Read Destiny 1 Inventory and Vault contents. For Destiny 2, this scope is needed to read anything regarded as private. This is the only scope a Destiny 2 app needs for read operations against Destiny 2 data such as inventory, vault, currency, vendors, milestones, progression, etc. |
| 128 | ReadUserData | Read user data such as who they are web notifications, clan/group memberships, recent activity, muted users. |
| 256 | EditUserData | Edit user data such as preferred language, status, motto, avatar selection and theme. |
| 512 | ReadDestinyVendorsAndAdvisors | Access vendor and advisor data specific to a user. OBSOLETE. This scope is only used on the Destiny 1 API. |
| 1024 | ReadAndApplyTokens | Read offer history and claim and apply tokens for the user. |
| 2048 | AdvancedWriteActions | Can perform actions that will result in a prompt to the user via the Destiny app. |
| 4096 | PartnerOfferGrant | Can use the partner offer api to claim rewards defined for a partner |
| 8192 | DestinyUnlockValueQuery | Allows an app to query sensitive information like unlock flags and values not available through normal methods. |
| 16384 | UserPiiRead | Allows an app to query sensitive user PII, most notably email information. |

## Usage Examples

### JavaScript
```javascript
// Using scope values
const scopes = {
  ReadBasicUserProfile: 1,
  ReadGroups: 2,
  WriteGroups: 4,
  MoveEquipDestinyItems: 32,
  ReadDestinyInventoryAndVault: 64
};

// Combining scopes using bitwise OR
const combinedScopes = scopes.ReadBasicUserProfile | scopes.ReadDestinyInventoryAndVault;
```

### Python
```python
# Using scope values
class ApplicationScopes:
    READ_BASIC_USER_PROFILE = 1
    READ_GROUPS = 2
    WRITE_GROUPS = 4
    MOVE_EQUIP_DESTINY_ITEMS = 32
    READ_DESTINY_INVENTORY_AND_VAULT = 64

# Combining scopes
combined_scopes = ApplicationScopes.READ_BASIC_USER_PROFILE | ApplicationScopes.READ_DESTINY_INVENTORY_AND_VAULT
```

## Related Entities
- **Applications.Application**: Uses these scopes to define permissions
- **Applications.ApplicationStatus**: Related to application management
- **Applications.OAuthApplicationType**: Defines application types

## Notes
- This is a flags enumeration where values can be combined using bitwise operations
- The ReadDestinyInventoryAndVault scope (64) is the primary scope needed for Destiny 2 applications
- Some scopes like ReadDestinyVendorsAndAdvisors are obsolete and only used for Destiny 1
- BnetWrite scope is reserved for Bungie.net internal use

## JSON Schema
```json
{
  "Applications.ApplicationScopes": {
    "format": "int64",
    "enum": [
      "1", "2", "4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384"
    ],
    "type": "integer",
    "x-enum-values": [
      {
        "numericValue": "1",
        "identifier": "ReadBasicUserProfile",
        "description": "Read basic user profile information such as the user's handle, avatar icon, etc."
      }
      // ... additional enum values
    ]
  }
}
```