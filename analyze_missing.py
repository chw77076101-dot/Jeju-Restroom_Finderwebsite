import csv
import json

def analyze_missing():
    input_file = '공중화장실정보.csv'
    
    print(f"Reading {input_file}...")
    
    missing_coords_count = 0
    missing_coords_examples = []
    
    try:
        with open(input_file, 'r', encoding='cp949') as f:
            reader = csv.reader(f)
            headers = next(reader)
            
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

            print(f"Indices: Name={name_idx}, Addr={road_addr_idx}/{jibun_addr_idx}, Lat={lat_idx}, Lng={lng_idx}")

            for row in reader:
                road_addr = row[road_addr_idx] if road_addr_idx != -1 else ""
                jibun_addr = row[jibun_addr_idx] if jibun_addr_idx != -1 else ""
                full_addr = road_addr + " " + jibun_addr
                
                if "제주" not in full_addr:
                    continue
                
                # Check specifics for Jeju-si
                is_jeju_si = "제주시" in full_addr

                lat_str = row[lat_idx] if lat_idx != -1 else ""
                lng_str = row[lng_idx] if lng_idx != -1 else ""
                
                has_coords = False
                if lat_str and lng_str:
                    try:
                        float(lat_str)
                        float(lng_str)
                        has_coords = True
                    except ValueError:
                        pass
                
                if not has_coords:
                    missing_coords_count += 1
                    if len(missing_coords_examples) < 10:
                        missing_coords_examples.append({
                            "name": row[name_idx],
                            "address": road_addr if road_addr else jibun_addr,
                            "is_jeju_si": is_jeju_si
                        })

    except Exception as e:
        print(f"Error: {e}")
        return

    print(f"Total Jeju records missing coordinates: {missing_coords_count}")
    print("Examples:")
    for ex in missing_coords_examples:
        print(ex)

if __name__ == "__main__":
    analyze_missing()
