import os
from variables import recipes_folder, assets_folder

def get_filenames(folder):
    def filename(i):
        return os.path.join(folder, i)

    def is_file(filename):
        return os.path.isfile(filename)
    return [filename(i) for i in os.listdir(folder) if is_file(filename(i))]

def get_recipe_filenames():
    return get_filenames(recipes_folder)

def professor_signature_filename():
    get_filenames(assets_folder)
    return os.path.join(assets_folder,'Carlos Rafael Fernandes Picanço.jpg')

if __name__ == '__main__':
    print(get_recipe_filenames())