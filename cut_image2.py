from PIL import Image


def cut_image(image_path, n, m):
    img = Image.open(image_path)
    w, h = img.size

    # 计算每个小块的宽度和高度
    tw = w // n
    th = h // m

    for i in range(m):
        for j in range(n):
            # 计算每个小块的坐标
            left = j * tw
            upper = i * th
            right = (j + 1) * tw if j < n - 1 else w
            down = (i + 1) * th if i < m - 1 else h

            # 切割小块
            box = (left, upper, right, down)
            img_piece = img.crop(box)
            if i == 0:
                img_piece.save(f'vampire_drag-{j + 1}.png')  # 保存小块图片
            # if i == 1:
            #     img_piece.save(f'vampire_magic-{j + 1 + 5}.png')  # 保存小块图片
            # if i == 2:
            #     img_piece.save(f'vampire_magic-{j + 1 + 10}.png')  # 保存小块图片
            # if i == 3:
            #     img_piece.save(f'vampire_magic-{j + 1 + 15}.png')  # 保存小块图片
            # if i == 4:
            #     img_piece.save(f'vampire_magic-{j + 1 + 20}.png')  # 保存小块图片


if __name__ == '__main__':
    n = 8  # 横向切割数量
    m = 4  # 纵向切割数量

    cut_image('95吸血鬼D4A7B8X.png', n, m)
