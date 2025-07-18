# Destiny.DestinyUnlockValueUIStyle

## Entity Information
- **Entity Name**: Destiny.DestinyUnlockValueUIStyle
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
If you're showing an unlock value in the UI, this is the format in which it should be shown. You'll have to build your own algorithms on the client side to determine how best to render these options.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Automatic | Generally, Automatic means "Just show the number" |
| 1 | Fraction | Show the number as a fractional value. For this to make sense, the value being displayed should have a comparable upper bound, like the progress to the next level of a Progression. |
| 2 | Checkbox | Show the number as a checkbox. 0 Will mean unchecked, any other value will mean checked. |
| 3 | Percentage | Show the number as a percentage. For this to make sense, the value being displayed should have a comparable upper bound, like the progress to the next level of a Progression. |
| 4 | DateTime | Show the number as a date and time. The number will be the number of seconds since the Unix Epoch (January 1st, 1970 at midnight UTC). It'll be up to you to convert this into a date and time format understandable to the user in their time zone. |
| 5 | FractionFloat | Show the number as a floating point value that represents a fraction, where 0 is min and 1 is max. For this to make sense, the value being displayed should have a comparable upper bound, like the progress to the next level of a Progression. |
| 6 | Integer | Show the number as a straight-up integer. |
| 7 | TimeDuration | Show the number as a time duration. The value will be returned as seconds. |
| 8 | Hidden | Don't bother showing the value at all, it's not easily human-interpretable, and used for some internal purpose. |
| 9 | Multiplier | Example: "1.5x" |
| 10 | GreenPips | Show the value as a series of green pips, like the wins in a Trials of Osiris score card. |
| 11 | RedPips | Show the value as a series of red pips, like the losses in a Trials of Osiris score card. |
| 12 | ExplicitPercentage | Show the value as a percentage. For example: "51%" - Does no division, only appends '%' |
| 13 | RawFloat | Show the value as a floating-point number. For example: "4.52" NOTE: Passed along from Investment as whole number with last two digits as decimal values (452 -> 4.52) |
| 14 | LevelAndReward | Show the value as a level and a reward. |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyUnlockValueUIStyle enumeration values
const DestinyUnlockValueUIStyle = {
  Automatic: 0,
  Fraction: 1,
  Checkbox: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyUnlockValueUIStyle.Automatic;
```

### Python
```python
# Destiny.DestinyUnlockValueUIStyle enumeration values
class DestinyUnlockValueUIStyle:
    AUTOMATIC = 0
    FRACTION = 1
    CHECKBOX = 2
    # ... more values

# Using the enumeration
value = DestinyUnlockValueUIStyle.AUTOMATIC
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyUnlockValueUIStyle":   {
      "format": "int32",
      "description": "If you're showing an unlock value in the UI, this is the format in which it should be shown. You'll have to build your own algorithms on the client side to determine how best to render these options.",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "10",
          "11",
          "12",
          "13",
          "14"
      ],
      "type": "integer"
  }
}
```
