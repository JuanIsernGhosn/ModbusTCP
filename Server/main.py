from alarmTrigger import AlarmTrigger

if __name__ == '__main__':
    alarm_trigger = AlarmTrigger('192.168.1.1', 502)
    alarm_trigger.start()
    alarm_trigger.send_detection_alarm()
