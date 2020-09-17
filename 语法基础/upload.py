import oss2

auth = oss2.Auth('LTAI4G4sTEAwfV9X5CDncoKg', 'QdGprD842QsNUB5SP4wYy3sweaCJTR')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'niit-soft')

bucket.put_object('temp/wf.jpg', 'res/image/code.jpg')     
print('https://niit-soft.oss-cn-hangzhou.aliyuncs.com/temp/wf.jpg')       
