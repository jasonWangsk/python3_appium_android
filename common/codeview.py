from io import BytesIO

import requests

from PIL import Image

header_app_aliyun = {'Content-Type': 'application/json', 'operator_user_id': '911107047817281','x-app-version': '1.13.0'}
url = 'https://test.88gongxiang.com/user/api/v1/common/getCaptchaCode?data=aNuxpEWjJqnQG%2BGywdASw5HLIjIvRRrTInQvggwYAb' \
      'S0fJUuFTBWFS9tKP9mahD7ISRladfZlWdMta5HhvMQYYQB1dv/H/qUOCbhsKmZve/U19HQPUWsmGsJeH6rwwvSdynh9HFUua66S85G9f7Z/U30k%2' \
      'BidZqo97vgLh8at7V8%3D&version=1130'


r = requests.put(headers = header_app_aliyun,url=url )
i = Image.open(BytesIO(r.content))
print(i.show())


from common import size_image

xxx = size_image.cut_image(new_text='new_text')
print(xxx)