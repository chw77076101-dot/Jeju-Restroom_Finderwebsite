import csv
import json

def process_nationwide():
    input_file = '공중화장실정보.csv'
    output_file = 'toilets.json'
    
    print(f"Reading {input_file}...")
    
    restrooms = []
    
    try:
        # CP949 is standard for Korean public data CSVs
        with open(input_file, 'r', encoding='cp949') as f:
            reader = csv.reader(f)
            headers = next(reader)
            
            # Find column indices
            try:
                # Flexible matching for column names
                def find_idx(keywords):
                    for i, h in enumerate(headers):
                        for k in keywords:
                            if k in h: return i
                    return -1

                name_idx = find_idx(['화장실명', '화장실'])
                road_addr_idx = find_idx(['소재지도로명주소', '도로명주소'])
                jibun_addr_idx = find_idx(['소재지지번주소', '지번주소'])
                lat_idx = find_idx(['WGS84위도', '위도'])
                lng_idx = find_idx(['WGS84경도', '경도'])
                time_idx = find_idx(['개방시간'])
                unisex_idx = find_idx(['남녀공용화장실여부'])
                diaper_idx = find_idx(['기저귀교환대유무', '기저귀교환대장소', '기저귀교환대여부'])
                
                print(f"Indices: Name={name_idx}, Addr={road_addr_idx}/{jibun_addr_idx}, Lat={lat_idx}, Lng={lng_idx}")
                
            except ValueError:
                print("Error finding columns")
                return

            for row in reader:
                # Filter for Jeju addresses
                road_addr = row[road_addr_idx] if road_addr_idx != -1 else ""
                jibun_addr = row[jibun_addr_idx] if jibun_addr_idx != -1 else ""
                
                full_addr = road_addr + " " + jibun_addr
                if "제주" not in full_addr:
                    continue
                
                # Check coordinates
                lat = 0.0
                lng = 0.0
                try:
                    lat_str = row[lat_idx]
                    lng_str = row[lng_idx]
                    
                    if lat_str and lng_str:
                        lat = float(lat_str)
                        lng = float(lng_str)
                        
                        # Basic Jeju Coordinate Bounding Box Validation
                        # Approx: 33.1 ~ 34.0 Lat, 126.1 ~ 127.0 Lng
                        if not (30 < lat < 40 and 120 < lng < 135):
                            lat = 0.0
                            lng = 0.0
                            
                except ValueError:
                    lat = 0.0
                    lng = 0.0

                # Extract other fields
                name = row[name_idx]
                open_time = row[time_idx] if time_idx != -1 else "Unknown"
                
                unisex = False
                if unisex_idx != -1:
                    val = row[unisex_idx]
                    if 'Y' in val or 'y' in val: unisex = True
                    
                diaper = False
                if diaper_idx != -1:
                    val = row[diaper_idx]
                    if 'Y' in val or 'y' in val: diaper = True
                    
                entry = {
                    "id": len(restrooms) + 1,
                    "name": name,
                    "lat": lat,
                    "lng": lng,
                    "address": road_addr if road_addr else jibun_addr,
                    "type": "Public",
                    "openTime": open_time,
                    "unisex": unisex,
                    "diaperTable": diaper
                }
                restrooms.append(entry)

    except Exception as e:
        print(f"Error processing file: {e}")
        return

    print(f"Found {len(restrooms)} valid Jeju restrooms.")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(restrooms, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_nationwide()
