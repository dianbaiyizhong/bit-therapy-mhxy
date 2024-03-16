from PIL import Image


def split_image(input_image_path, output_prefix, columns):
    with Image.open(input_image_path) as img:
        width, height = img.size
        part_height = height // columns
        index = 0
        for i in range(columns):
            if i > 0:
                box = (0, i * part_height, width, (i + 1) * part_height)
                img.crop(box).save(f"{output_prefix}-{index + 1}.png")
                index = index + 1


# 使用示例
split_image('105鬼将施法【敌】.png', '105GhostGeneral_attackSecond', 14)
