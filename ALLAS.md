# Allas commands

Setup:

```
module load allas
allas-conf
```

## Create and upload

commands to upload a directory as single files, and to publish it over the net

```
rclone mkdir allas:dhh23-em-illu
rclone sync illustration allas:dhh23-em-illu -P
a-access +p dhh23-em-illu
```
## public URL

https://a3s.fi/dhh23-em-illu/019550010604440_0.png


## list buckets

a-list

## list bucket contents

rclone ls [bucket]

## delete bucket with files

a-delete early-modern-clip-res1 --rmb --FORCE
