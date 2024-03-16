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

            # 输出小块图片
            if i == 0:
                img_piece.save(f'105GhostGeneral_drag-{j + 1}.png')  # 保存小块图片


if __name__ == '__main__':
    n = 8  # 横向切割数量
    m = 4  # 纵向切割数量

    cut_image('95鬼将D4A10B8X.png', n, m)
