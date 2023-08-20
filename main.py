import requests
from datetime import datetime
from proteckt_info import vk_token, vk_domain, vk_version
#from googletrans import Translator

res_dict = {}
#translator = Translator()


def api_vk_wall_get(token, version, domain):
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'domain': domain,
                                'count': 50,
                            })
    data = response.json()['response']['items']
    for i in range(len(data)):
        attachments = data[i]['attachments']
        if len(attachments) > 1 and 'link' in attachments[1] and 'button' in attachments[1]['link']:
            url = attachments[1]['link']['button']['action'].get('url', None)
            if url is not None:
                temp = url.split('-')
                for j in temp:
                    if j.isdigit():
                        ind = (temp.index(j))
                        res_dict[f"chapter_{i}"] = j
                        #eng_text = ' '.join(temp[1:ind])
                        #russian_translation = translator.translate(eng_text, src='en', dest='ru')
                        res_dict[f"name_{i}"] = ' '.join(temp[1:ind])
            else:
                continue
        elif len(attachments) > 2 and 'link' in attachments[2]:
            title = attachments[2]['link'].get('title', None)
            if title is not None:
                temp = title.split()
                for j in temp:
                    if j.isdigit():
                        res_dict[f"chapter_{i}"] = j
                        res_dict[f"name_{i}"] = ' '.join(temp[:temp.index('-')])
            else:
                continue
        else:
            continue
        try:
            res_dict[f"url_{i}"] = data[i]['attachments'][0]['photo']['sizes'][-1]['url']
        except IndexError:
            continue
        res_dict[f"date_create{i}"] = datetime.utcfromtimestamp(data[i]['date']).strftime('%Y-%m-%d %H:%M:%S')

    return res_dict


api_vk_wall_get(vk_token, vk_version, vk_domain)

