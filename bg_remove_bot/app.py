import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('images/test.png', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'H5rMinfQu6yopa7mwsYR7iqU'},
)
if response.status_code == requests.codes.ok:
    with open('images/out.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)

# try:
#     with open('test.jpg', 'wb') as img:
#         print("kut")
# except Exception as e:
#     print(e)
# else:
#     print("ISHLADI")
    
        

# url = 'https://www.cutout.pro/api/v1/matting?mattingType=6'
# r = requests.get(url)
# print(r.status_code)










# import os,sys
# print(f"Fayl : {os.path.abspath(__file__)}")
# print(f"Katalog : {os.getcwd()}")
# print(f"Import uchun katalog : {sys.path[0]}")
# print(f"TXT Faylga olib boruvchi path : {os.path.abspath('test_img.jpg')}")



# import requests

# URL = "https://api.slazzer.com/v2.0/remove_image_background"
# PATH = 
# API_KEY = "ae73dc80366e4e528be5f5e3a763b521"

# image_file = {'source_image_file': open(PATH, 'rb')}
# headers = {'API-KEY': API_KEY}
# response = requests.post(URL, files=image_file, headers=headers)
# with open('output.png', 'wb') as img:
#     img.write(response.content)















# # from PIL import Image, ImageEnhance, ImageFilter,ImageChops

# # im = Image.open("py.jpeg") #input image
# # im = im.filter(ImageFilter.MedianFilter())
# # enhancer = ImageEnhance.Contrast(im)
# # im = enhancer.enhance(2)
# # im = im.convert('1')
# # im.save('image_clear.jpg') #ouput image



# # import numpy as np
# # from scipy import signal
# # from PIL import Image


# # def load_image(path):
# #     return np.asarray(Image.open(path))/255.0

# # def save(path, img):
# #     tmp = np.asarray(img*255.0, dtype=np.uint8)
# #     Image.fromarray(tmp).save(path)

# # def denoise_image(inp):
# #     # estimate 'background' color by a median filter
# #     bg = signal.medfilt2d(inp,11)
# #     save('images/py.png', bg)

# #     # compute 'foreground' mask as anything that is significantly darker than
# #     # the background
# #     mask = inp < bg - 0.1
# #     save('images/py.png', mask)

# #     # return the input value for all pixels in the mask or pure white otherwise
# #     return np.where(mask, inp, 1.0)


# # image = Image.open('images/sample_DL.jpg')
# # image = image.convert('L') # convert image to grayscale
# # new_image = image.resize((832, 536))  
# # new_image.save('images/python.jpg')
# # inp_path = 'images/sample_DL_1.jpg'
# # out_path = 'images/output.png'

# # inp = load_image(inp_path)
# # out = denoise_image(inp)

# # save(out_path, out)


# # import numpy as np
# # from PIL import Image

# # im = Image.open('py.jpeg' )
# # im = im.convert('RGBA')
# # data = np.array(im)
# # # just use the rgb values for comparison
# # rgb = data[:,:,:3]
# # color = [246, 213, 139]   # Original value
# # black = [0,0,0, 255]
# # white = [255,255,255,255]
# # mask = np.all(rgb == color, axis = -1)
# # # change all pixels that match color to white
# # data[mask] = white

# # # change all pixels that don't match color to black
# # ##data[np.logical_not(mask)] = black
# # new_im = Image.fromarray(data)
# # new_im.save('python.png')


# # ImageChops.subtract(image1, image2, scale, offset) => image
# # Subtracts two images, dividing the result by scale and adding the offset.
# # If omitted, scale defaults to 1.0, and offset to 0.0.
# # out = (image1 - image2) / scale + offset