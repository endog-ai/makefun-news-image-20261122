#!/usr/bin/env python3
"""News-image entry for make.fun contest news-image-20261122.

The entry image (entry.jpg) sums up 22 November 2026 in one picture: a
small child in a dark room watching a giant glowing television, on which
oil tankers burn in the Strait of Hormuz. That is the day's most viral
story — Iran striking US assets in Kuwait and Bahrain, and tankers
attacked near Hormuz — as the whole world watched it unfold on screen.

This program is deterministic and uses no network: it copies entry.jpg
byte-for-byte to /output/entry.png, so two runs always produce the same
bytes.
"""

import os
import shutil


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.jpg")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
