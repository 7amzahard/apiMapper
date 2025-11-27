apiMapper
======================================

A multi-endpoint Google Maps API mapper for developers, researchers, and OSINT analysts.

apiMapper is a Python-powered command-line tool that sends requests across multiple Google Maps Platform APIs—Static Maps, Street View, Geocoding, Directions, Roads, Timezone, Elevation, and more. 
It outputs clean, colorized JSON responses and includes an optional ASCII banner for style.

Perfect for:

- API testing
- Rapid debugging
- Geodata research
- OSINT workflows
- Learning Google Maps endpoints

======================================
Features
======================================

✔ Multi-endpoint Google Maps API testing  
✔ Colorized terminal output  
✔ Pixel-art banner  
✔ Pretty JSON formatting  
✔ Optional single-URL mode  
✔ Error-safe request handling  
✔ Simple CLI flags (--all, --url, --key)  
✔ Easy to extend with new endpoints  

======================================
Banner
======================================

░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█████████████▓▒░  
                                                                                      

======================================
Installation
======================================

1. Clone the repository:
    git clone https://github.com/yourusername/apiMapper.git
    cd apiMapper

2. Install dependencies:
    pip install requests

3. Run:
    python3 apiMapper.py --key YOUR_API_KEY --all

======================================
Usage
======================================

List all options:
    python3 apiMapper.py --help

Run all Google Maps endpoints:
    python3 apiMapper.py --key YOUR_API_KEY --all

Test a single custom URL:
    python3 apiMapper.py --key YOUR_API_KEY --url "https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=YOUR_API_KEY"

======================================
Included Endpoints
======================================

apiMapper automatically queries:

- Static Maps API
- Directions API
- Street View API
- Geocoding API
- Distance Matrix API
- Places API (Find Place, Autocomplete)
- Elevation API
- Time Zone API
- Roads API
- Geolocation API

======================================
Example Output
======================================

→ URL: https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=...
✓ Success

{
    "results": [...],
    "status": "OK"
}

-------------------------------------------------------

======================================
Configuration
======================================

You only need one Google Maps API key with the following permissions:

- Geocoding API
- Maps JavaScript API
- Distance Matrix API
- Directions API
- Roads API
- Timezone API
- Elevation API
- Street View API
- Places API

Billing must be enabled in your Google Cloud project.

======================================
File Structure
======================================

apiMapper/
│
├── apiMapper.py     (main tool)
├── README.md        (documentation)
└── LICENSE          (optional)

======================================
Contributing
======================================

Contributions are welcome!

You can:

- Submit new endpoints
- Add color themes
- Improve the banner
- Add parallel request support
- Add export-to-file

Open a pull request or create an issue.

======================================
License
======================================

MIT License.

======================================
Author
======================================

Created by yourname.

