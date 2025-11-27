#!/usr/bin/env python3
import argparse
import requests
import json
import sys
import time

# ──────────────────────────────────────────────
# Colors
# ──────────────────────────────────────────────
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# ──────────────────────────────────────────────
# HOLLOW BANNER (ASCII Pixel Art)
# ──────────────────────────────────────────────
def banner():
    print(MAGENTA + r"""
░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█████████████▓▒░  
                                                                                      
                                                                                      
------------------------------------------------
Thank you for visiting https://asciiart.website/
This ASCII pic can be found at
https://asciiart.website/figlet.php
""" + RESET)

# ──────────────────────────────────────────────
# Requests helper
# ──────────────────────────────────────────────
def fetch(url):
    print(CYAN + "→ URL:" + RESET, url)
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(GREEN + "✓ Success\n" + RESET)
        print(json.dumps(r.json(), indent=4))
    except Exception as e:
        print(RED + f"✗ Error: {e}" + RESET)
    print(YELLOW + "-" * 55 + RESET)
    time.sleep(0.2)

# ──────────────────────────────────────────────
# API Calls
# ──────────────────────────────────────────────
def run_all(key):
    endpoints = [
        f"https://maps.googleapis.com/maps/api/staticmap?center=45,10&zoom=7&size=400x400&key={key}",
        f"https://maps.googleapis.com/maps/api/streetview?size=400x400&location=40.720032,-73.988354&fov=90&heading=235&pitch=10&key={key}",
        f"https://www.google.com/maps/embed/v1/place?q=place_id:ChIJyX7muQw8tokR2Vf5WBBk1iQ&key={key}",
        f"https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key={key}",
        f"https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key={key}",
        f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615,-73.9976592&key={key}",
        f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={key}",
        f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Bingh&types=(cities)&key={key}",
        f"https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&key={key}",
        f"https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key={key}",
        f"https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key={key}",
        f"https://www.googleapis.com/geolocation/v1/geolocate?key={key}"
    ]

    for url in endpoints:
        fetch(url)

# ──────────────────────────────────────────────
# Main CLI
# ──────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="HOLLOW, this is a simple script for cheack any api key is it working or not :)")

    parser.add_argument(
        "-k", "--key",
        help="Google Maps API Key",
        required=True
    )

    parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Run all Google Maps API queries"
    )

    parser.add_argument(
        "-u", "--url",
        help="Run a single custom URL"
    )

    args = parser.parse_args()

    banner()

    if args.url:
        fetch(args.url)

    if args.all:
        run_all(args.key)

    if not args.all and not args.url:
        print(RED + "No action selected. Use -a for all or -u for one URL." + RESET)

if __name__ == "__main__":
    main()
