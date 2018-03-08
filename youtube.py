import os
import sys
import re
import fileinput

def listdir(path):
    """
    recursively walk directory to specified depth
    :param path: (str) path to list files from
    :yields: (str) filename, including path
    """
    for filename in os.listdir(path):
        yield os.path.join(path, filename)


def walk(path='.', depth=None):
    """
    recursively walk directory to specified depth
    :param path: (str) the base path to start walking from
    :param depth: (None or int) max. recursive depth, None = no limit
    :yields: (str) filename, including path
    """
    if depth and depth == 1:
        for filename in listdir(path):
            yield filename
    else:
        top_pathlen = len(path) + len(os.path.sep)
        for dirpath, dirnames, filenames in os.walk(path):
            dirlevel = dirpath[top_pathlen:].count(os.path.sep)
            if depth and dirlevel >= depth:
                dirnames[:] = []
            else:
                for filename in filenames:
                    yield os.path.join(dirpath, filename)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='?', default='.', help=(
        "path to list files from (defaults to current directory)"))
    parser.add_argument('-d', '--depth', type=int, default=0, help=(
        "maximum level of sub-directories to decend"
        "(defaults to unlimited)."))
    # parser.add_argument('-v', '--version', action='version',
    #                     version='%(prog)s ' + __version__)
    
    mds = []
    args = parser.parse_args()
    for filename in walk(args.path, args.depth):
        if filename.endswith('.md'):
            mds.append(filename)

    print(mds)

    for file in mds:
        tmp_file = str(file) + '1'
        file_name = str(file)
        with open(file) as infile, open(tmp_file, 'w') as outfile:
            for line in infile:
                if 'youtube.com/embed/' in line:
                    youtubeString = re.findall(r'(www\.youtube\.com/embed/\S*)"', line)
                    youtubeStringStringed = youtubeString[0]
                    youtubeStringFixed = 'https//' + youtubeStringStringed
                    youtubeStringFixed = re.sub(r'embed/', 'watch?v=', youtubeStringFixed)
                    wholeLine = '{% youtube %}' + youtubeStringFixed + '{% endyoutube %}'
                    line = '\n' + wholeLine + '\n'
                outfile.write(line)
        infile.close()
        outfile.close()
        os.remove(file)
        os.rename(tmp_file, file_name)

# http://pythontesting.net/python/regex-search-replace-examples/#in_python