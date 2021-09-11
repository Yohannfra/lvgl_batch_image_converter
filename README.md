# LGVL helper script to batch and convert with lvgl offline image converter

## Clone this repository

```
$ git clone --recursive https://github.com/Yohannfra/lvgl_batch_image_converter.git
```


## How to use

Edit the variables **CF** and **FORMAT** in [run_batch.py]() to fit your needs.

```bash
# run on all directory (only .png, .jpg and .bmp will be converted)
./run_batch.py directory_with_images

# run on files
./run_batch.py file1.png file2.png file3.png ...
```
