import json

# Manual list of Jeju-si locations (that were lost or missing from CSV)
jeju_si_data = [
  {
    "id": 1001,
    "name": "Jeju Int'l Airport Restroom",
    "lat": 33.5104,
    "lng": 126.4913,
    "address": "2 Gonghang-ro, Jeju-si",
    "type": "Public",
    "openTime": "24 Hours",
    "unisex": False,
    "diaperTable": True
  },
  {
    "id": 1002,
    "name": "Hamdeok Beach Restroom",
    "lat": 33.5434,
    "lng": 126.6696,
    "address": "Hamdeok-ri, Jocheon-eup, Jeju-si",
    "type": "Public",
    "openTime": "24 Hours",
    "unisex": True,
    "diaperTable": True
  },
  {
    "id": 1003,
    "name": "Hyeopjae Beach Restroom",
    "lat": 33.3938,
    "lng": 126.2396,
    "address": "2497-1 Hyeopjae-ri, Hallim-eup, Jeju-si",
    "type": "Public",
    "openTime": "09:00 - 22:00",
    "unisex": False,
    "diaperTable": True
  },
  {
    "id": 1004,
    "name": "Dongmun Market Public Toilet",
    "lat": 33.5117,
    "lng": 126.5263,
    "address": "20 Gwandeok-ro 14-gil, Jeju-si",
    "type": "Open",
    "openTime": "08:00 - 21:00",
    "unisex": False,
    "diaperTable": False
  },
  {
    "id": 1005,
    "name": "Iho Tewoo Beach Restroom",
    "lat": 33.4975,
    "lng": 126.4528,
    "address": "Iho 1-dong, Jeju-si",
    "type": "Public",
    "openTime": "24 Hours",
    "unisex": False,
    "diaperTable": True
  },
  {
    "id": 1006,
    "name": "Manjanggul Cave Restroom",
    "lat": 33.5284,
    "lng": 126.7716,
    "address": "182 Manjanggul-gil, Gujwa-eup, Jeju-si",
    "type": "Public",
    "openTime": "09:00 - 18:00",
    "unisex": False,
    "diaperTable": True
  },
  {
    "id": 1007,
    "name": "Gwakji Gwamul Beach Restroom",
    "lat": 33.4503,
    "lng": 126.3056,
    "address": "Gwakji-ri, Aewol-eup, Jeju-si",
    "type": "Public",
    "openTime": "24 Hours",
    "unisex": True,
    "diaperTable": True
  },
  {
    "id": 1008,
    "name": "Aewol Handam Coastal Walk",
    "lat": 33.4632,
    "lng": 126.3101,
    "address": "Aewol-ri, Aewol-eup, Jeju-si",
    "type": "Open",
    "openTime": "10:00 - 20:00",
    "unisex": False,
    "diaperTable": False
  },
  {
    "id": 1009,
    "name": "Jeju City Hall Public Toilet",
    "lat": 33.4996,
    "lng": 126.5312,
    "address": "Gwangyang 9-gil, Jeju-si",
    "type": "Public",
    "openTime": "09:00 - 18:00",
    "unisex": True,
    "diaperTable": True
  },
  {
    "id": 1010,
    "name": "Yongduam Rock Restroom",
    "lat": 33.5163,
    "lng": 126.5121,
    "address": "Yongdam 2-dong, Jeju-si",
    "type": "Public",
    "openTime": "24 Hours",
    "unisex": False,
    "diaperTable": False
  },
  {
    "id": 1011,
    "name": "GS25 Jeju Nohyeong",
    "lat": 33.4851,
    "lng": 126.4801,
    "address": "Nohyeong-dong, Jeju-si",
    "type": "Open",
    "openTime": "24 Hours",
    "unisex": False,
    "diaperTable": False
  },
  {
    "id": 1012,
    "name": "Samyang Black Sand Beach",
    "lat": 33.5247,
    "lng": 126.5866,
    "address": "Samyang-dong, Jeju-si",
    "type": "Public",
    "openTime": "24 Hours",
    "unisex": True,
    "diaperTable": False
  },
  {
    "id": 1013,
    "name": "Bijarim Forest Restroom",
    "lat": 33.4886,
    "lng": 126.8115,
    "address": "Daecheon-dong, Gujwa-eup, Jeju-si",
    "type": "Public",
    "openTime": "09:00 - 17:00",
    "unisex": False,
    "diaperTable": False
  },
  {
    "id": 1014,
    "name": "Gimnyeong Seongsegi Beach",
    "lat": 33.5558,
    "lng": 126.7588,
    "address": "Gimnyeong-ri, Gujwa-eup, Jeju-si",
    "type": "Public",
    "openTime": "24 Hours",
    "unisex": True,
    "diaperTable": True
  },
  {
    "id": 1015,
    "name": "Jeju Intercity Bus Terminal",
    "lat": 33.4998,
    "lng": 126.5160,
    "address": "Ora 1-dong, Jeju-si",
    "type": "Public",
    "openTime": "06:00 - 22:00",
    "unisex": False,
    "diaperTable": True
  },
  {
    "id": 1016,
    "name": "Sangumburi Crater",
    "lat": 33.4299,
    "lng": 126.6874,
    "address": "Gyorae-ri, Jocheon-eup, Jeju-si",
    "type": "Public",
    "openTime": "09:00 - 18:00",
    "unisex": False,
    "diaperTable": False
  },
  {
    "id": 1017,
    "name": "Nexon Computer Museum",
    "lat": 33.4717,
    "lng": 126.4849,
    "address": "Nohyeong-dong, Jeju-si",
    "type": "Public",
    "openTime": "10:00 - 18:00",
    "unisex": False,
    "diaperTable": True
  },
  {
    "id": 1018,
    "name": "Jeju National Museum",
    "lat": 33.5136,
    "lng": 126.5488,
    "address": "Geonip-dong, Jeju-si",
    "type": "Public",
    "openTime": "09:00 - 18:00",
    "unisex": False,
    "diaperTable": True
  }
]

def restore():
    try:
        with open('toilets.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        data = []

    print(f"Original size: {len(data)}")
    
    # Append
    data.extend(jeju_si_data)
    
    print(f"New size: {len(data)}")
    
    with open('toilets.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    restore()
