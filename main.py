import os
import requests
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

def download_font(font_url, font_path):
    if not os.path.exists(font_path):
        print(f"Downloading font from {font_url}...")
        r = requests.get(font_url)
        r.raise_for_status()
        with open(font_path, 'wb') as f:
            f.write(r.content)
        print(f"Font saved to {font_path}")

fonts = {
    "font1": {
        "url": "https://github.com/google/fonts/raw/main/ofl/montserrat/Montserrat-Bold.ttf",
        "path": "fonts/Montserrat-Bold.ttf"
    },
    "font2": {
        "url": "https://github.com/google/fonts/raw/main/ofl/leaguespartan/LeagueSpartan-Regular.ttf",
        "path": "fonts/LeagueSpartan-Regular.ttf"
    }
}

os.makedirs("fonts", exist_ok=True)
for font in fonts.values():
    download_font(font["url"], font["path"])

# Configurações @TODO: colocar isso em um arquivo de configuração
excel_path = 'input.xlsx'
image_path = 'template.jpg'
result_dir = 'result'
font_size = 32
coord1 = (50, 50)
coord2 = (50, 100)

os.makedirs(result_dir, exist_ok=True)
df = pd.read_excel(excel_path)

font1 = ImageFont.truetype(fonts["font1"]["path"], font_size)
font2 = ImageFont.truetype(fonts["font2"]["path"], font_size)

for idx, row in df.iterrows():
    val1 = str(row.iloc[0])
    val2 = str(row.iloc[1])
    img = Image.open(image_path).convert('RGB')
    draw = ImageDraw.Draw(img)
    draw.text(coord1, val1, font=font1, fill='white')
    draw.text(coord2, val2, font=font2, fill='white')
    out_path = os.path.join(result_dir, f'result_{idx+1}.jpg')
    img.save(out_path)

print("Done!")