# -*- coding: UTF-8 -*-
from voduploadsdk.AliyunVodUtils import *
from voduploadsdk.AliyunVodUploader import AliyunVodUploader
from voduploadsdk.UploadAttachedMediaRequest import UploadAttachedMediaRequest


# 测试上传本地辅助媒资(水印、字幕等文件)
def testUploadLocalAttachedMedia(accessKeyId, accessKeySecret, filePath):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadAttachedRequest = UploadAttachedMediaRequest(filePath, 'watermark')
        uploadAttachedRequest.setTitle('test upload local watermark file')
        media = uploader.uploadAttachedMedia(uploadAttachedRequest, True)
        print(media)

    except AliyunVodException as e:
        print(e)


# 测试上传网络辅助媒资(水印、字幕等文件)
def testUploadWebAttachedMedia(accessKeyId, accessKeySecret, fileUrl):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadAttachedRequest = UploadAttachedMediaRequest(fileUrl, 'watermark')
        uploadAttachedRequest.setTitle('test upload web watermark file')
        media = uploader.uploadAttachedMedia(uploadAttachedRequest, False)
        print(media)

    except AliyunVodException as e:
        print(e)


####  执行测试代码   ####
accessKeyId = '<AccessKeyId>'
accessKeySecret = '<AccessKeySecret>'

localFilePath = '/opt/image/sample.png'
#testUploadLocalAttachedMedia(accessKeyId, accessKeySecret, localFilePath)

fileUrl = 'http://vod-download.cn-shanghai.aliyuncs.com/retina/pic/20180208/496AE240-54AE-4CC8-8578-3EEC8F386E0B.gif'
testUploadWebAttachedMedia(accessKeyId, accessKeySecret, fileUrl)



