import json

# Your JSON data as a string
json_data = '''
{
  "basic": {
    "rank": 1,
    "isCustomizable": false,
    "isDefault": true,
    "label": "Basic",
    "priceIncreasePercentage": 0,
    "includedServices": [
      "3 bed room [180 sft, 120 sft and 80 sft]"
    ],
    "selectedControls":{
      "bedRoom": {
        "includedUnits": 3,
        "selectedControls": [
          {
            "size": {
              "includedUnits": 180
            }
          },
          {
            "size": {
              "includedUnits": 120
            }
          },
          {
            "size": {
              "includedUnits": 80
            }
          }
        ]
      }
    }
  },
  "deepClean": {
    "rank": 2,
    "isCustomizable": false,
    "isDefault": true,
    "label": "Deep Clean",
    "priceIncreasePercentage": 0,
    "includedServices": [
      "3 bed room [260 sft, 180 sft and 120 sft]",
      "1 living room [large]"
    ],
    "selectedControls":{
      "bedRoom": {
        "includedUnits": 3,
        "selectedControls": [
          {
            "size": {
              "includedUnits": 260
            }
          },
          {
            "size": {
              "includedUnits": 180
            }
          },
          {
            "size": {
              "includedUnits": 120
            }
          }
        ]
      },
      "livingRoom": {
        "includedUnits": 1,
        "selectedControls": [
          {
            "size": {
              "includedUnits": 200
            }
          }
        ]
      }
    }
  }
}
'''

# Parse the JSON data into a Python dictionary
data = json.loads(json_data)
keys_of_json = data.keys()
print("keys_of_json", keys_of_json)

# Convert the keys to a list if needed
keys_list = list(keys_of_json)

# Print the keys
print("Keys of JSON object:", keys_list)


# Accessing data elements
basic_label = data["basic"]["label"]
deep_clean_label = data["deepClean"]["label"]
bedroom_sizes = data["basic"]["selectedControls"]["bedRoom"]["selectedControls"][2]["size"]["includedUnits"]

# Print some information
print("Basic Label:", basic_label)
print("Deep Clean Label:", deep_clean_label)
print("Bedroom Sizes:", bedroom_sizes)
