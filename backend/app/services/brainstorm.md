# Destiny API Tools: Project Brainstorm

This document outlines potential project ideas for tools utilizing the Bungie.net API for Destiny 2.

---

## Idea 1: Interactive Global System Map

### Concept

An interactive, live map of the Destiny 2 solar system that visualizes player activity. It would show where players are currently located and the most common "paths" or transitions they take between different activities and destinations, providing a "pulse" of the game world.

### Key Features

1.  **System-Level "Director" View:**
    *   The main view will be a top-down representation of the solar system, similar to the in-game Director.
    *   It will display major destinations: Planets (Earth, Nessus, etc.), The Last City, The Reef, Legendary Raid locations, and other key points of interest.
    *   The visual representation of a destination (e.g., size, brightness, or a numerical indicator) will reflect its current player population.

2.  **Live Player Population:**
    *   Aggregate and display the number of players currently engaged in activities at each major destination.
    *   This data would be based on a snapshot of in-progress activities over the last hour to provide a "live" feel.

3.  **Player "Flight Paths":**
    *   Visualize the flow of players between destinations.
    *   Analyze player activity history over the last 12 hours to determine sequences of activities (e.g., a player completing a strike on Nessus and then traveling to the Tower).
    *   Aggregate this "FROM -> TO" data to show the most common travel routes, perhaps represented by animated lines or paths of varying thickness/brightness depending on traffic volume.

### Data Requirements & API Endpoints

*   **Player Activity History**: To build the "FROM -> TO" paths, we'll need to track sequences of activities for a sample of players.
    *   `Destiny2.GetActivityHistory`: This will be the core endpoint to get a character's recent activities. This would need to be called for a large, representative sample of public profiles.
*   **Current Player Location (Approximation)**: Since there's no direct "where is everyone right now" endpoint, we can approximate this by looking at recently started activities across a wide sample of players using `GetActivityHistory`.
*   **Destination/Activity Information**: To build the map and understand what the activity hashes represent.
    *   `Destiny2.GetDestinyManifest` to get all static definitions.
    *   `DestinyActivityDefinition`, `DestinyDestinationDefinition`, and `DestinyPlaceDefinition` from the manifest will be crucial for building the map and labeling locations correctly.

### Technical Considerations & Challenges

*   **Data Aggregation**: The primary challenge is collecting enough data to be representative of the global player base without a dedicated firehose. This would require tracking a large number of public profiles and their activity history.
*   **API Rate Limits**: Making frequent calls to `GetActivityHistory` for many players will quickly run into API rate limits. A careful, distributed, and throttled approach to data collection is necessary.
*   **Data Storage**: A database will be needed to store the aggregated path data (e.g., a table with `from_location_hash`, `to_location_hash`, `count`, `timestamp`). This data would be periodically pruned (older than 12 hours).
*   **Frontend Visualization**: A library like D3.js, Three.js, or another suitable graphics library would be needed to render the interactive map and the animated paths between nodes.
*   **Defining "Locations"**: The API provides different hashes for `Place`, `Destination`, and `Activity`. A clear mapping needs to be established to group activities under their parent destinations/planets for a clean UI. For example, all Crucible maps could be grouped under a single "Crucible" node, and strikes under their respective planet nodes.

---

## Idea 2: Destiny "Stock Market"

### Concept

A "stock market" style game where players invest in the performance of in-game items, weapons, and builds. Players would earn a virtual currency by playing the game, which they can then use to "buy shares" in various markets. The value of these shares would fluctuate based on the collective usage and performance of the associated items/builds across the entire player base (or specific segments like PvP or Gambit players). This creates a meta-game that encourages players to analyze game trends, predict the meta, and even influence it with their own play style.

### Key Features

1.  **Point Earning:**
    *   Players earn points (the "currency" for the stock market) by playing activities.
    *   This could be tied to equipping specific, rotating emblems to encourage participation.

2.  **Dynamic Markets:**
    *   Markets are based on the aggregate performance of specific in-game elements.
    *   Examples:
        *   **Weapon Market:** A "stock" for a specific weapon (e.g., The Recluse) could rise or fall based on its total kills or usage rate in Crucible over the last 24 hours.
        *   **Stat Market:** A market for "Orbs Generated," where different subclasses or exotic armor pieces are the "stocks" and their value is determined by their orb generation efficiency.
        *   Markets could exist for any trackable stat: kills, assists, deaths, precision kill ratio, etc.

3.  **Investing and Portfolios:**
    *   Players use their earned points to invest in different markets.
    *   They can also invest in "futures," predicting how item performance will change with upcoming patches, new seasons, or DLC releases.
    *   The site would track each player's portfolio and its value over time.

4.  **Social and Community Features:**
    *   Leaderboards to display top "earners" and most successful investors.
    *   A feature allowing players to pool their points to fund the creation of a new, custom market type, which would then be implemented by the site admins.

### Data Requirements & API Endpoints

*   **Aggregate Player/Item Performance**: This is the core data for driving the market values. This would require analyzing a massive volume of game data.
    *   `Destiny2.GetActivityHistory`: To get a stream of recently played activities from a large sample of public profiles.
    *   `Destiny2.GetPostGameCarnageReport` (PGCR): This is the primary source of data. By processing many PGCRs, we can aggregate:
        *   Weapon stats (`extended.weapons`): Kills, precision kills, etc., for specific weapon hashes (`referenceId`).
        *   Player stats (`values`): Orbs generated, kills, deaths, assists for each player in the activity.
        *   Subclass (`player.classHash`): Can be used to track performance by class (Titan, Warlock, Hunter).
*   **Player Point Earning**: To track if a player should be earning points.
    *   `Destiny2.GetProfile` with the `CharacterEquipment` (205) component: Could be used to check a player's currently equipped emblem, but this is difficult to correlate with past activities.
*   **Static Information**: To understand what the hashes represent.
    *   `Destiny2.GetDestinyManifest`: To get all static definitions.
    *   `DestinyInventoryItemDefinition`: For weapon, armor, and emblem details.
    *   `DestinyHistoricalStatsDefinition`: To understand the stats returned in the PGCR.

### Technical Considerations & Challenges

*   **Data Aggregation at Scale**: Like the Global System Map idea, this requires a massive data collection effort. The application would need to continuously fetch activity history for a large pool of players and then fetch the PGCR for each of those activities.
*   **API Rate Limits**: This is a major concern. The number of API calls required to get a representative dataset would be enormous and would require a sophisticated, distributed, and heavily throttled collection system.
*   **Data Granularity Limitation**: This is the most significant challenge to the idea as described. The PGCR **does not** provide details on the specific subclass tree, aspects, fragments, or armor mods used by a player in an activity. Therefore, creating markets based on the performance of specific perks or build components is **not currently feasible** with the public API. Markets would be limited to what the PGCR provides: weapon performance, character class performance, and overall player stats.
*   **Point-Earning Mechanism**: Tying point generation to a specific equipped emblem is difficult. The API does not provide a way to see what emblem was equipped *during* a past activity. An alternative system would be needed, such as granting points for any activity completion by a registered user, or tying it to trackable objectives.
*   **Backend Complexity**: The logic to calculate market fluctuations, manage user portfolios, process buy/sell orders, and update leaderboards would be highly complex. It would require a robust database (likely a combination of SQL for user data and a time-series database for market data) and significant processing power.
*   **Defining "Markets"**: The logic for how a market's value is calculated (e.g., "Orbs Generated Per Hour") would need to be carefully designed to be both engaging and resistant to manipulation.