from PIL import Image, ImageFont, ImageDraw
import csv

def certgen(path):

  names = []

  with open(path, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
      for item in row:
        names.append(item)
  csvfile.close()
  names = names[1:]

  for name in names:
    blank_certificate = Image.open(r" --BLANK CERTIFICATE TEMPLATE PATH-- ")
    W, H = blank_certificate.size
    image_editable = ImageDraw.Draw(blank_certificate)
    name_font = ImageFont.truetype(r' --FONT PATH-- ',80)
    w, h = name_font.getsize(name)
    image_editable.text(((W - w) / 2, 750), name, (187, 130, 45), font=name_font) #Co-ordinates of the name and RGB values of the colour that is to be used for the name
    downfile = (" --DIRECTORY YOU WANT TO SAVE THE GENERATED CERTIFICATES IN-- " + name + ".png")
    blank_certificate.save(downfile)
  return names



# ----------------------##########################-------------------------------


if __name__ == '__main__':
  names = certgen(' --PATH TO CSV CONTAINING ALL THE NAMES-- ')
  print(names)