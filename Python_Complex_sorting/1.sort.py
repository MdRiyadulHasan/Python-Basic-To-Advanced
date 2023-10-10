data = {
    "results": [
        {
            "rank": 2,
            "bottomCategory": {
                "PhoneRepairing": {
                    "id": 6,
                    "rank1": 50,
                    "textId": "PhoneRepairing",
                    "title": "Phone Repairing",
                    "image": "/media/category/SFBU-logo_0.png"
                },
                "FloorCleaning": {
                    "id": 7,
                    "rank1": 600,
                    "textId": "FloorCleaning",
                    "title": "Floor Cleaning",
                    "image": "/media/category/SFBU-logo_0.png"
                }
            }
        },
        {
            "rank": 1,
            "topCategory": {
                "Cleaning": {
                    "id": 1,
                    "rank1": 100,
                    "textId": "Cleaning",
                    "title": "Cleaning",
                    "image": "/media/category/ieee-logo.png"
                },
                "Plumbing": {
                    "id": 2,
                    "rank1": 90,
                    "textId": "Plumbing",
                    "title": "Plumbing",
                    "image": "/media/category/SFBU-logo_0.png"
                },
                "Repairing": {
                    "id": 11,
                    "rank1": 800,
                    "textId": "Repairing",
                    "title": "Repairing",
                    "image": "/media/category/SFBU-logo_0.png"
                }
            }
        }
    ]
}

sorted_data=[
    {
        "rank": 1,
        "topCategory": {
            "Cleaning": {
                "id": 1,
                "rank1": 100,
                "textId": "Cleaning",
                "title": "Cleaning",
                "image": "/media/category/ieee-logo.png"
            },
            "Plumbing": {
                "id": 2,
                "rank1": 90,
                "textId": "Plumbing",
                "title": "Plumbing",
                "image": "/media/category/SFBU-logo_0.png"
            },
            "Repairing": {
                "id": 11,
                "rank1": 800,
                "textId": "Repairing",
                "title": "Repairing",
                "image": "/media/category/SFBU-logo_0.png"
            }
        }
    },
    {
        "rank": 2,
        "bottomCategory": {
            "PhoneRepairing": {
                "id": 6,
                "rank1": 50,
                "textId": "PhoneRepairing",
                "title": "Phone Repairing",
                "image": "/media/category/SFBU-logo_0.png"
            },
            "FloorCleaning": {
                "id": 7,
                "rank1": 600,
                "textId": "FloorCleaning",
                "title": "Floor Cleaning",
                "image": "/media/category/SFBU-logo_0.png"
            }
        }
    }
]


sorted_data = sorted(data["results"], key = lambda x :x['rank'] )

for result in sorted_data:
    print("Result111", result)
    print("\n\n")
    for key, value in result.items():
        if isinstance(value, dict):
            print("important ..", key, "-------", value)
            sorted_value = dict(sorted(value.items(), key=lambda x: x[1].get("rank1")))
            result[key] = sorted_value
# print (sorted_data)