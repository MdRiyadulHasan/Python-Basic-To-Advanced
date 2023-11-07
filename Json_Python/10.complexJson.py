class AttributeConfiguration(APIView):
    permission_classes = [AllowAny]
    def get(self, request, textId):
        data = Attribute.objects.raw("""
           SELECT
            a.id,
            ag.textId AS AttributeGroupTextId,
            a.textId,
            a.title,
            a. rank as attibuteRank,
            a.priceCalculationStrategy,
            a.defaultUnitValue,
            a.defaultSqftValue,
            a.defaultValue,
            a.minimumUnitValue,
            a.minimumSqftValue,
            a.minimumValue,
            ac.textId,
            ac.title AS attributeCollectionTitle,
            ac.textId AS attributeCollectionTextId,
            ac.rank
        FROM
            attributegroup ag
        INNER JOIN
            attribute a ON ag.textId = a.attributeGroupTextId
        INNER JOIN
            attributecollection ac ON a.attributeCollectionTextId = ac.textId
        WHERE
            (ag.dataRequireStatusOnNewUser = "optional" OR ag.dataRequireStatusOnNewUser = 'required')
            AND a.attributeGroupTextId = %s
        ORDER BY
            ac.rank, attibuteRank

        """, [textId])

        # Create an empty dictionary for the JSON response
        response_data = {
            "textId": textId,
            "label": f"{textId} Configuration",
            "attributeGroupTextId": textId,
            "allAttributes": {},
        }

        # Populate the attributes lists based on their attributeCollectionTextId
        for attribute in data:
            collection = attribute.attributeCollectionTextId
            if collection not in response_data["allAttributes"]:
                response_data["allAttributes"][collection] = []

            attribute_dict = {
                "textId": attribute.textId,
                "label": attribute.title,
                "rank": attribute.attibuteRank,
                "priceCalculationStrategy": attribute.priceCalculationStrategy,
                "allowDenyStatus": attribute.allowDenyStatus,
                "unitValue": attribute.defaultUnitValue,
                "attributeCollectionTitle": attribute.attributeCollectionTitle,
                "averageSqftValue": attribute.defaultSqftValue,
                "attributeValue": attribute.defaultValue,
                "minimumUnitValue": attribute.minimumUnitValue,
                "minimumSqftValue": attribute.minimumSqftValue,
                "minimumValue": attribute.minimumValue,
            }

            response_data["allAttributes"][collection].append(attribute_dict)

        # Return the JSON response
        return JsonResponse(response_data)
# output

{
    "textId": "Home",
    "label": "Home Configuration",
    "attributeGroupTextId": "Home",
    "allAttributes": {
        "houseTypeAndSize": [
            {
                "textId": "houseType",
                "label": "HouseType",
                "rank": 1,
                "priceCalculationStrategy": "perUnit",
                "allowDenyStatus": "allow",
                "unitValue": 1.0,
                "attributeCollectionTitle": "House Type And Size",
                "averageSqftValue": 0.0,
                "attributeValue": 1.0,
                "minimumUnitValue": 1.0,
                "minimumSqftValue": 0.0,
                "minimumValue": 1.0
            },
            {
                "textId": "houseSize",
                "label": "House Size",
                "rank": 2,
                "priceCalculationStrategy": "sqftPerUnit",
                "allowDenyStatus": "allow",
                "unitValue": 1.0,
                "attributeCollectionTitle": "House Type And Size",
                "averageSqftValue": 1600.0,
                "attributeValue": 1600.0,
                "minimumUnitValue": 1.0,
                "minimumSqftValue": 1200.0,
                "minimumValue": 1200.0
            },
            {
                "textId": "lotSize",
                "label": "Lot Size",
                "rank": 3,
                "priceCalculationStrategy": "sqftPerUnit",
                "allowDenyStatus": "allow",
                "unitValue": 1.0,
                "attributeCollectionTitle": "House Type And Size",
                "averageSqftValue": 2000.0,
                "attributeValue": 2000.0,
                "minimumUnitValue": 1.0,
                "minimumSqftValue": 1800.0,
                "minimumValue": 1800.0
            }
        ],
        "roomAndArea": [
            {
                "textId": "bedRoom",
                "label": "Bed Room ",
                "rank": 1,
                "priceCalculationStrategy": "perUnit",
                "allowDenyStatus": "allow",
                "unitValue": 4.0,
                "attributeCollectionTitle": "Room And Area",
                "averageSqftValue": 0.0,
                "attributeValue": 4.0,
                "minimumUnitValue": 2.0,
                "minimumSqftValue": 0.0,
                "minimumValue": 2.0
            },
            {
                "textId": "livingRoom",
                "label": "Living Room",
                "rank": 2,
                "priceCalculationStrategy": "perUnit",
                "allowDenyStatus": "allow",
                "unitValue": 3.0,
                "attributeCollectionTitle": "Room And Area",
                "averageSqftValue": 0.0,
                "attributeValue": 3.0,
                "minimumUnitValue": 2.0,
                "minimumSqftValue": 0.0,
                "minimumValue": 2.0
            },
            {
                "textId": "familyRoom",
                "label": "Family Room",
                "rank": 3,
                "priceCalculationStrategy": "perUnit",
                "allowDenyStatus": "allow",
                "unitValue": 2.0,
                "attributeCollectionTitle": "Room And Area",
                "averageSqftValue": 0.0,
                "attributeValue": 2.0,
                "minimumUnitValue": 2.0,
                "minimumSqftValue": 0.0,
                "minimumValue": 2.0
            },
            {
                "textId": "diningRoom",
                "label": "Dining Room",
                "rank": 4,
                "priceCalculationStrategy": "perUnit",
                "allowDenyStatus": "allow",
                "unitValue": 2.0,
                "attributeCollectionTitle": "Room And Area",
                "averageSqftValue": 0.0,
                "attributeValue": 2.0,
                "minimumUnitValue": 1.0,
                "minimumSqftValue": 0.0,
                "minimumValue": 1.0
            },
            {
                "textId": "hallway",
                "label": "Hallway",
                "rank": 5,
                "priceCalculationStrategy": "perUnit",
                "allowDenyStatus": "allow",
                "unitValue": 1.0,
                "attributeCollectionTitle": "Room And Area",
                "averageSqftValue": 0.0,
                "attributeValue": 1.0,
                "minimumUnitValue": 1.0,
                "minimumSqftValue": 0.0,
                "minimumValue": 1.0
            },
            {
                "textId": "kitchen",
                "label": "Kitchen",
                "rank": 6,
                "priceCalculationStrategy": "perUnit",
                "allowDenyStatus": "allow",
                "unitValue": 1.0,
                "attributeCollectionTitle": "Room And Area",
                "averageSqftValue": 0.0,
                "attributeValue": 1.0,
                "minimumUnitValue": 1.0,
                "minimumSqftValue": 0.0,
                "minimumValue": 1.0
            },
            {
                "textId": "bathRomm",
                "label": "Bath Room",
                "rank": 7,
                "priceCalculationStrategy": "perUnit",
                "allowDenyStatus": "allow",
                "unitValue": 1.0,
                "attributeCollectionTitle": "Room And Area",
                "averageSqftValue": 0.0,
                "attributeValue": 1.0,
                "minimumUnitValue": 1.0,
                "minimumSqftValue": 0.0,
                "minimumValue": 1.0
            },
            {
                "textId": "stair",
                "label": "Stair",
                "rank": 8,
                "priceCalculationStrategy": "perUnit",
                "allowDenyStatus": "allow",
                "unitValue": 1.0,
                "attributeCollectionTitle": "Room And Area",
                "averageSqftValue": 0.0,
                "attributeValue": 1.0,
                "minimumUnitValue": 1.0,
                "minimumSqftValue": 0.0,
                "minimumValue": 1.0
            }
        ],
        "garageAndCar": [
            {
                "textId": "garage",
                "label": "Garage",
                "rank": 1,
                "priceCalculationStrategy": "perUnit",
                "allowDenyStatus": "allow",
                "unitValue": 1.0,
                "attributeCollectionTitle": "Garage And Car",
                "averageSqftValue": 0.0,
                "attributeValue": 1.0,
                "minimumUnitValue": 1.0,
                "minimumSqftValue": 0.0,
                "minimumValue": 1.0
            },
            {
                "textId": "car",
                "label": "Car",
                "rank": 2,
                "priceCalculationStrategy": "perUnit",
                "allowDenyStatus": "allow",
                "unitValue": 2.0,
                "attributeCollectionTitle": "Garage And Car",
                "averageSqftValue": 0.0,
                "attributeValue": 2.0,
                "minimumUnitValue": 1.0,
                "minimumSqftValue": 0.0,
                "minimumValue": 1.0
            }
        ],
        "swmmingPool": [
            {
                "textId": "swmmingPool",
                "label": "Swmming Pool",
                "rank": 1,
                "priceCalculationStrategy": "sqftPerUnit",
                "allowDenyStatus": "allow",
                "unitValue": 1.0,
                "attributeCollectionTitle": "Swmming Pool",
                "averageSqftValue": 500.0,
                "attributeValue": 500.0,
                "minimumUnitValue": 1.0,
                "minimumSqftValue": 300.0,
                "minimumValue": 300.0
            }
        ]
    }
}