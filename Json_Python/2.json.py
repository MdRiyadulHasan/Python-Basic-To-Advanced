import json

# JSON string representing the configuration
json_string = '''
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
        "pricePerUnit": 0
      }, 
      "kitchenRoom": {
        "textId": "kitchenRoom", 
        "dataType": "unsignedInteger",
        "label": "Kitchen Room",  
        "requiredPriceCustomize": true,
        "default": 80,
        "minimum": 25,
        "pricePerUnit": 0
      }, 
      "diningRoom": {
        "textId": "diningRoom", 
        "dataType": "unsignedInteger",
        "label": "Dining Room",  
        "requiredPriceCustomize": true,
        "default": 120,
        "minimum": 80,
        "pricePerUnit": 0
      } 
    }
}
'''

# Parse the JSON string into a Python dictionary
config = json.loads(json_string)

# Access the properties of the JSON object
text_id = config["textId"]  # "FloorCleaning"
target_units = config["targetunits"]  # "sqft"

# Access and work with the controls (room types)
bedroom_config = config["controls"]["bedRoom"]
kitchen_config = config["controls"]["kitchenRoom"]
dining_config = config["controls"]["diningRoom"]

# Access specific properties of each room type
bedroom_label = bedroom_config["label"]  # "BedRoom"
bedroom_default_area = bedroom_config["default"]  # 80
bedroom_minimum_area = bedroom_config["minimum"]  # 25
bedroom_price_per_unit = bedroom_config["pricePerUnit"]  # 0
bedroom_requires_customization = bedroom_config["requiredPriceCustomize"]  # True

# You can perform similar operations for kitchen_config and dining_config

# Now you can use this configuration to calculate cleaning prices or perform other tasks
# For example, calculating the price for cleaning a bedroom of a given area:
def calculate_bedroom_cleaning_price(area):
    if area < bedroom_minimum_area:
        return f"The minimum cleaning area for a {bedroom_label} is {bedroom_minimum_area} {target_units}."
    
    price = area * bedroom_price_per_unit
    return f"The cleaning price for a {bedroom_label} of {area} {target_units} is ${price}."

# Usage example:
bedroom_area_to_clean = 100  # You can change this value
bedroom_cleaning_price = calculate_bedroom_cleaning_price(bedroom_area_to_clean)
print(bedroom_cleaning_price)

# You can create similar functions for kitchen_config and dining_config as needed.

# Additionally, you can use this configuration to dynamically generate forms or interfaces for users to customize cleaning prices for each room type.
