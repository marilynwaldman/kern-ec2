
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
from utils import download_from_gdrive


url = "https://drive.google.com/file/d/1bqhQ0Wuv_iVOmQKJafpXpbx891rzPLgV/view?usp=sharing"

download_from_gdrive(url,"CenCal.html.zip","xxx") 