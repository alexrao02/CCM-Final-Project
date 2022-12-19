from facebook_scraper import get_posts
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def getApiIp():
    # 获取且仅获取一个ip
    # Get and only get an ip
    api_url = 'http://api.proxy.ipidea.io/getProxyIp?num=100&return_type=txt&lb=1&sb=0&flow=1&regions=&protocol=http'
    res = requests.get(api_url, timeout=5)
    try:
        if res.status_code == 200:
            api_data = res.json()['data'][0]
            proxies = f'http://{api_data["ip"]}:{api_data["port"]}'
            print(proxies)
            return proxies
        else:
            print('获取失败')
    except:
        print('获取失败')

#Initialize dataframe to scrape Facebook post
post_df_full = pd.DataFrame(columns = [])
for post in get_posts(account='cnbc', cookies='/Users/raowenjun/Desktop/facebook.com_cookies.txt', extra_info=True, pages=50, options={"comments": True}):
    post_entry = post
    fb_post_df = pd.DataFrame.from_dict(post_entry, orient='index')
    fb_post_df = fb_post_df.transpose()
    proxy = getApiIp()
    fb.set_proxy(proxy)
    post_df_full = post_df_full.append(fb_post_df)
    post_df_full.to_json(r'fb_scrapped_cnbc.json', indent=4, orient='records')
    post_df_full.to_csv('fb_scrapped_cnbc.csv')
    post_df_full.to_excel('fb_scrapped_cnbc.xlsx')
    print(post['post_id']+' get')


