from psd_tools import PSDImage
import shutil

from psd_tools.api.layers import Layer

bb_type = '105GhostGeneral'
psd = PSDImage.open(r'../105GhostGeneral/105GhostGeneral.psd')
dept_num = 9


def extract_layer_image(layer: Layer):
    if layer.is_group() is not True:
        if 'front' in layer.name:
            image = layer.composite(viewport=(0, 0, 160, 160))
        else:
            image = layer.composite(viewport=(0, 0, 314, 314))
        image.save(str('../{}/' + layer.name + '.png').format(bb_type))
        if 'dead' in layer.name and str('-' + str(dept_num)) in layer.name:
            path = str('../{}/' + layer.name + '.png').format(bb_type)
            for i in range(dept_num, dept_num + 36):
                shutil.copy(path, path.replace(str('-' + str(dept_num)), str('-' + str(dept_num + i))))


if __name__ == "__main__":
    # 遍历图层
    for layer in psd.descendants():
        extract_layer_image(layer)
