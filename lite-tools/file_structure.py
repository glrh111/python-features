# -*- coding: utf-8 -*-
import os
import argparse
'''
os.name : type of os, posix | nt

os.listdir(path)

os.path.abspath(path) : os.path.abspath('.')
os.path.basename(path) : /abc/def return def    split()'s second value
os.path.dirname(path) : /abc/d/e return /abc/d
os.path.exists(path) : True | False

os.path.getatime(path) : last access time
os.path.getmtime(path) : last modification time

os.path.getsize(path) : return the size in bytes

os.path.isabs(path) : is an abs path?
os.path.isfile(path) : 
os.path.isdir(path) :
os.path.islink(path) : is symbol link?

os.path.join(path, *paths)

os.path.normcase(path) : on case-insensitive file system, converts path to lowercase
                         On windows, also converts forward slashed to backward slashes

os.path.split(path) : (dirname, basename)
os.path.splitdrive(path) : (drive, path)
os.path.splitext(path) : (root, extentname)

# sad experiences
    all_contents = os.listdir(path)
    dirs = [unicode(x) for x in all_contents if os.path.isdir(os.path.join(path, x))]
    files = [unicode(x) for x in all_contents if os.path.isfile(os.path.join(path, x))]
Some error accurs when parsing: System Volume Information

'''
# set command line args
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', default='.')
parser.add_argument('-d', '--depth', default=3, type=int)

class Prefix:
    '''
    prefix = DEPTH_EVERY * DEPTH + DIR/FILE
    '''
    DIR_NOT_LAST = u'├─'
    DIR_LAST = u'└─'
    FILE = u' ' * 4
    DEPTH_EVERY = u' ' * 4
    DEPTH = 0

def print_dirs(dirname, dirs, depth, mode=1):
    '''
    print_dirs(dirname, dirs, depth, mode=1)
    dirname : file = dirname + dirs[idx]
    dirs : list of files or direc
    mode : mode = 1 list of dirs; mode = other any list of files
    ├ : \u251c
    ─ : \u2500
    └ : \u2514
    '''
    # cal indent prefix
    indent_depth = Prefix.DEPTH - depth
    indent_prefix = indent_depth * Prefix.DEPTH_EVERY

    # cal prefix
    dir_not_last_prefix = indent_prefix + Prefix.DIR_NOT_LAST
    dir_last_prefix = indent_prefix + Prefix.DIR_LAST
    file_prefix = indent_prefix + Prefix.FILE

    # None return
    if not dirs:
        return
    
    # print dir
    if 1 == mode:
        nowname = dirs[0]
        try:
            if len(dirs) <= 1:
                print u'%s%s' % (dir_last_prefix, nowname)
            else:
                print u'%s%s' % (dir_not_last_prefix, nowname)
            # print this dir
            new_dir = os.path.join(dirname, nowname)
            print_dir_structure(new_dir, depth-1)
        except:
            pass
        # print other dir recursively
        dirs.pop(0)
        print_dirs(dirname, dirs, depth, mode)

    # print file
    else:
        # not recursive
        for i in dirs:
            try:
                print u'%s%s' % (file_prefix, i)
            # error accur
            except:
                print u'...'



def print_dir_structure(path, depth):
    '''
    print_dir_structure(path, depth)
    path : destination directory
    depth : directory recursive depth
    '''
    if 0 >= depth:
        return
    # achieve contents
    all_contents = os.listdir(path)
    dirs = [unicode(x) for x in all_contents if os.path.isdir(os.path.join(path, x))]
    files = [unicode(x) for x in all_contents if os.path.isfile(os.path.join(path, x))]
    # print every file and dir in list
    print_dirs(path, dirs, depth, 1)
    print_dirs(path, files, depth, 2)



if __name__ == '__main__':
    # parse args
    args = parser.parse_args()

    path = args.path
    path = os.path.abspath(path)

    depth = args.depth
    Prefix.DEPTH = depth
    print path

    # print
    print_dir_structure(path, depth)