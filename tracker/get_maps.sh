wget -O static/CenCal.html.zip  "https://drive.google.com/uc?export=download&id=1bqhQ0Wuv_iVOmQKJafpXpbx891rzPLgV" 
wget -O static/california_venturacounty_4dec2021.html.zip "https://drive.google.com/file/d/1lnylSF11Yz9g1db-INgNeXFuQN0fikQa/view?usp=sharing"
wget -O static/california_kerncounty.html.zip  "https://drive.google.com/file/d/16ktPy0Ui9-XulwK5VEEJCRYCYoE3m-3A/view?usp=sharing"

cd static

gdown 
unzip -qq CenCal.html.zip
unzip -qq california_venturacounty_4dec2021.html.zip
unzip -qq california_kerncounty.html.zip    
