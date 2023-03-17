import requests
import datetime

def download_media(url):
    try:
        # 檢查是否為影片
        if '/videos/' in url:
            content = requests.get(url).content
            video_url = content.split(b'src="')[1].split(b'"')[0].decode()
            content = requests.get(video_url).content
            extension = '.mp4'
        else:
            content = requests.get(url + '/media/').content
            extension = '.jpg'
        
        # 檢查檔案是否已存在，如果不存在則創建一個新檔案
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = timestamp + extension
        with open(filename, 'wb') as out_file:
            out_file.write(content)
            print(f'{filename} 下載完成！')
    except Exception as e:
        print(f'發生錯誤：{e}')

if __name__ == '__main__':
    url = input('請輸入 Instagram 照片或影片連結：')
    download_media(url)
