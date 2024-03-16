import os

from PIL import Image

from photoshop.photoshop_util import PhotoshopUtil

if __name__ == '__main__':
    folder = '../105GhostGeneral'
    file_list = os.listdir(folder)
    width_list = list()
    height_list = list()
    image_list = list()
    for file_name in file_list:
        if file_name.endswith('png'):
            PhotoshopUtil.crop_transparency(folder + '/' + file_name, file_name)
            image_list.append(file_name)
            with Image.open(file_name) as img:
                width, height = img.size
                width_list.append(width)
                height_list.append(height)
    max_width = max(width_list)
    max_height = max(height_list)
    print(max_width, max_height)
    # width = 384
    # height = 384
    for file_name in image_list:
        from PIL import Image

        # 创建一个新的透明画布，
        width, height = max([max_width, max_height]), max([max_width, max_height])
        canvas = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        # 保存为PNG文件
        canvas.save('background.png')
        # 加载背景图片和要置中的PNG图片
        background = Image.open("background.png")

        overlay = Image.open(file_name)

        # 获取背景图片的尺寸和PNG图片的尺寸
        background_width, background_height = background.size
        overlay_width, overlay_height = overlay.size

        # 计算PNG图片的置中位置
        position_x = (background_width - overlay_width) // 2
        position_y = (background_height - overlay_height) // 2

        # 将PNG图片置中于背景图片
        background.paste(overlay, (position_x, position_y), overlay)

        # 保存合成后的图片
        background.save(file_name)
