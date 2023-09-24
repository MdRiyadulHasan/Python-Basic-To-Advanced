json_data = '''
{
  "basic": {
    "rank": 1,
    "label": "Basic",
    "shortDescription": [
      "3 bed room [180 sft, 120 sft and 80 sft]"
    ],
    "selectedControls":{
      "bedRoom": {
        "includedUnits": "",
        "rank": 1,
        "label": "Bed Room",
        "minimum": 120,
        "units":["sqft","sqmt","pice"]
      },
      "DrawingRoom": {
        "includedUnits": 3,
        "rank": 2,
        "label": "Drawing Room",
        "minimum": 150,
        "units":["sqft","sqmt","pice"]
      },

       "DiningRoom": {
        "includedUnits": 3,
        "rank": 3,
        "label": "Dining Room",
        "minimum": 180,
        "units":["sqft","sqmt","pice"]
      },

      "BathRoom": {
        "includedUnits": 3,
        "rank": 4,
        "label": "Bath Room",
        "minimum": 100,
        "units":["sqft","sqmt","pice"]
      },

      "Kitchen": {
        "includedUnits": 3,
        "rank": 5,
        "label": "Kitchen",
        "minimum": 100,
        "units":["sqft","sqmt","pice"]
      },
      "Stair": {
        "includedUnits": 3,
        "rank": 4,
        "label": "Stair",
        "minimum": 100,
        "units":["sqft","sqmt","pice"]
      },
     

      


      



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