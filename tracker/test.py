
import folium
import geocoder
import string
import os as os
import pathlib
import zipfile
import json
from functools import wraps, update_wrapper
from datetime import datetime
from pathlib import Path


PATH = Path.cwd()
print(PATH)
STATIC_PATH = Path.cwd() / "static"
MAP_PATH = Path.cwd() / "maps"
print(STATIC_PATH)
out_zip = os.path.join(MAP_PATH, "map.zip")
print(out_zip)
zip_ref = zipfile.ZipFile(out_zip, "r")
zip_ref.extractall(STATIC_PATH)