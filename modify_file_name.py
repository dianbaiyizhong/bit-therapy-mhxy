import os

folder = '105GhostGeneral'
file_list = os.listdir(folder)
action = 'drag'
cmd_path = os.getcwd() + '/' + folder
origin_type = 'output_'
for file_name in file_list:
    if file_name.endswith('png') and origin_type in file_name:
        new_file_name = file_name.split('.')[0]
        index = new_file_name.replace(origin_type, '')
        new_file_name = folder + '_' + action + '-' + index + '.png'
        os.rename(os.path.join(cmd_path, file_name),
                  os.path.join(cmd_path,
                               new_file_name))
