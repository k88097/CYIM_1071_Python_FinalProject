import os
import pytube
import sys
import requests
from bs4 import BeautifulSoup as bs4


def main():
    print('---歡迎使用此程式下載YouTube影片---')
    global path
    path = './video'
    mode_select()


def mode_select():
    print('請選擇下載模式：')
    print('1.直接輸入YouTube網址下載影片')
    print('2.輸入欲搜尋之關鍵字將會列出相關影片提供下載')
    choice = input('請選擇：')
    if choice == '1':
        mode_1()
    elif choice == '2':
        mode_2()
    else:
        print('請輸入 1 或 2')
        mode_select()


def mode_1():
    global file_size
    video_url = input('YouTube網址：')
    try:
        yt = pytube.YouTube(video_url, on_progress_callback=show_progress_bar)
    except TypeError as e:
        print(e)
        video_continue()
    try:
        mkdir(path)
        print('影片名稱：%s' % yt.title)
        print('下載中...')
        video_type = yt.streams.filter(type='video', subtype='mp4').first()
        file_size = video_type.filesize
        video_type.download(path)
        print('下載完成！！')
        video_continue()
    except pytube.exceptions.RegexMatchError as e:
        print(e)
        print('下載失敗！！')
        video_continue()


def mode_2():
    global file_size
    count = 1
    video_list = []
    url_list = []
    # print('功能尚未開啟！！抱歉')
    kw = input('請輸入關鍵字：')
    # kw = '蠟筆小新'
    url = 'https://www.youtube.com/results?search_query=%s' % kw
    req = requests.get(url)
    soup = bs4(req.content, 'html.parser')
    for all_mv in soup.select(".yt-lockup-video"):
        data = all_mv.select("a[rel='spf-prefetch']")
        video_list.append(data[0].get("title"))
        video_url = 'https://www.youtube.com'
        video_url += data[0].get('href')
        url_list.append(video_url)
        print('%d. %s' % (count, data[0].get("title")))
        count += 1
    choice_video_index = int(input('請選擇欲下載的影片(輸入編號即可)：'))
    choice_video_index -= 1
    video_url = url_list[choice_video_index]
    # , on_progress_callback = show_progress_bar
    try:
        yt = pytube.YouTube(video_url, on_progress_callback=show_progress_bar)
    except TypeError as e:
        print(e)
        video_continue()
    try:
        mkdir(path)
        print('影片名稱：%s' % yt.title)
        print('下載中...')
        video_type = yt.streams.filter(type='video', subtype='mp4').first()
        file_size = video_type.filesize
        video_type.download(path)
        print('下載完成！！')
        video_continue()
    except pytube.exceptions.RegexMatchError as e:
        print(e)
        print('下載失敗！！')
        video_continue()


def mkdir(dir_path):
    folder = os.path.exists(dir_path)
    # 判斷資料夾是否存在，如果不存在即會自動建立
    if not folder:
        print("---建立資料夾中---")
        os.makedirs(path)  # 建立資料夾
        print("---創建OK---")


def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
    print(round((1 - bytes_remaining / file_size) * 100, 1), '% done...')


def video_continue():
    print('是否要繼續下載影片？')
    con = input('輸入Q離開程式，任意鍵繼續下載其他影片')
    if con.upper() == 'Q':
        print('感謝您的使用')
        sys.exit(0)
    else:
        mode_select()


if __name__ == '__main__':
    main()
