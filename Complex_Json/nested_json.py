data = {
  "endUserTextId":"example@gmail.com",
  "plan": "Basic/Stain Buster/Deep", 
  "SelectedData":{
    "BedRoom":{
      "quantity":4,
      "BedRoomSize1":120, 
      "BedRoomSize2":140,
      "BedRoomSize3":200,
      "BedRoomSize4":240
    },
    "DiningRoom":{
      "quantity":1,
      "DiningRoomSize1":300
    },
    "BathRoom":{
      "quantity":3,
      "BathroomSize1":100,
      "BathroomSize2":120,
      "BathroomSize3":150
    },
    "Kitchen":{
      "quantity":1,
      "KitchenSize":200
    },
    "Stair":{
      "quantity":2,
      "StairSize1":160,
      "StairSize2":160
    },
    "Hallway":{
      "quantity":2,
      "HallwaySize1":300,
      "HallwaySize2":250
    }
  }
}
selected_data = data['SelectedData']
print(selected_data)
placejson = {}

for room_name, room_data in selected_data.items():
    print(room_name, " :: ", room_data)
    addition = 0
    for key,value in room_data.items():
        if key != 'quantity':
            addition = addition+value
    placejson[room_name]=addition
    
print ("\n================================", placejson)