#!/usr/bin/env python3
"""
Generate table-of-content (toc) for each of the markdown notes in a directory

This requires Python 3.6+
"""
import os
import subprocess
import copy

if __name__ == "__main__":
    topdir = '.'
    # The extension to search for
    exten = '.md'

    lines = "# Table of content\n<!-- toc -->\n<!-- tocstop -->\n\n"
    toc_start = "<!-- toc -->"

    for dirpath, dirnames, files in os.walk(topdir):
        for ix, name in enumerate(files):
            if name.endswith(exten):
                file_path = f"{dirpath}/{name}"
                print(f"!!!! ---Processing " +
                      f"{file_path} {ix + 1} out of {len(files)}--- !!!")
                with open(file_path) as f:
                    file_content = "".join(f.readlines())

                if toc_start not in file_content:
                    print(f"!!!! ---TOC mark {toc_start} not present -!!!")
                    file_content = lines + file_content
                    with open(file_path, "w") as f:
                        print('!!!! ---Adding TOC mark to file content -!!!')
                        # print(file_content)
                        f.writelines(file_content)

                print(f"!!!! --- Generating TOC for {file_path} - !!!!")
                subprocess.call(
                        [f"/usr/local/bin/markdown-toc -i {file_path}"],
                        shell=True)
