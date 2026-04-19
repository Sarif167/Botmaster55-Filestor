
import requests
import re

OMDB_API = "http://www.omdbapi.com/?apikey=YOUR_API_KEY&t="

def clean_name(name):
    name = re.sub(r'\.(mkv|mp4|avi).*','', name, flags=re.I)
    return name.replace('.', ' ').replace('_',' ')

def fetch_imdb(name):
    try:
        url = OMDB_API + name
        r = requests.get(url).json()
        return {
            "title": r.get("Title","Unknown"),
            "year": r.get("Year","Unknown"),
            "rating": r.get("imdbRating","N/A"),
            "poster": r.get("Poster","")
        }
    except:
        return {"title":name,"year":"Unknown","rating":"N/A","poster":""}

def detect_lang(name):
    name = name.lower()
    if "hindi" in name: return "Hindi"
    if "english" in name: return "English"
    if "tamil" in name: return "Tamil"
    if "telugu" in name: return "Telugu"
    return "Unknown"
