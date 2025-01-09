# The Process to build LUPerson

All the videos' YouTube key can be found at [vnames.txt](https://drive.google.com/file/d/1eopcxZPNHnaobjnSwP37U2YFlptNE0A0/view?usp=sharing)

All detection results can be found at [dets.pkl](https://drive.google.com/file/d/1t_XPHOI_VzuebaAnXccu4iIzDXMNpTJO/view?usp=sharing)

**!! The following scripts are not well tested, but provide the main processes !!**.

## Download the raw videos: There are 2 ways
### 1st: Download whole videos in one time
```
python download.py -f ${YOUR_VIDEO_NAME_FILE_DIR}/vname.txt -s ${YOUR_VIDEO_DIR}
```
### 2nd: Split whole videos into 8 parts then download each part one by one
#### Run the script to split video keys
```
python split_vnames.py
```
#### Run download script
Default (Part 1):

```
./run_download.sh
```
Specify Part Number (e.g., Part 2):
```
./run_download.sh 2
```

[youtube-dl](https://github.com/ytdl-org/youtube-dl) is needed.

## Extract images from raw videos and their detections
### 1st: 
```
python extract.py -v ${YOUR_VIDEO_DIR} -d ${DETECTION_DIR} -s ${SAVE_DIR}
```
### 2nd: Extract images from each part
Extract default part 1:

```
./run_extract.sh
```
Extract specify part pumber (e.g., Part 2):
```
./run_extract.sh 2
```
## Convert extracted images to lmdb data
```
python convert_lmdb.py
```

# Three is a third reconstruction at [Issue](https://github.com/DengpanFu/LUPerson/issues/8#issuecomment-1004611808), please refer to it.
