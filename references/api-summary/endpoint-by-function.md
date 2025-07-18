# Endpoints Organized by Function

This document organizes all Bungie API endpoints by their functional purpose, making it easier to find the right endpoint for your use case.

## User Management & Authentication

### User Profile Operations
- `GET /User/GetBungieNetUserById/{id}/` - Get user profile by Bungie.net ID
- `GET /User/GetSanitizedPlatformDisplayNames/{membershipId}/` - Get sanitized display names
- `GET /User/GetMembershipsById/{membershipId}/{membershipType}/` - Get memberships by ID
- `GET /User/GetMembershipsForCurrentUser/` - Get current user's memberships (Auth: OAuth)
- `GET /User/GetCredentialTypesForTargetAccount/{membershipId}/` - Get credential types
- `GET /User/GetMembershipFromHardLinkedCredential/{crType}/{credential}/` - Get membership from credential

### User Search
- `GET /User/Search/Prefix/{displayNamePrefix}/{page}/` - Search users by display name prefix
- `POST /User/Search/GlobalName/{page}/` - Search users by global name

### User Preferences
- `GET /User/GetAvailableThemes/` - Get available user themes

## Destiny 2 Game Data

### Player Profiles & Characters
- `GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/` - Get player profile
- `GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/` - Get character details
- `GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/LinkedProfiles/` - Get linked profiles
- `POST /Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/` - Search player by Bungie Name

### Game Manifest & Definitions
- `GET /Destiny2/Manifest/` - Get game manifest information
- `GET /Destiny2/Manifest/{entityType}/{hashIdentifier}/` - Get specific manifest entity

### Inventory & Items
- `GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Item/{itemInstanceId}/` - Get item details
- `GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Collectibles/{collectiblePresentationNodeHash}/` - Get collectibles

### Vendors
- `GET /Destiny2/Vendors/` - Get public vendors
- `GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/` - Get character vendors (Auth: OAuth)
- `GET /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/` - Get specific vendor (Auth: OAuth)

### Activities & Milestones
- `GET /Destiny2/Milestones/` - Get public milestones
- `GET /Destiny2/Milestones/{milestoneHash}/Content/` - Get milestone content

### Search & Discovery
- `GET /Destiny2/Armory/Search/{type}/{searchTerm}/` - Search armory items

## Inventory & Item Management

### Item Actions (All require OAuth with MoveEquipDestinyItems scope)
- `POST /Destiny2/Actions/Items/TransferItem/` - Transfer items between characters/vault
- `POST /Destiny2/Actions/Items/EquipItem/` - Equip single item
- `POST /Destiny2/Actions/Items/EquipItems/` - Equip multiple items
- `POST /Destiny2/Actions/Items/PullFromPostmaster/` - Pull items from postmaster
- `POST /Destiny2/Actions/Items/SetLockState/` - Lock/unlock items
- `POST /Destiny2/Actions/Items/SetTrackedState/` - Set item tracking state

### Loadout Management (All require OAuth with MoveEquipDestinyItems scope)
- `POST /Destiny2/Actions/Loadouts/EquipLoadout/` - Equip a loadout
- `POST /Destiny2/Actions/Loadouts/SnapshotLoadout/` - Create loadout snapshot
- `POST /Destiny2/Actions/Loadouts/UpdateLoadoutIdentifiers/` - Update loadout identifiers
- `POST /Destiny2/Actions/Loadouts/ClearLoadout/` - Clear loadout

### Item Modification (All require OAuth with MoveEquipDestinyItems scope)
- `POST /Destiny2/Actions/Items/InsertSocketPlug/` - Insert socket plug
- `POST /Destiny2/Actions/Items/InsertSocketPlugFree/` - Insert free socket plug

## Statistics & Performance

### Player Statistics
- `GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/` - Get account stats
- `GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/` - Get character stats
- `GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/` - Get activity stats
- `GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/UniqueWeapons/` - Get unique weapons stats
- `GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/AggregateActivityStats/` - Get aggregate activity stats

### Leaderboards
- `GET /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/` - Get account leaderboards
- `GET /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/` - Get character leaderboards
- `GET /Destiny2/Stats/Leaderboards/Clans/{groupId}/` - Get clan leaderboards

### Activity Reports
- `GET /Destiny2/Stats/PostGameCarnageReport/{activityId}/` - Get post-game carnage report
- `POST /Destiny2/Stats/PostGameCarnageReport/{activityId}/Report/` - Report activity
- `GET /Destiny2/Stats/Definition/` - Get stats definitions

### Clan Statistics
- `GET /Destiny2/Stats/AggregateClanStats/{groupId}/` - Get aggregate clan stats
- `GET /Destiny2/Clan/{groupId}/WeeklyRewardState/` - Get clan weekly rewards
- `GET /Destiny2/Clan/ClanBannerDictionary/` - Get clan banner dictionary

## Social Features

### Friends Management (All require OAuth with ReadUserData scope)
- `GET /Social/Friends/` - Get friend list
- `GET /Social/Friends/Requests/` - Get friend requests
- `POST /Social/Friends/Add/{membershipId}/` - Send friend request
- `POST /Social/Friends/Requests/Accept/{membershipId}/` - Accept friend request
- `POST /Social/Friends/Requests/Decline/{membershipId}/` - Decline friend request
- `POST /Social/Friends/Remove/{membershipId}/` - Remove friend
- `POST /Social/Friends/Requests/Remove/{membershipId}/` - Remove friend request

### Platform Friends
- `GET /Social/PlatformFriends/{friendPlatform}/{page}/` - Get platform friends

## Group & Clan Management

### Group Information
- `GET /GroupV2/{groupId}/` - Get group details
- `GET /GroupV2/Name/{groupName}/{groupType}/` - Get group by name
- `POST /GroupV2/NameV2/` - Get group by name (v2)
- `POST /GroupV2/Search/` - Search groups
- `POST /GroupV2/Recommended/{groupType}/{createDateRange}/` - Get recommended groups

### Group Membership
- `GET /GroupV2/{groupId}/Members/` - Get group members
- `GET /GroupV2/{groupId}/AdminsAndFounder/` - Get group admins and founder
- `GET /GroupV2/{groupId}/Members/Pending/` - Get pending members
- `GET /GroupV2/{groupId}/Members/InvitedIndividuals/` - Get invited individuals
- `GET /GroupV2/{groupId}/Banned/` - Get banned members

### User Groups
- `GET /GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/` - Get user groups
- `GET /GroupV2/User/Potential/{membershipType}/{membershipId}/{filter}/{groupType}/` - Get potential groups
- `GET /GroupV2/Recover/{membershipType}/{membershipId}/{groupType}/` - Recover group membership

### Group Administration (Require OAuth with appropriate group permissions)
- `POST /GroupV2/{groupId}/Edit/` - Edit group
- `POST /GroupV2/{groupId}/EditClanBanner/` - Edit clan banner
- `POST /GroupV2/{groupId}/EditFounderOptions/` - Edit founder options
- `POST /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/SetMembershipType/{memberType}/` - Set member type
- `POST /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Kick/` - Kick member
- `POST /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Ban/` - Ban member
- `POST /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Unban/` - Unban member
- `POST /GroupV2/{groupId}/Admin/AbdicateFoundership/{membershipType}/{founderIdNew}/` - Abdicate founder

### Member Management (Require OAuth with appropriate group permissions)
- `POST /GroupV2/{groupId}/Members/ApproveAll/` - Approve all pending members
- `POST /GroupV2/{groupId}/Members/DenyAll/` - Deny all pending members
- `POST /GroupV2/{groupId}/Members/ApproveList/` - Approve member list
- `POST /GroupV2/{groupId}/Members/DenyList/` - Deny member list
- `POST /GroupV2/{groupId}/Members/Approve/{membershipType}/{membershipId}/` - Approve member
- `POST /GroupV2/{groupId}/Members/IndividualInvite/{membershipType}/{membershipId}/` - Invite individual
- `POST /GroupV2/{groupId}/Members/IndividualInviteCancel/{membershipType}/{membershipId}/` - Cancel invite

### Group Features
- `GET /GroupV2/{groupId}/OptionalConversations/` - Get optional conversations
- `POST /GroupV2/{groupId}/OptionalConversations/Add/` - Add optional conversation
- `POST /GroupV2/{groupId}/OptionalConversations/Edit/{conversationId}/` - Edit optional conversation
- `GET /GroupV2/{groupId}/EditHistory/` - Get edit history

### Group Resources
- `GET /GroupV2/GetAvailableAvatars/` - Get available avatars
- `GET /GroupV2/GetAvailableThemes/` - Get available themes
- `GET /GroupV2/GetUserClanInviteSetting/{mType}/` - Get user clan invite setting

## Fireteam & Activity Finding

### Legacy Fireteam System
- `GET /Fireteam/Clan/{groupId}/ActiveCount/` - Get active fireteam count
- `GET /Fireteam/Clan/{groupId}/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{publicOnly}/{page}/` - Get available clan fireteams
- `GET /Fireteam/Search/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{page}/` - Search available fireteams
- `GET /Fireteam/Clan/{groupId}/My/{platform}/{includeClosed}/{page}/` - Get my clan fireteams
- `GET /Fireteam/Clan/{groupId}/Summary/{fireteamId}/` - Get fireteam summary

### Modern Fireteam Finder (All require OAuth with appropriate scopes)

#### Fireteam Finder Information
- `GET /FireteamFinder/Listing/{listingId}/` - Get listing details
- `GET /FireteamFinder/Application/{applicationId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Get application details
- `GET /FireteamFinder/Listing/{listingId}/Applications/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Get listing applications
- `GET /FireteamFinder/Lobby/{lobbyId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Get lobby details
- `GET /FireteamFinder/Offer/{offerId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Get offer details
- `GET /FireteamFinder/CharacterActivityAccess/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Get character activity access

#### Player Fireteam Finder Data
- `GET /FireteamFinder/PlayerLobbies/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Get player lobbies
- `GET /FireteamFinder/PlayerApplications/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Get player applications
- `GET /FireteamFinder/PlayerOffers/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Get player offers
- `GET /FireteamFinder/Lobby/{lobbyId}/Offers/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Get lobby offers

#### Fireteam Finder Actions
- `POST /FireteamFinder/Listing/{listingId}/Apply/{applicationType}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Apply to listing
- `POST /FireteamFinder/Listing/BulkStatus/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Get bulk status
- `POST /FireteamFinder/Application/Leave/{applicationId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Leave application
- `POST /FireteamFinder/Application/Respond/{applicationId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Respond to application
- `POST /FireteamFinder/Authentication/Respond/{applicationId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Respond to authentication
- `POST /FireteamFinder/Offer/Respond/{offerId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Respond to offer

#### Lobby Management
- `POST /FireteamFinder/Lobby/Host/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Host lobby
- `POST /FireteamFinder/Lobby/Join/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Join lobby
- `POST /FireteamFinder/Lobby/Leave/{lobbyId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Leave lobby
- `POST /FireteamFinder/Lobby/Activate/{lobbyId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Activate lobby
- `POST /FireteamFinder/Lobby/ActivateForNewListingId/{lobbyId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Activate for new listing
- `POST /FireteamFinder/Lobby/UpdateSettings/{lobbyId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Update lobby settings
- `POST /FireteamFinder/Lobby/KickPlayer/{lobbyId}/{targetMembershipId}/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Kick player

#### Fireteam Finder Search
- `POST /FireteamFinder/Search/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Search fireteams
- `POST /FireteamFinder/Search/Clan/{destinyMembershipType}/{destinyMembershipId}/{destinyCharacterId}/` - Search clan fireteams

## Forum & Community

### Forum Operations
- `GET /Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/` - Get topics paged
- `GET /Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/` - Get core topics paged
- `GET /Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/` - Get posts threaded paged
- `GET /Forum/GetPostsThreadedPagedFromChild/{childPostId}/{page}/{pageSize}/{replySize}/{rootThreadMode}/{sortMode}/` - Get posts from child
- `GET /Forum/GetPostAndParent/{childPostId}/` - Get post and parent
- `GET /Forum/GetPostAndParentAwaitingApproval/{childPostId}/` - Get post awaiting approval
- `GET /Forum/GetTopicForContent/{contentId}/` - Get topic for content
- `GET /Forum/Poll/{topicId}/` - Get poll
- `POST /Forum/Recruit/Summaries/` - Get recruitment summaries

### Forum Utilities
- `GET /Forum/GetForumTagSuggestions/` - Get forum tag suggestions

## Content & Media

### Content Management
- `GET /Content/GetContentType/{type}/` - Get content type
- `GET /Content/GetContentById/{id}/{locale}/` - Get content by ID
- `GET /Content/GetContentByTagAndType/{tag}/{type}/{locale}/` - Get content by tag and type
- `GET /Content/Search/{locale}/` - Search content
- `GET /Content/SearchContentByTagAndType/{tag}/{type}/{locale}/` - Search content by tag and type
- `GET /Content/SearchHelpArticles/{searchtext}/{size}/` - Search help articles
- `GET /Content/Rss/NewsArticles/{pageToken}/` - Get RSS news articles

### Community Content
- `GET /CommunityContent/Get/{sort}/{mediaFilter}/{page}/` - Get community content

### Trending Content
- `GET /Trending/Categories/` - Get trending categories
- `GET /Trending/Categories/{categoryId}/{pageNumber}/` - Get trending category content
- `GET /Trending/Details/{trendingEntryType}/{identifier}/` - Get trending details

## Rewards & Tokens

### Bungie Rewards
- `GET /Tokens/Rewards/GetRewardsForUser/{membershipId}/` - Get rewards for user
- `GET /Tokens/Rewards/GetRewardsForPlatformUser/{membershipId}/{membershipType}/` - Get rewards for platform user
- `GET /Tokens/Rewards/BungieRewards/` - Get Bungie rewards

### Partner Offers (Require OAuth with appropriate scopes)
- `GET /Tokens/Partner/History/{partnerApplicationId}/{targetBnetMembershipId}/` - Get partner history
- `GET /Tokens/Partner/History/{targetBnetMembershipId}/Application/{partnerApplicationId}/` - Get partner application history
- `POST /Tokens/Partner/ClaimOffer/` - Claim partner offer
- `POST /Tokens/Partner/ApplyMissingOffers/{partnerApplicationId}/{targetBnetMembershipId}/` - Apply missing offers
- `POST /Tokens/Partner/ForceDropsRepair/` - Force drops repair

## Application Management

### Application Information
- `GET /App/ApiUsage/{applicationId}/` - Get API usage statistics
- `GET /App/FirstParty/` - Get first party applications

## Advanced Features

### AWA (Advanced Warfare Actions) (Require OAuth with AdvancedWriteActions scope)
- `POST /Destiny2/Awa/Initialize/` - Initialize AWA
- `POST /Destiny2/Awa/AwaProvideAuthorizationResult/` - Provide authorization result
- `GET /Destiny2/Awa/GetActionToken/{correlationId}/` - Get action token

## System Information

### General System
- `GET /GetAvailableLocales/` - Get available locales
- `GET /Settings/` - Get system settings
- `GET /UserSystemOverrides/` - Get user system overrides
- `GET /GlobalAlerts/` - Get global alerts

## Authentication Requirements Summary

- **No Authentication**: Most read-only endpoints for public data
- **OAuth Required**: User-specific data, inventory actions, social features, group management
- **Special Scopes**: Advanced actions require specific OAuth scopes (see authentication guide)

For detailed authentication requirements and OAuth scopes, see the [Authentication Guide](authentication-guide.md).