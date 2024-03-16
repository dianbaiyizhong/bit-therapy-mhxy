import os

folder = '../deal_dead'
file_list = os.listdir(folder)
bb_type = '105GhostGeneral'
cmd_path = os.getcwd()
print(cmd_path)
for file_name in file_list:
    if file_name.endswith('png'):
        new_file_name = file_name.replace('死亡【敌】', bb_type + '_dead-')
        print(new_file_name)
        os.rename(os.path.join(cmd_path, file_name),
                  os.path.join(cmd_path,
                               new_file_name))
