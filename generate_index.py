#!/usr/bin/python3

import os

HEAD = """
<!DOCTYPE html>
<html>
<head>
<title>Paperwork</title>
</head>
<body>
"""

FOOT = """
</body>
</html>
"""


def generate(fd):
    fd.write(HEAD)
    for (dirpath, subdirs, filenames) in os.walk("."):
        if dirpath.startswith("./."):
            continue
        if dirpath == ".":
            fd.write("\n<h1>Root</h1>\n".format(dirpath))
        else:
            fd.write("\n<h1>{}</h1>\n".format(dirpath))
        fd.write("<ul>\n")
        for filename in filenames:
            if (filename.startswith(".") or filename.endswith("~") or
                    filename == "index.html"):
                continue
            fd.write("\t<li><a href=\"{}\">{}</a></li>\n".format(
                os.path.join(dirpath, filename),
                filename
            ))
        fd.write("</ul>\n")

    fd.write(FOOT)


if __name__ == "__main__":
    with open("index.html", "w") as file_desc:
        generate(file_desc)
