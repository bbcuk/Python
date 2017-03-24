# batch_file_rename.py
# Created: 2017 3 24

'''
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
'''

__author__  = 'Li Chao'
__version__ = '1.0'
import sys
import os.path
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='the directory where to change extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser

def batch_file_rename(rootdir,ext):
	if not os.path.isdir(rootdir):
		print("The directory is invalid:",rootdir)
		return
	for parent,dirnames,filenames in os.walk(rootdir):

		for filename in filenames:
			print("file: ",parent,filename,os.path.join(parent,filename))	
			newfilename = "{0}.{1}".format(os.path.splitext(filename)[0],ext)
			os.rename(os.path.join(parent,filename),os.path.join(parent,newfilename))

def main():
	    # adding command line argument
    parser = get_parser()
    args = vars(parser.parse_args())

    # Set the variable work_dir with the first argument passed
    work_dir = args['work_dir'][0]

    # Set the variable new_ext with the third argument passed
    new_ext = args['new_ext'][0]
    batch_file_rename(work_dir,new_ext)

if __name__ == '__main__':
	main()

