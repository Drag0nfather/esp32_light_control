import time
import machine
import network
import ds1302
from html_page import home_page, success_setting_schedule, set_time_page, success_set_time
from MicroWebSrv import MicroWebSrv
import _thread


first_pwm = ''
second_pwm = ''
third_pwm = ''
fourth_pwm = ''

start_time = ''
end_time = ''

light_on = False
light_off = True

wi_fi = False

# rtc init
ds = ds1302.DS1302(machine.Pin(25), machine.Pin(26), machine.Pin(27))


# bind button to 13 pin
button = machine.Pin(13, machine.Pin.IN)


def start_led(pin_num, freq_num, duty_num):
    pin = machine.Pin(pin_num)
    pwm = machine.PWM(pin)
    pwm.freq(freq_num)
    pwm.duty(duty_num)


def stop_led(pin_num):
    pin = machine.Pin(pin_num)
    pwm = machine.PWM(pin)
    pwm.deinit()


def activate_wi_fi():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='esp32', password='123123123')


def deactivate_wi_fi():
    ap = network.WLAN(network.AP_IF)
    ap.active(False)


def start_server(threaded):
    try:
        mws = MicroWebSrv(port=80, bindIP="192.168.4.1", webPath="/flash/www")
        mws.MaxWebSocketRecvLen = 256
        mws.WebSocketThreaded = False
        mws.Start(threaded=threaded)
    except KeyboardInterrupt:
        pass


@MicroWebSrv.route("/test2")
def main_get_handler(httpClient, httpResponse):
    content = home_page % ds.date_time()
    httpResponse.WriteResponseOk(headers=None, contentType="text/html", contentCharset="UTF-8", content=content)


@MicroWebSrv.route('/test2', 'POST')
def main_post_handler(httpClient, httpResponse):
    global first_pwm, second_pwm, third_pwm, fourth_pwm, start_time, end_time

    form_data = httpClient.ReadRequestPostedFormData()
    first_pwm = form_data["input1"]
    second_pwm = form_data["input2"]
    third_pwm = form_data["input3"]
    fourth_pwm = form_data["input4"]
    start_time = form_data["input5"]
    end_time = form_data["input6"]

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
    ds.hour(hour)
    ds.minute(minute)
    content = success_set_time
    httpResponse.WriteResponseOk(headers=None, contentType="text/html", contentCharset="UTF-8", content=content)


def loop():
    while True:
        global first_pwm, second_pwm, third_pwm, fourth_pwm, start_time, end_time, light_on, light_off, wi_fi
        time.sleep(5)
        button_state = button.value()
        if button_state == 1 and wi_fi is False:
            activate_wi_fi()
            wi_fi = True
        if button_state == 0 and wi_fi is True:
            deactivate_wi_fi()
            wi_fi = False
        current_datetime_from_ds1302 = ds.date_time()
        curr_time = f'{current_datetime_from_ds1302[4]}:{current_datetime_from_ds1302[5]}'
        if len(curr_time) == 4:
            curr_time = '0' + curr_time
        if curr_time == start_time and light_off:
            start_led(16, 50, int(first_pwm))
            start_led(17, 50, int(second_pwm))
            start_led(18, 50, int(third_pwm))
            start_led(19, 50, int(fourth_pwm))
            light_on = True
            light_off = False
        if curr_time == end_time and light_on:
            stop_led(16)
            stop_led(17)
            stop_led(18)
            stop_led(19)
            light_on = False
            light_off = True


_thread.start_new_thread(start_server, (False,))
_thread.start_new_thread(loop, ())
