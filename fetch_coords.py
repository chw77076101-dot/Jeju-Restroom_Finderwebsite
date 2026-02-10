import json
import requests
import time

def fetch_coordinates():
    # api_key = "YOUR_KAKAO_API_KEY"
    api_key = input("Enter Kakao API Key: ")
    headers = {"Authorization": f"KakaoAK {api_key}"}
    
    input_file = 'toilets.json'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("toilets.json not found.")
        return

    print(f"Total restrooms: {len(data)}")
    
    updated_count = 0
    error_count = 0
    
    for item in data:
        # Check if coords are missing or invalid (0,0) or empty string
        lat = item.get('lat')
        lng = item.get('lng')
        
        needs_update = False
        if not lat or not lng:
            needs_update = True
        elif isinstance(lat, str) and lat.strip() == "":
            needs_update = True
        elif isinstance(lng, str) and lng.strip() == "":
            needs_update = True
            
        if needs_update:
            address = item.get('address', '')
            if not address:
                continue
                
            # Clean address specifically for API query if needed
            # Removing parentheses details might help
            query_addr = address.split('(')[0].strip()
            
            url = f"https://dapi.kakao.com/v2/local/search/address.json?query={query_addr}"
            
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    result = response.json()
                    documents = result.get('documents')
                    if documents:
                        # Take the first result
                        coords = documents[0]
                        item['lat'] = float(coords['y'])
                        item['lng'] = float(coords['x'])
                        updated_count += 1
                        print(f"Updated: {item['name']} -> {item['lat']}, {item['lng']}")
                    else:
                        print(f"No result for: {address}")
                        error_count += 1
                else:
                    print(f"API Error {response.status_code} for {address}")
                    error_count += 1
                    
                # Rate limit politeness
                time.sleep(0.1)
                
            except Exception as e:
                print(f"Exception for {address}: {e}")
                error_count += 1

    print(f"Finished. Updated: {updated_count}, Errors/Not Found: {error_count}")
    
    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    fetch_coordinates()
