'''
GUI 的資訊連結與 API 還有詳細說明：

    先幫我下載這個：
    pip install ttkbootstrap

    API 模組：
    https://ttkbootstrap.readthedocs.io/en/latest/api/

    初學使用指南：
    https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/tutorial/#the-traditional-approach

    主題一般預設為 Litera 如果想使用其他主題，可以輸入其他內置主題的名字

    使用 python 版本：3.10.7
'''

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def show_selected_option():
    '''
    顯示下拉式選單所選的選項

    '''
    selected_option = cb.get()
    label.config(text="您所選擇的區域為："+str(selected_option))
    label.pack(pady=20)
    back_button.pack(pady=10)
    hide_homepage()



def go_back():
    '''
    回到原本的主畫面

    '''
    label.pack_forget()
    back_button.pack_forget()
    show_homepage()


# 隱藏首頁的元件
def hide_homepage():
    title_label.pack_forget()
    cb.pack_forget()
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()
    b5.pack_forget()
    b6.pack_forget()
    b7.pack_forget()


# 顯示首頁的元件
def show_homepage():
    title_label.pack(pady=50)
    cb.pack(pady=10)
    b1.pack(pady=10)
    b2.pack(pady=10)
    b3.pack(pady=10)
    b4.pack(pady=10)
    b5.pack(pady=10)
    b6.pack(pady=10)
    b7.pack(pady=10)


root = ttk.Window(themename="minty")
root.title("天氣顯示系統 Weather Display System")
root.geometry("640x650")

# 標題
title_label = ttk.Label(root, text="天氣顯示系統 Weather Display System", font=("microsoft yahei", 18))
title_label.pack(pady=50)


# 縣市下拉式選單
city_options = ["台北市", "新北市", "基隆市", "桃園市", "新竹市", "台中市", "彰化縣", "台南市", "高雄市", "屏東縣", "宜蘭縣", "花蓮縣", "台東縣", "澎湖縣", "金門縣", "連江縣"]
cb = ttk.Combobox(root, bootstyle="secondary", values=city_options)
cb.pack(pady=10)


# 行政區、鄉、鎮
district_options = dict()




# 按鈕
b1 = ttk.Button(root, text="氣候 climate", command=show_selected_option, bootstyle=(PRIMARY,OUTLINE))
b1.pack(pady=10)

b2 = ttk.Button(root, text="預報 forecast", command=show_selected_option, bootstyle=(SECONDARY,OUTLINE))
b2.pack(pady=10)

b3 = ttk.Button(root, text="觀測 observation", command=show_selected_option, bootstyle=(SUCCESS,OUTLINE))
b3.pack(pady=10)

b4 = ttk.Button(root, text="天文 astronomical", command=show_selected_option, bootstyle=(INFO,OUTLINE))
b4.pack(pady=10)

b5 = ttk.Button(root, text="天氣警特報 weather alert", command=show_selected_option, bootstyle=(WARNING,OUTLINE))
b5.pack(pady=10)

b6 = ttk.Button(root, text="數值預報 numerical forecast", command=show_selected_option, bootstyle=(DANGER,OUTLINE))
b6.pack(pady=10)

b7 = ttk.Button(root, text="地震與海嘯 earthquake & tsunami", command=show_selected_option, bootstyle=(DARK,OUTLINE))
b7.pack(pady=10)

back_button = ttk.Button(root, text="回首頁", command=go_back, bootstyle=DARK)
back_button.pack(pady=10)

label = ttk.Label(root, font=("microsoft yahei", 18))

show_homepage()

root.mainloop()