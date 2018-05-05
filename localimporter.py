import re
import glob
import click
import ast


def needs_reorder(source_file):
    local_include = re.compile(r'#include ".*"')
    standard_include = re.compile(r'#include <.*>')

    standard_include_found = False
    standard_before_local = False

    with open(source_file, 'r') as f:
        for line in f.read().splitlines():
            if standard_include.match(line):
                standard_include_found = True
            if local_include.match(line):
                if standard_include_found:
                    standard_before_local = True

    return standard_before_local


def glob_sources(root, suffixes):
    sources = []
    for suffix in suffixes:
        pattern = '{0}/**/*.{1}'.format(root, suffix)
        sources += glob.glob(pattern, recursive=True)
    return sources


@click.command()
@click.option('--root',
              help='Directory root under which the script will search files.')
@click.option('--suffixes',
              default="['h', 'hpp', 'c', 'cpp']",
              help="List of suffixes to search, default: ['h', 'hpp', 'c', 'cpp'].")
def main(root, suffixes):
    sources = glob_sources(root, ast.literal_eval(suffixes))

    sources_need_reorder = [s for s in sources if needs_reorder(s)]

    if len(sources_need_reorder) > 0:
        print('the following sources include standard headers')
        print('before including local headers:\n')
        for source in sources_need_reorder:
            print(source)


if __name__ == '__main__':
    main()
