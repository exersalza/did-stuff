#!/bin/python3.11

import argparse
import subprocess

idk_how_to_call_that = {
    "cpp": "CMakeLists.txt",
    "python": ""
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("language", type=str, help=f"The language to use. Supportet are: "
                                                   f"{', '.join(idk_how_to_call_that.keys())}.")
    parser.add_argument("name", type=str, help="The name of the project.")
    args = parser.parse_args()

    project_name = args.name

    subprocess.run(f"mkdir {project_name} && cp -r /usr/share/salty-create/{args.language}/* {project_name}/",
                   shell=True)

    if idk_how_to_call_that[args.language]:
        add_project_name(project_name, f"{project_name}/{idk_how_to_call_that[args.language]}")  # TOO FCKING LONG

    return 0


def add_project_name(project_name: str, file: str) -> int:
    try:
        with open(file, "r", encoding="utf-8") as f:
            buffer = f.read()
            try:
                buffer = buffer % project_name
            except TypeError:
                pass

        with open(file, "w", encoding="utf-8") as f:
            f.write(buffer)

    except FileNotFoundError:
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
