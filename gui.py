from IPython.display import display
from PIL import Image

def get_file(path):
    return path.split("/")[-1].split(".")[0]

def get_result_path(content_path, style_path):
    return "./output/" + get_file(content_path) + "_stylized_" + get_file(style_path) + ".jpg"

def display_image(path):
    display(Image.open(path))
