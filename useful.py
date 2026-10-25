'''
Useful Import - 李翊瑜 製作

這是一個多功能 Python 工具箱，提供數學、隨機、時間、特殊效果、Windows 自動化、滑鼠鍵盤控制、螢幕操作、網頁自動化等實用功能。

使用方法：
    import useful      # 假設檔案名為 useful.py
    help("主題")       # 查看特定主題的詳細說明
    help()             # 顯示主選單

主要功能分類（詳細請使用 help("主題名稱")）：

【基礎工具】
    hello()           印出 Hello World
    useful()          印出彩色 Useful 字樣
    elseError(cond, msg)  條件不成立則報錯
    unique(thing)     去除重複元素
    count_proportion(list)  計算佔比

【數學】
    is_prime(n)       判斷質數
    carry_system(num, N, M)  進制轉換
    Fraction(分子, 分母)  分數類別

【隨機】
    choose(src, count, uniq)  隨機抽選
    proba(p)          機率判斷
    random_country(continent, count, uniq)  隨機國家

【時間】
    wait(sec)         延遲
    @during_time      裝飾器：計算函式執行時間
    current_time()    精確計時器
    get_time(format, timezone)  格式化現在時間

【特殊效果】
    special_print(words, color, bg, special)  彩色/特效輸出
    print_special(words, color, bg, special)  另一個彩色/特效輸出
    loadings(list, count, wait)  載入動畫
    gentle_say(word, wait, is_input)  打字機效果
    morse(letter, turn_to_morse)  摩斯密碼轉換
    password(text, key, turn_back)  加密/解密

【Windows 系統 (Win 類別)】
    Win.turn_off_com(sec)      倒數關機
    Win.turn_off_com_mac(sec)  倒數關機（Mac）
    Win.restart_com(sec)       倒數重啟
    Win.restart_com_mac(sec)   倒數重啟（Mac）
    Win.stop_shutdown_com()    取消關機/重啟
    Win.stop_shutdown_com_mac()  取消關機/重啟（Mac）
    Win.stop_task(name, force) 結束程式
    Win.delete_file(path, quiet, force) 刪除檔案
    Win.open(where)            開啟檔案/程式/網頁
    Win.alert(text, title)     彈出對話框
    Win.easy_alert(text)       簡易彈窗
    Win.confirm_alert(text, title) -> 確認/取消對話框
    Win.warn_alert(text, title, is_error) -> 警告/錯誤對話框
    Win.is_running(process)    偵測程式是否執行
    Win.is_running_mac(process)  偵測程式是否執行（Mac）
    Win.make_txt(path, content)  建立文字檔
    Win.read_txt(path)         讀取文字檔
    Win.get_desktop_path()     取得桌面路徑

【滑鼠控制 (Mouse 類別)】
    Mouse.get_where()          取得座標
    Mouse.move_to(x, y, time)  移動到座標
    Mouse.move(dx, dy, time)   相對移動
    Mouse.drag_to(x, y, time)  拖曳
    Mouse.click(button)        點擊
    Mouse.scroll(clicks)       滾動滾輪

【鍵盤控制 (Keyboard 類別)】
    Keyboard.press(keys)       按鍵 (支援組合鍵)
    Keyboard.gentle_write(text, interval)  模擬打字
    Keyboard.push(keys)         按住按鍵
    Keyboard.stop_push(keys)    放開按鍵
    Keyboard.scroll(clicks)    滾動滾輪

【螢幕操作 (Screen 類別)】
    Screen.get_size()          解析度
    Screen.screenshot(path)    截圖
    Screen.find_on_screen(image_path)  尋找圖片位置
    Screen.find_and_click(image_path)  尋找並點擊
    Screen.get_color(x, y)     取得顏色

【幽靈指令 (Ghost_Com 類別)】
    Ghost_Com.random_go(time, times)  隨機移動滑鼠
    Ghost_Com.alt_f4()         送出 Alt+F4 並按 N
    Ghost_Com.alt_f4_mac()     送出 Alt+F4（Mac）
    Ghost_Com.open_txt_and_write(word, sec, with_ghost=True)  開啟 Notepad 並打字
    Ghost_Com.open_txt_and_write_mac(word, sec, with_ghost=True)  開啟 Notepad 並打字（Mac）
    Ghost_Com.search_weird_words()  在 Chrome 開啟奇怪搜尋
    Ghost_Com.search_weird_words_mac()  在 Chrome 開啟奇怪搜尋（Mac）
    Ghost_Com.blue_screen()  嘗試藍屏（危險）
    Ghost_Com.fake_blue_screen()  假裝藍屏（安全）
    Ghost_Com.fake_turn_off(sec)  假裝關機後取消
    Ghost_Com.fake_turn_off_mac(sec)  假裝關機後取消（Mac）
    Ghost_Com.crazy_mouse(sec, with_click=False)  讓滑鼠瘋狂亂動
    Ghost_Com.lock_com()  鎖定電腦
    Ghost_Com.lock_com_mac()  鎖定電腦（Mac）
    Ghost_Com.random_scroll(times)  隨機滾動滑鼠滾輪
    Ghost_Com.type_weird_sentence()  當前焦點輸入奇怪句子
    Ghost_Com.random_click_around(times)  隨機在螢幕上點擊
    Ghost_Com.open_calc_and_mess()  打開計算機並亂輸入
    Ghost_Com.open_calc_and_mess_mac()  打開計算機並亂輸入（Mac）
    Ghost_Com.spam_typing(times, sec)  連續打字
    Ghost_Com.random_keyboard_press(times)  隨機按鍵亂打
    Ghost_Com.open_multiple_tabs(count)  開多個 Chrome 搜尋分頁
    Ghost_Com.open_notepad_spam(count, sec)  連續開 Notepad 並打字
    Ghost_Com.a_lot_alerts(times)  連續彈出警告對話框
    Ghost_Com.a_lot_cmd(times)  連續開命令提示字元
    Ghost_Com.a_lot_cmd_mac(times)  連續開命令提示字元（Mac）

【網頁自動化 (web 類別)】需安裝 selenium
    web.connect()              連接到 Chrome
    web.open(url)              開啟網址
    web.find_by(by, value)     尋找元素
    web.click(element)         點擊元素
    web.key(element, word)     輸入文字
    web.get_html()             取得原始碼
    web.close_all()            關閉瀏覽器

更多說明請在 Python 互動環境中輸入 help() 或 help("主題")。
'''

from __future__ import annotations
import random
import time
import subprocess
from typing import Any, Iterable
from random import randint
from datetime import datetime, timedelta, timezone
from pathlib import Path
import os
import pyautogui
import sys
import pyperclip
from urllib.parse import quote_plus
import tkinter as tk
from tkinter import messagebox
import platform
import subprocess
import types
import math
import socket
import io
from PIL import Image

# 告訴各位本import

def help(topic: str | None = None):
    '''提供使用說明，輸入主題名稱可以查看詳細說明，不輸入則顯示主選單
    主題包含: math, random, time, special, os, web, mouse, keyboard, screen, ghost
    '''
    # ANSI 顏色 (深色模式友善)
    C = "\x1b[36m"   # 青色：標題
    Y = "\x1b[33m"   # 黃色：強調
    G = "\x1b[32m"   # 綠色：函式名稱
    R = "\x1b[31m"   # 紅色：錯誤
    RESET = "\x1b[0m"

    if topic is not None:
        os.system('cls')  # 清空畫面
        print(f"{C}=== Useful Help: {Y}{topic.upper()}{C} ==={RESET}")

        if topic == "math":
            print(f"{G}is_prime{RESET}(num) -> 判斷是否為質數")
            print(f"{G}carry_system{RESET}(num, N, M) -> N進制轉M進制")
            print(f"{G}Fraction{RESET}(分子, 分母) -> 分數類別（支援加減乘除）")

        elif topic == "random":
            print(f"{G}choose{RESET}(src, count, uniq) -> 隨機抽選")
            print(f"{G}proba{RESET}(probability) -> 機率回傳 True/False")
            print(f"{G}random_country{RESET}(continent, count, uniq) -> 隨機國家")
            print(f"{G}unique{RESET}(thing) -> 去除重複元素")
            print(f"{G}count_proportion{RESET}(list, low, high, round) -> 計算佔比")

        elif topic == "time":
            print(f"{G}wait{RESET}(sec) -> 暫停秒數")
            print(f"{G}@during_time{RESET} -> 裝飾器：計算函式執行時間")
            print(f"{G}current_time{RESET}() -> 獲取精確計數器")
            print(f"{G}get_time{RESET}(format, timezone) -> 格式化現在時間")

        elif topic == "special":
            print(f"{G}special_print{RESET}(words, color, bg, special) -> 彩色印出")
            print(f"{G}print_special{RESET}(words, color, bg, special) -> 另一個彩色印出")
            print(f"{G}loadings{RESET}(iterable, count, wait) -> 載入動畫")
            print(f"{G}gentle_say{RESET}(word, wait, is_input) -> 打字機效果")
            print(f"{G}morse{RESET}(letter, turn_to_morse) -> 摩斯密碼轉換")
            print(f"{G}password{RESET}(text, key, turn_back) -> 加密/解密")

        elif topic == "os":
            print(f"{G}Win.turn_off_com{RESET}(sec) -> 倒數關機")
            print(f"{G}Win.turn_off_com_mac{RESET}(sec) -> 倒數關機（Mac）")
            print(f"{G}Win.restart_com{RESET}(sec) -> 倒數重啟")
            print(f"{G}Win.restart_com_mac{RESET}(sec) -> 倒數重啟（Mac）")
            print(f"{G}Win.stop_shutdown_com{RESET}() -> 取消電源排程")
            print(f"{G}Win.stop_shutdown_com_mac{RESET}() -> 取消電源排程（Mac）")
            print(f"{G}Win.stop_task{RESET}(name, force) -> 結束程序")
            print(f"{G}Win.delete_file{RESET}(path, quiet, force) -> 刪除檔案")
            print(f"{G}Win.open{RESET}(where) -> 開啟檔案/網頁/程式")
            print(f"{G}Win.alert{RESET}(text, title) -> 視窗彈窗")
            print(f"{G}Win.easy_alert{RESET}(text) -> 簡易彈窗")
            print(f"{G}Win.confirm_alert{RESET}(text, title) -> 確認/取消對話框")
            print(f"{G}Win.warn_alert{RESET}(text, title, is_error) -> 警告/錯誤對話框")
            print(f"{G}Win.is_running{RESET}(process_name) -> 偵測程式是否執行")
            print(f"{G}Win.is_running_mac{RESET}(process_name) -> 偵測程式是否執行（Mac）")
            print(f"{G}Win.make_txt{RESET}(file_path, content) -> 建立 txt 檔案")
            print(f"{G}Win.read_txt{RESET}(file_path) -> 讀取 txt 檔案")
            print(f"{G}Win.get_desktop_path{RESET}() -> 取得桌面路徑")

        elif topic == "web":
            print(f"{G}web.connect{RESET}() -> 連接到 Chrome 瀏覽器")
            print(f"{G}web.open{RESET}(url) -> 開啟網址")
            print(f"{G}web.close_all{RESET}() -> 關閉瀏覽器")
            print(f"{G}web.find_by{RESET}(by, value) -> 尋找元素 (id/name/class_name/...)" )
            print(f"{G}web.click{RESET}(element) / {G}key{RESET}(element, word) -> 操作元素")
            print(f"{G}web.get_html{RESET}() / {G}get_text{RESET}(element) -> 取得內容")

        elif topic == "mouse":
            print(f"{G}Mouse.get_where{RESET}() -> 取得滑鼠座標")
            print(f"{G}Mouse.move_to{RESET}(x, y, time) / {G}move{RESET}(dx, dy, time)")
            print(f"{G}Mouse.drag_to{RESET}(x, y, time) / {G}click{RESET}(button)")

        elif topic == "keyboard":
            print(f"{G}Keyboard.press{RESET}(keys) -> 按鍵 (支援組合鍵)")
            print(f"{G}Keyboard.gentle_write{RESET}(text, each_wait) -> 模擬打字")
            print(f"{G}Keyboard.push{RESET}(keys) -> 按住按鍵")
            print(f"{G}Keyboard.stop_push{RESET}(keys) -> 放開按鍵")
            print(f"{G}Keyboard.scroll{RESET}(clicks) -> 滾動滾輪")

        elif topic == "screen":
            print(f"{G}Screen.get_size{RESET}() -> 螢幕解析度")
            print(f"{G}Screen.screenshot{RESET}(path) -> 截圖")
            print(f"{G}Screen.find_on_screen{RESET}(image_path) -> 尋找圖片位置")
            print(f"{G}Screen.find_and_click{RESET}(image_path) -> 尋找並點擊")
            print(f"{G}Screen.get_color{RESET}(x, y) -> 取得像素顏色")

        elif topic == "ghost":
            print(f"{G}Ghost_Com.random_go{RESET}(time, times) -> 隨機移動滑鼠")
            print(f"{G}Ghost_Com.alt_f4{RESET}() -> 送出 Alt+F4 並按 N 取消儲存")
            print(f"{G}Ghost_Com.alt_f4_mac{RESET}() -> 送出 Alt+F4（Mac）")
            print(f"{G}Ghost_Com.open_txt_and_write{RESET}(word, sec, with_ghost=True) -> 開啟 Notepad 並打字")
            print(f"{G}Ghost_Com.open_txt_and_write_mac{RESET}(word, sec, with_ghost=True) -> 開啟 Notepad 並打字（Mac）")
            print(f"{G}Ghost_Com.search_weird_words{RESET}() -> 在 Chrome 開啟奇怪搜尋")
            print(f"{G}Ghost_Com.search_weird_words_mac{RESET}() -> 在 Chrome 開啟奇怪搜尋（Mac）")
            print(f"{G}Ghost_Com.blue_screen{RESET}() -> 嘗試藍屏（危險）")
            print(f"{G}Ghost_Com.fake_blue_screen{RESET}() -> 假裝藍屏（安全）")
            print(f"{G}Ghost_Com.fake_turn_off{RESET}(sec) -> 假裝關機後取消")
            print(f"{G}Ghost_Com.fake_turn_off_mac{RESET}(sec) -> 假裝關機後取消（Mac）")
            print(f"{G}Ghost_Com.crazy_mouse{RESET}(sec, with_click=False) -> 讓滑鼠瘋狂亂動")
            print(f"{G}Ghost_Com.lock_com{RESET}() -> 鎖定電腦")
            print(f"{G}Ghost_Com.lock_com_mac{RESET}() -> 鎖定電腦（Mac）")
            print(f"{G}Ghost_Com.random_scroll{RESET}(times) -> 隨機滾動滑鼠滾輪")
            print(f"{G}Ghost_Com.type_weird_sentence{RESET}() -> 當前焦點輸入奇怪句子")
            print(f"{G}Ghost_Com.random_click_around{RESET}(times) -> 隨機在螢幕上點擊")
            print(f"{G}Ghost_Com.open_calc_and_mess{RESET}() -> 打開計算機並亂輸入")
            print(f"{G}Ghost_Com.open_calc_and_mess_mac{RESET}() -> 打開計算機並亂輸入（Mac）")
            print(f"{G}Ghost_Com.spam_typing{RESET}(times, sec) -> 目前焦點處連續打字")
            print(f"{G}Ghost_Com.random_keyboard_press{RESET}(times) -> 隨機按鍵，鍵盤會亂打")
            print(f"{G}Ghost_Com.open_multiple_tabs{RESET}(count) -> 打開多個 Chrome 分頁")
            print(f"{G}Ghost_Com.open_notepad_spam{RESET}(count, sec) -> 連續開 Notepad 並打字")
            print(f"{G}Ghost_Com.a_lot_alerts{RESET}(times) -> 連續彈出警告對話框")
            print(f"{G}Ghost_Com.a_lot_cmd{RESET}(times) -> 連續開命令提示字元")
            print(f"{G}Ghost_Com.a_lot_cmd_mac{RESET}(times) -> 連續開命令提示字元（Mac）")

        else:
            raise SomethingError(f"{R}沒有這個主題：{topic}{RESET}")

        print(f"\n{C}------------------------------{RESET}")
        return

    # ==================== 主選單 (topic 為 None) ====================
    print(f"""
{C}╔══════════════════════════════════════════════════════════════╗
║ {Y}Useful Import{RESET}{C} - 您的多功能 Python 工具箱                     ║
║ {C}Maker: {Y}李翊瑜 {C}                                               ║
╚══════════════════════════════════════════════════════════════╝{RESET}

{Y}💡 使用提示：{RESET} 輸入 {G}help("主題名稱"){RESET} 查看詳細說明
主題包含: {C}math{RESET}, {C}random{RESET}, {C}time{RESET}, {C}special{RESET}, {C}os{RESET},
          {C}web{RESET}, {C}mouse{RESET}, {C}keyboard{RESET}, {C}screen{RESET}, {C}ghost{RESET}

{C}──────────────────────────────────────────────────────────────{RESET}
{Y}[ 快速功能清單 ]{RESET}  (詳細用法請查閱各主題)

{G}● 基礎工具{RESET}
  {G}hello(){RESET} | {G}useful(){RESET} | {G}elseError{RESET}(cond, msg) | {G}unique{RESET}(thing)

{G}● 數學與邏輯{RESET}
  {G}is_prime{RESET} | {G}carry_system{RESET} | {G}Fraction{RESET} | {G}count_proportion{RESET}

{G}● 隨機與國家{RESET}
  {G}choose{RESET} | {G}proba{RESET} | {G}random_country{RESET}

{G}● 時間與裝飾器{RESET}
  {G}get_time{RESET} | {G}@during_time{RESET} | {G}current_time{RESET}

{G}● 特殊效果{RESET}
  {G}special_print{RESET} | {G}loadings{RESET} | {G}gentle_say{RESET} | {G}morse{RESET} | {G}password{RESET}

{G}● Windows 自動化 (Win 類別){RESET}
  {G}Win.turn_off_com{RESET} | {G}Win.stop_task{RESET} | {G}Win.open{RESET} | {G}Win.alert{RESET}
  {G}Win.is_running{RESET} | {G}Win.make_txt{RESET} | {G}Win.get_desktop_path{RESET}

{G}● 瀏覽器自動化 (web 類別){RESET}
  {G}web.connect{RESET} → {G}web.open{RESET} → {G}web.find_by{RESET} → {G}web.click{RESET}

{G}● 滑鼠／鍵盤／螢幕 (Mouse, Keyboard, Screen){RESET}
  {G}Mouse.get_where{RESET} | {G}Keyboard.press{RESET} | {G}Screen.screenshot{RESET}

{G}● 幽靈指令 (Ghost_Com){RESET}
  {G}Ghost_Com.random_go{RESET} | {G}Ghost_Com.alt_f4{RESET} | {G}Ghost_Com.random_keyboard_press{RESET}
  {G}Ghost_Com.open_multiple_tabs{RESET} | {G}Ghost_Com.open_notepad_spam{RESET} | {G}Ghost_Com.spam_typing{RESET}
{C}──────────────────────────────────────────────────────────────{RESET}
    """)

#Useful
def useful():
    """印出美麗的useful"""
    for i in "It's an import that is very very Useful!":
        print(f"\x1b[{random.randint(30,36)}m{i}\x1b[0m",end="")
    print()
# Hello World
def hello():
    """印出 'Hello World!'"""
    print("Hello world!")
# 特殊印出
ansi_colors = {
    #大部分
    #special
    "重置": 0,
    "粗體": 1,
    "淡化": 2,
    "斜體": 3,
    "底線": 4,
    "閃爍": 5,
    "反白": 7,
    "隱藏": 8,
    "刪除線": 9,
    #word_color
    "黑色字": 30,
    "紅色字": 31,
    "綠色字": 32,
    "黃色字": 33,
    "藍色字": 34,
    "洋紅色字": 35,
    "青色字": 36,
    "白色字": 37,
    #background_color
    "黑色底": 40,
    "紅色底": 41,
    "綠色底": 42,
    "黃色底": 43,
    "藍色底": 44,
    "洋紅色底": 45,
    "青色底": 46,
    "白色底": 47
}
def special_print(words:str,word_color:str|int=0,background_color:str|int=0,special:str|int|None=None) -> None:
    """可以印出特別樣式的文字，請依據以下字典輸入
    ```
    {
        #大部分
        #word_color
        "黑色字": 30,
        "紅色字": 31,
        "綠色字": 32,
        "黃色字": 33,
        "藍色字": 34,
        "洋紅色字": 35,
        "青色字": 36,
        "白色字": 37,

        #background_color
        "黑色底": 40,
        "紅色底": 41,
        "綠色底": 42,
        "黃色底": 43,
        "藍色底": 44,
        "洋紅色底": 45,
        "青色底": 46,
        "白色底": 47,

        #special
        "重置": 0,
        "粗體": 1,
        "淡化": 2,
        "斜體": 3,
        "底線": 4,
        "閃爍": 5,
        "反白": 7,
        "隱藏": 8,
        "刪除線": 9,
        "無",None
    }"""
    #特效
    if not isinstance(special,int):
        if special in ansi_colors:
            Special=ansi_colors[special] # type: ignore #把文字經字典變數字
        elif special is None:
            Special=None # type: ignore
        else:
            raise SomethingError("該特效不存在")
    elif special>9 or special<0:
        raise SomethingError("該特效不存在")
    #顏色
    if not isinstance(word_color,int):
        if word_color in ansi_colors:
            word_color=ansi_colors[word_color] #把文字經字典變數字
        else:
            raise SomethingError("該顏色不存在")
    elif word_color>108 or word_color<0:
        raise SomethingError("該顏色不存在")
    #底色
    if not isinstance(background_color,int):
        if background_color in ansi_colors:
            background_color=ansi_colors[background_color] #把文字經字典變數字
        else:
            raise SomethingError("該底色不存在")
    elif background_color>108 or background_color<0:
        raise SomethingError("該底色不存在")
    if special is None:
        print(f"\x1b[{word_color};{background_color}m{words}\x1b[0m")
    else:
        print(f"\x1b[{special};{word_color};{background_color}m{words}\x1b[0m")


# 自訂Error
class SomethingError(Exception):pass
# 不成立則報錯
def elseError(cond:bool,message:str="Something Error"):
    """cond中輸入條件
    條件若 不成立 則報出SomethingError(message)"""
    if not cond:
        raise SomethingError(message)


#     休閒寫程式區的
def unique(thing):
    '''可以把一個東西裡面重複的東西刪掉，回傳一個不重複的東西
    thing可以是list,tuple,set,dict,str'''
    Type=type(thing)
    if Type in (set,dict):
        finish=thing
    elif Type in (list,tuple,str):
        finish=[]
        for i in thing:
            if not i in finish: finish.append(i)
        finish="".join(finish) if Type==str else Type(finish)
    else:
        raise ValueError(f"本型別({Type})不適用unique函式")
    return finish

def count_proportion(thing:list,return_low:int=0,return_high:int=100,Round:int=2):
    '''從 return_low ~ return_high 取值做為佔比(預設為0~100)
    會回傳一個dict，內容：
    {值1:佔比1,值2,佔比2...}

    ex:
    count_proportion([0,"2","3","3",0]) -> {0:40.00,"2":20.00,"3":40.00}
    count_proportion([0,"2","3","3",0],Round=0) -> {0:40,"2":20,"3":40}
    count_proportion([0,"2","3","3",0],10,60) -> {0:30,"2":20,"3":30}'''
    assert isinstance(thing,list),"thing型別錯誤"
    assert len(thing)!=0,"thing不能是空的"
    assert all(isinstance(i,int) for i in (return_high,return_low,Round)),"型別錯誤"
    assert return_high > return_low,"return_low 不能大於或等於 return_high"
    how_many_dict={}
    for i in thing:
        if i not in how_many_dict:
            how_many_dict[i]=0
        how_many_dict[i]+=1
    total=len(thing)
    finish={}
    for i in how_many_dict.keys():
        finish[i]=round(
         (how_many_dict[i]/total)#算出佔比(小數)
         *(return_high-return_low)#變成應有格式
         + return_low#加上最小值
         ,Round)
    return finish

#               MATH

# 是否為質數
def is_prime(num:int) ->bool:
    '''回傳num是否為質數'''
    if num<2:
        return False
    for i in range(2,int(num**(1/2))+1):
        #持續往上除，除到自己的根號
        #若有整除則回傳False
        if (num % i)==0:
            return False
    #否則True
    return True
# N轉M進制
def carry_system(num_before:str|int, carry_system_before:int=10, carry_system_after:int=2) -> str:
    """可以把一個 N 進制的 num
    轉為 M 進制數字(最多只能計算至36進制)"""
    #先改為10進制
    number=int(str(num_before),carry_system_before) #python本身就有
    #再更改為其他進制
    letter=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    num_after=[]
    while not number==0:
        num_after.append(letter[number % carry_system_after]) # type: ignore
        number= number // carry_system_after
    num_after.reverse() #翻轉
    num_after="".join(num_after) # type: ignore #把M整個塞進去一個str
    return num_after


#               RANDOM

#抽選
def choose(src, count:int=1, uniq:bool=True) ->object:
    '''
    在 src 中隨機選東西，可以選多個也可以不重複。
    count 是選幾個，uniq 是是否重複。
    選一個時直接回傳，否則回傳 list。
    '''
    if not uniq:
        return random.choices(src,k=count)
    else:
        return random.sample(src,k=count)
#運氣
def proba(probability:float) -> bool:
    """輸入機率(例如50%是0.5)，如果抽到就會回傳True"""
    if random.random()<=probability:
        return True
    else:
        return False
#隨機國家
class country:
    asia = (
    "台灣","中國", "日本", "韓國", "印度", "印尼", "泰國", "越南", "菲律賓", "馬來西亞",
    "新加坡", "孟加拉", "巴基斯坦", "斯里蘭卡", "阿聯酋", "沙烏地阿拉伯", "以色列",
    "土耳其", "伊朗", "哈薩克", "蒙古", "柬埔寨", "老撾", "尼泊爾", "緬甸"
    )
    europe = (
        "英國", "法國", "德國", "義大利", "西班牙", "俄羅斯", "荷蘭", "比利時",
        "瑞典", "挪威", "丹麥", "芬蘭", "波蘭", "葡萄牙", "希臘", "捷克", "奧地利",
        "瑞士", "愛爾蘭", "匈牙利", "羅馬尼亞", "保加利亞"
    )
    north_america = (
        "美國", "加拿大", "墨西哥", "古巴", "牙買加", "巴拿馬", "多明尼加", "海地"
    )
    south_america = (
        "巴西", "阿根廷", "哥倫比亞", "智利", "秘魯", "委內瑞拉", "厄瓜多爾", "烏拉圭", "玻利維亞"
    )
    africa = (
        "南非", "埃及", "奈及利亞", "肯亞", "衣索比亞", "迦納", "摩洛哥", "突尼西亞", "坦尚尼亞",
        "安哥拉", "贊比亞", "烏干達", "塞內加爾"
    )
    oceania = (
        "澳大利亞", "紐西蘭", "巴布亞紐幾內亞", "斐濟", "薩摩亞", "湯加", "密克羅尼西亞"
    )
    all=asia+europe+north_america+south_america+africa+oceania
    continent_chi_eng={
        "亞洲":asia,
        "北美洲":north_america,
        "美洲":north_america,
        "南美洲":south_america,
        "歐洲":europe,
        "大洋洲":oceania,
        "澳洲":oceania,
        "Asia":asia,
        "North America":north_america,
        "South America":south_america,
        "Europe":europe,
        "Oceania":oceania,
        "all":all
    }
def random_country(continent:str="all",count:int=1,uniq:bool=False):
    """從大部分國家中隨機抽取一個國家，可以選特定一個洲
    洲：亞洲、北美洲、南美洲、歐洲、大洋洲、澳洲
    (寫英文記得首字母大寫)"""
    return choose(country.continent_chi_eng[continent],count,uniq)


#               TIME


#等
def wait(sec:int|float):
    """等 sec 秒"""
    time.sleep(sec)
#計時並印出
def during_time(func):
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs) # 執行並拿到回傳值
        end = time.perf_counter()
        print(f"耗時: {end-start} 秒")
        return result # 記得把原函式的結果傳回去
    return wrap
#精確時間
def current_time():
    return time.perf_counter()
#人話時間
def get_time(format:str="%Y年%m月%d日%A %H:%M:%S",Timezone:int=8) ->str:
    """回傳現在的時間(人讀得懂的那種)
    format中要填寫(在str中)(放著有就可以了)
    %Y->年分 %y->年分後2位 %m->月份 %d->日
    %H->幾點 %M->幾分 %S->幾秒
    %A->週幾英文 %a->週幾英文縮寫 %B->月份英文 %b->月份縮寫
    Timezone中輸入時區，預設為台灣的+8時區
    就可以得到他對應的結果"""
    tz = timezone(timedelta(hours=Timezone))  # 台灣是 UTC+8
    now = datetime.now(tz)
    return str(now.strftime(format))


#               SPECIAL

#印出
def print_special(words:str,word_color:int=0,background_color:int=0,special:int|None=None) -> None:
    """可以印出特別樣式的文字，請依據以下字典輸入
    ansi_colors = {
        #大部分
        #word_color
        "黑色字": 30,
        "紅色字": 31,
        "綠色字": 32,
        "黃色字": 33,
        "藍色字": 34,
        "洋紅色字": 35,
        "青色字": 36,
        "白色字": 37,

        #background_color
        "黑色底": 40,
        "紅色底": 41,
        "綠色底": 42,
        "黃色底": 43,
        "藍色底": 44,
        "洋紅色底": 45,
        "青色底": 46,
        "白色底": 47,

        #special
        "重置": 0,
        "粗體": 1,
        "淡化": 2,
        "斜體": 3,
        "底線": 4,
        "閃爍": 5,
        "反白": 7,
        "隱藏": 8,
        "刪除線": 9,
        "無",None
    }"""

    #特效
    if not isinstance(special,int):
        if special in ansi_colors:
            Special=ansi_colors[special] #把文字經字典變數字
        else:
            raise SomethingError("該特效不存在")
    elif special==None:
        Special=None
    elif special>9 or special<0:
        raise SomethingError("該特效不存在")
    #顏色
    if not isinstance(word_color,int):
        if word_color in ansi_colors:
            word_color=ansi_colors[word_color] #把文字經字典變數字
        else:
            raise SomethingError("該顏色不存在")
    elif word_color>108 or word_color<0:
        raise SomethingError("該顏色不存在")
    #底色
    if not isinstance(background_color,int):
        if background_color in ansi_colors:
            background_color=ansi_colors[background_color] #把文字經字典變數字
        else:
            raise SomethingError("該底色不存在")
    elif background_color>108 or background_color<0:
        raise SomethingError("該底色不存在")
    if special is None:
        print(f"\x1b[{word_color};{background_color}m{words}\x1b[0m")
    else:
        print(f"\x1b[{special};{word_color};{background_color}m{words}\x1b[0m")

# loading圖示
default_loading=[
    "loading------",
    "-loading-----",
    "--loading----",
    "---loading---",
    "----loading--",
    "-----loading-",
    "------loading",
    "-----loading-",
    "----loading--",
    "---loading---",
    "--loading----",
    "-loading-----"]
def loadings(be_printed:list|None=default_loading,count:int|None=1,each_wait:float=0.3):
    """會印出一個東西，他會直到次數結束會依次變成list中物品
    times是要重覆繞幾次，若為None就會永遠不停止到世界毀滅
    each_wait是每變一次要等多久(至少為0.3)
    若輸入東西不和法會改為default值"""
    if not isinstance(be_printed,list):
        be_printed=default_loading
    if count is not None and not isinstance(count, int):
        count=1
    elif isinstance(count,int) and count<1:
        count=1
    if not isinstance(each_wait,(int,float)):
        each_wait=0.3
    elif each_wait<0.3:
        each_wait=0.3
    print("",end="")
    time.sleep(0.2)
    if not count == None:
        for _ in range(count):
            for i in be_printed:
                print("\r"+str(i),end="")
                time.sleep(each_wait)
        print("\r",end="")
    else:
        raise SomethingError("當然不能讓你這樣耗")
#慢印(很像說話)
def gentle_say(word:str, each_wait:int|float=0.25, is_input:bool=False) -> None|str:
    '''word是要印出的東西，
    each_wait要輸入每印一個字要等幾秒(default=0.25)，
    is_input可以改成input而非print'''
    for i in word:
        print(i,end="")
        time.sleep(each_wait)
    if is_input:
        user_answer=input("")
        return user_answer
    else:
        print()
#摩斯密碼
class Morse:
    become= {
        "A": "01",    "B": "1000",  "C": "1010",  "D": "100",   "E": "0",
        "F": "0010",  "G": "110",   "H": "0000",  "I": "00",    "J": "0111",
        "K": "101",   "L": "0100",  "M": "11",    "N": "10",    "O": "111",
        "P": "0110",  "Q": "1101",  "R": "010",   "S": "000",   "T": "1",
        "U": "001",   "V": "0001",  "W": "011",   "X": "1001",  "Y": "1011",
        "Z": "1100",
        "0": "11111", "1": "01111", "2": "00111", "3": "00011", "4": "00001",
        "5": "00000", "6": "10000", "7": "11000", "8": "11100", "9": "11110",
        " ":"000000", "!":"000001", "@":"000010", "#":"000011", "$":"000100",
        "%":"000101", "^":"000110", "&":"000111", "*":"001000", "(":"001001",
        ")":"001010", "-":"001011", "_":"001100", "+":"001101", "=":"001110",
        "[":"001111", "]":"010000", "{":"010001", "}":"010010",
        "|":"010011","\\":"010100", "/":"010101", "<":"010110", ">":"011000",
        ",":"011001", ".":"011010", "?":"011011","\"":"011100","\'":"011101",
        "~":"011110", "`":"011111", ":":"100000"}
    back= {
        "01": "A",    "1000": "B",   "1010": "C",   "100":"D",     "0":"E",
        "0010": "F",     "110": "G",   "0000": "H",    "00":"I",  "0111":"J",
        "101": "K",    "0100": "L",     "11": "M",    "10":"N",   "111":"O",
        "0110": "P",    "1101": "Q",    "010": "R",   "000":"S",     "1":"T",
        "001": "U",    "0001": "V",    "011": "W",  "1001":"X",  "1011":"Y",
        "1100": "Z",
        "11111":"0",   "01111" : "1",  "00111": "2",  "00011":"3", "00001":"4",
        "00000": "5",  "10000" : "6",  "11000": "7",  "11100":"8", "11110":"9",
        "000000": " ", "000001": "!", "000010": "@", "000011": "#", "000100": "$",
        "000101": "%", "000110": "^", "000111": "&", "001000": "*", "001001": "(",
        "001010": ")", "001011": "-", "001100": "_", "001101": "+", "001110": "=",
        "001111": "[", "010000": "]", "010001": "{", "010010": "}",
        "010011": "|", "010100": "\\","010101": "/", "010110": "<", "011000": ">",
        "011001": ",", "011010": ".", "011011": "?", "011100": "\"", "011101": "'",
        "011110": "~", "011111": "`", "100000": ":"}
def morse(letter:str|list,turn_to_morse:bool) -> str|list:
    """
    letter輸入你要轉換的字(如果是摩斯文字要輸入在一個list中)
    (否則千萬輸入於str中)
    turn_to_morse要輸入是否為轉成摩斯電碼
    True:轉成摩斯電碼 False:摩斯電碼轉成文字
    0是短音，1是長音
    useful->['001', '000', '0', '0010', '001', '0100']
    """
    l=len(letter)
    become_letter=[]
    for a_letter in letter:
        if turn_to_morse:
            a_letter=a_letter.upper()
            if a_letter in Morse.become:
                become_letter.append(Morse.become[a_letter])
            else:
                become_letter.append(a_letter)
        else:
            if a_letter in Morse.back:
                become_letter.append(Morse.back[a_letter])
            else:
                become_letter.append(a_letter)
    try:
        int("".join(become_letter)) #確認是否全為數字
    except ValueError:
        return "".join(become_letter)
    return become_letter

def password(to_change:str|int,key:list[int]|None=None,turn_back:bool|None=None) -> dict[str,str|list]|str:
    '''
    轉成密碼，key若是None會隨機配給(若是要解密則不可以為None)
    turn_back是 是否為解密(預設為None是自動偵測)
    若字數較大，建議將次方數設為2的次方數(如2,4,8...)避免巨大誤差
    
    key=[
        次方數,
        乘數,
        凱薩加數,
        額外更換位,
        額外更換數
    ]

    算法：
    
    0.輸入N
    1.把 **N** 摩斯化
    2.將 **N** 以"2"分別隔開，首尾均有"2"
    3.把 **N** 從3進位轉為10進位
    4.使 **N** 加上 **次方數** 的 **次方數** 次方
    5.讓 **N** 乘以 **乘數**
    6.把 **N** 的每個數依序 + **凱薩加數** 後 取10餘數
    7.在 **N** 的索引中，找到 **額外更換位** 的倍數，每個依凱薩方法額外 + **額外更換數**

    '''
    to_change=str(to_change)
    if turn_back is None:
        try:
            int(to_change)
            turn_back=True
        except:
            turn_back=False

    if not turn_back:
        with_key= key is not None
        if not with_key:
            key=[random.randint(1,40)]
        if len(key)!=5:
            for _ in range(5):
                key.append(random.randint(1,5))
            key=(key+[0]*5)[:5]

        for i in range(5):
            if key[i]<=0:
                key[i]=random.randint(1,5)

        end=morse(to_change,True)
        end="2"+"2".join(end)+"2"
        end = str((int(end,3)+key[0]**key[0]) *key[1])
        end1=""
        for i in end:
            end1+= str((int(i)+key[2])%10)
        end2=""
        for i in range(len(end1)):
            if i%key[3]==0:
                end2+= str((int(end1[i])+key[4])%10)
            else:
                end2+= end1[i]
        if with_key:
            return end2
        else:
            return {
                "password":end2,
                "key":key
            }
    else:
        if key is None: raise ValueError("你要解碼就得給我key")
        if len(key)!=5: raise ValueError("key不正確")

        end=""
        for i in range(len(to_change)):
            if i%key[3]==0:
                end+= str((int(to_change[i])-key[4]+10)%10)
            else:
                end+= to_change[i]
        end1=""
        for i in end:
            end1+= str((int(i)-key[2]+10)%10)
        end1=int((int(end1)//key[1])-key[0]**key[0])
        end1=carry_system(end1,10,3)
        end1 = end1.strip('2').split('2')
        return morse(end1,False) #type:ignore

class Win:
    # @staticmethod是不用Win.就可以直接用裡面的函式
    @staticmethod
    def turn_off_com(in_how_many_seconds:int=30):
        """在 in_how_many_seconds 秒後關機，預設為0秒"""
        if platform.system()=="Windows":
            os.system(f"shutdown /s /t {in_how_many_seconds}")
        else:
            minutes=in_how_many_seconds//60
            subprocess.run(["sudo", "shutdown", "-h", f"+{minutes}"])
    @staticmethod
    def restart_com(in_how_many_seconds:int=30):
        """在 in_how_many_seconds 秒後重啟，預設為0秒"""
        if platform.system()=="Windows":
            os.system(f"shutdown /r /t {in_how_many_seconds}")
        else:
            minutes=in_how_many_seconds//60
            subprocess.run(["sudo", "shutdown", "-r", f"+{minutes}"])
    @staticmethod
    def stop_shutdown_com():
        """取消關機/重啟"""
        if platform.system()=="Windows":
            os.system("shutdown /a")
        else:
            subprocess.run(["sudo", "killall", "shutdown"])

    @staticmethod
    def stop_task(task_name:str,force:bool=True):
        """結束一個程式
        task_name是程式名稱(例如chrome.exe)
        force是是否強制結束(預設為True)"""
        # 使用 subprocess 執行關閉指令，不再跳出黑色視窗
        args = ["taskkill"]
        if force: args.append("/f")
        args.extend(["/im", task_name])
        # creationflags=0x08000000 是一個魔法參數，代表「隱藏視窗」
        subprocess.run(args, shell=True, creationflags=0x08000000)

    @staticmethod
    def delete_file(file_path:str,quiet:bool=True,force:bool=True):
        """刪除一個檔案
        file_path是檔案路徑(例如C:\\Users\\User\\Desktop\\file.txt)
        quiet是是否安靜模式(預設為True)，force是是否強制刪除(預設為True)"""
        to_add=""
        if quiet: to_add+=" /q"
        if force: to_add+=" /f"
        os.system(f"del {to_add} {file_path}")

    @staticmethod
    def open(where:str):
        '''跨平台開啟檔案/應用程式'''
        if platform.system() == "Windows":
            os.system(f'start "" "{where}"')
        elif platform.system() == "Darwin":
            subprocess.run(["open", "-a", where])
        else:
            raise SomethingError("不支援的作業系統")

    @staticmethod
    def alert(text: str, title: str = "系統通知"):
        '''在 Windows 上彈出一個標準對話框，顯示指定的文字和標題'''
        # 這是一行叫 Windows 彈出標準對話框的指令
        command = f'powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show(\'{text}\', \'{title}\')"'
        os.system(command)
    @staticmethod
    def easy_alert(text:str):
        '''在 Windows 上彈出一個標準對話框，顯示指定的文字和標題(簡易版，沒有title)'''
        os.system(f"msg * {text}")
    @staticmethod
    def confirm_alert(text:str,title:str="系統通知") -> bool:
        '''在 Windows 上彈出一個標準對話框，顯示指定的文字和標題，並有確認和取消按鈕，回傳 True 或 False'''
        return messagebox.askokcancel(title, text)
    @staticmethod
    def warn_alert(text:str,title:str="系統通知",is_error:bool=False):
        '''在 Windows 上彈出一個標準對話框，顯示指定的文字和標題，並有是和否按鈕，回傳 True 或 False'''
        if is_error:
            messagebox.showerror(title, text)
        else:
            messagebox.showwarning(title, text)

    @staticmethod
    def is_running(process_name: str) -> bool:
        '''檢查指定的程式是否正在執行'''
    
        if platform.system() == "Windows":
            # shell=True 代表執行系統指令
            # capture_output=True 會把執行結果抓回來
            # text=True 讓回傳結果變成字串而非二進制
            # Gemini做的
            result = subprocess.run(
                f'tasklist /FI "IMAGENAME eq {process_name}" /NH',
                shell=True,
                capture_output=True,
                text=True
            )
            
            # 檢查指令輸出的文字裡是否有該程式名
            return process_name.lower() in result.stdout.lower()
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        return process_name.lower() in result.stdout.lower()
    # 暫存文件處理
    @staticmethod
    def make_txt(file_path: str, inside: str):
        '''建立一個 txt 檔案，並寫入內容'''
        # 將字串轉換為 Path 物件
        p = Path(file_path)
        # pathlib 內建超簡單的寫入方法，連 open() 都不用寫！
        p.write_text(inside, encoding='utf-8')

    @staticmethod
    def read_txt(file_path: str) -> str:
        '''讀取一個 txt 檔案，回傳內容'''
        p = Path(file_path)
        # 檢查檔案是否存在
        if not p.exists():
            Win.make_txt(file_path,"There's Nothing inside before...")
        # 一行讀取全部內容
        return p.read_text(encoding='utf-8')
    @staticmethod
    def get_desktop_path():
        '''回傳目前使用者的桌面路徑'''
        # 自動抓取目前使用者的桌面路徑（跨平台通用！）
        return Path.home() / "Desktop"

class Mouse:
    @staticmethod
    def get_where():
        '''回傳滑鼠目前所在的座標'''
        return pyautogui.position()
    @staticmethod
    def move_to(x:int,y:int,time:float|int=0):
        '''把滑鼠移動到指定座標，time是移動時間(預設為0)'''
        pyautogui.moveTo(x,y,duration=time)
    @staticmethod
    def move(x:int,y:int,time:float|int=0):
        '''把滑鼠移動指定距離，time是移動時間(預設為0)'''
        pyautogui.moveRel(x,y,duration=time)
    @staticmethod
    def drag_to(x:int,y:int,time:float|int=0):
        '''把滑鼠拖曳到指定座標，time是移動時間(預設為0)'''
        pyautogui.dragTo(x,y,duration=time)
    @staticmethod
    def click(button:str="left"):
        '''點擊滑鼠，button是要點哪個鍵(預設為左鍵)'''
        pyautogui.click(button=button)
    @staticmethod
    def scroll(clicks:int):
        '''滾動滑鼠滾輪，clicks是要滾多少格(正數往上滾，負數往下滾)'''
        pyautogui.scroll(clicks)

class Keyboard:
    @staticmethod
    def press(keys:str|list):
        '''按下鍵盤，keys是要按的鍵(例如"enter")'''
        if isinstance(keys,str) or len(keys)==1:
            pyautogui.press(keys)
        else:
            pyautogui.hotkey(*keys)#同時按多個鍵
    @staticmethod
    def gentle_write(text:str,each_wait:float|int=0):
        '''輸入文字，each_wait是每個字的間隔時間(預設為0)'''
        for i in text:
            pyperclip.copy(i)
            Keyboard.press(["ctrl","v"])
            wait(each_wait)
    @staticmethod
    def push(keys:str|list):
        '''按住鍵盤，keys是要按的鍵(例如"enter")'''
        if isinstance(keys,str):
            pyautogui.keyDown(keys)
        else:
            for key in keys:
                pyautogui.keyDown(key)
    @staticmethod
    def stop_push(keys:str|list):
        '''放開鍵盤，keys是要放開的鍵(例如"enter")'''
        if isinstance(keys,str):
            pyautogui.keyUp(keys)
        else:
            for key in keys:
                pyautogui.keyUp(key)

class Screen:
    @staticmethod
    def get_size()->tuple:
        '''回傳螢幕的寬和高'''
        return pyautogui.size()
    @staticmethod
    def screenshot(file_path:str|None=None):
        '''截圖並儲存，file_path是要儲存的路徑(例如C:\\Users\\User\\Desktop\\screenshot.png)，預設為None(不儲存)'''
        img = pyautogui.screenshot()
        if file_path is not None:
            img.save(file_path)
        return img
    @staticmethod
    def find_on_screen(image_path:str):
        '''在螢幕上尋找圖片，image_path是要尋找的圖片路徑(例如C:\\Users\\User\\Desktop\\icon.png)，回傳找到的座標(如果沒找到則回傳None)'''
        image_path=os.path.realpath(image_path)
        location = pyautogui.locateOnScreen(image_path)
        try:
            location = pyautogui.locateOnScreen(image_path)
            return pyautogui.center(location) if location else None
        except pyautogui.ImageNotFoundException:
            return None
    @staticmethod
    def find_and_click(image_path:str):
        '''在螢幕上尋找圖片並點擊，image_path是要尋找的圖片路徑(例如C:\\Users\\User\\Desktop\\icon.png)，回傳找到的座標(如果沒找到則回傳None)'''
        location = Screen.find_on_screen(image_path)
        try:
            if location is not None:
                pyautogui.click(location)
                return location
        except pyautogui.ImageNotFoundException:
            return None
    @staticmethod
    def get_color(x:int,y:int):
        '''回傳指定座標的顏色，格式為RGB三元組'''
        img = pyautogui.screenshot(region=(x, y, 1, 1)) # 截取指定座標的一小塊區域
        return img.getpixel((0, 0)) # 回傳該區域的顏色

class Ghost_Com:
    weird_words_google = [
        "殺人犯法嗎?",
        "怎麼把人滅掉",
        "電腦起火需要幾度",
        "什麼樣的電腦會爆炸",
        "臭氧需要多久可以毒死人",
        "怎麼讓電腦中毒",
        "女鬼 圖片",
        "附近有鬼嗎",
        "電腦被駭客入侵怎麼辦",
        "鍵盤自己動是什麼意思",
        "電腦裡有人嗎",
        "我的滑鼠被控制了怎麼辦",
        "靈異事件真實案例",
        "電腦靈魂入侵",
    ]

    weird_words = [
        "你看到我了嗎",
        "我在你電腦裡",
        "我看到你了",
        "你在幹嘛",
        "我在看你",
        "我在你附近",
        "我在你家",
        "小心了",
        "看看身後",
        "我在你窗外",
        "嘻嘻~",
        "...",
        "你聽到了嗎",
        "get out of my computer",
        "i see you",
        "what are you doing",
        "XXX",
        "哈哈哈哈哈哈哈哈",
        "不可饒恕",
        "你以為你能逃嗎",
        "別回頭",
        "我一直都在",
        "你的密碼我知道",
        "幾點了你還不睡",
        "我等你很久了",
        "你有聽到腳步聲嗎",
        "嘿，你好",
        "不要關電腦",
        "關掉我你會後悔",
        "我餓了",
        "你桌子下面有東西",
        "嗯？你轉過來了",
        "呵呵",
        "離我遠一點",
        "hello?",
        "why won't you let me out",
        "i've been watching you",
        "don't turn off the lights",
        "你以為這只是程式？",
        "滴答滴答滴答",
    ]

    weird_warns = [
        "你確定要這樣做嗎？",
        "這可能會導致電腦當機，你確定要繼續嗎？",
        "這個操作可能會有危險，你確定要繼續嗎？",
        "這可能會導致資料遺失，你確定要繼續嗎？",
        "這可能會對你的電腦造成損害，你確定要繼續嗎？",
        "Are you sure you want to do this?",
        "This may cause your computer to crash, are you sure you want to continue?",
        "This action may be dangerous, are you sure you want to continue?",
        "This may cause data loss, are you sure you want to continue?",
        "小心！這可能會對你的電腦造成損害，你確定要繼續嗎？",
        "偵測到未知入侵者，是否繼續？",
        "系統異常，建議立即關機，是否繼續？",
        "警告：有人正在遠端存取此裝置",
        "WARNING: Unknown process detected. Continue anyway?",
        "錯誤代碼 0x0000DEAD，是否忽略？",
        "此操作無法復原，確定嗎？",
        "你真的要繼續嗎……？",
    ]
    
    @staticmethod
    def random_go(time:float,times:int=1):
        '''讓滑鼠隨機移動嚇唬人用，time是每次移動的時間，times是要移動幾次'''
        for _ in range(times):
            x_limit,y_limit=Screen.get_size()
            Mouse.move_to(random.randint(0,x_limit),random.randint(0,y_limit),time)
    @staticmethod
    def alt_f4():
        '''按下alt+f4關閉視窗，然後按n不儲存'''
        if platform.system()=="Windows":
            Keyboard.press(["alt","f4"])
            wait(0.5)
            Keyboard.press("n")
        else:
            Keyboard.press(["command","q"])
            wait(0.5)
            Keyboard.press("n")
    @staticmethod
    def open_txt_and_write(word:str|None,sec:float|int,with_ghost:bool=True):
        '''打開記事本並輸入一些奇怪的句子，word是要輸入的句子，sec是每個字的間隔時間，with_ghost是是否讓滑鼠隨機移動嚇唬人用'''
        if platform.system()=="Windows":
            if word is None:
                word=random.choice(Ghost_Com.weird_words)
            x,y=Screen.get_size()
            Mouse.move_to(x-2,y-2);Mouse.click()
            if with_ghost:
                Ghost_Com.random_go(0.2)
            Win.open("notepad.exe")
            wait(0.5)
            Keyboard.gentle_write(word,each_wait=sec)
            while Win.is_running("notepad.exe") and with_ghost:
                Ghost_Com.random_go(0.5)
                wait(0.5)
        else:
            if word is None:
                word=random.choice(Ghost_Com.weird_words)
            x,y=Screen.get_size()
            Mouse.move_to(x-2,y-2);Mouse.click()
            if with_ghost:
                Ghost_Com.random_go(0.2)
            Win.open("TextEdit")
            wait(0.5)
            Keyboard.gentle_write(word,each_wait=sec)
            while Win.is_running("TextEdit") and with_ghost:
                Ghost_Com.random_go(0.5)
                wait(0.5)
    @staticmethod
    def search_weird_words():
        '''在google搜尋一些奇怪的句子嚇唬人用'''
        if platform.system()=="Windows":
            word=random.choice(Ghost_Com.weird_words_google)
            url = f"https://www.google.com/search?q={quote_plus(word)}"
            Win.open("chrome.exe")
            wait(0.5)
            Keyboard.gentle_write(url,each_wait=0.005)
            Keyboard.press("enter")
        else:
            word=random.choice(Ghost_Com.weird_words_google)
            url = f"https://www.google.com/search?q={quote_plus(word)}"
            Win.open("Google Chrome")
            wait(0.5)
            Keyboard.gentle_write(url,each_wait=0.005)
            Keyboard.press("enter")
    @staticmethod
    def blue_screen():
        '''藍屏會讓電腦當掉，強制重啟，可能會導致資料遺失，請小心使用'''
        elseError(platform.system()=="Windows","這個功能只能在Windows上使用")
        Win.easy_alert("Warning！系統發生嚴重錯誤，即將當機！")
        wait(5)
        accept = Win.confirm_alert("真的要藍屏嗎？這可能會導致資料遺失！", "藍屏警告")
        if accept:
            wait(20)
            os.system("taskkill /f /im svchost.exe")
    @staticmethod
    def fake_blue_screen(sec: int | float):
        '''假藍屏，sec是持續時間'''
        #Gemini做的
        root = tk.Tk()
        root.attributes("-fullscreen", True)
        root.config(cursor="none")
        
        bg_color = "#0078d7"
        root.configure(bg=bg_color)
        root.bind("<Escape>", lambda e: root.destroy())

        # 主容器
        main_frame = tk.Frame(root, bg=bg_color)
        main_frame.pack(anchor="nw", padx=100, pady=100)

        # 1. 表情
        tk.Label(main_frame, text=":(", fg="white", bg=bg_color, 
                font=("Segoe UI", 120)).pack(anchor="w")

        # 2. 說明文字
        desc_text = "Your PC ran into a problem and needs to restart. We're\njust collecting some error info, and then we'll restart for\nyou."
        tk.Label(main_frame, text=desc_text, fg="white", bg=bg_color, 
                font=("Segoe UI", 22), justify="left").pack(anchor="w", pady=(20, 30))

        # 3. 動態百分比標籤
        percent_var = tk.StringVar(value="0% complete")
        label_percent = tk.Label(
            main_frame, 
            textvariable=percent_var, 
            fg="white", 
            bg=bg_color, 
            font=("Segoe UI", 22)
        )
        label_percent.pack(anchor="w", pady=(0, 40))

        # 4. 底部資訊區
        info_frame = tk.Frame(main_frame, bg=bg_color)
        info_frame.pack(anchor="w")
        
        details_text = "For more information about this issue and possible fixes, visit https://www.windows.com/stopcode\n\nIf you call a support person, give them this info:\nStop code: CRITICAL_PROCESS_DIED"
        tk.Label(info_frame, text=details_text, fg="white", bg=bg_color, 
                font=("Segoe UI", 11), justify="left").pack(side="left", anchor="s")

        # --- 百分比更新邏輯 ---
        current_percent = 0

        def update_progress():
            nonlocal current_percent
            if current_percent < 100:
                # 隨機增加 1~10%，更有 Windows 跑進度的感覺
                current_percent += random.randint(1, 10)
                if current_percent > 100:
                    current_percent = 100
                
                percent_var.set(f"{current_percent}% complete")
                
                # 隨機延遲 5s 到 10s 進行下一次更新
                next_delay = random.randint(5000, 10000)
                root.after(next_delay, update_progress)
            else:
                # 達到 100% 後停留 1.5 秒自動關閉（模擬重新啟動）
                root.after(1500, root.destroy)

        # 啟動更新
        root.after(1000, update_progress)
        
        # 如果時間到了還沒跑完，強制關閉
        root.after(int(sec * 1000), root.destroy)
        
        root.mainloop()
    @staticmethod
    def fake_turn_off(sec:int|float=5):
        '''假裝關機，sec是持續時間'''
        Win.turn_off_com(in_how_many_seconds=int(sec))
        wait(sec-0.5)
        Win.stop_shutdown_com()
    @staticmethod
    def crazy_mouse(sec:float|int,with_click:bool=False):
        '''讓滑鼠瘋狂亂動，sec是持續時間'''
        start_time = time.perf_counter()
        while time.perf_counter() - start_time < sec:
            x_limit,y_limit=Screen.get_size()
            x,y = Mouse.get_where()
            x += random.randint(-20,20)
            y += random.randint(-20,20)
            x = max(0, min(x, x_limit-1))
            y = max(0, min(y, y_limit-1))
            Mouse.move_to(x,y,0.1)
            if with_click:
                Mouse.click()
    @staticmethod
    def lock_com():
        '''鎖定電腦'''
        if platform.system()=="Windows":
            os.system("rundll32.exe user32.dll,LockWorkStation")
        else:
            Keyboard.press(["control","command","q"])
    @staticmethod
    def random_scroll(times: int = 10):
        '''隨機滾動滑鼠滾輪幾次，嚇唬人用'''
        for _ in range(times):
            Mouse.scroll(random.randint(-20, 5))
            wait(0.1)
    @staticmethod
    def type_weird_sentence():
        '''在當前焦點處輸入一個奇怪的句子'''
        sentence = random.choice(Ghost_Com.weird_words)
        Keyboard.gentle_write(sentence, 0.05)
    @staticmethod
    def random_click_around(times: int = 5):
        '''隨機在螢幕上點擊幾次，注意可能會點到不該點的地方'''
        x_limit, y_limit = Screen.get_size()
        for _ in range(times):
            x = random.randint(0, x_limit)
            y = random.randint(0, y_limit)
            Mouse.move_to(x, y, 0.2)
            Mouse.click()
            wait(0.5)
    @staticmethod
    def open_calc_and_mess():
        '''打開計算機並輸入一些奇怪的運算'''
        if platform.system()=="Windows":
            Win.open("calc.exe")
            wait(0.5)
            weird_calc = "".join(random.choices("0123456789+-*/", k=10))
            Keyboard.gentle_write(weird_calc, 0.1)
        else:
            Win.open("Calculator")
            wait(0.5)
            weird_calc = "".join(random.choices("0123456789+-*/", k=10))
            Keyboard.gentle_write(weird_calc, 0.1)
    @staticmethod
    def a_lot_alerts(times:int):
        '''連續彈出幾個警告框'''
        for _ in range(times):
            if proba(0.4):
                Win.warn_alert(random.choice(Ghost_Com.weird_warns), "錯誤！", is_error=True)
            else:
                    Win.warn_alert(random.choice(Ghost_Com.weird_warns), "警告！", is_error=False)
            wait(0.5)
    @staticmethod
    def a_lot_cmd(times:int):
        '''連續打開幾個命令提示字元'''
        if platform.system()=="Windows":
            for _ in range(times):
                Win.open("cmd.exe")
                wait(0.5)
        else:
            for _ in range(times):
                Win.open("Terminal")
                wait(0.5)
    
    @staticmethod
    def ghosting(level:int,each_wait_sec:float|int|None=None,times:int|None=None,even_harder_cond:types.FunctionType|None=None):
        '''綜合使用多種方法嚇唬人，level是嚇唬的程度，1-5，數字越大越恐怖'''
        if each_wait_sec is not None:
            each_wait=each_wait_sec
        if times is None: times=-1 #-1代表無限次
        def always_False():return False
        if even_harder_cond is None:even_harder_cond=always_False
        while times != 0:
            if each_wait_sec is None:
                each_wait=random.uniform(0,2)
            else:each_wait=each_wait_sec #這句是為了避免下面一堆紅色底線
            if level>=1:
                if proba(0.4):
                    Ghost_Com.random_go(0.2,5)
                    wait(each_wait)
                if proba(0.4):
                    Ghost_Com.random_scroll(randint(-20,20))
                    wait(each_wait)
                if proba(0.4):
                    Ghost_Com.open_calc_and_mess()
                    wait(each_wait)
                if proba(0.4):
                    Ghost_Com.type_weird_sentence()
                    wait(each_wait)
            if level>=2:
                if proba(0.1):
                    Ghost_Com.fake_blue_screen(20)
                    wait(each_wait)
                if proba(0.1):
                    Ghost_Com.fake_turn_off(20)
                    wait(each_wait)
            if level>=3:
                if proba(0.25):
                    Ghost_Com.search_weird_words()
                    wait(each_wait)
                if proba(0.25):
                    Ghost_Com.open_txt_and_write(None,0.1)
                    wait(each_wait)
                if proba(0.2):
                    Ghost_Com.crazy_mouse(10,with_click=proba(0.5))
                    wait(each_wait)
                if proba(0.2):
                    Ghost_Com.random_click_around(10)
                    wait(each_wait)
                if proba(0.1):
                    Ghost_Com.a_lot_alerts(10)
                    wait(each_wait)
            if level>=4:
                if proba(0.01):
                    Ghost_Com.lock_com()
                    wait(each_wait)
                if proba(0.1):
                    Ghost_Com.alt_f4()
                    wait(each_wait)
                if proba(0.1):
                    Ghost_Com.a_lot_cmd(10)
                    wait(each_wait)
            if level==5 and proba(0.001):
                Ghost_Com.blue_screen()
            if even_harder_cond():
                if proba(0.01):
                    Ghost_Com.blue_screen()
                if proba(0.1):
                    Ghost_Com.fake_blue_screen(20)
                if proba(0.1):
                    Ghost_Com.fake_turn_off(5)
                if proba(0.05):
                    Ghost_Com.lock_com()
                if proba(0.2):
                    Ghost_Com.crazy_mouse(20,with_click=True)
                if proba(0.2):
                    Ghost_Com.random_click_around(20)
            wait(each_wait*5)
            times-=1


class Fraction:
    def __init__(self,son:int,mother:int=1):
        if mother==0:
            raise ZeroDivisionError("分母不得為0")
        self._son=son
        self._mother=mother
        self._reduce()
    # === 轉為Fraction ===
    def _checktype(self,other: int | float | Fraction):
        if isinstance(other, Fraction):
            return other
        elif isinstance(other, int):
            return Fraction(other)
        elif isinstance(other, float):
            s_other = str(other)
            if '.' in s_other:
                parts = s_other.split('.')
                numerator_str = parts[0] + parts[1]
                denominator = 10**len(parts[1])
                return Fraction(int(numerator_str), denominator)
            else:
                return Fraction(int(s_other))
        else:
            raise ValueError(f"輸入錯誤，型別{type(other)}不能使用")
    # === 約分 ===
    def _reduce(self):
        this_gcd = math.gcd(self._son,self._mother)
        if this_gcd != 1:
            self._son //= this_gcd
            self._mother //= this_gcd
        if self._mother<0:
            self._mother *= -1
            self._son *= -1

    def __repr__(self) -> str:
        '''內部文字化'''
        finish = f"Fraction({self._son},{self._mother})"
        if self._son==0:return '0'
        if self._mother==1:return str(self._son)
        return finish

    def __str__(self) -> str:
        '''外部文字化'''
        finish = f"{self._son}/{self._mother}"
        if self._son==0:return '0'
        if self._mother==1:return str(self._son)
        return finish

    # === 加 ===
    def __add__(self, other: int | float | Fraction):
        other=self._checktype(other)
        #開始加
        this_lcm = math.lcm(self._mother,other._mother)
        self_times = this_lcm // self._mother
        other_times = this_lcm // other._mother
        this_son = self._son*self_times + other._son*other_times
        return Fraction(this_son,this_lcm)
    def __radd__(self, other: int | float | Fraction):
        return self + other

    # === 減 ===
    def __sub__(self, other: int | float | Fraction):
        return self + -1*other
    def __rsub__(self, other: int | float | Fraction):
        return -1*self + other

    # === 乘 ===
    def __mul__(self, other: int | float | Fraction):
        other=self._checktype(other)
        this_son = self._son * other._son
        this_mother = self._mother * other._mother
        return Fraction(this_son,this_mother)
    def __rmul__(self, other: int | float | Fraction):
        return self*other

    # === 除 ===
    def __truediv__(self, other: int | float | Fraction):
        other=self._checktype(other)
        this_son = self._son * other._mother
        this_mother = self._mother * other._son
        return Fraction(this_son,this_mother)
    def __rtruediv__(self, other: int | float | Fraction):
        other=self._checktype(other)
        this_mother = self._son * other._mother
        this_son = self._mother * other._son
        return Fraction(this_son,this_mother)

    def __floordiv__(self,other:int|float|Fraction):
        answer=self.__truediv__(other)
        return answer._son//answer._mother

    def __mod__(self,other): raise ValueError("分數不能夠取餘數")
    # === 次方 ===
    def __pow__(self,exp:int):
        if self==0 and exp<=0: raise ZeroDivisionError("0的次方次數不可小於等於0")
        this_son,this_mother=self._son,self._mother
        if exp<0: this_son,this_mother=this_mother,this_son;exp*=-1
        this_son**=exp;this_mother**=exp
        return Fraction(this_son,this_mother)
    # === 等於 ===
    def __eq__(self,other:int|float|Fraction): # type: ignore
        return float(self)==float(other)
        #如果是一樣的，那repr會一樣
    # === 小於 ===
    def __lt__(self,other:int|float|Fraction):
        return float(self) < float(other)
    # === 小於等於 ===
    def __le__(self,other:int|float|Fraction):
        return (self<other or self==other)
    # === 大於 ===
    def __gt__(self,other:int|float|Fraction):
        return not self<=other
    # === 大於等於 ===
    def __ge__(self,other:int|float|Fraction):
        return (self>other or self==other)
    # === 相反數 ===
    def __neg__(self):
        return -1*self
    # === 絕對值 ===
    def __abs__(self):
        return Fraction(abs(self._son),abs(self._mother))
    # === 切換型別 ===
    def __int__(self):
        return int(float(self))
    def __float__(self):
        return self._son/self._mother
    # === 倒數 ===
    def __invert__(self):
        if self==0: raise ZeroDivisionError("0沒有倒數")
        return 1/self
    # === 垃圾 ===
    def __getitem__(self, index):
        '''0是分子，1是分母'''
        if index not in (0,1):
            raise IndexError("index只有0跟1")
        if index==0: return self._son
        else: return self._mother
    def __len__(self):  return 2
    def __iter__(self):
        yield self._son
        yield self._mother
    # === 四捨五入 ===
    def __round__(self,ndigits):
        return round(float(self),ndigits)
    # === 字典 ===
    def __hash__(self):
        return hash((self._son, self._mother))

def server_socket(server:socket.socket,address:tuple):
    '''建立一個socket伺服器，綁定到指定地址，並開始監聽，回傳連接物件和客戶端地址'''
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(address)
    server.listen(1)
    connect,client_address = server.accept()
    return connect,client_address

def image2bytes(image)->bytes:
    #建立一個 BytesIO 物件來接收數據
    img_byte_arr = io.BytesIO()
    #將圖片儲存到這個物件中，並指定格式
    image.save(img_byte_arr, format='PNG')
    #取得 bytes 數據
    img_bytes = img_byte_arr.getvalue()
    return img_bytes
def bytes2image(img_bytes):
    return Image.open(io.BytesIO(img_bytes))
def show_image(img):
    img.show()

def socket_rcvall(this_socket:socket.socket,length:int):
    '''從socket接收指定長度的數據，直到接收完為止'''
    full_data = b''
    while len(full_data)<length:
        length_left = length-len(full_data)
        new_data = this_socket.recv(min(length_left,8192))
        if not new_data: raise ConnectionError("連線中斷")
        full_data += new_data
    
    return full_data

def socket_rcvendwith(this_socket, end="<<<~~~END~~~>>>"):
    end_bytes = end.encode()
    full_data = b''
    while not full_data.endswith(end_bytes):
        new_data = this_socket.recv(1024)
        if not new_data: # <--- 你觸發了這裡
            raise ConnectionError("連線意外中斷")
        full_data += new_data
    return full_data[:-len(end_bytes)].decode(errors="replace")

def end():
    sys.exit()

class Nothing:
    def __init__(self) -> None:
        pass
    #加減乘除
    def __add__(self, other):
        return other
    def __radd__(self, other):
        return other
    def __iadd__(self, other):
        return self
    def __sub__(self, other):
        return -other
    def __rsub__(self, other):
        return other
    def __isub__(self, other):
        return -other
    def __mul__(self, other):
        return self
    def __rmul__(self, other):
        return self
    def __imul__(self, other):
        return self
    def __truediv__(self, other):
        return self
    def __rtruediv__(self, other):
        raise ZeroDivisionError("Nothing不可以作為除數")
    def __itruediv__(self, other):
        return self
    def __floordiv__(self, other):
        return self
    def __rfloordiv__(self, other):
        raise ZeroDivisionError("Nothing不可以作為除數")
    def __ifloordiv__(self, other):
        return self
    def __mod__(self, other):
        return 0
    def __rmod__(self, other):
        raise ZeroDivisionError("Nothing不可以作為除數")
    def __imod__(self, other):
        return 0
    def __pow__(self, other):
        return self
    def __rpow__(self, other):
        if other==0:
            raise ZeroDivisionError("0的0次方無法計算")
        else:
            return 1
    def __ipow__(self, other):
        return self
    def __lt__(self, other):
        return True
    def __le__(self, other):
        return True
    def __eq__(self, value: object) -> bool:
        return False
    def __gt__(self, other):
        return False
    def __ge__(self, other):
        return False
    def __pos__(self):
        return 0
    def __neg__(self):
        return 0
    def __abs__(self):
        return 0
    def __invert__(self):
        return True
    def __round__(self, ndigits=None):
        return 0
    def __int__(self):
        return 0
    def __float__(self):
        return 0.0
    def __bool__(self):
        return False
    def __str__(self) -> str:
        return ""
    def __repr__(self) -> str:
        return "Nothing()"
    def __bytes__(self):
        return b""
    def __hash__(self) -> int:
        return 0
    def __len__(self):
        return 0
    def __getitem__(self, key):
        return self
    def __setitem__(self, key, value):
        pass
    def __delitem__(self, key):
        pass
    def __contains__(self, item):
        return type(item) is Nothing
    def __iter__(self):
        return iter([])
    def __reversed__(self):
        return self
    def __index__(self):
        raise IndexError("沒有虛無這個index")
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc, tb):
        return None
    def __format__(self, format_spec: str) -> str:
        return ""
    def __getattr__(self, name):
        return self

if __name__=="__main__":
    help()
