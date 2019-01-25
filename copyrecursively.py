from distutils.dir_util import copy_tree

# copy subdirectory example
fromDirectory = "/home/suresh/test/"
toDirectory = "/home/suresh/sample/"

copy_tree(fromDirectory, toDirectory)