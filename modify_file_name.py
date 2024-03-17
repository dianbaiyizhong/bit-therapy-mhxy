import os

folder = 'ghost_general'
file_list = os.listdir(folder)
cmd_path = os.getcwd() + '/' + folder
for file_name in file_list:
    if file_name.endswith('png') or file_name.endswith('json') or file_name.endswith('psd'):
        new_file_name = file_name.replace('ghostGeneral', 'ghost_general')
        os.rename(os.path.join(cmd_path, file_name),
                  os.path.join(cmd_path,
                               new_file_name))
