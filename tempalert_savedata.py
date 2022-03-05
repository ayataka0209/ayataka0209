import calendar
import pickle
import tkinter as tk
from tkinter import StringVar, ttk

#github test

main = tk.Tk()
main.title('気温アラート ― 登録地点選択')
main.geometry('578x130')
main.resizable(width=False, height=False)
main.configure(bg='white')

style = ttk.Style()
var_high_low = StringVar()

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def save_data():
    last_sent_mail_day = ''
    last_sent_mail_month = ''
    last_sent_mail_year = ''
    with open(r'savedata\data' + registration_location + r'.pickle', mode='wb') as data:
        pickle.dump(location, data)
        pickle.dump(location_code, data)
        pickle.dump(standard_temps, data)
        pickle.dump(mailaddress, data)
        pickle.dump(high_low, data)
        pickle.dump(notification_frequency, data)
        if notification_frequency == 'user_setting':
            pickle.dump(user_setting_num, data)
            pickle.dump(user_setting_dataunit, data)
        pickle.dump(frequency_year, data)
        pickle.dump(frequency_month, data)
        pickle.dump(frequency_day, data)
        pickle.dump(frequency_hour, data)
        pickle.dump(frequency_minute, data)
        pickle.dump(last_sent_mail_day,data)
        pickle.dump(last_sent_mail_month,data)
        pickle.dump(last_sent_mail_year,data)
        pickle.dump(acquisition_date,data)
    return save_data

def select_location():
    global location_code
    if location == '北海道 宗谷地方':
        location_code = '011000'
        save_data()
        main_register.destroy()
    elif location == '北海道 網走・北見・紋別地方':
        location_code = '013000'
        save_data()
        main_register.destroy()
    elif location == '北海道 釧路・根室地方':
        location_code = '014100'
        save_data()
        main_register.destroy()
    elif location == '北海道 石狩・空知・後志地方':
        location_code = '016000'
        save_data()
        main_register.destroy()
    elif location == '北海道 上川・留萌地方':
        location_code = '012000'
        save_data()
        main_register.destroy()
    elif location == '北海道 十勝地方':
        location_code = '014100'
        save_data()
        main_register.destroy()
    elif location == '北海道 胆振・日高地方':
        location_code = '015000'
        save_data()
        main_register.destroy()
    elif location == '北海道 渡島・檜山地方':
        location_code = '017000'
        save_data()
        main_register.destroy()
    elif location == '青森県 津軽・下北':
        location_code = '020000'
        save_data()
        main_register.destroy()
    elif location == '青森県 三八上北':
        location_code = '020000'
        save_data()
        main_register.destroy()
    elif location == '岩手県 内陸':
        location_code = '030000'
        save_data()
        main_register.destroy()
    elif location == '岩手県 沿岸':
        location_code = '030000'
        save_data()
        main_register.destroy()
    elif location == '宮城県 東部':
        location_code = '040000'
        save_data()
        main_register.destroy()
    elif location == '宮城県 西部':
        location_code = '040000'
        save_data()
        main_register.destroy()
    elif location == '秋田県':
        location_code = '050000'
        save_data()
        main_register.destroy()
    elif location == '山形県':
        location_code = '060000'
        save_data()
        main_register.destroy()
    elif location == '福島県 中通り・浜通り':
        location_code = '070000'
        save_data()
        main_register.destroy()
    elif location == '福島県 会津':
        location_code = '070000'
        save_data()
        main_register.destroy()
    elif location == '茨城県':
        location_code = '080000'
        save_data()
        main_register.destroy()
    elif location == '栃木県':
        location_code = '090000'
        save_data()
        main_register.destroy()
    elif location == '群馬県 北部':
        location_code = '100000'
        save_data()
        main_register.destroy()
    elif location == '群馬県 南部':
        location_code = '100000'
        save_data()
        main_register.destroy()
    elif location == '埼玉県':
        location_code = '110000'
        save_data()
        main_register.destroy()
    elif location == '千葉県':
        location_code = '120000'
        save_data()
        main_register.destroy()
    elif location == '東京都':
        location_code = '130000'
        save_data()
        main_register.destroy()
    elif location == '東京都 伊豆諸島南部':
        location_code = '130000'
        save_data()
        main_register.destroy()
    elif location == '東京都 伊豆諸島北部':
        location_code = '130000'
        save_data()
        main_register.destroy()
    elif location == '東京都 小笠原諸島':
        location_code = '130000'
        save_data()
        main_register.destroy()
    elif location == '神奈川県':
        location_code = '140000'
        save_data()
        main_register.destroy()
    elif location == '山梨県':
        location_code = '190000'
        save_data()
        main_register.destroy()
    elif location == '長野県 北部':
        location_code = '200000'
        save_data()
        main_register.destroy()
    elif location == '長野県 中部・南部':
        location_code = '200000'
        save_data()
        main_register.destroy()
    elif location == '新潟県':
        location_code = '150000'
        save_data()
        main_register.destroy()
    elif location == '富山県':
        location_code = '160000'
        save_data()
        main_register.destroy()
    elif location == '石川県':
        location_code = '170000'
        save_data()
        main_register.destroy()
    elif location == '福井県':
        location_code = '180000'
        save_data()
        main_register.destroy()
    elif location == '岐阜県 美濃地方':
        location_code = '210000'
        save_data()
        main_register.destroy()
    elif location == '岐阜県 飛騨地方':
        location_code = '210000'
        save_data()
        main_register.destroy()
    elif location == '静岡県':
        location_code = '220000'
        save_data()
        main_register.destroy()
    elif location == '愛知県':
        location_code = '230000'
        save_data()
        main_register.destroy()
    elif location == '三重県':
        location_code = '240000'
        save_data()
        main_register.destroy()
    elif location == '滋賀県 南部':
        location_code = '250000'
        save_data()
        main_register.destroy()
    elif location == '滋賀県 北部':
        location_code = '250000'
        save_data()
        main_register.destroy()
    elif location == '京都府 北部':
        location_code = '260000'
        save_data()
        main_register.destroy()
    elif location == '京都府 南部':
        location_code = '260000'
        save_data()
        main_register.destroy()
    elif location == '大阪府':
        location_code = '270000'
        save_data()
        main_register.destroy()
    elif location == '兵庫県 南部':
        location_code = '280000'
        save_data()
        main_register.destroy()
    elif location == '兵庫県 北部':
        location_code = '280000'
        save_data()
        main_register.destroy()
    elif location == '奈良県':
        location_code = '290000'
        save_data()
        main_register.destroy()
    elif location == '和歌山県':
        location_code = '300000'
        save_data()
        main_register.destroy()
    elif location == '鳥取県':
        location_code = '310000'
        save_data()
        main_register.destroy()
    elif location == '島根県':
        location_code = '320000'
        save_data()
        main_register.destroy()
    elif location == '岡山県 南部':
        location_code = '330000'
        save_data()
        main_register.destroy()
    elif location == '岡山県 北部':
        location_code = '330000'
        save_data()
        main_register.destroy()
    elif location == '広島県 南部':
        location_code = '340000'
        save_data()
        main_register.destroy()
    elif location == '広島県 北部':
        location_code = '340000'
        save_data()
        main_register.destroy()
    elif location == '山口県':
        location_code = '350000'
        save_data()
        main_register.destroy()
    elif location == '徳島県':
        location_code = '360000'
        save_data()
        main_register.destroy()
    elif location == '香川県':
        location_code = '370000'
        save_data()
        main_register.destroy()
    elif location == '愛媛県':
        location_code = '380000'
        save_data()
        main_register.destroy()
    elif location == '高知県':
        location_code = '390000'
        save_data()
        main_register.destroy()
    elif location == '福岡県':
        location_code = '400000'
        save_data()
        main_register.destroy()
    elif location == '佐賀県':
        location_code = '410000'
        save_data()
        main_register.destroy()
    elif location == '長崎県 南部・北部・五島':
        location_code = '420000'
        save_data()
        main_register.destroy()
    elif location == '長崎県 壱岐・対馬':
        location_code = '420000'
        save_data()
        main_register.destroy()
    elif location == '熊本県':
        location_code = '430000'
        save_data()
        main_register.destroy()
    elif location == '大分県':
        location_code = '440000'
        save_data()
        main_register.destroy()
    elif location == '宮崎' or location == '宮崎県':
        location_code = '450000'
        save_data()
        main_register.destroy()
    elif location == '鹿児島県（奄美地方を除く）':
        location_code = '460100'
        save_data()
        main_register.destroy()
    elif location == '鹿児島県 奄美地方':
        location_code = '460100'
        save_data()
        main_register.destroy()
    elif location == '沖縄県 沖縄本島地方':
        location_code = '471000'
        save_data()
        main_register.destroy()
    elif location == '沖縄県 大東島地方':
        location_code = '472000'
        save_data()
        main_register.destroy()
    elif location == '沖縄県 宮古島地方':
        location_code = '473000'
        save_data()
        main_register.destroy()
    elif location == '沖縄県 八重山地方':
        location_code = '474000'
        save_data()
        main_register.destroy()
    else:
        label_ok_error1.place(x=20, y=375)

def button_ok_k():
    def a():
        global mailaddress, standard_temps, location, location_code, user_setting_num, user_setting_dataunit, frequency_year, frequency_month, frequency_day, frequency_hour, frequency_minute, acquisition_date
        label_ok_error1.place_forget()
        label_ok_error2.place_forget()
        mailaddress = txt_mailaddress.get()
        mailaddress.replace(' ', '')
        if len(mailaddress) > 0:
            standard_temps = txt_standard_temps.get()
            if len(standard_temps) > 0:
                if is_int(standard_temps) == True:
                    standard_temps = int(standard_temps)
                    location = combo_location.get()
                    if high_low == 'high' or high_low == 'low':
                        frequency_year = entry_year.get()
                        if len(frequency_year) > 0:
                            if is_int(frequency_year) == True:
                                frequency_month = combo_month.get()
                                if len(frequency_month) > 0:
                                    frequency_day = combo_day.get()
                                    if len(frequency_day) > 0:
                                        frequency_hour = combo_hour.get()
                                        if len(frequency_hour) > 0:
                                            frequency_minute = combo_minute.get()
                                            if len(frequency_minute) > 0:
                                                acquisition_date = combo_acquisition_date.get()
                                                if len(acquisition_date) > 0:
                                                    if var_notification_frequency.get() == 'user_setting':
                                                        user_setting_num = txt_user_setting_num.get()#ユーザー設定を選択している場合
                                                        if len(user_setting_num) > 0:
                                                            if is_int(user_setting_num) == True:
                                                                user_setting_num = int(user_setting_num)
                                                                user_setting_dataunit = combo_user_setting_dataunit.get()
                                                                if len(user_setting_dataunit) > 0:
                                                                    select_location()
                                                                else:
                                                                    label_ok_error1.place(x=20, y=375)
                                                            else:
                                                                label_ok_error2.place(x=20, y=375)
                                                        else:
                                                            label_ok_error1.place(x=20, y=375)
                                                    elif var_notification_frequency.get() == 'weekday' or var_notification_frequency.get() == 'everyday' or var_notification_frequency.get() == 'everyweek' or var_notification_frequency.get() == 'everymonth' or var_notification_frequency.get() == 'everyyear':
                                                        select_location()#ユーザー設定以外にしている場合
                                                    else:
                                                        label_ok_error1.place(x=20, y=375)
                                                else:
                                                    label_ok_error1.place(x=20, y=375)
                                            else:
                                                label_ok_error1.place(x=20, y=375)
                                        else:
                                            label_ok_error1.place(x=20, y=375)
                                    else:
                                        label_ok_error1.place(x=20, y=375)
                                else:
                                    label_ok_error1.place(x=20, y=375)
                            else:
                                label_ok_error2.place(x=20, y=375)
                        else:
                            label_ok_error1.place(x=20, y=375)
                    else:
                        label_ok_error1.place(x=20, y=375)
                else:
                    label_ok_error2.place(x=20, y=375)
            else:
                label_ok_error1.place(x=20, y=375)
        else:
            label_ok_error1.place(x=20, y=375)
    return a

def high_low_k():
    def b():
        global high_low, var_high_low
        if var_high_low.get() == 'high':
            high_low = 'high'
        elif var_high_low.get() == 'low':
            high_low = 'low'
    return b

def button_del_k():
    def c():
        global location, location_code, standard_temps, mailaddress, high_low, notification_frequency, user_setting_num, user_setting_dataunit, frequency_year, frequency_month, frequency_day, day_list, frequency_hour, frequency_minute, last_sent_mail_day, last_sent_mail_month, last_sent_mail_year
        location = ''
        location_code = ''
        standard_temps = ''
        mailaddress = ''
        high_low = ''
        notification_frequency = ''
        frequency_year = ''
        frequency_month = ''
        frequency_day = ''
        day_list = ''
        frequency_hour = ''
        frequency_minute = ''
        last_sent_mail_day = ''
        last_sent_mail_month = ''
        last_sent_mail_year = ''
        if notification_frequency == 'user_setting':
            user_setting_num = ''
            user_setting_dataunit = ''
        save_data()
        main_register.destroy()
    return c

def button_close_k():
    def d():
        main_register.destroy()
    return d

def rdo_notification_frequency():
    def g():
        global notification_frequency, var_notification_frequency
        if var_notification_frequency.get() == 'weekday':
            notification_frequency = 'weekday'
            txt_user_setting_num['state'] = 'disable'
            combo_user_setting_dataunit['state'] = 'disable'
        if var_notification_frequency.get() == 'everyday':
            notification_frequency = 'everyday'
            txt_user_setting_num['state'] = 'disable'
            combo_user_setting_dataunit['state'] = 'disable'
        if var_notification_frequency.get() == 'everyweek':
            notification_frequency = 'everyweek'
            txt_user_setting_num['state'] = 'disable'
            combo_user_setting_dataunit['state'] = 'disable'
        if var_notification_frequency.get() == 'everymonth':
            notification_frequency = 'everymonth'
            txt_user_setting_num['state'] = 'disable'
            combo_user_setting_dataunit['state'] = 'disable'
        if var_notification_frequency.get() == 'everyyear':
            notification_frequency = 'everyyear'
            txt_user_setting_num['state'] = 'disable'
            combo_user_setting_dataunit['state'] = 'disable'
        if var_notification_frequency.get() == 'user_setting':
            notification_frequency = 'user_setting'
            txt_user_setting_num['state'] = 'normal'
            combo_user_setting_dataunit['state'] = 'readonly'
            #ここにユーザー設定に関してのやつを有効化するプログラムを入れる。
    return g

day_list = []

def month_k(event):
    global day_list, combo_day, month_list
    if len(combo_day.get()) > 0:
        day_list = ['']
        combo_day['values'] = day_list
        combo_day.current(0)
    if len(combo_month.get()) > 0:
        days_setting = calendar.monthrange(int(entry_year.get()), int(combo_month.get()))[1] + 1
        day_list = []
        for i in range(1, days_setting):
            day_list.append(str(i))
        combo_day['values'] = day_list

def year_k(event):
    global day_list, combo_day, month_list
    if len(combo_day.get()) > 0:
        day_list = ['']
        combo_day['values'] = day_list
        combo_day.current(0)
    if len(combo_month.get()) > 0:
        if len(combo_day.get()) == 0:
            combo_month.set('')
    

def settei_window():
    global main_register
    global label_ok_error1
    global label_ok_error2
    global txt_mailaddress
    global txt_standard_temps
    global combo_location
    global var_notification_frequency
    global txt_user_setting_num
    global combo_user_setting_dataunit
    global combo_month
    global combo_day
    global entry_year
    global combo_month
    global combo_hour
    global combo_minute
    global combo_acquisition_date
    global location, location_code, standard_temps, mailaddress, high_low, var_high_low, notification_frequency, user_setting_num, day_list, frequency_hour, frequency_minute, last_sent_mail_day, last_sent_mail_month, last_sent_mail_year, acquisition_date

    main_register = tk.Toplevel()
    main_register.title('気温アラート ― 設定')
    main_register.geometry('590x420')
    main_register.resizable(width=False, height=False)
    main_register.configure(bg='white')

    with open(r'savedata\data' + registration_location + r'.pickle', mode='rb') as data:
        location = pickle.load(data)
        location_code = pickle.load(data)
        standard_temps = pickle.load(data)
        mailaddress = pickle.load(data)
        high_low = pickle.load(data)
        notification_frequency = pickle.load(data)
        if notification_frequency == 'user_setting':
            user_setting_num = pickle.load(data)
            user_setting_dataunit = pickle.load(data)
        frequency_year = pickle.load(data)
        frequency_month = pickle.load(data)
        frequency_day = pickle.load(data)
        frequency_hour = pickle.load(data)
        frequency_minute = pickle.load(data)
        last_sent_mail_day = pickle.load(data)
        last_sent_mail_month = pickle.load(data)
        last_sent_mail_year = pickle.load(data)
        acquisition_date = pickle.load(data)

    #GUI_メールアドレスのテキストボックス
    label_mailaddress = ttk.Label(main_register, text='メールアドレス', font=('Yu Gothic',15), background='white')
    label_mailaddress.place(x=35,y=10)
    txt_mailaddress = ttk.Entry(main_register, width=30, font=('Yu Gothic',15))
    txt_mailaddress.place(x=210, y=10, height=30)
    txt_mailaddress.insert(0, mailaddress)

    #最高気温か最低気温のどちらで判断するかのラジオボタン
    label_high_low = ttk.Label(main_register, text='最高or最低気温', font=('Yu Gothic',15), background='white')
    label_high_low.place(x=35,y=50)
    label_explanation = ttk.Label(main_register, text='※「最低気温」は基準の気温以下、「最高気温」\r は基準の気温以上になると通知が来ます。', font=('Yu Gothic',10), background='white')
    label_explanation.place(x=280,y=85)
    var_high_low = StringVar(value = high_low)
    ttk.Style().configure("rdo_high_low.TRadiobutton", foreground="black", background="white", font=('Yu Gothic',15))
    rdo_high = ttk.Radiobutton(main_register, value='high', variable=var_high_low, text='最高気温', style='rdo_high_low.TRadiobutton', command=high_low_k())
    rdo_high.place(x=210, y=50)
    rdo_low = ttk.Radiobutton(main_register, value='low', variable=var_high_low, text='最低気温', style='rdo_high_low.TRadiobutton', command=high_low_k())
    rdo_low.place(x=320, y=50) 

    #GUI_基準の気温のテキストボックス
    label_standard_temps1 = ttk.Label(main_register, text='基準の気温(整数)', font=('Yu Gothic',15), background='white')
    label_standard_temps2 = ttk.Label(main_register, text='℃', font=('Yu Gothic',15), background='white')
    label_standard_temps1.place(x=35,y=90)
    label_standard_temps2.place(x=250,y=90)
    txt_standard_temps = ttk.Entry(main_register, width=3, font=('Yu Gothic',15), background='white')
    txt_standard_temps.place(x=210, y=90, height=30)
    txt_standard_temps.insert(0, standard_temps)

    #GUI_都道府県のリスト
    label_location = ttk.Label(main_register, text='都道府県名', font=('Yu Gothic',15), background='white')
    label_location.place(x=35,y=130)
    location_list = ['北海道 宗谷地方', '北海道 網走・北見・紋別地方', '北海道 釧路・根室地方', '北海道 石狩・空知・後志地方', '北海道 上川・留萌地方', '北海道 十勝地方', '北海道 胆振・日高地方', '北海道 渡島・檜山地方',
                    '青森県 津軽・下北', '青森県 三八上北', 
                    '岩手県 内陸', '岩手県 沿岸',
                    '宮城県 東部', '宮城県 西部',
                    '秋田県', '山形県',
                    '福島県 中通り・浜通り', '福島県 会津',
                    '茨城県', '栃木県',
                    '群馬県 北部','群馬県 南部',
                    '埼玉県', '千葉県',
                    '東京都', '東京都 伊豆諸島北部', '東京都 伊豆諸島南部', '東京都 小笠原諸島',
                    '神奈川県', '山梨県',
                    '長野県 北部', '長野県 南部',
                    '新潟県', '富山県', '石川県', '福井県',
                    '岐阜県 美濃地方', '岐阜県 飛騨地方',
                    '静岡県', '愛知県', '三重県',
                    '滋賀県 南部', '滋賀県 北部',
                    '京都府 北部', '京都府 南部',
                    '大阪府',
                    '兵庫県 南部', '兵庫県 北部',
                    '奈良県', '和歌山県', '鳥取県', '島根県',
                    '岡山県 南部', '岡山県 北部',
                    '広島県 南部', '広島県 北部',
                    '山口県', '徳島県', '香川県', '愛媛県', '高知県','福岡県', '佐賀県',
                    '長崎県 南部・北部・五島', '長崎県 壱岐・対馬'
                    '熊本県', '大分県', '宮崎県',
                    '鹿児島県（奄美地方を除く）', '鹿児島県 奄美地方',
                    '沖縄県 沖縄本島地方', '沖縄県 大東島地方', '沖縄県 宮古島地方', '沖縄県 八重山地方']
    combo_location = ttk.Combobox(main_register, width=28, font=('Yu Gothic',15), values=location_list, background='white', state='readonly')
    combo_location.place(x=210, y=130, height=30)
    if len(location) >= 1:
        combo_location.current(location_list.index(location))

    #日付決定
    #年
    entry_year = ttk.Entry(main_register, width=4, font=('Yu Gothic',15), background='white')
    entry_year.place(x=60, y=205, height=30)
    label_year = ttk.Label(main_register, text='年', font=('Yu Gothic',15), background='white')
    label_year.place(x=110,y=205)
    entry_year.insert(0, frequency_year)
    #月
    month_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    combo_month = ttk.Combobox(main_register, width=2, font=('Yu Gothic',15), values=month_list, background='white', state='readonly')
    combo_month.place(x=135, y=205, height=30)
    label_month = ttk.Label(main_register, text='月', font=('Yu Gothic',15), background='white')
    label_month.place(x=180,y=205)
    if len(frequency_month) > 0:
        combo_month.current(month_list.index(frequency_month))

    #日
    combo_day = ttk.Combobox(main_register, width=2, font=('Yu Gothic',15), values=day_list, background='white', state='readonly')
    combo_day.place(x=205, y=205, height=30)
    label_day = ttk.Label(main_register, text='日', font=('Yu Gothic',15), background='white')
    label_day.place(x=250,y=205)
    if len(frequency_year) > 0:
        if len(frequency_month) > 0:
            days_setting = calendar.monthrange(int(frequency_year), int(frequency_month))[1] + 1
            day_list = []
            for i in range(1, days_setting):
                day_list.append(str(i))
            combo_day['values'] = day_list
            if len(frequency_day) > 0:
                combo_day.current(day_list.index((str(frequency_day))))

    entry_year.bind("<KeyPress>", year_k)
    combo_month.bind("<<ComboboxSelected>>", month_k)

    #時
    hour_list = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    combo_hour = ttk.Combobox(main_register, width=2, font=('Yu Gothic',15), values=hour_list, background='white', state='readonly')
    combo_hour.place(x=275, y=205, height=30)
    label_hour = ttk.Label(main_register, text='時', font=('Yu Gothic',15), background='white')
    label_hour.place(x=320,y=205)
    if len(frequency_hour) > 0:
        combo_hour.current(hour_list.index(frequency_hour))

    #分
    minute_list = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
    combo_minute = ttk.Combobox(main_register, width=2, font=('Yu Gothic',15), values=minute_list, background='white', state='readonly')
    combo_minute.place(x=345, y=205, height=30)
    label_minute = ttk.Label(main_register, text='分から', font=('Yu Gothic',15), background='white')
    label_minute.place(x=390,y=205)
    if len(frequency_minute) > 0:
        combo_minute.current(minute_list.index(frequency_minute))

    #頻度ラジオボタン
    label_notification_frequency = ttk.Label(main_register, text='通知頻度', font=('Yu Gothic',15), background='white')
    label_notification_frequency.place(x=35,y=170)
    var_notification_frequency = StringVar(value = notification_frequency)
    ttk.Style().configure("rdo_notification_frequency.TRadiobutton", foreground="black", background="white", font=('Yu Gothic',15))
    rdo_notification_frequency1 = ttk.Radiobutton(main_register, value='weekday', variable=var_notification_frequency, text='平日', style='rdo_notification_frequency.TRadiobutton', command=rdo_notification_frequency())
    rdo_notification_frequency1.place(x=60, y=235)
    rdo_notification_frequency2 = ttk.Radiobutton(main_register, value='everyday', variable=var_notification_frequency, text='毎日', style='rdo_notification_frequency.TRadiobutton', command=rdo_notification_frequency())
    rdo_notification_frequency2.place(x=125, y=235)
    rdo_notification_frequency3 = ttk.Radiobutton(main_register, value='everyweek', variable=var_notification_frequency, text='毎週', style='rdo_notification_frequency.TRadiobutton', command=rdo_notification_frequency())
    rdo_notification_frequency3.place(x=190, y=235)
    rdo_notification_frequency4 = ttk.Radiobutton(main_register, value='everymonth', variable=var_notification_frequency, text='毎月', style='rdo_notification_frequency.TRadiobutton', command=rdo_notification_frequency())
    rdo_notification_frequency4.place(x=255, y=235)
    rdo_notification_frequency5 = ttk.Radiobutton(main_register, value='everyyear', variable=var_notification_frequency, text='毎年', style='rdo_notification_frequency.TRadiobutton', command=rdo_notification_frequency())
    rdo_notification_frequency5.place(x=320, y=235)
    rdo_notification_frequency6 = ttk.Radiobutton(main_register, value='user_setting', variable=var_notification_frequency, text='ユーザー設定', style='rdo_notification_frequency.TRadiobutton', command=rdo_notification_frequency())
    rdo_notification_frequency6.place(x=385, y=235)

    #頻度のラジオボタンをユーザー設定にしたときに入力できるエントリー
    txt_user_setting_num = ttk.Entry(main_register, width=3, font=('Yu Gothic',13))
    txt_user_setting_num.place(x=405, y=265, height=25)
    if notification_frequency == 'user_setting':
        txt_user_setting_num.insert(0, user_setting_num)

    #頻度のラジオボタンをユーザー設定にしたときに選択できるリストボックス
    dataunit_list = ['分に一回', '時間に一回', '日に一回', '週間に一回', '月に一回', '年に一回']
    combo_user_setting_dataunit = ttk.Combobox(main_register, width=10, font=('Yu Gothic',13), values=dataunit_list, background='white', state='readonly')
    combo_user_setting_dataunit.place(x=440, y=265, height=25)
    if var_notification_frequency.get() == 'user_setting':
        txt_user_setting_num['state'] = 'normal'
        combo_user_setting_dataunit['state'] = 'readonly'
    else:
        txt_user_setting_num['state'] = 'disable'
        combo_user_setting_dataunit['state'] = 'disable'
    if notification_frequency == 'user_setting':
        if len(user_setting_dataunit) > 0:
            combo_user_setting_dataunit.current(dataunit_list.index(user_setting_dataunit))

    #いつの天気予報を取得するかのリスト
    label_acquisition_date1 = ttk.Label(main_register, text='天気予報取得日', font=('Yu Gothic',15), background='white')
    label_acquisition_date1.place(x=35,y=300)
    label_acquisition_date2 = ttk.Label(main_register, text='その日の', font=('Yu Gothic',15), background='white')
    label_acquisition_date2.place(x=210,y=300)
    acquisition_date_list = ['1日後', '2日後', '3日後', '4日後', '5日後', '6日後', '7日後']
    combo_acquisition_date = ttk.Combobox(main_register, width=6, font=('Yu Gothic',15), values=acquisition_date_list, background='white', state='readonly')
    combo_acquisition_date.place(x=295, y=300, height=30)
    if len(acquisition_date) > 0:
        combo_acquisition_date.current(acquisition_date_list.index(acquisition_date))

    #決定ボタン
    button_ok = ttk.Button(main_register, text='OK', command=button_ok_k())
    button_ok.place(x=490, y=375, height=30)

    #閉じるボタン
    button_back = ttk.Button(main_register, text='閉じる', command=button_close_k())
    button_back.place(x=403, y=375, height=30)

    #登録地点削除ボタン
    button_del = ttk.Button(main_register, text='登録地点削除', command=button_del_k())
    button_del.place(x=310, y=375, height=30)

    #決定エラーラベル
    label_ok_error1 = ttk.Label(main_register, text='すべての欄に入力してください。', font=('Yu Gothic',14), foreground='red', background='white')
    label_ok_error2 = ttk.Label(main_register, text='規則に従って入力してください。', font=('Yu Gothic',14), foreground='red', background='white')

def button_select_registration_location_k(select_num):
    def e():
        global registration_location
        registration_location = select_num
        settei_window()
    return e

def button_close_main_k():
    def f():
        main.destroy()
    return f

#登録地点選択
select_label = tk.Label(main, text='設定したい登録地点を選んでください。', font=('Yu Gothic',15), bg='white')
select_label.place(x=110,y=10)
button_select1 = tk.Button(main, text='登録地点①', font=('Yu Gothic',10), bg='gray', fg='white', command=button_select_registration_location_k('1'))
button_select1.place(x=20,y=50)
button_select2 = tk.Button(main, text='登録地点②', font=('Yu Gothic',10), bg='gray', fg='white', command=button_select_registration_location_k('2'))
button_select2.place(x=112,y=50)
button_select3 = tk.Button(main, text='登録地点③', font=('Yu Gothic',10), bg='gray', fg='white', command=button_select_registration_location_k('3'))
button_select3.place(x=204,y=50)
button_select4 = tk.Button(main, text='登録地点④', font=('Yu Gothic',10), bg='gray', fg='white', command=button_select_registration_location_k('4'))
button_select4.place(x=296,y=50)
button_select5 = tk.Button(main, text='登録地点⑤', font=('Yu Gothic',10), bg='gray', fg='white', command=button_select_registration_location_k('5'))
button_select5.place(x=388,y=50)
button_select6 = tk.Button(main, text='登録地点⑥', font=('Yu Gothic',10), bg='gray', fg='white', command=button_select_registration_location_k('6'))
button_select6.place(x=480,y=50)

#閉じるボタン
button_close_main = ttk.Button(main, text='閉じる', command=button_close_main_k())
button_close_main.place(x=485,y=95)

main.mainloop()