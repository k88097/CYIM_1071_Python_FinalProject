## **YouTube影片下載器**

### **_CYIM 107-1 Python程式設計 期末專案_**
組員：

1. **10444133 資管四甲 趙品淵**
2. **10444148 資管四甲 徐子婷**

---

### **使用此程式前，務必閱讀下列說明**

於命令提示字元(CMD)中輸入
``` bash
pip install -r requirements.txt
```
確認相關套件是否安裝成功。  

接著輸入
``` bash
python main.py
```
開始執行程式。

---

## **此程式有分為兩種模式。**

1. 直接輸入**YouTube網址**即可下載影片。
2. 輸入**關鍵字**，下載影片。

---

##  **_模式一_**
使用步驟：

1. 進入程式後，輸入**1**進入到**模式一**。
2. 貼上**YouTube網址**並且按下**Enter**。  
3. 程式會自動判斷指定資料夾是存在，若是不存在則會自動建立。
4. 影片自動下載至指定資料夾。
5. 下載完成。
6. 程式會詢問是否繼續下載或是離開程式。
7. 輸入 **Q** or **q** 離開程式。

---

##  **_模式二_**
使用步驟：

1. 進入程式後，輸入**2**進入到**模式二**。
2. 輸入**關鍵字**，程式會自動搜尋[YouTube](https://www.youtube.com/)上有關此**關鍵字**的影片。
3. 程式列出幾個與輸入的關鍵字相關的影片。
4. 輸入**影片清單編號**即可下載影片。
5. 程式會自動判斷指定資料夾是存在，若是不存在則會自動建立。
6. 影片自動下載至指定資料夾。
7. 下載完成。
8. 程式會詢問是否繼續下載或是離開程式。
9.  輸入 **Q** or **q** 離開程式。

---

## **_Functions說明_**

* ### **mode_select()**
    * 影片下載的模式選擇。  
    * **Return Type:** _None_
* ### **mode_1()**
    * 下載模式一。  
    * **Return Type:** _None_
* ### **mode_2()**
    * 下載模式二。  
    * **Return Type:** _None_
* ### **mkdir(path)**
    * 檢查下載資料夾路徑是否存在，不存在的話將會自動創建。
    * **Parameters**:
        * `path`(_str_)--資料夾路徑 
    * **Return Type:** _None_
* ### **show_progress_bar(stream, chunk, file_handle, bytes_remaining)**
    * 顯示下載進度。
    * **Parameters**:
        * `stream`(_object_)--Stream型態的物件。
        * `chunk`(_str_)--尚未寫進資料的影片二維數據。
        * `file_handle`(_io.BufferedWriter_)--正在處理影片的寫入。
        * `bytes_remaining`(_int_)--尚未下載完成的影片容量(_Bytes_)。           
    * **Return Type:** _None_
* ### **video_continue()**
    * 是否要離開或是繼續下載其他影片。  
    * **Return Type:** _None_

---

## **錯誤報告**

如果執行後得到這串錯誤訊息
```consloe
pytube.exceptions.RegexMatchError: regex pattern (yt\.akamaized\.net/\)\s*\|\|\s*.*?\s*c\s*&&\s*d\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\() had zero matches
```
**解決辦法：**  
修改 **pytube/cipher.py** 中的第 **38**~**43** 行  
**原本：**
```python
pattern = [
        r'yt\.akamaized\.net/\)\s*\|\|\s*'
        r'.*?\s*c\s*&&\s*d\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(',
        r'\.sig\|\|(?P<sig>[a-zA-Z0-9$]+)\(',
        r'\bc\s*&&\s*d\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(',
    ]
```
**修改後：**
```python
pattern = [
        r'\bc\s*&&\s*d\.set\([^,]+,.*?\((?P<sig>[a-zA-Z0-9$]+)\(\(0\s*,\s*window.decodeURIComponent',
        r'yt\.akamaized\.net/\)\s*\|\|\s*'
        r'.*?\s*c\s*&&\s*d\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(',
        r'\.sig\|\|(?P<sig>[a-zA-Z0-9$]+)\(',
        r'\bc\s*&&\s*d\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(',
    ]
```
這樣即可解決錯誤訊息了。
