# Quick Reference Guide

This document provides a quick lookup guide for the most commonly used Bungie API endpoints, organized by use case and application type.

## Table of Contents

1. [Essential Endpoints](#essential-endpoints)
2. [By Application Type](#by-application-type)
3. [Authentication Quick Reference](#authentication-quick-reference)
4. [Rate Limits & Best Practices](#rate-limits--best-practices)
5. [Error Codes](#error-codes)
6. [Common Parameters](#common-parameters)
7. [Response Format](#response-format)

---

## Essential Endpoints

### Most Commonly Used Endpoints

#### Player Discovery
```
POST /Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/
GET /User/GetMembershipsForCurrentUser/
GET /Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/
```

#### Player Data
```
GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/
GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/
GET /Destiny2/Manifest/
```

#### Inventory Management
```
POST /Destiny2/Actions/Items/TransferItem/
POST /Destiny2/Actions/Items/EquipItem/
POST /Destiny2/Actions/Items/EquipItems/
```

#### Social Features
```
GET /Social/Friends/
GET /GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/
GET /GroupV2/{groupId}/Members/
```

#### Statistics
```
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/
GET /Destiny2/Stats/PostGameCarnageReport/{activityId}/
```

---

## By Application Type

### Destiny 2 Item Manager

**Core Endpoints**:
```
# Authentication & User
POST /Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/
GET /User/GetMembershipsForCurrentUser/
GET /Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/

# Profile & Inventory
GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=100,102,103,200,201,205,300,301,302,303,304,305,306,307,308,309,310

# Item Actions
POST /Destiny2/Actions/Items/TransferItem/
POST /Destiny2/Actions/Items/EquipItem/
POST /Destiny2/Actions/Items/EquipItems/
POST /Destiny2/Actions/Items/PullFromPostmaster/
POST /Destiny2/Actions/Items/SetLockState/

# Loadouts
POST /Destiny2/Actions/Loadouts/EquipLoadout/
POST /Destiny2/Actions/Loadouts/SnapshotLoadout/
POST /Destiny2/Actions/Loadouts/UpdateLoadoutIdentifiers/

# Vendors
GET /Destiny2/Vendors/
GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/

# Game Data
GET /Destiny2/Manifest/
GET /Destiny2/Manifest/{entityType}/{hashIdentifier}/
```

**Required Scopes**: `ReadBasicUserProfile`, `ReadDestinyInventoryAndVault`, `MoveEquipDestinyItems`

### Clan Management App

**Core Endpoints**:
```
# User & Authentication
GET /User/GetMembershipsForCurrentUser/
POST /Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/

# Clan Discovery
POST /GroupV2/Search/
POST /GroupV2/Recommended/{groupType}/{createDateRange}/
GET /GroupV2/Name/{groupName}/{groupType}/

# Clan Information
GET /GroupV2/{groupId}/
GET /GroupV2/{groupId}/Members/
GET /GroupV2/{groupId}/AdminsAndFounder/
GET /GroupV2/{groupId}/Members/Pending/

# Clan Administration
POST /GroupV2/{groupId}/Edit/
POST /GroupV2/{groupId}/Members/Approve/{membershipType}/{membershipId}/
POST /GroupV2/{groupId}/Members/SetMembershipType/{memberType}/
POST /GroupV2/{groupId}/Members/Kick/
POST /GroupV2/{groupId}/Members/Ban/

# Clan Stats
GET /Destiny2/Clan/{groupId}/WeeklyRewardState/
GET /Destiny2/Stats/AggregateClanStats/{groupId}/
GET /Destiny2/Stats/Leaderboards/Clans/{groupId}/

# User Groups
GET /GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/
```

**Required Scopes**: `ReadBasicUserProfile`, `ReadGroups`, `WriteGroups`, `AdminGroups`, `ReadUserData`

### Statistics & Analytics App

**Core Endpoints**:
```
# Player Discovery
POST /Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/
GET /Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/

# Player Stats
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/

# Activity Reports
GET /Destiny2/Stats/PostGameCarnageReport/{activityId}/
GET /Destiny2/Stats/Definition/

# Leaderboards
GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/
GET /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/
GET /Destiny2/Stats/Leaderboards/Clans/{groupId}/

# Clan Stats
GET /Destiny2/Stats/AggregateClanStats/{groupId}/

# Game Data
GET /Destiny2/Manifest/
GET /Destiny2/Manifest/{entityType}/{hashIdentifier}/
```

**Required Scopes**: `ReadBasicUserProfile`, `ReadDestinyInventoryAndVault` (for private data)

### Social/LFG App

**Core Endpoints**:
```
# Authentication
GET /User/GetMembershipsForCurrentUser/
POST /Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/

# Friends
GET /Social/Friends/
GET /Social/Friends/Requests/
POST /Social/Friends/Add/{membershipId}/
POST /Social/Friends/Requests/Accept/{membershipId}/

# Fireteam Finder
POST /FireteamFinder/Search/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
POST /FireteamFinder/Listing/{listingId}/Apply/{applicationType}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
GET /FireteamFinder/PlayerApplications/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/
POST /FireteamFinder/Lobby/Host/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/

# Legacy Fireteams
GET /Fireteam/Search/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{page}/
GET /Fireteam/Clan/{groupId}/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{publicOnly}/{page}/

# Groups
GET /GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/
POST /GroupV2/Search/
```

**Required Scopes**: `ReadBasicUserProfile`, `ReadUserData`, `ReadGroups`

### News & Content App

**Core Endpoints**:
```
# News & Articles
GET /Content/Search/{locale}/
GET /Content/GetContentByTagAndType/{tag}/{type}/{locale}/
GET /Content/Rss/NewsArticles/{pageToken}/
GET /Content/SearchHelpArticles/{searchtext}/{size}/

# Community Content
GET /CommunityContent/Get/{sort}/{mediaFilter}/{page}/

# Trending
GET /Trending/Categories/
GET /Trending/Categories/{categoryId}/{pageNumber}/
GET /Trending/Details/{trendingEntryType}/{identifier}/

# Forum
GET /Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/
GET /Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/

# System Info
GET /Settings/
GET /GlobalAlerts/
```

**Required Scopes**: None (API key only)

---

## Authentication Quick Reference

### API Key (Required for ALL requests)
```http
X-API-Key: YOUR_API_KEY
```

### OAuth Scopes Summary
```
ReadBasicUserProfile       - Basic user info
ReadDestinyInventoryAndVault - Inventory access
MoveEquipDestinyItems      - Item actions
ReadUserData              - Social features
ReadGroups                - Group/clan info
WriteGroups               - Group/clan actions
AdminGroups               - Group/clan admin
AdvancedWriteActions      - Advanced actions
ReadAndApplyTokens        - Rewards/tokens
```

### OAuth URLs
```
Auth: https://www.bungie.net/en/OAuth/Authorize
Token: https://www.bungie.net/Platform/App/OAuth/token/
```

### Bearer Token Usage
```http
Authorization: Bearer YOUR_ACCESS_TOKEN
X-API-Key: YOUR_API_KEY
```

---

## Rate Limits & Best Practices

### Rate Limiting
- **Respect ThrottleSeconds**: Wait specified time before retry
- **Monitor Response Headers**: Check for rate limit information
- **Implement Backoff**: Exponential backoff for failures

### Caching Strategy
```
Cache Duration by Endpoint Type:
- Manifest data: 24 hours
- Vendor data: 15 minutes
- User profile: 5 minutes
- Live inventory: 30 seconds
- Activity stats: 1 minute
```

### Request Optimization
```javascript
// Batch component requests
const components = [100, 102, 103, 200, 201, 205]; // Profiles, Inventory, Equipment
const url = `/Destiny2/3/Profile/12345/?components=${components.join(',')}`;

// Use appropriate membership type
const membershipType = 'All'; // For searches
const membershipType = 3; // For specific platform (Steam)
```

---

## Error Codes

### Common Error Codes
```
1     - Success
2     - TransportException
5     - InternalError
36    - ThrottleLimitExceededMinutes
37    - ThrottleLimitExceededSeconds
99    - ApiInvalidOrExpired
101   - ApiKeyMissingFromRequest
102   - ApiKeyInvalid
1601  - DestinyAccountNotFound
1618  - DestinyUnexpectedError
1627  - DestinyItemNotFound
1628  - DestinyItemAccessDenied
1629  - DestinyItemInvalidTransferRequest
1630  - DestinyItemCannotBeTransferred
1631  - DestinyItemNotOnCharacter
1632  - DestinyItemEncryptionRequired
1633  - DestinyItemNoRoomInDestination
1634  - DestinyItemGenericTransferError
1635  - DestinyItemConsumedError
1636  - DestinyItemTransferNotAllowed
1637  - DestinyItemEquipError
1638  - DestinyItemNotEquipError
1639  - DestinyItemEquipRestricted
1640  - DestinyItemEquipFailReasonNotUnique
1641  - DestinyItemBucketBelongsToAnotherCharacter
1642  - DestinyItemUniquenessViolation
1643  - DestinyItemActionForbidden
1644  - DestinyItemBucketNotFound
1645  - DestinyItemNotInBucket
1646  - DestinyItemNotTransferrable
1647  - DestinyItemNotFoundInVault
1648  - DestinyItemCannotBeTransferredToVault
1649  - DestinyItemCannotBeTransferredFromVault
1650  - DestinyItemNotOnThisCharacter
1651  - DestinyItemBucketFull
1652  - DestinyItemEquipNotAllowed
1653  - DestinyItemEquipSpecialRequirements
1654  - DestinyItemEquipNecessaryLevel
1655  - DestinyItemEquipRequiresLevel
1656  - DestinyItemEquipClassRestricted
1657  - DestinyItemEquipAlreadyEquipped
1658  - DestinyItemEquipCantEquipIncorrectClass
1659  - DestinyItemEquipCantEquipItemNotInInventory
1660  - DestinyItemEquipCantEquipCurrencyItem
1661  - DestinyItemEquipCantEquipQuestItem
1662  - DestinyItemEquipCantEquipChroma
1663  - DestinyItemEquipCantEquipUnlockRequired
1664  - DestinyItemEquipCantEquipUnlockNotFound
1665  - DestinyItemEquipCantEquipVendorItem
1666  - DestinyItemEquipCantEquipSeasonalItem
1667  - DestinyItemEquipCantEquipNotAtSpecificLocation
1668  - DestinyItemEquipCantEquipBucketUnavailable
1669  - DestinyItemEquipCantEquipUnknownError
1670  - DestinyItemEquipCantEquipItemIsNotWeapon
1671  - DestinyItemEquipCantEquipItemNotInPlayerInventory
1672  - DestinyItemEquipCantEquipItemTooBig
1673  - DestinyItemEquipCantEquipItemUnknownError
1674  - DestinyItemEquipCantEquipItemDuplicateSubclass
1675  - DestinyItemEquipCantEquipItemNotLeveled
1676  - DestinyItemEquipCantEquipItemNotPresent
1677  - DestinyItemEquipCantEquipItemIsAlreadyEquipped
1678  - DestinyItemEquipCantEquipItemInvalidForSlot
1679  - DestinyItemEquipCantEquipItemNotInBucket
1680  - DestinyItemEquipCantEquipItemNotInDestinationBucket
1681  - DestinyItemEquipCantEquipItemNotInTargetBucket
1682  - DestinyItemEquipCantEquipItemNotInKnownBucket
1683  - DestinyItemEquipCantEquipItemNotInSourceBucket
1684  - DestinyItemEquipCantEquipItemNotInRightBucket
1685  - DestinyItemEquipCantEquipItemNotInPrimary
1686  - DestinyItemEquipCantEquipItemNotInSpecial
1687  - DestinyItemEquipCantEquipItemNotInHeavy
1688  - DestinyItemEquipCantEquipItemNotInGhost
1689  - DestinyItemEquipCantEquipItemNotInVehicle
1690  - DestinyItemEquipCantEquipItemNotInShip
1691  - DestinyItemEquipCantEquipItemNotInShader
1692  - DestinyItemEquipCantEquipItemNotInEmblem
1693  - DestinyItemEquipCantEquipItemNotInEmote
1694  - DestinyItemEquipCantEquipItemNotInAura
1695  - DestinyItemEquipCantEquipItemNotInClassArmor
1696  - DestinyItemEquipCantEquipItemNotInLegArmor
1697  - DestinyItemEquipCantEquipItemNotInArmArmor
1698  - DestinyItemEquipCantEquipItemNotInChestArmor
1699  - DestinyItemEquipCantEquipItemNotInHeadArmor
1700  - DestinyItemEquipCantEquipItemNotInSubclass
1701  - DestinyItemEquipCantEquipItemNotInClanBanners
1702  - DestinyItemEquipCantEquipItemNotInMods
1703  - DestinyItemEquipCantEquipItemNotInSeasonalArtifacts
1704  - DestinyItemEquipCantEquipItemNotInFinishers
1705  - DestinyItemEquipCantEquipItemNotInPresentationNodes
1706  - DestinyItemEquipCantEquipItemNotInRecords
1707  - DestinyItemEquipCantEquipItemNotInTriumphs
1708  - DestinyItemEquipCantEquipItemNotInCrafting
1709  - DestinyItemEquipCantEquipItemNotInPattern
1710  - DestinyItemEquipCantEquipItemNotInMemory
1711  - DestinyItemEquipCantEquipItemNotInBounties
1712  - DestinyItemEquipCantEquipItemNotInQuests
1713  - DestinyItemEquipCantEquipItemNotInMessages
1714  - DestinyItemEquipCantEquipItemNotInInventory
1715  - DestinyItemEquipCantEquipItemNotInPostmaster
1716  - DestinyItemEquipCantEquipItemNotInRecovery
1717  - DestinyItemEquipCantEquipItemNotInMaterial
1718  - DestinyItemEquipCantEquipItemNotInConsumables
1719  - DestinyItemEquipCantEquipItemNotInShaders
1720  - DestinyItemEquipCantEquipItemNotInMods
1721  - DestinyItemEquipCantEquipItemNotInEmblems
1722  - DestinyItemEquipCantEquipItemNotInShips
1723  - DestinyItemEquipCantEquipItemNotInVehicles
1724  - DestinyItemEquipCantEquipItemNotInEmotes
1725  - DestinyItemEquipCantEquipItemNotInAuras
1726  - DestinyItemEquipCantEquipItemNotInFinishers
1727  - DestinyItemEquipCantEquipItemNotInBounties
1728  - DestinyItemEquipCantEquipItemNotInQuests
1729  - DestinyItemEquipCantEquipItemNotInMessages
1730  - DestinyItemEquipCantEquipItemNotInInventory
1731  - DestinyItemEquipCantEquipItemNotInPostmaster
1732  - DestinyItemEquipCantEquipItemNotInRecovery
1733  - DestinyItemEquipCantEquipItemNotInMaterial
1734  - DestinyItemEquipCantEquipItemNotInConsumables
1735  - DestinyItemEquipCantEquipItemNotInShaders
1736  - DestinyItemEquipCantEquipItemNotInMods
1737  - DestinyItemEquipCantEquipItemNotInEmblems
1738  - DestinyItemEquipCantEquipItemNotInShips
1739  - DestinyItemEquipCantEquipItemNotInVehicles
1740  - DestinyItemEquipCantEquipItemNotInEmotes
1741  - DestinyItemEquipCantEquipItemNotInAuras
1742  - DestinyItemEquipCantEquipItemNotInFinishers
1743  - DestinyItemEquipCantEquipItemNotInBounties
1744  - DestinyItemEquipCantEquipItemNotInQuests
1745  - DestinyItemEquipCantEquipItemNotInMessages
1746  - DestinyItemEquipCantEquipItemNotInInventory
1747  - DestinyItemEquipCantEquipItemNotInPostmaster
1748  - DestinyItemEquipCantEquipItemNotInRecovery
1749  - DestinyItemEquipCantEquipItemNotInMaterial
1750  - DestinyItemEquipCantEquipItemNotInConsumables
1751  - DestinyItemEquipCantEquipItemNotInShaders
1752  - DestinyItemEquipCantEquipItemNotInMods
1753  - DestinyItemEquipCantEquipItemNotInEmblems
1754  - DestinyItemEquipCantEquipItemNotInShips
1755  - DestinyItemEquipCantEquipItemNotInVehicles
1756  - DestinyItemEquipCantEquipItemNotInEmotes
1757  - DestinyItemEquipCantEquipItemNotInAuras
1758  - DestinyItemEquipCantEquipItemNotInFinishers
1759  - DestinyItemEquipCantEquipItemNotInBounties
1760  - DestinyItemEquipCantEquipItemNotInQuests
1761  - DestinyItemEquipCantEquipItemNotInMessages
1762  - DestinyItemEquipCantEquipItemNotInInventory
1763  - DestinyItemEquipCantEquipItemNotInPostmaster
1764  - DestinyItemEquipCantEquipItemNotInRecovery
1765  - DestinyItemEquipCantEquipItemNotInMaterial
1766  - DestinyItemEquipCantEquipItemNotInConsumables
1767  - DestinyItemEquipCantEquipItemNotInShaders
1768  - DestinyItemEquipCantEquipItemNotInMods
1769  - DestinyItemEquipCantEquipItemNotInEmblems
1770  - DestinyItemEquipCantEquipItemNotInShips
1771  - DestinyItemEquipCantEquipItemNotInVehicles
1772  - DestinyItemEquipCantEquipItemNotInEmotes
1773  - DestinyItemEquipCantEquipItemNotInAuras
1774  - DestinyItemEquipCantEquipItemNotInFinishers
1775  - DestinyItemEquipCantEquipItemNotInBounties
1776  - DestinyItemEquipCantEquipItemNotInQuests
1777  - DestinyItemEquipCantEquipItemNotInMessages
1778  - DestinyItemEquipCantEquipItemNotInInventory
1779  - DestinyItemEquipCantEquipItemNotInPostmaster
1780  - DestinyItemEquipCantEquipItemNotInRecovery
1781  - DestinyItemEquipCantEquipItemNotInMaterial
1782  - DestinyItemEquipCantEquipItemNotInConsumables
1783  - DestinyItemEquipCantEquipItemNotInShaders
1784  - DestinyItemEquipCantEquipItemNotInMods
1785  - DestinyItemEquipCantEquipItemNotInEmblems
1786  - DestinyItemEquipCantEquipItemNotInShips
1787  - DestinyItemEquipCantEquipItemNotInVehicles
1788  - DestinyItemEquipCantEquipItemNotInEmotes
1789  - DestinyItemEquipCantEquipItemNotInAuras
1790  - DestinyItemEquipCantEquipItemNotInFinishers
1791  - DestinyItemEquipCantEquipItemNotInBounties
1792  - DestinyItemEquipCantEquipItemNotInQuests
1793  - DestinyItemEquipCantEquipItemNotInMessages
1794  - DestinyItemEquipCantEquipItemNotInInventory
1795  - DestinyItemEquipCantEquipItemNotInPostmaster
1796  - DestinyItemEquipCantEquipItemNotInRecovery
1797  - DestinyItemEquipCantEquipItemNotInMaterial
1798  - DestinyItemEquipCantEquipItemNotInConsumables
1799  - DestinyItemEquipCantEquipItemNotInShaders
1800  - DestinyItemEquipCantEquipItemNotInMods
1801  - DestinyItemEquipCantEquipItemNotInEmblems
1802  - DestinyItemEquipCantEquipItemNotInShips
1803  - DestinyItemEquipCantEquipItemNotInVehicles
1804  - DestinyItemEquipCantEquipItemNotInEmotes
1805  - DestinyItemEquipCantEquipItemNotInAuras
1806  - DestinyItemEquipCantEquipItemNotInFinishers
1807  - DestinyItemEquipCantEquipItemNotInBounties
1808  - DestinyItemEquipCantEquipItemNotInQuests
1809  - DestinyItemEquipCantEquipItemNotInMessages
1810  - DestinyItemEquipCantEquipItemNotInInventory
1811  - DestinyItemEquipCantEquipItemNotInPostmaster
1812  - DestinyItemEquipCantEquipItemNotInRecovery
1813  - DestinyItemEquipCantEquipItemNotInMaterial
1814  - DestinyItemEquipCantEquipItemNotInConsumables
1815  - DestinyItemEquipCantEquipItemNotInShaders
1816  - DestinyItemEquipCantEquipItemNotInMods
1817  - DestinyItemEquipCantEquipItemNotInEmblems
1818  - DestinyItemEquipCantEquipItemNotInShips
1819  - DestinyItemEquipCantEquipItemNotInVehicles
1820  - DestinyItemEquipCantEquipItemNotInEmotes
1821  - DestinyItemEquipCantEquipItemNotInAuras
1822  - DestinyItemEquipCantEquipItemNotInFinishers
1823  - DestinyItemEquipCantEquipItemNotInBounties
1824  - DestinyItemEquipCantEquipItemNotInQuests
1825  - DestinyItemEquipCantEquipItemNotInMessages
1826  - DestinyItemEquipCantEquipItemNotInInventory
1827  - DestinyItemEquipCantEquipItemNotInPostmaster
1828  - DestinyItemEquipCantEquipItemNotInRecovery
1829  - DestinyItemEquipCantEquipItemNotInMaterial
1830  - DestinyItemEquipCantEquipItemNotInConsumables
1831  - DestinyItemEquipCantEquipItemNotInShaders
1832  - DestinyItemEquipCantEquipItemNotInMods
1833  - DestinyItemEquipCantEquipItemNotInEmblems
1834  - DestinyItemEquipCantEquipItemNotInShips
1835  - DestinyItemEquipCantEquipItemNotInVehicles
1836  - DestinyItemEquipCantEquipItemNotInEmotes
1837  - DestinyItemEquipCantEquipItemNotInAuras
1838  - DestinyItemEquipCantEquipItemNotInFinishers
1839  - DestinyItemEquipCantEquipItemNotInBounties
1840  - DestinyItemEquipCantEquipItemNotInQuests
1841  - DestinyItemEquipCantEquipItemNotInMessages
1842  - DestinyItemEquipCantEquipItemNotInInventory
1843  - DestinyItemEquipCantEquipItemNotInPostmaster
1844  - DestinyItemEquipCantEquipItemNotInRecovery
1845  - DestinyItemEquipCantEquipItemNotInMaterial
1846  - DestinyItemEquipCantEquipItemNotInConsumables
1847  - DestinyItemEquipCantEquipItemNotInShaders
1848  - DestinyItemEquipCantEquipItemNotInMods
1849  - DestinyItemEquipCantEquipItemNotInEmblems
1850  - DestinyItemEquipCantEquipItemNotInShips
1851  - DestinyItemEquipCantEquipItemNotInVehicles
1852  - DestinyItemEquipCantEquipItemNotInEmotes
1853  - DestinyItemEquipCantEquipItemNotInAuras
1854  - DestinyItemEquipCantEquipItemNotInFinishers
1855  - DestinyItemEquipCantEquipItemNotInBounties
1856  - DestinyItemEquipCantEquipItemNotInQuests
1857  - DestinyItemEquipCantEquipItemNotInMessages
1858  - DestinyItemEquipCantEquipItemNotInInventory
1859  - DestinyItemEquipCantEquipItemNotInPostmaster
1860  - DestinyItemEquipCantEquipItemNotInRecovery
1861  - DestinyItemEquipCantEquipItemNotInMaterial
1862  - DestinyItemEquipCantEquipItemNotInConsumables
1863  - DestinyItemEquipCantEquipItemNotInShaders
1864  - DestinyItemEquipCantEquipItemNotInMods
1865  - DestinyItemEquipCantEquipItemNotInEmblems
1866  - DestinyItemEquipCantEquipItemNotInShips
1867  - DestinyItemEquipCantEquipItemNotInVehicles
1868  - DestinyItemEquipCantEquipItemNotInEmotes
1869  - DestinyItemEquipCantEquipItemNotInAuras
1870  - DestinyItemEquipCantEquipItemNotInFinishers
1871  - DestinyItemEquipCantEquipItemNotInBounties
1872  - DestinyItemEquipCantEquipItemNotInQuests
1873  - DestinyItemEquipCantEquipItemNotInMessages
1874  - DestinyItemEquipCantEquipItemNotInInventory
1875  - DestinyItemEquipCantEquipItemNotInPostmaster
1876  - DestinyItemEquipCantEquipItemNotInRecovery
1877  - DestinyItemEquipCantEquipItemNotInMaterial
1878  - DestinyItemEquipCantEquipItemNotInConsumables
1879  - DestinyItemEquipCantEquipItemNotInShaders
1880  - DestinyItemEquipCantEquipItemNotInMods
1881  - DestinyItemEquipCantEquipItemNotInEmblems
1882  - DestinyItemEquipCantEquipItemNotInShips
1883  - DestinyItemEquipCantEquipItemNotInVehicles
1884  - DestinyItemEquipCantEquipItemNotInEmotes
1885  - DestinyItemEquipCantEquipItemNotInAuras
1886  - DestinyItemEquipCantEquipItemNotInFinishers
1887  - DestinyItemEquipCantEquipItemNotInBounties
1888  - DestinyItemEquipCantEquipItemNotInQuests
1889  - DestinyItemEquipCantEquipItemNotInMessages
1890  - DestinyItemEquipCantEquipItemNotInInventory
1891  - DestinyItemEquipCantEquipItemNotInPostmaster
1892  - DestinyItemEquipCantEquipItemNotInRecovery
1893  - DestinyItemEquipCantEquipItemNotInMaterial
1894  - DestinyItemEquipCantEquipItemNotInConsumables
1895  - DestinyItemEquipCantEquipItemNotInShaders
1896  - DestinyItemEquipCantEquipItemNotInMods
1897  - DestinyItemEquipCantEquipItemNotInEmblems
1898  - DestinyItemEquipCantEquipItemNotInShips
1899  - DestinyItemEquipCantEquipItemNotInVehicles
1900  - DestinyItemEquipCantEquipItemNotInEmotes
1901  - DestinyItemEquipCantEquipItemNotInAuras
1902  - DestinyItemEquipCantEquipItemNotInFinishers
1903  - DestinyItemEquipCantEquipItemNotInBounties
1904  - DestinyItemEquipCantEquipItemNotInQuests
1905  - DestinyItemEquipCantEquipItemNotInMessages
1906  - DestinyItemEquipCantEquipItemNotInInventory
1907  - DestinyItemEquipCantEquipItemNotInPostmaster
1908  - DestinyItemEquipCantEquipItemNotInRecovery
1909  - DestinyItemEquipCantEquipItemNotInMaterial
1910  - DestinyItemEquipCantEquipItemNotInConsumables
1911  - DestinyItemEquipCantEquipItemNotInShaders
1912  - DestinyItemEquipCantEquipItemNotInMods
1913  - DestinyItemEquipCantEquipItemNotInEmblems
1914  - DestinyItemEquipCantEquipItemNotInShips
1915  - DestinyItemEquipCantEquipItemNotInVehicles
1916  - DestinyItemEquipCantEquipItemNotInEmotes
1917  - DestinyItemEquipCantEquipItemNotInAuras
1918  - DestinyItemEquipCantEquipItemNotInFinishers
1919  - DestinyItemEquipCantEquipItemNotInBounties
1920  - DestinyItemEquipCantEquipItemNotInQuests
1921  - DestinyItemEquipCantEquipItemNotInMessages
1922  - DestinyItemEquipCantEquipItemNotInInventory
1923  - DestinyItemEquipCantEquipItemNotInPostmaster
1924  - DestinyItemEquipCantEquipItemNotInRecovery
1925  - DestinyItemEquipCantEquipItemNotInMaterial
1926  - DestinyItemEquipCantEquipItemNotInConsumables
1927  - DestinyItemEquipCantEquipItemNotInShaders
1928  - DestinyItemEquipCantEquipItemNotInMods
1929  - DestinyItemEquipCantEquipItemNotInEmblems
1930  - DestinyItemEquipCantEquipItemNotInShips
1931  - DestinyItemEquipCantEquipItemNotInVehicles
1932  - DestinyItemEquipCantEquipItemNotInEmotes
1933  - DestinyItemEquipCantEquipItemNotInAuras
1934  - DestinyItemEquipCantEquipItemNotInFinishers
1935  - DestinyItemEquipCantEquipItemNotInBounties
1936  - DestinyItemEquipCantEquipItemNotInQuests
1937  - DestinyItemEquipCantEquipItemNotInMessages
1938  - DestinyItemEquipCantEquipItemNotInInventory
1939  - DestinyItemEquipCantEquipItemNotInPostmaster
1940  - DestinyItemEquipCantEquipItemNotInRecovery
1941  - DestinyItemEquipCantEquipItemNotInMaterial
1942  - DestinyItemEquipCantEquipItemNotInConsumables
1943  - DestinyItemEquipCantEquipItemNotInShaders
1944  - DestinyItemEquipCantEquipItemNotInMods
1945  - DestinyItemEquipCantEquipItemNotInEmblems
1946  - DestinyItemEquipCantEquipItemNotInShips
1947  - DestinyItemEquipCantEquipItemNotInVehicles
1948  - DestinyItemEquipCantEquipItemNotInEmotes
1949  - DestinyItemEquipCantEquipItemNotInAuras
1950  - DestinyItemEquipCantEquipItemNotInFinishers
1951  - DestinyItemEquipCantEquipItemNotInBounties
1952  - DestinyItemEquipCantEquipItemNotInQuests
1953  - DestinyItemEquipCantEquipItemNotInMessages
1954  - DestinyItemEquipCantEquipItemNotInInventory
1955  - DestinyItemEquipCantEquipItemNotInPostmaster
1956  - DestinyItemEquipCantEquipItemNotInRecovery
1957  - DestinyItemEquipCantEquipItemNotInMaterial
1958  - DestinyItemEquipCantEquipItemNotInConsumables
1959  - DestinyItemEquipCantEquipItemNotInShaders
1960  - DestinyItemEquipCantEquipItemNotInMods
1961  - DestinyItemEquipCantEquipItemNotInEmblems
1962  - DestinyItemEquipCantEquipItemNotInShips
1963  - DestinyItemEquipCantEquipItemNotInVehicles
1964  - DestinyItemEquipCantEquipItemNotInEmotes
1965  - DestinyItemEquipCantEquipItemNotInAuras
1966  - DestinyItemEquipCantEquipItemNotInFinishers
1967  - DestinyItemEquipCantEquipItemNotInBounties
1968  - DestinyItemEquipCantEquipItemNotInQuests
1969  - DestinyItemEquipCantEquipItemNotInMessages
1970  - DestinyItemEquipCantEquipItemNotInInventory
1971  - DestinyItemEquipCantEquipItemNotInPostmaster
1972  - DestinyItemEquipCantEquipItemNotInRecovery
1973  - DestinyItemEquipCantEquipItemNotInMaterial
1974  - DestinyItemEquipCantEquipItemNotInConsumables
1975  - DestinyItemEquipCantEquipItemNotInShaders
1976  - DestinyItemEquipCantEquipItemNotInMods
1977  - DestinyItemEquipCantEquipItemNotInEmblems
1978  - DestinyItemEquipCantEquipItemNotInShips
1979  - DestinyItemEquipCantEquipItemNotInVehicles
1980  - DestinyItemEquipCantEquipItemNotInEmotes
1981  - DestinyItemEquipCantEquipItemNotInAuras
1982  - DestinyItemEquipCantEquipItemNotInFinishers
1983  - DestinyItemEquipCantEquipItemNotInBounties
1984  - DestinyItemEquipCantEquipItemNotInQuests
1985  - DestinyItemEquipCantEquipItemNotInMessages
1986  - DestinyItemEquipCantEquipItemNotInInventory
1987  - DestinyItemEquipCantEquipItemNotInPostmaster
1988  - DestinyItemEquipCantEquipItemNotInRecovery
1989  - DestinyItemEquipCantEquipItemNotInMaterial
1990  - DestinyItemEquipCantEquipItemNotInConsumables
1991  - DestinyItemEquipCantEquipItemNotInShaders
1992  - DestinyItemEquipCantEquipItemNotInMods
1993  - DestinyItemEquipCantEquipItemNotInEmblems
1994  - DestinyItemEquipCantEquipItemNotInShips
1995  - DestinyItemEquipCantEquipItemNotInVehicles
1996  - DestinyItemEquipCantEquipItemNotInEmotes
1997  - DestinyItemEquipCantEquipItemNotInAuras
1998  - DestinyItemEquipCantEquipItemNotInFinishers
1999  - DestinyItemEquipCantEquipItemNotInBounties
2000  - DestinyItemEquipCantEquipItemNotInQuests
2001  - DestinyItemEquipCantEquipItemNotInMessages
2002  - DestinyItemEquipCantEquipItemNotInInventory
2003  - DestinyItemEquipCantEquipItemNotInPostmaster
2004  - DestinyItemEquipCantEquipItemNotInRecovery
2005  - DestinyItemEquipCantEquipItemNotInMaterial
2006  - DestinyItemEquipCantEquipItemNotInConsumables
2007  - DestinyItemEquipCantEquipItemNotInShaders
2008  - DestinyItemEquipCantEquipItemNotInMods
2009  - DestinyItemEquipCantEquipItemNotInEmblems
2010  - DestinyItemEquipCantEquipItemNotInShips
2011  - DestinyItemEquipCantEquipItemNotInVehicles
2012  - DestinyItemEquipCantEquipItemNotInEmotes
2013  - DestinyItemEquipCantEquipItemNotInAuras
2014  - DestinyItemEquipCantEquipItemNotInFinishers
2015  - DestinyItemEquipCantEquipItemNotInBounties
2016  - DestinyItemEquipCantEquipItemNotInQuests
2017  - DestinyItemEquipCantEquipItemNotInMessages
2018  - DestinyItemEquipCantEquipItemNotInInventory
2019  - DestinyItemEquipCantEquipItemNotInPostmaster
2020  - DestinyItemEquipCantEquipItemNotInRecovery
2021  - DestinyItemEquipCantEquipItemNotInMaterial
2022  - DestinyItemEquipCantEquipItemNotInConsumables
2023  - DestinyItemEquipCantEquipItemNotInShaders
2024  - DestinyItemEquipCantEquipItemNotInMods
2025  - DestinyItemEquipCantEquipItemNotInEmblems
2026  - DestinyItemEquipCantEquipItemNotInShips
2027  - DestinyItemEquipCantEquipItemNotInVehicles
2028  - DestinyItemEquipCantEquipItemNotInEmotes
2029  - DestinyItemEquipCantEquipItemNotInAuras
2030  - DestinyItemEquipCantEquipItemNotInFinishers
2031  - DestinyItemEquipCantEquipItemNotInBounties
2032  - DestinyItemEquipCantEquipItemNotInQuests
2033  - DestinyItemEquipCantEquipItemNotInMessages
2034  - DestinyItemEquipCantEquipItemNotInInventory
2035  - DestinyItemEquipCantEquipItemNotInPostmaster
2036  - DestinyItemEquipCantEquipItemNotInRecovery
2037  - DestinyItemEquipCantEquipItemNotInMaterial
2038  - DestinyItemEquipCantEquipItemNotInConsumables
2039  - DestinyItemEquipCantEquipItemNotInShaders
2040  - DestinyItemEquipCantEquipItemNotInMods
2041  - DestinyItemEquipCantEquipItemNotInEmblems
2042  - DestinyItemEquipCantEquipItemNotInShips
2043  - DestinyItemEquipCantEquipItemNotInVehicles
2044  - DestinyItemEquipCantEquipItemNotInEmotes
2045  - DestinyItemEquipCantEquipItemNotInAuras
2046  - DestinyItemEquipCantEquipItemNotInFinishers
2047  - DestinyItemEquipCantEquipItemNotInBounties
2048  - DestinyItemEquipCantEquipItemNotInQuests
2049  - DestinyItemEquipCantEquipItemNotInMessages
2050  - DestinyItemEquipCantEquipItemNotInInventory
2051  - DestinyItemEquipCantEquipItemNotInPostmaster
2052  - DestinyItemEquipCantEquipItemNotInRecovery
2053  - DestinyItemEquipCantEquipItemNotInMaterial
2054  - DestinyItemEquipCantEquipItemNotInConsumables
2055  - DestinyItemEquipCantEquipItemNotInShaders
2056  - DestinyItemEquipCantEquipItemNotInMods
2057  - DestinyItemEquipCantEquipItemNotInEmblems
2058  - DestinyItemEquipCantEquipItemNotInShips
2059  - DestinyItemEquipCantEquipItemNotInVehicles
2060  - DestinyItemEquipCantEquipItemNotInEmotes
2061  - DestinyItemEquipCantEquipItemNotInAuras
2062  - DestinyItemEquipCantEquipItemNotInFinishers
2063  - DestinyItemEquipCantEquipItemNotInBounties
2064  - DestinyItemEquipCantEquipItemNotInQuests
2065  - DestinyItemEquipCantEquipItemNotInMessages
2066  - DestinyItemEquipCantEquipItemNotInInventory
2067  - DestinyItemEquipCantEquipItemNotInPostmaster
2068  - DestinyItemEquipCantEquipItemNotInRecovery
2069  - DestinyItemEquipCantEquipItemNotInMaterial
2070  - DestinyItemEquipCantEquipItemNotInConsumables
2071  - DestinyItemEquipCantEquipItemNotInShaders
2072  - DestinyItemEquipCantEquipItemNotInMods
2073  - DestinyItemEquipCantEquipItemNotInEmblems
2074  - DestinyItemEquipCantEquipItemNotInShips
2075  - DestinyItemEquipCantEquipItemNotInVehicles
2076  - DestinyItemEquipCantEquipItemNotInEmotes
2077  - DestinyItemEquipCantEquipItemNotInAuras
2078  - DestinyItemEquipCantEquipItemNotInFinishers
2079  - DestinyItemEquipCantEquipItemNotInBounties
2080  - DestinyItemEquipCantEquipItemNotInQuests
2081  - DestinyItemEquipCantEquipItemNotInMessages
2082  - DestinyItemEquipCantEquipItemNotInInventory
2083  - DestinyItemEquipCantEquipItemNotInPostmaster
2084  - DestinyItemEquipCantEquipItemNotInRecovery
2085  - DestinyItemEquipCantEquipItemNotInMaterial
2086  - DestinyItemEquipCantEquipItemNotInConsumables
2087  - DestinyItemEquipCantEquipItemNotInShaders
2088  - DestinyItemEquipCantEquipItemNotInMods
2089  - DestinyItemEquipCantEquipItemNotInEmblems
2090  - DestinyItemEquipCantEquipItemNotInShips
2091  - DestinyItemEquipCantEquipItemNotInVehicles
2092  - DestinyItemEquipCantEquipItemNotInEmotes
2093  - DestinyItemEquipCantEquipItemNotInAuras
2094  - DestinyItemEquipCantEquipItemNotInFinishers
2095  - DestinyItemEquipCantEquipItemNotInBounties
2096  - DestinyItemEquipCantEquipItemNotInQuests
2097  - DestinyItemEquipCantEquipItemNotInMessages
2098  - DestinyItemEquipCantEquipItemNotInInventory
2099  - DestinyItemEquipCantEquipItemNotInPostmaster
2100  - DestinyItemEquipCantEquipItemNotInRecovery
```

### Error Handling Pattern
```javascript
async function handleApiResponse(response) {
    const data = await response.json();
    
    if (data.ErrorCode !== 1) {
        switch (data.ErrorCode) {
            case 36:
            case 37:
                // Rate limited - wait and retry
                await new Promise(resolve => setTimeout(resolve, data.ThrottleSeconds * 1000));
                break;
            case 1601:
                throw new Error('Destiny account not found');
            case 1627:
                throw new Error('Item not found');
            case 1629:
                throw new Error('Invalid item transfer request');
            default:
                throw new Error(data.Message || 'Unknown API error');
        }
    }
    
    return data.Response;
}
```

---

## Common Parameters

### Membership Types
```
1  - Xbox
2  - PlayStation
3  - Steam
4  - Blizzard (deprecated)
5  - Stadia (deprecated)
6  - Epic Games Store
10 - Demon
254 - BungieNext
-1 - All
```

### Destiny Component Types
```
100 - Profiles
101 - VendorReceipts
102 - ProfileInventories
103 - ProfileCurrencies
104 - ProfileProgression
105 - PlatformSilver
106 - Characters
107 - CharacterInventories
108 - CharacterProgressions
109 - CharacterRenderData
110 - CharacterActivities
111 - CharacterEquipment
112 - ItemInstances
113 - ItemObjectives
114 - ItemPerks
115 - ItemRenderData
116 - ItemStats
117 - ItemSockets
118 - ItemTalentGrids
119 - ItemCommonData
120 - ItemPlugStates
121 - ItemPlugObjectives
122 - ItemReusablePlugs
123 - Vendors
124 - VendorCategories
125 - VendorSales
126 - Kiosks
127 - CurrencyLookups
128 - PresentationNodes
129 - Collectibles
130 - Records
131 - Transitory
132 - Metrics
133 - StringVariables
134 - Craftables
135 - CraftingRecipes
136 - SocialCommendations
137 - LoadoutConstants
138 - Loadouts
139 - AllVendorReceipts
```

### Item Bucket Types
```
1498876634  - Kinetic Weapons
2465295065  - Energy Weapons
953998645   - Power Weapons
3448274439  - Helmet
3551918588  - Gauntlets
14239492    - Chest Armor
20886954    - Leg Armor
1585787867  - Class Armor
4274335291  - Emblem
284967655   - Shader
2025709351  - Vehicle
284967655   - Ships
375726501   - Emotes
1107761855  - Auras
4023194814  - Ghost
138197802   - Consumables
1469714392  - Modifications
3621873013  - Clan Banners
1506418338  - Finishers
```

---

## Response Format

### Standard Response Structure
```json
{
  "Response": {
    // Actual response data varies by endpoint
  },
  "ErrorCode": 1,
  "ThrottleSeconds": 0,
  "ErrorStatus": "Success",
  "Message": "Ok",
  "MessageData": {},
  "DetailedErrorTrace": ""
}
```

### Success Response (ErrorCode: 1)
```json
{
  "Response": { /* Data here */ },
  "ErrorCode": 1,
  "ThrottleSeconds": 0,
  "ErrorStatus": "Success",
  "Message": "Ok"
}
```

### Error Response (ErrorCode: != 1)
```json
{
  "Response": null,
  "ErrorCode": 1627,
  "ThrottleSeconds": 0,
  "ErrorStatus": "DestinyItemNotFound",
  "Message": "The item was not found.",
  "MessageData": {
    "itemId": "1234567890"
  }
}
```

### Rate Limited Response
```json
{
  "Response": null,
  "ErrorCode": 36,
  "ThrottleSeconds": 60,
  "ErrorStatus": "ThrottleLimitExceededMinutes",
  "Message": "You are making too many requests"
}
```

---

## Quick Start Checklist

### Setting Up Your First API Request
1. ✅ Register application at https://www.bungie.net/en/Application
2. ✅ Get your API key
3. ✅ Make your first request to `/Settings/` with API key
4. ✅ Test OAuth flow if needed
5. ✅ Implement error handling and rate limiting

### Basic Request Template
```javascript
const apiKey = 'YOUR_API_KEY';
const baseUrl = 'https://www.bungie.net/Platform';

async function makeRequest(endpoint, options = {}) {
    const response = await fetch(`${baseUrl}${endpoint}`, {
        ...options,
        headers: {
            'X-API-Key': apiKey,
            ...options.headers
        }
    });
    
    return handleApiResponse(response);
}

// Usage
const manifest = await makeRequest('/Destiny2/Manifest/');
```

For more detailed implementation examples, see the [Common Workflows](common-workflows.md) and [Authentication Guide](authentication-guide.md).