#coding=utf-8
import material
import json
import media

accesstoken = 'NkNXMSORDQ841mDYyXFEheCLaFHriMlS-VIVOfL-k8HpJ18RSun48qbFQOd9XQCh12h12wuRqm4yQI_SF-tXlwE10aJ3abJ_jSHxG8VNcPNXbmMffpxAmoYVhhOydgDkQJCaAFAATM'
filepath = '/Users/qsong/Desktop/素材/QQ20161129-0.jpg'
mediatype = 'image'

news =(
    {
        "articles":
        [
            {
            "title": "test",
            "thumb_media_id": "X2UMe5WdDJSS2AS6BQkhTw9raS0pBdpv8wMZ9NnEzns",
            "author": "vickey",
            "digest": "",
            "show_cover_pic": 1,
            "content": "<p><img data-s=\"300,640\" data-type=\"jpeg\" data-src=\"http://mmbiz.qpic.cn/mmbiz/iaK7BytM0QFPLhxfSMhOHlZd2Q5cw3YibKVf4dgNpLHXdUkvl65NBSMU71rFfOEKF3ucmXuwAQbNdiaaS3441d5rg/0?wx_fmt=jpeg\" data-ratio=\"0.748653500897666\" data-w=\"\"  /><br  /><img data-s=\"300,640\" data-type=\"jpeg\" data-src=\"http://mmbiz.qpic.cn/mmbiz/iaK7BytM0QFPLhxfSMhOHlZd2Q5cw3YibKiaibdNgh0ibgOXAuz9phrGjYFBUKlyTBcrv5WE5zic08FUcz5ODXCHEykQ/0?wx_fmt=jpeg\" data-ratio=\"0.748653500897666\" data-w=\"\"  /><br  /></p>",
            "content_source_url": "",
            }
        ]
    })

news = json.dumps(news, ensure_ascii=False)
sucai = material.Material()
# sucai = media.Media()
sucai.uplaod(accesstoken,filepath,mediatype)
# sucai.add_news(accesstoken,news)




