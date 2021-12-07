#get maps

from pathlib import Path
from utils import download_from_gdrive

map_dict = {  'CenCal.html' : ['California Water Districts and Pits',
                                'Top 3 producers',
                                "https://drive.google.com/file/d/1bqhQ0Wuv_iVOmQKJafpXpbx891rzPLgV/view?usp=sharing"],
              'california_venturacounty_4dec2021.html' : ['Ventura County', 
                                'Todd Arbetter',
                                "https://drive.google.com/file/d/1lnylSF11Yz9g1db-INgNeXFuQN0fikQa/view?usp=sharing"],
               'california_kerncounty.html' : ['Kern County',
                                 'Todd Arbetter',
                                 "https://drive.google.com/file/d/16ktPy0Ui9-XulwK5VEEJCRYCYoE3m-3A/view?usp=sharing"]
             }


def download_maps(dict, dir):

  for key in dict:
    file_name = key + ".zip"
    url = dict[key][2] 
    print(url)
    download_from_gdrive(url,file_name,dir)

  pass  



if __name__ == '__main__':

  
  download_maps(map_dict, "static") 
