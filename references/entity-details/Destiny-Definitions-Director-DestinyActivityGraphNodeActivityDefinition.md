# Destiny.Definitions.Director.DestinyActivityGraphNodeActivityDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Director.DestinyActivityGraphNodeActivityDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The actual activity to be redirected to when you click on the node. Note that a node can have many Activities attached to it: but only one will be active at any given time. The list of Node Activities will be traversed, and the first one found to be active will be displayed. This way, a node can layer multiple variants of an activity on top of each other. For instance, one node can control the weekly Crucible Playlist. There are multiple possible playlists, but only one is active for the week.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| nodeActivityId | integer (uint32) | An identifier for this node activity. It is only guaranteed to be unique within the Activity Graph. | No |
| activityHash | integer (uint32) | The activity that will be activated if the user clicks on this node. Controls all activity-related information displayed on the node if it is active (the text shown in the tooltip etc) | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Director.DestinyActivityGraphNodeActivityDefinition object
const example = {
  nodeActivityId: 123,
  activityHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Director.DestinyActivityGraphNodeActivityDefinition object
example = {
    "nodeActivityId": 123,
    "activityHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Director.DestinyActivityGraphNodeActivityDefinition":   {
      "description": "The actual activity to be redirected to when you click on the node. Note that a node can have many Activities attached to it: but only one will be active at any given time. The list of Node Activities will be traversed, and the first one found to be active will be displayed. This way, a node can layer multiple variants of an activity on top of each other. For instance, one node can control the weekly Crucible Playlist. There are multiple possible playlists, but only one is active for the week.",
      "type": "object",
      "properties": {
          "nodeActivityId": {
              "format": "uint32",
              "description": "An identifier for this node activity. It is only guaranteed to be unique within the Activity Graph.",
              "type": "integer"
          },
          "activityHash": {
              "format": "uint32",
              "description": "The activity that will be activated if the user clicks on this node. Controls all activity-related information displayed on the node if it is active (the text shown in the tooltip etc)",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          }
      }
  }
}
```
