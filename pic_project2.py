from PIL import Image, ImageFilter
n = 0
lst_files = []
box = (100, 100, 400, 450)
class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []
    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не знайдено!')
        self.original.show()
    def do_left(self):
        global n
        conveted_image = self.original.transpose(Image.ROTATE_90)
        conveted_image.show()
        self.changed.append(conveted_image)
        print("")
        print('*** CONVERTED ***')
        print("")
        print('Pозмip:', conveted_image.size)
        print('copмat:', conveted_image.format)
        print('Tиn:', conveted_image.mode)
        print("")
        n += 1
        name = f'Image{n}.jpg'
        conveted_image.save(name)
        lst_files.append(name)

    def do_cropped(self):
        global n
        cropped_image = self.original.crop(box)
        cropped_image.show()
        self.changed.append(cropped_image)
        print("")
        print('*** CROPPED ***')
        print("")
        print('Pозмip:', cropped_image.size)
        print('copмat:', cropped_image.format)
        print('Tиn:', cropped_image.mode)
        print("")
        n += 1
        name = f'Image{n}.jpg'
        cropped_image.save(name)
        lst_files.append(name)

    def do_blurred(self):
        global n
        blurred_image = self.original.filter(ImageFilter.BLUR)
        blurred_image.show()
        self.changed.append(blurred_image)
        print("")
        print('*** BLURRED ***')
        print("")
        print('Pозмip:', blurred_image.size)
        print('copмat:', blurred_image.format)
        print('Tиn:', blurred_image.mode)
        print("")
        n += 1
        name = f'Image{n}.jpg'
        blurred_image.save(name)
        lst_files.append(name)

    def do_ch_b(self):
        global n
        chebeshechka = self.original.convert('L')
        chebeshechka.show()
        self.changed.append(chebeshechka)
        print("")
        print('*** CHEBESHKA ***')
        print("")
        print('Pозмip:', chebeshechka.size)
        print('copмat:', chebeshechka.format)
        print('Tиn:', chebeshechka.mode)
        print("")
        n += 1
        name = f'Image{n}.jpg'
        chebeshechka.save(name)
        lst_files.append(name)

    def australian_mode(self):
        global n
        au = self.original.transpose(Image.ROTATE_180)
        au.show()
        self.changed.append(au)
        print("")
        print('*** AUSTRALIAN MODE ***')
        print("")
        print('Pозмip:', au.size)
        print('copмat:', au.format)
        print('Tиn:', au.mode)
        print("")
        n += 1
        name = f'Image{n}.jpg'
        au.save(name)
        lst_files.append(name)

image = ImageEditor('kit.jpg')
image.open()
image.do_blurred()
image.do_left()
image.do_cropped()
image.do_ch_b()
image.australian_mode()
print(lst_files)