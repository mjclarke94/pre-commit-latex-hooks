import argparse
import os

from pybtex.database import OrderedCaseInsensitiveDict, parse_file


def sort_library(library):
    original_keys = list(library.entries.keys())
    library.original_keys = original_keys

    sorted_entries = sorted(library.entries.items(), key=lambda x: x[1].key)
    library.entries = OrderedCaseInsensitiveDict()
    library.add_entries(sorted_entries)

    library.sorted_keys = list(library.entries.keys())


def check_reorder(library):
    if library.original_keys == library.sorted_keys:
        return False
    return True


def overwrite_library(library, filename):
    library.to_file(filename)


def main(argv=None):

    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to run")
    parser.add_argument(
        "--silent-overwrite", action="store_true", dest="silent", default=False
    )
    parser.add_argument(
        "--check-only", action="store_true", dest="check_only", default=False
    )
    args = parser.parse_args(argv)

    return_value = 0

    for filename in args.filenames:

        library = parse_file(filename)
        sort_library(library)

        if check_reorder(library):
            if args.check_only:
                return_value = 1
            elif args.silent:
                overwrite_library(library, filename)
            else:
                return_value = 1
                overwrite_library(library, filename)
                print("FIXED: {0}".format(os.path.abspath(filename)))
    return return_value


if __name__ == "__main__":
    exit(main())
