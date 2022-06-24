import argparse

from dictionary_download_rsi import download_rsi
from dictionary_download_ueexi import download_ueexi

tools = {
    "xyan-dictionary-rsi": download_rsi,
    "xyan-dictionary-ueexi": download_ueexi
}

parser = argparse.ArgumentParser(description=f'Using all the tools for CIG. Available tools: {tools.keys()}')
parser.add_argument('tool', type=str, help='The tool, to run.')
parser.add_argument('--folder',
                    metavar='f',
                    default='.',
                    help='If a tool needs a location to safe anything in use this parameter.')

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        print(f'Starting tool: {args.tool}')
        tools[args.tool](args)
    except KeyError:
        parser.print_help()
