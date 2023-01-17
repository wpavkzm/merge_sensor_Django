from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RadarSensor
from .models import GateIr

import pymysql
import threading
import time
import requests
import json
from datetime import datetime

pymysql.install_as_MySQLdb()

def get_sensor_connection():
    """Connect to the DataBase"""
    return pymysql.connect(
        host='10.0.0.5',
        user='couter656',
        password='!6_ATdm4ElYPO88AlPHTW4S2xW4VCwCV',
        db='embedded',
        cursorclass=pymysql.cursors.DictCursor
    )


def radar_info(request):
    if request.method == 'POST':
        mac = request.POST['mac_address'].upper()

        if len(mac) < 20:
            Mac = mac

        con = get_sensor_connection()
        cur = con.cursor()

        cur.execute(
            f"Select id, mac_address, motion_detection, detect_time, detect_distance, created_at, radar_rssi, detected_at from `radar_sensor` WHERE mac_address='{Mac}'")
        data = cur.fetchone()
        return render(request, 'blog/main.html', data)

    return render(request, 'blog/main.html')


def ir_info(request):
    if request.method == 'POST':
        serial = request.POST['serial'].upper()

        if len(serial) < 10:
            SERIAL = serial

        con = get_sensor_connection()
        cur = con.cursor()

        cur.execute(
            f"Select id, serial, rx_battery, tx_battery, pushed_at, created_at from `gate_ir` WHERE serial='{SERIAL}'")
        data = cur.fetchone()
        return render(request, 'blog/ir.html', data)

    return render(request, 'blog/ir.html')



# def person_test(request):
#     person_list = RadarInfo.objects.all()
#     context = {'person_list': person_list}
#     return render(request, 'blog/main.html', context)