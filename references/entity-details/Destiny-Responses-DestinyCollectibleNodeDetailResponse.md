# Destiny.Responses.DestinyCollectibleNodeDetailResponse

## Entity Information
- **Entity Name**: Destiny.Responses.DestinyCollectibleNodeDetailResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Returns the detailed information about a Collectible Presentation Node and any Collectibles that are direct descendants.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| collectibles | object | COMPONENT TYPE: Collectibles | No |
| collectibleItemComponents | object | Item components, keyed by the item hash of the items pointed at collectibles found under the requested Presentation Node.
NOTE: I had a lot of hemming and hawing about whether these should be keyed by collectible hash or item hash... but ultimately having it be keyed by item hash meant that UI that already uses DestinyItemComponentSet data wouldn't have to have a special override to do the collectible -> item lookup once you delve into an item's details, and it also meant that you didn't have to remember that the Hash being used as the key for plugSets was different from the Hash being used for the other Dictionaries. As a result, using the Item Hash felt like the least crappy solution.
We may all come to regret this decision. We will see.
COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.] | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.DestinyCollectibleNodeDetailResponse object
const example = {
  collectibles: null,
  collectibleItemComponents: null,
};
```

### Python
```python
# Example Destiny.Responses.DestinyCollectibleNodeDetailResponse object
example = {
    "collectibles": None,
    "collectibleItemComponents": None,
}
```

## Related Entities
- **DestinyItemComponentSetOfuint32**: Referenced in this entity
- **SingleComponentResponseOfDestinyCollectiblesComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.DestinyCollectibleNodeDetailResponse":   {
      "description": "Returns the detailed information about a Collectible Presentation Node and any Collectibles that are direct descendants.",
      "type": "object",
      "properties": {
          "collectibles": {
              "description": "COMPONENT TYPE: Collectibles",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyCollectiblesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Collectibles"
          },
          "collectibleItemComponents": {
              "description": "Item components, keyed by the item hash of the items pointed at collectibles found under the requested Presentation Node.\r\nNOTE: I had a lot of hemming and hawing about whether these should be keyed by collectible hash or item hash... but ultimately having it be keyed by item hash meant that UI that already uses DestinyItemComponentSet data wouldn't have to have a special override to do the collectible -> item lookup once you delve into an item's details, and it also meant that you didn't have to remember that the Hash being used as the key for plugSets was different from the Hash being used for the other Dictionaries. As a result, using the Item Hash felt like the least crappy solution.\r\nWe may all come to regret this decision. We will see.\r\nCOMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DestinyItemComponentSetOfuint32"
                  }
              ]
          }
      }
  }
}
```
