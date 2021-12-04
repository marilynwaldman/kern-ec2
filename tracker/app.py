import requests
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
#from flask_bootstrap import Bootstrap
#from flask_nav import Nav
#from flask_nav.elements import *
#from dominate.tags import img


from ediblepickle import checkpoint
from flask import Flask, render_template, request, redirect, url_for, send_file, make_response


###############################################
#      Define navbar with logo                #
###############################################



app = Flask(__name__)
#Bootstrap(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True
map_dict = {  'CenCal.html' : ['California Water Districts and Pits','Top 3 producers'],
              'california_kerncounty.html' : ['Kern County', ' map by Todd']
}
app.vars = {}

def nocache(view):
  @wraps(view)
  def no_cache(*args, **kwargs):
    response = make_response(view(*args, **kwargs))
    response.headers['Last-Modified'] = datetime.now()
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response
        
  return update_wrapper(no_cache, view)


@app.route('/')
def main():
  return redirect('/index.html')

@app.route('/index.html', methods=['GET'])
def index():
  if request.method == 'GET':
    #return render_template('input.html')
    map_name = f"california_kerncounty.html"
    #map_name = f"CenCal.html"
    
    #have to set map path - used by template
    map_path = os.path.join(app.root_path, 'static/' + map_name)
    print(map_path)
    app.vars['map_path'] = map_path
    print(app.vars['map_path'])
    app.vars['Title_line1'] = map_dict[map_name][0]
    app.vars['Title_line2'] = map_dict[map_name][1]

    
    if Path(map_path).exists():
        return render_template('display.html', vars=app.vars)
    else:     
        return redirect('/maperror.html')

    pass

@app.route('/map', methods=['GET'])
# http://localhost:5000/map?map=CenCal.html
# http://localhost:5000/map?map=california_kerncounty.html
@nocache
def get_map():
  args = request.args
  print (args) # For debugging
  map_name = args['map']
  print(type(map_name))
  map_path = os.path.join(app.root_path, 'static/' + map_name)
  print(map_path)
  app.vars['map_path'] = map_path
  app.vars['Title_line1'] = map_dict[map_name][0]
  app.vars['Title_line2'] = map_dict[map_name][1]
  
  if Path(map_path).exists():
        return render_template('display.html', vars=app.vars)
  else:     
        return redirect('/maperror.html')

  pass

@app.route('/maps/map.html')
@nocache
def show_map():
  map_path = app.vars.get("map_path")
  print("show map")
  print(map_path)
  map_file = Path(map_path)
  if map_file.exists():
    return send_file(map_path)
  else:
    return render_template('error.html', culprit='map file', details="the map file couldn't be loaded")

  pass


@app.route('/error.html')
def error():
  details = "There was some kind of error."
  return render_template('error.html', culprit='logic', details=details)

@app.route('/apierror.html')
def apierror():
  details = "There was an error with one of the API calls you attempted."
  return render_template('error.html', culprit='API', details=details)

@app.route('/maperror.html')
def geoerror():
  details = "Map not found."
  return render_template('error.html', culprit='the Map', details=details)

#nav.init_app(app)

if __name__ == '__main__':

   PATH = Path.cwd()
   print(PATH)
   STATIC_PATH = Path.cwd() / "static"
   MAP_PATH = Path.cwd() / "maps"
   out_zip = os.path.join(MAP_PATH, "map.zip")
   zip_ref = zipfile.ZipFile(out_zip, "r")
   zip_ref.extractall(STATIC_PATH)
   app.debug = True

   app.run(host='0.0.0.0')