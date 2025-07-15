import json

# Parse data-1.json (already in compatible format, just rename "temperature" to "temperature_celsius")
def parse_data1(path="data-1.json"):
    with open(path) as f:
        data = json.load(f)
    result = []
    for entry in data:
        result.append({
            "device_id": entry["device_id"],
            "timestamp_ms": entry["timestamp_ms"],
            "temperature_celsius": entry["temperature"]  # Rename key
        })
    return result

# Parse data-2.json (already matches target format)
def parse_data2(path="data-2.json"):
    with open(path) as f:
        data = json.load(f)
    return data  # Already in correct format

# Combine both and write result
def unify_and_save():
    data1 = parse_data1()
    data2 = parse_data2()
    unified = data1 + data2
    with open("data-result.json", "w") as f:
        json.dump(unified, f, indent=2)

# Run the transformation
if __name__ == "__main__":
    unify_and_save()
    print("✅ Data unified and written to data-result.json")
