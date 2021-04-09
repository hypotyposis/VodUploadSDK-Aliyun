# -*- coding: UTF-8 -*-
from voduploadsdk.AliyunVodUtils import *
from voduploadsdk.AliyunVodUploader import AliyunVodUploader
from voduploadsdk.UploadVideoRequest import UploadVideoRequest 

# 测试上传本地视频
def testUploadLocalVideo(accessKeyId, accessKeySecret, filePath, storageLocation=None):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        #点播中心接入区域标识(默认为上海)，其他区域请填写对应区域标识，例：深圳cn-shenzhen
        #uploader.setApiRegion('cn-shanghai')
        uploadVideoRequest = UploadVideoRequest(filePath, 'test upload local video')
        # 可以设置视频封面，如果是本地或网络图片可使用UploadImageRequest上传图片到点播，获取到ImageURL
        #uploadVideoRequest.setCoverURL('https://sample.com/sample.jpg')  
        #uploadVideoRequest.setTags('tag1,tag2')
        if storageLocation:
            uploadVideoRequest.setStorageLocation(storageLocation)
        videoId = uploader.uploadLocalVideo(uploadVideoRequest)
        print("file: %s, videoId: %s" % (uploadVideoRequest.filePath, videoId))
        
    except AliyunVodException as e:
        print(e)
 
# 测试上传网络视频
def testUploadWebVideo(accessKeyId, accessKeySecret, fileUrl, storageLocation=None):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadVideoRequest = UploadVideoRequest(fileUrl, 'test upload web video')
        uploadVideoRequest.setTags('tag1,tag2')
        if storageLocation:
            uploadVideoRequest.setStorageLocation(storageLocation)
        videoId = uploader.uploadWebVideo(uploadVideoRequest)
        print("file: %s, videoId: %s" % (uploadVideoRequest.filePath, videoId))
        
    except AliyunVodException as e:
        print(e)
 
# 测试上传m3u8本地视频
def testUploadLocalM3u8(accessKeyId, accessKeySecret, m3u8LocalFile):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadVideoRequest = UploadVideoRequest(m3u8LocalFile, 'test upload local m3u8')
        # uploadVideoRequest.setTemplateGroupId('<TemplateGroupId>')
        # 分片文件和m3u8文件位于同一目录，SDK会自动解析上传
        videoId = uploader.uploadLocalM3u8(uploadVideoRequest)
        print("file: %s, videoId: %s" % (uploadVideoRequest.filePath, videoId))
        
    except AliyunVodException as e:
        print(e)
               
# 测试上传m3u8网络视频
def testUploadWebM3u8(accessKeyId, accessKeySecret, m3u8FileUrl):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadVideoRequest = UploadVideoRequest(m3u8FileUrl, 'test upload web m3u8')
        # 解析分片文件地址（适用于分片地址和m3u8文件签名相同或无签名的情况，其它情况需要您自行解析）
        sliceFileUrls = uploader.parseWebM3u8(m3u8FileUrl)
        videoId = uploader.uploadWebM3u8(uploadVideoRequest, sliceFileUrls)
        print("file: %s, videoId: %s" % (uploadVideoRequest.filePath, videoId))
        
    except AliyunVodException as e:
        print(e)


####  执行测试代码   ####
accessKeyId = '<AccessKeyId>'
accessKeySecret = '<AccessKeySecret>'

localFilePath = '/opt/video/sample.mp4'
testUploadLocalVideo(accessKeyId, accessKeySecret, localFilePath)

fileUrl = 'http://sample.oss.aliyuncs.com/video/sample.mp4'
#testUploadWebVideo(accessKeyId, accessKeySecret, fileUrl)

m3u8LocalFile = '/opt/video/m3u8/sample.m3u8'
#testUploadLocalM3u8(accessKeyId, accessKeySecret, m3u8LocalFile)

m3u8FileUrl = 'http://sample.oss.aliyuncs.com/video/m3u8/sample.m3u8'
#testUploadWebM3u8(accessKeyId, accessKeySecret, m3u8FileUrl)


