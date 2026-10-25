# useful
這是我自己做的一個useful的函式庫

Useful Import - 張三 製作

這是一個多功能 Python 工具箱，提供數學、隨機、時間、特殊效果、Windows 自動化、滑鼠鍵盤控制、螢幕操作、網頁自動化等實用功能。

使用方法：<br>
    import useful      # 假設檔案名為 useful.py<br>
    help("主題")       # 查看特定主題的詳細說明<br>
    help()             # 顯示主選單<br>

主要功能分類（詳細請使用 help("主題名稱")）：

【基礎工具】<br>
    hello()           印出 Hello World<br>
    useful()          印出彩色 Useful 字樣<br>
    elseError(cond, msg)  條件不成立則報錯<br>
    unique(thing)     去除重複元素<br>
    count_proportion(list)  計算佔比<br>

【數學】<br>
    is_prime(n)       判斷質數<br>
    carry_system(num, N, M)  進制轉換<br>
    Fraction(分子, 分母)  分數類別<br>

【隨機】<br>
    choose(src, count, uniq)  隨機抽選<br>
    proba(p)          機率判斷<br>
    random_country(continent, count, uniq)  隨機國家<br>

【時間】
    wait(sec)         延遲<br>
    @during_time      裝飾器：計算函式執行時間<br>
    current_time()    精確計時器<br>
    get_time(format, timezone)  格式化現在時間<br>

【特殊效果】<br>
    special_print(words, color, bg, special)  彩色/特效輸出<br>
    print_special(words, color, bg, special)  另一個彩色/特效輸出<br>
    loadings(list, count, wait)  載入動畫<br>
    gentle_say(word, wait, is_input)  打字機效果<br>
    morse(letter, turn_to_morse)  摩斯密碼轉換<br>
    password(text, key, turn_back)  加密/解密<br>

【Windows 系統 (Win 類別)】<br>
    Win.turn_off_com(sec)      倒數關機<br>
    Win.turn_off_com_mac(sec)  倒數關機（Mac）<br>
    Win.restart_com(sec)       倒數重啟<br>
    Win.restart_com_mac(sec)   倒數重啟（Mac）<br>
    Win.stop_shutdown_com()    取消關機/重啟<br>
    Win.stop_shutdown_com_mac()  取消關機/重啟（Mac）<br>
    Win.stop_task(name, force) 結束程式<br>
    Win.delete_file(path, quiet, force) 刪除檔案<br>
    Win.open(where)            開啟檔案/程式/網頁<br>
    Win.alert(text, title)     彈出對話框<br>
    Win.easy_alert(text)       簡易彈窗<br>
    Win.confirm_alert(text, title) -> 確認/取消對話框<br>
    Win.warn_alert(text, title, is_error) -> 警告/錯誤對話框<br>
    Win.is_running(process)    偵測程式是否執行<br>
    Win.is_running_mac(process)  偵測程式是否執行（Mac）<br>
    Win.make_txt(path, content)  建立文字檔<br>
    Win.read_txt(path)         讀取文字檔<br>
    Win.get_desktop_path()     取得桌面路徑<br>

【滑鼠控制 (Mouse 類別)】<br>
    Mouse.get_where()          取得座標<br>
    Mouse.move_to(x, y, time)  移動到座標<br>
    Mouse.move(dx, dy, time)   相對移動<br>
    Mouse.drag_to(x, y, time)  拖曳<br>
    Mouse.click(button)        點擊<br>
    Mouse.scroll(clicks)       滾動滾輪<br>

【鍵盤控制 (Keyboard 類別)】<br>
    Keyboard.press(keys)       按鍵 (支援組合鍵)<br>
    Keyboard.gentle_write(text, interval)  模擬打字<br>
    Keyboard.push(keys)         按住按鍵<br>
    Keyboard.stop_push(keys)    放開按鍵<br>
    Keyboard.scroll(clicks)    滾動滾輪<br>

【螢幕操作 (Screen 類別)】<br>
    Screen.get_size()          解析度<br>
    Screen.screenshot(path)    截圖<br>
    Screen.find_on_screen(image_path)  尋找圖片位置<br>
    Screen.find_and_click(image_path)  尋找並點擊<br>
    Screen.get_color(x, y)     取得顏色<br>

【幽靈指令 (Ghost_Com 類別)】<br>
    Ghost_Com.random_go(time, times)  隨機移動滑鼠<br>
    Ghost_Com.alt_f4()         送出 Alt+F4 並按 N<br>
    Ghost_Com.alt_f4_mac()     送出 Alt+F4（Mac）<br>
    Ghost_Com.open_txt_and_write(word, sec, with_ghost=True)  開啟 Notepad 並打字<br>
    Ghost_Com.open_txt_and_write_mac(word, sec, with_ghost=True)  開啟 Notepad 並打字（Mac）<br>
    Ghost_Com.search_weird_words()  在 Chrome 開啟奇怪搜尋<br>
    Ghost_Com.search_weird_words_mac()  在 Chrome 開啟奇怪搜尋（Mac）<br>
    Ghost_Com.blue_screen()  嘗試藍屏（危險）<br>
    Ghost_Com.fake_blue_screen()  假裝藍屏（安全）<br>
    Ghost_Com.fake_turn_off(sec)  假裝關機後取消<br>
    Ghost_Com.fake_turn_off_mac(sec)  假裝關機後取消（Mac）<br>
    Ghost_Com.crazy_mouse(sec, with_click=False)  讓滑鼠瘋狂亂動<br>
    Ghost_Com.lock_com()  鎖定電腦<br>
    Ghost_Com.lock_com_mac()  鎖定電腦（Mac）<br>
    Ghost_Com.random_scroll(times)  隨機滾動滑鼠滾輪<br>
    Ghost_Com.type_weird_sentence()  當前焦點輸入奇怪句子<br>
    Ghost_Com.random_click_around(times)  隨機在螢幕上點擊<br>
    Ghost_Com.open_calc_and_mess()  打開計算機並亂輸入<br>
    Ghost_Com.open_calc_and_mess_mac()  打開計算機並亂輸入（Mac）<br>
    Ghost_Com.spam_typing(times, sec)  連續打字<br>
    Ghost_Com.random_keyboard_press(times)  隨機按鍵亂打<br>
    Ghost_Com.open_multiple_tabs(count)  開多個 Chrome 搜尋分頁<br>
    Ghost_Com.open_notepad_spam(count, sec)  連續開 Notepad 並打字<br>
    Ghost_Com.a_lot_alerts(times)  連續彈出警告對話框<br>
    Ghost_Com.a_lot_cmd(times)  連續開命令提示字元<br>
    Ghost_Com.a_lot_cmd_mac(times)  連續開命令提示字元（Mac）<br>

【網頁自動化 (web 類別)】需安裝 selenium<br>
    web.connect()              連接到 Chrome<br>
    web.open(url)              開啟網址<br>
    web.find_by(by, value)     尋找元素<br>
    web.click(element)         點擊元素<br>
    web.key(element, word)     輸入文字<br>
    web.get_html()             取得原始碼<br>
    web.close_all()            關閉瀏覽器<br>

更多說明請在 Python 互動環境中輸入 help() 或 help("主題")。
