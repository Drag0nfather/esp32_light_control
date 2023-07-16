import time
import os

import json
import utime
import machine
import network
import ds1302
from html_page import home_page, success_setting_schedule, set_time_page, success_set_time, settings_page, \
    success_reset_settings
from MicroWebSrv import MicroWebSrv
import _thread

first_pwm = ''
second_pwm = ''
third_pwm = ''
fourth_pwm = ''

start_time = ''
end_time = ''

start_time_utime = ''
end_time_utime = ''
curr_time_utime = ''

time_range = ''

is_sunrise = ''

wi_fi = False

# rtc init
ds = ds1302.DS1302(machine.Pin(25), machine.Pin(26), machine.Pin(27))

# bind button to 13 pin
button = machine.Pin(13, machine.Pin.IN)


def start_led(pin_num, duty_num):
    pin = machine.Pin(pin_num)
    pwm = machine.PWM(pin, freq=180, duty=duty_num)


def stop_led(pin_num):
    pin = machine.Pin(pin_num)
    pwm = machine.PWM(pin)
    pwm.freq(200000)


def activate_wi_fi():
    ap = network.WLAN(network.AP_IF)
    ap.config(essid='esp32', password='123123123')
    ap.active(True)


def deactivate_wi_fi():
    ap = network.WLAN(network.AP_IF)
    ap.active(False)


def start_server(threaded):
    try:
        mws = MicroWebSrv(port=80, bindIP="192.168.4.1", webPath="/www")
        mws.MaxWebSocketRecvLen = 256
        mws.WebSocketThreaded = False
        mws.Start(threaded=threaded)
    except KeyboardInterrupt:
        pass


def set_end_time(start_time, time_range):
    global end_time
    start_time_utime = utime.mktime((2000, 1, 2, int(start_time[:2]), int(start_time[3:]), 0, 1, 1))
    end_time_utime = utime.gmtime(start_time_utime + int(time_range) * 60 * 60)
    end_time = f'{end_time_utime[3]}:{end_time_utime[4]}'
    if len(end_time) == 4:
        if end_time[1] == ':':
            end_time = '0' + end_time
        elif end_time[2] == ':':
            end_time = end_time.split(':')[0] + ':0' + end_time.split(':')[1]
    elif len(end_time) == 3:
        end_time = '0' + end_time.split(':')[0] + ':0' + end_time.split(':')[1]
    return end_time


def set_utime_time(start, end):
    global start_time_utime, end_time_utime, curr_time_utime
    ds1302_time = ds.date_time()
    curr_time = f'{ds1302_time[4]}:{ds1302_time[5]}'
    hour, minute = curr_time.split(':')
    if len(hour) == 1:
        hour = '0' + hour
        curr_time = hour + ':' + minute
    if len(minute) == 1:
        curr_time = hour + ':0' + minute
    if int(start[:2]) < int(end[:2]):
        start_time_utime = utime.mktime((2000, 1, 2, int(start[:2]), int(start[3:]), 0, 1, 1))
        end_time_utime = utime.mktime((2000, 1, 2, int(end[:2]), int(end[3:]), 0, 1, 1))
        curr_time_utime = utime.mktime((2000, 1, 2, int(curr_time[:2]), int(curr_time[3:]), 0, 1, 1))
        if -86340 <= curr_time_utime - end_time_utime <= -84600:
            curr_time_utime = utime.mktime((2000, 1, 3, int(curr_time[:2]), int(curr_time[3:]), 0, 1, 1))
        if 84600 <= curr_time_utime - start_time_utime <= 86340:
            start_time_utime = time.mktime((2000, 1, 3, int(start[:2]), int(start[3:]), 0, 1, 1))
            curr_time_utime = utime.mktime((2000, 1, 2, int(curr_time[:2]), int(curr_time[3:]), 0, 1, 1))
    elif int(start[:2]) >= int(end[:2]):
        start_time_utime = utime.mktime((2000, 1, 2, int(start[:2]), int(start[3:]), 0, 1, 1))
        end_time_utime = utime.mktime((2000, 1, 3, int(end[:2]), int(end[3:]), 0, 2, 2))
        if int(start[:2]) <= int(curr_time[:2]) >= int(end[:2]):
            curr_time_utime = utime.mktime((2000, 1, 2, int(curr_time[:2]), int(curr_time[3:]), 0, 1, 1))
        elif int(start[:2]) >= int(curr_time[:2]) <= int(end[:2]):
            curr_time_utime = utime.mktime((2000, 1, 3, int(curr_time[:2]), int(curr_time[3:]), 0, 1, 1))
            if 1840 <= curr_time_utime - end_time_utime <= 3540:
                curr_time_utime = utime.mktime((2000, 1, 2, int(curr_time[:2]), int(curr_time[3:]), 0, 1, 1))
        elif int(start[:2]) >= int(curr_time[:2]) >= int(end[:2]):
            curr_time_utime = utime.mktime((2000, 1, 2, int(curr_time[:2]), int(curr_time[3:]), 0, 1, 1))
            if -86340 <= curr_time_utime - end_time_utime <= -84600:
                curr_time_utime = utime.mktime((2000, 1, 3, int(curr_time[:2]), int(curr_time[3:]), 0, 1, 1))


def light_control_by_time(curr_time, start_time, end_time, is_sunrise):
    if is_sunrise == 'off':
        if start_time <= curr_time <= end_time:
            return 0
        else:
            return False
    elif is_sunrise == 'on':
        if start_time <= curr_time <= end_time:
            return 0
        elif curr_time < start_time and start_time - curr_time <= 1800:
            return start_time - curr_time
        elif curr_time > end_time and curr_time - end_time <= 1800:
            return curr_time_utime - end_time_utime
        else:
            return False


def light_by_utime_ticks(ticks, power, led_num):
    increase_num = (850 - power) / 10
    if ticks == 0:
        start_led(led_num, power)
    elif 1800 >= ticks > 1620:
        start_led(led_num, int(850 - increase_num))
    elif 1620 >= ticks > 1440:
        start_led(led_num, int(850 - increase_num * 2))
    elif 1440 >= ticks > 1260:
        start_led(led_num, int(850 - increase_num * 3))
    elif 1260 >= ticks > 1080:
        start_led(led_num, int(850 - increase_num * 4))
    elif 1080 >= ticks > 900:
        start_led(led_num, int(850 - increase_num * 5))
    elif 900 >= ticks > 720:
        start_led(led_num, int(850 - increase_num * 6))
    elif 720 >= ticks > 540:
        start_led(led_num, int(850 - increase_num * 7))
    elif 540 >= ticks > 360:
        start_led(led_num, int(850 - increase_num * 8))
    elif 360 >= ticks > 1:
        start_led(led_num, int(850 - increase_num * 9))
    else:
        stop_led(led_num)

def set_time_to_html_page():
    if len(str(ds.hour())) == 1:
        hour = '0' + str(ds.hour())
    else:
        hour = str(ds.hour())
    if len(str(ds.minute())) == 1:
        minute = '0' + str(ds.minute())
    else:
        minute = str(ds.minute())
    return f'{hour}:{minute}'


@MicroWebSrv.route('/')
def schedule_page(httpClient, httpResponse):
    hour_minute = set_time_to_html_page()
    content = home_page % hour_minute
    httpResponse.WriteResponseOk(headers=None, contentType="text/html", contentCharset="UTF-8", content=content)


@MicroWebSrv.route('/', 'POST')
def schedule_page(httpClient, httpResponse):
    global start_time, end_time, time_range, first_pwm, second_pwm, third_pwm, fourth_pwm, is_sunrise, time_range
    form_data = httpClient.ReadRequestPostedFormData()
    first_pwm = form_data["input1"]
    second_pwm = form_data["input2"]
    third_pwm = form_data["input3"]
    fourth_pwm = form_data["input4"]
    start_time = form_data["input5"]
    is_sunrise = form_data['input7']
    try:
        end_time = form_data["input6"]
    except KeyError:
        pass
    try:
        time_range = form_data['input10']
        end_time = set_end_time(start_time, time_range)
    except KeyError:
        pass
    time_json = json.dumps(
        {
            'start_time': start_time,
            'end_time': end_time,
            'first_pwm': first_pwm,
            'is_sunrise': is_sunrise,
        }
    )
    with open('time_json.json', 'w+') as file:
        file.write(time_json)
    content = success_setting_schedule % (start_time, end_time)
    httpResponse.WriteResponseOk(headers=None, contentType="text/html", contentCharset="UTF-8", content=content)


@MicroWebSrv.route("/set-time")
def main_get_handler(httpClient, httpResponse):
    content = set_time_page
    httpResponse.WriteResponseOk(headers=None, contentType="text/html", contentCharset="UTF-8", content=content)


@MicroWebSrv.route("/set-time", 'POST')
def main_get_handler(httpClient, httpResponse):
    form_data = httpClient.ReadRequestPostedFormData()
    hour, minute = form_data['input6'].split(':')
    ds.hour(int(hour))
    ds.minute(int(minute))
    content = success_set_time
    httpResponse.WriteResponseOk(headers=None, contentType="text/html", contentCharset="UTF-8", content=content)

@MicroWebSrv.route("/settings")
def main_get_handler(httpClient, httpResponse):
    hour_minute = set_time_to_html_page()
    content = settings_page % hour_minute
    httpResponse.WriteResponseOk(headers=None, contentType="text/html", contentCharset="UTF-8", content=content)

@MicroWebSrv.route("/settings", 'POST')
def main_get_handler(httpClient, httpResponse):
    global start_time, end_time, time_range, first_pwm, second_pwm, third_pwm, fourth_pwm, is_sunrise
    start_time = ''
    end_time = ''
    first_pwm = ''
    is_sunrise = ''
    try:
        os.remove('time_json.json')
    except FileNotFoundError:
        pass
    content = success_reset_settings
    httpResponse.WriteResponseOk(headers=None, contentType="text/html", contentCharset="UTF-8", content=content)


def loop():
    while True:
        global first_pwm, second_pwm, third_pwm, fourth_pwm, start_time, end_time, wi_fi, is_sunrise
        time.sleep(1)
        button_state = button.value()
        if button_state == 1 and wi_fi is False:
            activate_wi_fi()
            wi_fi = True
        if button_state == 0 and wi_fi is True:
            deactivate_wi_fi()
            wi_fi = False
        if start_time and end_time:
            set_utime_time(start_time, end_time)
            global start_time_utime, end_time_utime, curr_time_utime
            ticks = light_control_by_time(curr_time_utime, start_time_utime, end_time_utime, is_sunrise)
        else:
            try:
                with open('time_json.json', 'r') as openfile:
                    try:
                        time_json = json.load(openfile)
                    except ValueError:
                        ticks = False
                    if time_json:
                        start_time = time_json['start_time']
                        end_time = time_json['end_time']
                        first_pwm = time_json['first_pwm']
                        is_sunrise = time_json['is_sunrise']
                        continue
            except OSError:
                ticks = False

        if ticks is not False:
            light_by_utime_ticks(ticks, abs(int(first_pwm)), 16)
            # light_by_utime_ticks(ticks, abs(int(second_pwm)), 17)
            # light_by_utime_ticks(ticks, abs(int(third_pwm)), 18)
            # light_by_utime_ticks(ticks, abs(int(fourth_pwm)), 19)
        if ticks is False:
            stop_led(16)
            stop_led(17)
            stop_led(18)
            stop_led(19)

_thread.start_new_thread(start_server, (False,))
_thread.start_new_thread(loop, ())
