import os

from PIL import Image


def cut_image(bb_type, type_name: str, n, m, need_start_index, need_num, ignore_range=None):
    ignore = list()
    if ignore_range is not None:
        for i in range(ignore_range[0], ignore_range[1]):
            ignore.append(i)
    print(ignore)
    image_path = None
    file_list = os.listdir(os.getcwd() + '/factory')
    if type_name == 'attack':
        for file_name in file_list:
            if '敌' in file_name and '攻击' in file_name:
                image_path = file_name
    elif type_name == 'magic':
        for file_name in file_list:
            if '敌' in file_name and '施法' in file_name:
                image_path = file_name
    elif type_name == 'standby':
        for file_name in file_list:
            if '敌' in file_name and '待机' in file_name:
                image_path = file_name
    elif type_name == 'walk' or type_name == 'drag' or type_name == 'fly':
        for file_name in file_list:
            if 'D' in file_name:
                image_path = file_name

    print(image_path)
    img = Image.open(os.getcwd() + '/factory/' + image_path)
    w, h = img.size

    # 计算每个小块的宽度和高度
    tw = w // n
    th = h // m

    flag = 0
    name_index = 1
    play_index = 0
    for i in range(m):
        for j in range(n):
            if flag < need_start_index:
                flag = flag + 1
            else:
                # 计算每个小块的坐标
                left = j * tw
                upper = i * th
                right = (j + 1) * tw if j < n - 1 else w
                down = (i + 1) * th if i < m - 1 else h
                # 切割小块
                box = (left, upper, right, down)
                img_piece = img.crop(box)
                if play_index not in ignore:
                    img_piece.save(os.getcwd() + '/factory/' + f'{bb_type}_{type_name}-{name_index}.png')
                    name_index = name_index + 1
                play_index = play_index + 1
                if name_index == need_num + 1:
                    return


if __name__ == '__main__':
    cut_image('ts', 'attack', 5, 5, 0, 13, (4, 16))
    # cut_image('ts', 'magic', 5, 4, 1, 17)
    # cut_image('ts', 'standby', 5, 3, 0, 10)
    # cut_image('ts', 'fly', 8, 4, 0, 8)
    # cut_image('ts', 'drag', 8, 4, 0, 8)
