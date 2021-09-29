#!/usr/bin/env python3

import sys
import os
from typing import List

PATH_TO_LVGL_IMG_CONVERTER = "./lv_utils/img_conv_core.php"

# Possible values are:
# true_color, true_color_alpha, true_color_chroma, indexed_1, indexed_2,
# indexed_4, indexed_8, alpha_1, alpha_2, alpha_4, alpha_8, raw, raw_alpha, raw_chroma
CF = "true_color"


# Possible values are:
# c_array, bin_332, bin_565, bin_565_swap, bin_888
FORMAT = "bin_565_swap"


def convert_file(fp: str):
    if not fp.endswith(('.png', '.jpg', '.bmp')):
        return
    output_file_name = fp.rsplit(".", 1)[0]
    print(f"Converting {fp}")
    command = f"php {PATH_TO_LVGL_IMG_CONVERTER} \"name={output_file_name}&img={fp}&format={FORMAT}&cf={CF}\""
    os.system(command)
    print("Done")


def run_batch_on_dir(dp: str):
    print(f"Batchin {dp}...")

    all_files = [f for f in os.listdir(dp) if os.path.isfile(os.path.join(dp, f))]

    for i in all_files:
        convert_file(os.path.join(dp, i))


def main(argc: int, argv: List[str]):
    if argc == 1:
        sys.exit("USAGE: ./run_batch.py [files] [directories]")

    for arg in argv[1:]:
        if os.path.isdir(arg):
            run_batch_on_dir(arg)
        elif os.path.isfile(arg):
            convert_file(arg)
        else:
            sys.exit(f"{arg} is not a file or a directory")


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
