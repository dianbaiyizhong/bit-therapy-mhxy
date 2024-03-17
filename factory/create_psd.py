from PIL import Image
from psd_tools import PSDImage

from psd_tools import PSDImage

psd = PSDImage.new("RGBA", (380, 380), 0)
psd.save("fr.psd")
