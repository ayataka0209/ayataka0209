import pickle
import datetime

#test



print(123)

print(datetime.datetime.now())

select = input('セーブデータをフォーマットするなら「1」、\nセーブデータに保存されているデータの確認なら「2」を入力し、\n何も行わないならenterキーを押してください')

if select == '1':
    location = ''
    location_code = ''
    standard_temps = ''
    mailaddress = ''
    high_low = ''
    notification_frequency = ''
    user_setting_num = ''
    user_setting_dataunit = ''
    frequency_year = ''
    frequency_month = ''
    frequency_day = ''
    frequency_hour = ''
    frequency_minute = ''
    last_sent_mail_day = ''
    last_sent_mail_month = ''
    last_sent_mail_year = ''
    acquisition_date = ''

    for i in range(1,7):
        with open(r'savedata\data' + str(i) + r'.pickle', mode='wb') as data:
            pickle.dump(location, data)
            pickle.dump(location_code, data)
            pickle.dump(standard_temps, data)
            pickle.dump(mailaddress, data)
            pickle.dump(high_low, data)
            pickle.dump(notification_frequency, data)
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

        print('data' + str(i), 'Completed')
    print('All completed')
if select == '2':
    for i in range(1,7):
        user_setting_num = ''
        user_setting_dataunit = ''
        with open(r'savedata\data' + str(i) + r'.pickle', mode='rb') as data:
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

        print('savedata' + str(i) + '\nlocation', ':', location, '\nlocation_code', ':', location_code, '\nstandard_temps', ':', standard_temps, '\nmailaddress', ':', mailaddress, '\nhigh_low', ':', high_low, '\nnotification_frequency', ':', notification_frequency, '\nuser_setting_num', ':', user_setting_num, '\nuser_setting_dataunit', ':', user_setting_dataunit, '\nfrequency_year', ':', frequency_year, '\nfrequency_month', ':', frequency_month, '\nfrequency_day', ':', frequency_day, '\nfrequency_hour', ':', frequency_hour, '\nfrequency_minute', ':', frequency_minute, '\nlast_sent_mail_day', ':', last_sent_mail_day, '\nlast_sent_mail_month', ':', last_sent_mail_month, '\nlast_sent_mail_year', ':', last_sent_mail_year, '\nacquisition_date', ':', acquisition_date, '\n')