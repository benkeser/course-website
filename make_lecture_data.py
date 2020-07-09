#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import yaml
import sys
import os

# ----------------------------------------------------------
# function to get yaml front-matter from an open file
# ----------------------------------------------------------
def get_yaml(f):
  pointer = f.tell()
  if f.readline() != '---\n':
    f.seek(pointer)
    return ''
  readline = iter(f.readline, '')
  readline = iter(readline.__next__, '---\n')
  return ''.join(readline)

# ----------------------------------------------------------
# main script
# ----------------------------------------------------------
# get directory from input
top_dir=sys.argv[1:]
os.chdir(top_dir)

# find folders with lecture in title
all_files=os.listdir(top_dir)
lecture_dirs = [f for f in all_files if ('lecture' in f and os.path.isdir(f))]

# declare empty dictionary
lecture_dict_list=[]

# loop over lecture directories to build dictionary that contains
# filename, directory name, title and tldr of lecture
for dir in lecture_dirs:
  os.chdir(dir)
  all_files_in_dir=os.listdir(".")
  # get rmd file name
  # assumes there is only one rmd file in the directory!
  rmd_file = [f for f in all_files_in_dir if ('.Rmd' in f or '.rmd' in f)]
  # get yaml from rmd file
  with open(rmd_file[0]) as f:
    config = yaml.load(get_yaml(f))
  this_dict = { 
     "filename" : os.path.splitext(rmd_file[0])[0], 
     "dirname" : dir, 
     "title" : config['title'],
     "tldr" : config['tldr'],
     "recording" : config['recording']
  }
  lecture_dict_list.append(this_dict)
  # back to top directory
  os.chdir(top_dir)

yaml_contents = yaml.dump(lecture_dict_list, default_flow_style = False)

# write to _data/lectures.yml file
save_file = os.path.join(top_dir, "_data", "lectures.yml")
with open(save_file, "wt") as f:
  f.write(yaml_contents)
  f.close()

