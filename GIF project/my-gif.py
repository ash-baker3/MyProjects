import imageio.v3 as iio

filenames = ['unagi1.jpg', 'unagi2.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('unagi.gif', images, duration = 500, loop = 0)