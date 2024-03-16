from psd_tools import PSDImage
import shutil

from psd_tools.api.layers import Layer

bb_type = 'vampire'
psd = PSDImage.open('../{}/{}.psd'.format(bb_type, bb_type))
dead_num = 8


def extract_layer_image(layer: Layer):
    if layer.is_group() is not True:
        if 'front' in layer.name:
            image = layer.composite(viewport=(0, 0, 160, 160))
        else:
            image = layer.composite(viewport=(0, 0, 192, 192))
        image.save(str('../{}/' + layer.name + '.png').format(bb_type))
        if 'dead' in layer.name and str('-' + str(dead_num)) in layer.name:
            path = str('../{}/' + layer.name + '.png').format(bb_type)
            for i in range(dead_num, dead_num + 36):
                shutil.copy(path, path.replace(str('-' + str(dead_num)), str('-' + str(dead_num + i))))


if __name__ == "__main__":
    # 遍历图层
    for layer in psd.descendants():
        extract_layer_image(layer)
