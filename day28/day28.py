import requests
from pydantic import BaseModel, EmailStr, Field, field_validator, HttpUrl

# schema(strict rules)
class GeoCoordinates(BaseModel):
    lat: float  # API gives string "-37.3159", Pydantic converts to float -37.3159
    lng: float

    @field_validator('lat', 'lng')
    @classmethod
    def check_bounds(cls, v: float) -> float:
        """Ensure coordinates are physically possible"""
        if not (-180 <= v <= 180):
            raise ValueError(f"Coordinate {v} is out of bounds")
        return v

class UserProfile(BaseModel):
    id: int
    name: str = Field(..., min_length=2)
    email: EmailStr  # must be a valid email format
    website: str     # keep as str initially to fix it or use HttpUrl
    geo_location: GeoCoordinates

    # custom validator
    @field_validator('website')
    @classmethod
    def ensure_url_protocol(cls, v: str) -> str:
        """
        Real World Messiness - API returns 'hildegard.org'
        System Needs - 'http://hildegard.org'
        """
        if not v.startswith(('http://', 'https://')):
            return f"http://{v}"
        return v

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    print(f"Fetching data from {url}...")
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    return resp.json()

def process_data():
    raw_users = fetch_users()
    print(f"Received {len(raw_users)} raw records.")

    valid_users = []
    
    print("Starting Validation Layer...")
    for record in raw_users:
        try:
            # MAP raw dictionary -> strict schema
            mapped_data = {
                "id": record['id'],
                "name": record['name'],
                "email": record['email'],
                "website": record['website'],
                "geo_location": record['address']['geo'] 
            }

            # validate
            user = UserProfile(**mapped_data)
            valid_users.append(user)
            print(f"Valid: {user.name:<20} | Web: {user.website} | Lat: {user.geo_location.lat}")

        except Exception as e:
            print(f"Rejected: User ID {record.get('id')}: {e}")

    print(f"Success. {len(valid_users)}/{len(raw_users)} records cleaned and imported.")
    return valid_users

if __name__ == "__main__":
    process_data()