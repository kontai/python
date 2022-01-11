import json

menu = \
    {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
        "lunch": {
            "hours": {
                "hours": "11-3",
                "items": {
                    "hamkburger": "$5.00"
                }
            }
        },
        "Dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
            }
        }
    }

def read_json(js):
    menu_json=json.dumps(js)
    print(menu_json)

read_json(menu)
print(menu)