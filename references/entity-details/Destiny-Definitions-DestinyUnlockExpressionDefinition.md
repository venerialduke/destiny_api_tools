# Destiny.Definitions.DestinyUnlockExpressionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyUnlockExpressionDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Where the sausage gets made. Unlock Expressions are the foundation of the game's gating mechanics and investment-related restrictions. They can test Unlock Flags and Unlock Values for certain states, using a sufficient amount of logical operators such that unlock expressions are effectively Turing complete.
Use UnlockExpressionParser to evaluate expressions using an IUnlockContext parsed from Babel.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| scope | integer (int32) | A shortcut for determining the most restrictive gating that this expression performs. See the DestinyGatingScope enum's documentation for more details. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyUnlockExpressionDefinition object
const example = {
  scope: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyUnlockExpressionDefinition object
example = {
    "scope": 123,
}
```

## Related Entities
- **Destiny.DestinyGatingScope**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyUnlockExpressionDefinition":   {
      "description": "Where the sausage gets made. Unlock Expressions are the foundation of the game's gating mechanics and investment-related restrictions. They can test Unlock Flags and Unlock Values for certain states, using a sufficient amount of logical operators such that unlock expressions are effectively Turing complete.\r\nUse UnlockExpressionParser to evaluate expressions using an IUnlockContext parsed from Babel.",
      "type": "object",
      "properties": {
          "scope": {
              "format": "int32",
              "description": "A shortcut for determining the most restrictive gating that this expression performs. See the DestinyGatingScope enum's documentation for more details.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyGatingScope"
              }
          }
      }
  }
}
```
