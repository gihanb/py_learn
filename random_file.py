import argparse
import os
import random
import string


def random_string(len):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(len))


def create_files(extention, count, folder):
    for i in range(count):
        filename = f"{random_string(5)}.{extention}"
        filepath = os.path.join(folder, filename)
        with open(filepath, "w") as file:
            file.write("this is a sample file")


parser = argparse.ArgumentParser(description='creare random files with different extentions')

parser.add_argument('--count', type=int, help='total number of files to create')
parser.add_argument('--folder', type=str, help='folder location to save the files')

args = parser.parse_args()

if args.count and args.folder:
    count = args.count
    folder = args.folder
    create_files(".txt", count, folder)
    create_files(".pdf", count, folder)
    create_files(".xlxs", count, folder)
    create_files(".gif", count, folder)
