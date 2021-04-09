# -*- coding: UTF-8 -*-
from voduploadsdk.AliyunVodUtils import *
from voduploadsdk.AliyunVodUploader import AliyunVodUploader
from voduploadsdk.UploadImageRequest import UploadImageRequest 

# 测试上传本地图片
def testUploadLocalImage(accessKeyId, accessKeySecret, filePath):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadImageRequest = UploadImageRequest(filePath)
        uploadImageRequest.setTitle('test upload local image')  # 设置图片标题，默认为空
        imageId, imageUrl = uploader.uploadImage(uploadImageRequest, True)
        print("file: %s, imageId: %s, imageUrl: %s" % (uploadImageRequest.filePath, imageId, imageUrl))
        
    except AliyunVodException as e:
        print(e)

# 测试上传网络图片
def testUploadWebImage(accessKeyId, accessKeySecret, fileUrl):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadImageRequest = UploadImageRequest(fileUrl)
        uploadImageRequest.setTitle('test upload web image')  # 设置图片标题，默认为空
        imageId, imageUrl = uploader.uploadImage(uploadImageRequest, False)
        print("file: %s, imageId: %s, imageUrl: %s" % (uploadImageRequest.filePath, imageId, imageUrl))
        
    except AliyunVodException as e:
        print(e)


####  执行测试代码   ####   
accessKeyId = '<AccessKeyId>'
accessKeySecret = '<AccessKeySecret>'

localFilePath = '/opt/image/sample.png'
#testUploadLocalImage(accessKeyId, accessKeySecret, localFilePath)

fileUrl = 'http://vod-download.cn-shanghai.aliyuncs.com/retina/pic/20180208/496AE240-54AE-4CC8-8578-3EEC8F386E0B.gif'
testUploadWebImage(accessKeyId, accessKeySecret, fileUrl)

        

