import pytube
import os


def main():
    print('---歡迎使用此程式下載YouTube影片---')
    print('請選擇下載模式：')
    print('1.直接輸入YouTube網址下載影片')
    print('2.輸入欲搜尋之關鍵字將會列出相關影片提供下載')
    choice = mode_select()
    if choice == '1':
        mode_1()
    elif choice == '2':
        mode_2()
    else:
        print('請輸入 1 或 2')
        choice = mode_select()


def mode_select():
    return input('請選擇：')


def mode_1():
    url = input()
    yt = pytube.YouTube(url)
    try:
        mkdir('../videos')
        print('影片名稱：%s' % yt.title)
        print('下載中...')
        yt.streams.filter(type='video', subtype='mp4').first().download('../videos')
        print('下載完成！！')
    except:
        print('下載失敗！！')


def mode_2():
    print('功能尚未開啟！！抱歉')


def mkdir(path):
    folder = os.path.exists(path)

    # 判斷資料夾是否存在，如果不存在即會自動建立
    if not folder:
        print("---建立資料夾中---")
        os.makedirs(path)  # 建立資料夾
        print("---創建OK---")


if __name__ == '__main__':
    main()
