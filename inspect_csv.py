
import csv

def inspect_jeju_data():
    input_file = '공중화장실정보.csv'
    
    try:
        with open(input_file, 'r', encoding='cp949', errors='replace') as f:
            reader = csv.reader(f)
            headers = next(reader)
            
            # Find indices
            def find_idx(keywords):
                for i, h in enumerate(headers):
                    for k in keywords:
                        if k in h: return i
                return -1

            addr_idx = find_idx(['소재지도로명주소', '도로명주소'])
            jibun_idx = find_idx(['소재지지번주소', '지번주소'])
            lat_idx = find_idx(['WGS84위도', '위도'])
            lng_idx = find_idx(['WGS84경도', '경도'])
            name_idx = find_idx(['화장실명', '화장실'])

            print(f"Indices: Name={name_idx}, Addr={addr_idx}, Lat={lat_idx}, Lng={lng_idx}")

            jeju_si_count = 0
            jeju_si_missing_coords = 0
            
            for row in reader:
                addr = row[addr_idx] if addr_idx != -1 else ""
                jibun = row[jibun_idx] if jibun_idx != -1 else ""
                full_addr = addr + " " + jibun
                
                if "제주시" in full_addr:
                    jeju_si_count += 1
                    lat = row[lat_idx] if lat_idx != -1 else ""
                    lng = row[lng_idx] if lng_idx != -1 else ""
                    
                    if not lat or not lng:
                        jeju_si_missing_coords += 1
                        if jeju_si_missing_coords <= 5:
                            print(f"Missing Coords: {row[name_idx]} - {full_addr}")
            
            print(f"Total Jeju-si entries: {jeju_si_count}")
            print(f"Jeju-si entries missing coords: {jeju_si_missing_coords}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_jeju_data()
