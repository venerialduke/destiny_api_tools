# Applications.Datapoint

## Entity Information
- **Entity Name**: Applications.Datapoint
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a single data point in a time series, containing a timestamp and associated count value. Used for tracking API usage metrics over time.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| time | string (date-time) | Timestamp for the related count. | No |
| count | number (double) | Count associated with timestamp | No |

## Usage Examples

### JavaScript
```javascript
// Example datapoint
const datapoint = {
  time: "2023-12-01T14:30:00Z",
  count: 150.0
};

// Working with datapoints
console.log(`Time: ${datapoint.time}`);
console.log(`Count: ${datapoint.count}`);

// Convert timestamp to Date object
const timestamp = new Date(datapoint.time);
console.log(`Formatted time: ${timestamp.toLocaleString()}`);

// Create new datapoint
const newDatapoint = {
  time: new Date().toISOString(),
  count: 200.0
};

// Array of datapoints for trending analysis
const datapoints = [
  { time: "2023-12-01T00:00:00Z", count: 100.0 },
  { time: "2023-12-01T01:00:00Z", count: 150.0 },
  { time: "2023-12-01T02:00:00Z", count: 200.0 }
];

// Calculate average count
const averageCount = datapoints.reduce((sum, dp) => sum + dp.count, 0) / datapoints.length;
console.log(`Average count: ${averageCount}`);
```

### Python
```python
from datetime import datetime
import json

# Example datapoint
datapoint = {
    "time": "2023-12-01T14:30:00Z",
    "count": 150.0
}

# Working with datapoints
print(f"Time: {datapoint['time']}")
print(f"Count: {datapoint['count']}")

# Convert timestamp to datetime object
timestamp = datetime.fromisoformat(datapoint['time'].replace('Z', '+00:00'))
print(f"Formatted time: {timestamp}")

# Create new datapoint
new_datapoint = {
    "time": datetime.now().isoformat() + "Z",
    "count": 200.0
}

# Array of datapoints for analysis
datapoints = [
    {"time": "2023-12-01T00:00:00Z", "count": 100.0},
    {"time": "2023-12-01T01:00:00Z", "count": 150.0},
    {"time": "2023-12-01T02:00:00Z", "count": 200.0}
]

# Calculate average count
average_count = sum(dp["count"] for dp in datapoints) / len(datapoints)
print(f"Average count: {average_count}")

# Find datapoint with maximum count
max_datapoint = max(datapoints, key=lambda dp: dp["count"])
print(f"Peak at {max_datapoint['time']}: {max_datapoint['count']}")
```

## Related Entities
- **Applications.Series**: Contains arrays of Datapoint objects
- **Applications.ApiUsage**: Uses Datapoint objects within Series for usage tracking
- **Applications.Application**: Indirectly related through usage statistics

## Notes
- The time property follows ISO 8601 date-time format (RFC 3339)
- The count property is typically a double/float value representing usage metrics
- Used for tracking API calls, throttled requests, and other time-based metrics
- Datapoints are usually ordered chronologically within their parent Series
- The count can represent various metrics depending on context (requests per hour, errors, etc.)

## JSON Schema
```json
{
  "Applications.Datapoint": {
    "type": "object",
    "properties": {
      "time": {
        "format": "date-time",
        "description": "Timestamp for the related count.",
        "type": "string"
      },
      "count": {
        "format": "double",
        "description": "Count associated with timestamp",
        "type": "number"
      }
    }
  }
}
```