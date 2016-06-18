#!/usr/bin/env python
import os
import argparse

env_vars = ['GAZEBO_MODEL_PATH', 'GAZEBO_RESOURCE_PATH', 'GAZEBO_PLUGIN_PATH']

def process(line):
    line = ' '.join(line.split())
    for var in env_vars:
        #print(line.find('export '+var))
        #print(line.count(var))
        if line.find('export '+var)>-1 and line.count(var)==1:
            return line+':$'+var+'\n'
    return line+'\n'

def main(path):
    temp_name = path+".temp"
    with open(temp_name, 'w') as new:
        with open(path, 'r') as original:
            for line in original:
                #print(line)
                new_line = process(line)
                #print new_line+'\n'
                new.write(new_line)

    save_copy = path+'.orig'
    if not os.path.isfile(save_copy): os.rename(path,save_copy)
    os.rename(temp_name,path)

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path', type=str, help="path to gazebo's setup.sh (generally something like /usr/share/gazebo/setup.sh)")
    args = parser.parse_args()
    main(args.path)