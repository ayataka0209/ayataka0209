import calendar
from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib
import time
import urllib.request as req
import json
import pickle
import datetime

def save_data():
    with open(r'savedata\data' + str(registration_location) + r'.pickle', mode='wb') as data:
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
    return save_data

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def sendmail():
    if high_low == 'low':
        if int(temps_min) <= int(standard_temps):
            #メールの送り主の設定をする
            smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpobj.starttls()
            smtpobj.ehlo()
            smtpobj.login('ayaha0209@gmail.com', 'gmdpwlpsskckqwun')
            #メールの内容の設定をする
            msg = MIMEText(location + ' で' + timedefines[:10] + '、予想気温が基準の' + str(standard_temps) + '℃以下になる予報が出ました。（最低気温:' + str(temps_min) + '℃）')
            msg['Subject'] = location + ' の予想気温が基準以下になりました。'
            msg['From'] = 'ayaha0209@gmail.com'
            msg['To'] = mailaddress
            msg['Date'] = formatdate()
            #メールを送信する
            smtpobj.sendmail('ayaha0209@gmail.com', mailaddress, msg.as_string())
            smtpobj.close()
    if high_low == 'high':
        if int(temps_max) >= int(standard_temps):
            #メールの送り主の設定をする
            smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpobj.starttls()
            smtpobj.ehlo()
            smtpobj.login('ayaha0209@gmail.com', 'gmdpwlpsskckqwun')
            #メールの内容の設定をする
            msg = MIMEText(location + ' で' + timedefines[:10] + '、予想気温が基準の' + str(standard_temps) + '℃以上になる予報が出ました。（最高気温:' + str(temps_max) + '℃）')
            msg['Subject'] = location + ' の予想気温が基準以上になりました。'
            msg['From'] = 'ayaha0209@gmail.com'
            msg['To'] = mailaddress
            msg['Date'] = formatdate()
            #メールを送信する
            smtpobj.sendmail('ayaha0209@gmail.com', mailaddress, msg.as_string())
            smtpobj.close()

def sendmail_config():
    global high_low, temps_min, temps_max, location, timedefines, mailaddress, standard_temps, frequency_year, frequency_month, frequency_day, frequency_hour, frequency_minute
    if len(location) >= 1:
        #現時点の天気予報のjsonファイルを取得する
        url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/' + location_code + '.json'
        filename = 'tenki.json'
        req.urlretrieve(url, filename)

        #jsonファイル内の天気予報を取得する
        with open('tenki.json', 'r', encoding='UTF=8') as f:
            df = json.load(f)

        print(location)
        if location == '北海道 渡島・檜山地方' or location == '北海道 胆振・日高地方' or location == '北海道 十勝地方' or location == '北海道 上川・留萌地方' or location == '北海道 石狩・空知・後志地方' or location == '北海道 網走・北見・紋別地方' or location == '北海道 宗谷地方' or location == '北海道 釧路・根室地方' or location == '青森県 津軽・下北' or location == '岩手県 内陸' or location == '宮城県 東部' or location == '秋田県' or location == '山形県' or location == '福島県 中通り・浜通り' or location == '茨城県' or location == '栃木県' or location == '群馬県 南部' or location == '埼玉県' or location == '千葉県' or location ==  '東京都' or location == '山梨県' or location == '長野県 北部' or location == '新潟県' or location == '富山県' or location == '石川県' or location == '福井県' or location == '岐阜県 美濃地方' or location == '静岡県' or location == '愛知県' or location == '三重県' or location == '滋賀県 南部' or location == '大阪府' or location == '京都府 南部' or location == '兵庫県 南部' or location == '奈良県' or location == '和歌山県' or location == '鳥取県' or location == '島根県' or location == '岡山県 南部' or location == '広島県 南部' or location == '徳島県' or location == '香川県' or location =='愛媛県' or location == '高知県' or location == '山口県' or location == '福岡県' or location == '佐賀県' or location == '長崎県 南部・北部・五島' or location == '熊本県' or location == '大分県' or location == '宮崎県' or location == '鹿児島県（奄美地方を除く）':
            temps_list = (df[0]['timeSeries'][2]['areas'][0]['temps'])#[temps]の要素
            if len(temps_list) == 2:#[temps]の要素が二個の場合
                timedefines = (df[0]['timeSeries'][0]['timeDefines'][0])#その気温の日
                temps_min = (df[0]['timeSeries'][2]['areas'][0]['temps'][0])#最低気温
                temps_max = (df[0]['timeSeries'][2]['areas'][0]['temps'][1])#最高気温
            if len(temps_list) == 4:#[temps]の要素が四個の場合
                timedefines = (df[0]['timeSeries'][0]['timeDefines'][1])#その気温の日
                temps_min = (df[0]['timeSeries'][2]['areas'][0]['temps'][2])#最低気温
                temps_max = (df[0]['timeSeries'][2]['areas'][0]['temps'][3])#最高気温
            sendmail()
        elif location == '青森県 三八上北' or location == '岩手県 沿岸' or location == '群馬県 北部' or location ==  '東京都 伊豆諸島南部' or location == '長野県 南部' or location == '岐阜県 飛騨地方'or location == '滋賀県 北部' or location == '京都府 北部' or location == '兵庫県 北部' or location == '岡山県 北部':
            temps_list = (df[0]['timeSeries'][2]['areas'][1]['temps'])#[temps]の要素
            if len(temps_list) == 2:#[temps]の要素が二個の場合
                timedefines = (df[0]['timeSeries'][0]['timeDefines'][0])#その気温の日
                temps_min = (df[0]['timeSeries'][2]['areas'][1]['temps'][0])#最低気温
                temps_max = (df[0]['timeSeries'][2]['areas'][1]['temps'][1])#最高気温
            if len(temps_list) == 4:#[temps]の要素が四個の場合
                timedefines = (df[0]['timeSeries'][0]['timeDefines'][1])#その気温の日
                temps_min = (df[0]['timeSeries'][2]['areas'][1]['temps'][2])#最低気温
                temps_max = (df[0]['timeSeries'][2]['areas'][1]['temps'][3])#最高気温
            sendmail()
        elif location == '福島県 会津' or location ==  '東京都 伊豆諸島北部' or location == '長崎県 壱岐・対馬':
            temps_list = (df[0]['timeSeries'][2]['areas'][2]['temps'])#[temps]の要素
            if len(temps_list) == 2:#[temps]の要素が二個の場合
                timedefines = (df[0]['timeSeries'][0]['timeDefines'][0])#その気温の日
                temps_min = (df[0]['timeSeries'][2]['areas'][2]['temps'][0])#最低気温
                temps_max = (df[0]['timeSeries'][2]['areas'][2]['temps'][1])#最高気温
            if len(temps_list) == 4:#[temps]の要素が四個の場合
                timedefines = (df[0]['timeSeries'][0]['timeDefines'][1])#その気温の日
                temps_min = (df[0]['timeSeries'][2]['areas'][2]['temps'][2])#最低気温
                temps_max = (df[0]['timeSeries'][2]['areas'][2]['temps'][3])#最高気温
            sendmail()
        elif location == '宮城県 西部' or location == '東京都 小笠原諸島' or location == '広島県 北部':
            temps_list = (df[0]['timeSeries'][2]['areas'][3]['temps'])#[temps]の要素
            if len(temps_list) == 2:#[temps]の要素が二個の場合
                timedefines = (df[0]['timeSeries'][0]['timeDefines'][0])#その気温の日
                temps_min = (df[0]['timeSeries'][2]['areas'][3]['temps'][0])#最低気温
                temps_max = (df[0]['timeSeries'][2]['areas'][3]['temps'][1])#最高気温
            if len(temps_list) == 4:#[temps]の要素が四個の場合
                timedefines = (df[0]['timeSeries'][0]['timeDefines'][1])#その気温の日
                temps_min = (df[0]['timeSeries'][2]['areas'][3]['temps'][2])#最低気温
                temps_max = (df[0]['timeSeries'][2]['areas'][3]['temps'][3])#最高気温
            sendmail()
        elif location == '鹿児島県 奄美地方':
            temps_list = (df[0]['timeSeries'][2]['areas'][5]['temps'])#[temps]の要素
            if len(temps_list) == 2:#[temps]の要素が二個の場合
                timedefines = (df[0]['timeSeries'][0]['timeDefines'][0])#その気温の日
                temps_min = (df[0]['timeSeries'][2]['areas'][5]['temps'][0])#最低気温
                temps_max = (df[0]['timeSeries'][2]['areas'][5]['temps'][1])#最高気温
            if len(temps_list) == 4:#[temps]の要素が四個の場合
                timedefines = (df[0]['timeSeries'][0]['timeDefines'][1])#その気温の日
                temps_min = (df[0]['timeSeries'][2]['areas'][5]['temps'][2])#最低気温
                temps_max = (df[0]['timeSeries'][2]['areas'][5]['temps'][3])#最高気温
            sendmail()
        else:
            print('error')

def now_day_of_week():
    global frequency_year, frequency_month, frequency_day
    # return datetime.datetime.today().weekday()
    return datetime.date(int(now_year), int(now_month), int(now_day)).weekday()

def frequency_day_of_week():
    global frequency_year, frequency_month, frequency_day
    if len(frequency_year) > 0:
        if len(frequency_month) > 0:
            if len(frequency_day) > 0:
                return datetime.date(int(frequency_year), int(frequency_month), int(frequency_day)).weekday()

while True:
    now_year = datetime.datetime.now().year
    # now_year = 2023
    now_month = datetime.datetime.now().month
    # now_month = 2
    now_day = datetime.datetime.now().day
    # now_day = 1
    now_hour = datetime.datetime.now().hour
    # now_hour = 22
    now_minute = datetime.datetime.now().minute
    # now_minute = 13
    
    for registration_location in range(1,7):
        with open(r'savedata\data' + str(registration_location) + r'.pickle', mode='rb') as data:
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

        if len(frequency_year) > 0:
            if len(frequency_month) > 0:
                if len(frequency_day) > 0:
                    frequency_date = datetime.date(int(frequency_year), int(frequency_month), int(frequency_day))
                    frequency_datetime = datetime.datetime(int(frequency_year), int(frequency_month), int(frequency_day), int(frequency_hour), int(frequency_minute))
                    now_date = datetime.date(int(now_year), int(now_month), int(now_day))
                    # now_date = datetime.date.today()
                    now_datetime = datetime.datetime(int(now_year), int(now_month), int(now_day), int(now_hour), int(now_minute))
                    # now_datetime = datetime.datetime.now()
                    print('now', now_date, 'frequency', frequency_date)

        print('location :', location)
        print('frequency :', frequency_datetime, frequency_day_of_week(), last_sent_mail_year, last_sent_mail_month, last_sent_mail_day, notification_frequency)
        print('now       :', now_datetime, now_day_of_week(), now_year, now_month, now_day, now_minute)
        print('last_sent_mail :', 'day :', last_sent_mail_day, 'month :', last_sent_mail_month, 'year :', last_sent_mail_year)

        if notification_frequency == 'weekday':#確認OK
            if now_day_of_week() == 0 or now_day_of_week() == 1 or now_day_of_week() == 2 or now_day_of_week() == 3 or now_day_of_week() == 4:
                if frequency_date <= now_date:
                    if int(frequency_hour) == now_hour:
                        if int(frequency_minute) == now_minute:
                            if is_int(last_sent_mail_day) == True:
                                if int(last_sent_mail_day) != now_day:
                                    last_sent_mail_day = now_day
                                    save_data()
                                    print('メール送信へ（二回目以降）')
                                    sendmail_config()
                            elif is_int(last_sent_mail_day) == False:
                                last_sent_mail_day = now_day
                                save_data()
                                print('メール送信へ（一回目）')
                                sendmail_config()
        elif notification_frequency == 'everyday':#確認OK
            if frequency_datetime <= now_datetime:
                if int(frequency_hour) == now_hour:
                    if int(frequency_minute) == now_minute:
                        if is_int(last_sent_mail_day) == True:
                            if int(last_sent_mail_day) != now_day:
                                last_sent_mail_day = now_day
                                save_data()
                                print('メール送信へ（二回目以降）')
                                sendmail_config()
                        elif is_int(last_sent_mail_day) == False:
                            last_sent_mail_day = now_day
                            save_data()
                            print('メール送信へ（一回目）')
                            sendmail_config()
        elif notification_frequency == 'everyweek':#確認OK
            if frequency_day_of_week() == now_day_of_week():
                if frequency_date <= now_date:
                    if int(frequency_hour) == now_hour:
                        if int(frequency_minute) == now_minute:
                            if is_int(last_sent_mail_day) == True:
                                if int(last_sent_mail_day) != now_day:
                                    last_sent_mail_day = now_day
                                    save_data()
                                    print('メール送信へ（二回目以降）')
                                    sendmail_config()
                            elif is_int(last_sent_mail_day) == False:
                                last_sent_mail_day = now_day
                                save_data()
                                print('メール送信へ（一回目）')
                                sendmail_config()
        elif notification_frequency == 'everymonth':#確認OK
            if frequency_datetime <= now_datetime:
                print('2', calendar.monthrange(now_year, now_month)[1])
                print(frequency_day)
                if int(frequency_day) == now_day or int(frequency_day) >= calendar.monthrange(now_year, now_month)[1] == now_day:
                    print(1)
                    if int(frequency_hour) == now_hour:
                        print(1)
                        if int(frequency_minute) == now_minute:
                            print(1)
                            if is_int(last_sent_mail_month) == True:
                                print(1)
                                if int(last_sent_mail_month) != now_month:
                                    print(2)
                                    last_sent_mail_month = now_month
                                    save_data()
                                    print('メール送信へ（二回目以降）')
                                    sendmail_config()
                            elif is_int(last_sent_mail_month) == False:
                                print(3)
                                last_sent_mail_month = now_month
                                save_data()
                                print('メール送信へ（一回目）')
                                sendmail_config() 
        elif notification_frequency == 'everyyear': #確認OK
            if frequency_datetime <= now_datetime:
                if int(frequency_month) == now_month:
                    if int(frequency_day) == now_day:
                        if int(frequency_hour) == now_hour:
                            if int(frequency_minute) == now_minute:
                                if is_int(last_sent_mail_year) == True:
                                    if int(last_sent_mail_year) < now_year:
                                        last_sent_mail_year = now_year
                                        print('メール送信へ（二回目以降）')
                                        sendmail_config()
                                elif is_int(last_sent_mail_year) == False:
                                    last_sent_mail_year = now_year
                                    save_data()
                                    print('メール送信へ（一回目）')
                                    sendmail_config()
        elif notification_frequency == 'user_setting':
            if user_setting_dataunit == '分に一回':
                print('user_setting', user_setting_num, user_setting_dataunit)
            if user_setting_dataunit == '時間に一回':
                print('user_setting', user_setting_num, user_setting_dataunit)
            if user_setting_dataunit == '日に一回':
                print('user_setting', user_setting_num, user_setting_dataunit)
            if user_setting_dataunit == '週間に一回':
                print('user_setting', user_setting_num, user_setting_dataunit)
            if user_setting_dataunit == '月に一回':
                print('user_setting', user_setting_num, user_setting_dataunit)
            if user_setting_dataunit == '年に一回':
                print('user_setting', user_setting_num, user_setting_dataunit)
    time.sleep(60)