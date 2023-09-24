import json

# Your JSON data as a string
json_data = '''
{
  "textId": "FloorCleaning",
  "targetunits": "sqft",
  "controls": {
    "bedRoom": {
      "textId": "bedRoom",
      "dataType": "unsignedInteger",
      "label": "BedRoom",
      "requiredPriceCustomize": true,
      "default": 80,
      "minimum": 25,
      "pricePerUnit": "40"
    },
    "kitchenRoom": {
      "textId": "kitchenRoom",
      "dataType": "unsignedInteger",
      "label": "Kitchen Room",
      "requiredPriceCustomize": true,
      "default": 80,
      "minimum": 25,
      "pricePerUnit": "20"
    },
    "diningRoom": {
      "textId": "diningRoom",
      "dataType": "unsignedInteger",
      "label": "Dining Room",
      "requiredPriceCustomize": true,
      "default": 120,
      "minimum": 80,
      "pricePerUnit": "30"
    }
  }
}
'''

# Parse the JSON data into a Python dictionary
data = json.loads(json_data)

# Accessing data elements
text_id = data["textId"]
target_units = data["targetunits"]
controls = data["controls"]
keys =list(controls.keys())
print("keys", keys)

for key, value in controls.items():
    text_id = value["textId"]
    label = value["label"]
    default_value = value["default"]
    
    print(f"Room Name: {key}")
    print(f"Text ID: {text_id}")
    print(f"Label: {label}")
    print(f"Default Value: {default_value}")
    print("................................................")  # Add a separator between rooms


# Accessing specific control properties
bedroom_label = controls["bedRoom"]["label"]
kitchen_price_per_unit = controls["kitchenRoom"]["pricePerUnit"]

# Print some information
print("textId:", text_id)
print("targetunits:", target_units)
print("Bedroom Label:", bedroom_label)
print("Kitchen Price Per Unit:", kitchen_price_per_unit)
