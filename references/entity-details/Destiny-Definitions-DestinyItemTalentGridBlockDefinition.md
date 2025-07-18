# Destiny.Definitions.DestinyItemTalentGridBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemTalentGridBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This defines information that can only come from a talent grid on an item. Items mostly have negligible talent grid data these days, but instanced items still retain grids as a source for some of this common information.
Builds/Subclasses are the only items left that still have talent grids with meaningful Nodes.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| talentGridHash | integer (uint32) | The hash identifier of the DestinyTalentGridDefinition attached to this item. | No |
| itemDetailString | string | This is meant to be a subtitle for looking at the talent grid. In practice, somewhat frustratingly, this always merely says the localized word for "Details". Great. Maybe it'll have more if talent grids ever get used for more than builds and subclasses again. | No |
| buildName | string | A shortcut string identifier for the "build" in question, if this talent grid has an associated build. Doesn't map to anything we can expose at the moment. | No |
| hudDamageType | integer (int32) | If the talent grid implies a damage type, this is the enum value for that damage type. | No |
| hudIcon | string | If the talent grid has a special icon that's shown in the game UI (like builds, funny that), this is the identifier for that icon. Sadly, we don't actually get that icon right now. I'll be looking to replace this with a path to the actual icon itself. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemTalentGridBlockDefinition object
const example = {
  talentGridHash: 123,
  itemDetailString: "example value",
  buildName: "example value",
  hudDamageType: 123,
  hudIcon: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemTalentGridBlockDefinition object
example = {
    "talentGridHash": 123,
    "itemDetailString": "example value",
    "buildName": "example value",
    "hudDamageType": 123,
    "hudIcon": "example value",
}
```

## Related Entities
- **Destiny.DamageType**: Referenced in this entity
- **Destiny.Definitions.DestinyTalentGridDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemTalentGridBlockDefinition":   {
      "description": "This defines information that can only come from a talent grid on an item. Items mostly have negligible talent grid data these days, but instanced items still retain grids as a source for some of this common information.\r\nBuilds/Subclasses are the only items left that still have talent grids with meaningful Nodes.",
      "type": "object",
      "properties": {
          "talentGridHash": {
              "format": "uint32",
              "description": "The hash identifier of the DestinyTalentGridDefinition attached to this item.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyTalentGridDefinition"
              }
          },
          "itemDetailString": {
              "description": "This is meant to be a subtitle for looking at the talent grid. In practice, somewhat frustratingly, this always merely says the localized word for \"Details\". Great. Maybe it'll have more if talent grids ever get used for more than builds and subclasses again.",
              "type": "string"
          },
          "buildName": {
              "description": "A shortcut string identifier for the \"build\" in question, if this talent grid has an associated build. Doesn't map to anything we can expose at the moment.",
              "type": "string"
          },
          "hudDamageType": {
              "format": "int32",
              "description": "If the talent grid implies a damage type, this is the enum value for that damage type.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DamageType"
              }
          },
          "hudIcon": {
              "description": "If the talent grid has a special icon that's shown in the game UI (like builds, funny that), this is the identifier for that icon. Sadly, we don't actually get that icon right now. I'll be looking to replace this with a path to the actual icon itself.",
              "type": "string"
          }
      }
  }
}
```
