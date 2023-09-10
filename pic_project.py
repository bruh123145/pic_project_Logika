from PIL import Image, ImageFilter, ImageEnhance
with Image.open("pic.jpg") as pic:

    print("До")
    print('Pозмip:', pic.size)
    print('copмat:', pic.format)
    print('Tиn:', pic.mode)

    pic.show()

    pic_gray = pic.convert('L')
    pic_gray.save('gray.jpg')
    print("Після")
    print('Pозмip:', pic.size)
    print('copмat:', pic.format)
    print('Tиn:', pic.mode)
    pic_gray.show()

    pic_blur = pic.filter(ImageFilter.BLUR)
    pic_blur.save('blured.jpg')
    pic_blur.show()

    pic_up = pic.transpose(Image.ROTATE_180)
    pic_up.save('pic_up.jpg')
    pic_up.show()

    mirrow = pic.transpose(Image.FLIP_LEFT_RIGHT)
    mirrow.save('mirrow.jpg')
    mirrow.show()

    pic_contrast = ImageEnhance.Contrast(pic)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save('contr.jpg')
    pic_contrast.show()