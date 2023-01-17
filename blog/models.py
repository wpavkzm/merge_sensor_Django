# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Forwindowfunc(models.Model):
#     id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
#     groupid = models.IntegerField(db_column='GroupId', blank=True, null=True)  # Field name made lowercase.
#     amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'ForWindowFunc'


class CameraCount(models.Model):
    camera_ip = models.CharField(max_length=30)
    count = models.IntegerField(blank=True, null=True)
    pushed_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'camera_count'


class CameraSensor(models.Model):
    obj_label = models.CharField(max_length=45)
    distance = models.CharField(max_length=45)
    zed_serial = models.CharField(max_length=45)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'camera_sensor'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DoorSensor(models.Model):
    serial_number = models.CharField(max_length=30)
    value = models.IntegerField()
    alive = models.IntegerField()
    battery = models.IntegerField()
    rssi = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'door_sensor'


class FireSensor(models.Model):
    serial_number = models.CharField(max_length=30)
    value = models.IntegerField()
    alive = models.IntegerField()
    battery = models.IntegerField()
    rssi = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fire_sensor'


class GateBattery(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    mac_address = models.CharField(max_length=12)
    data_id = models.PositiveIntegerField()
    voltage = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'gate_battery'
        unique_together = (('mac_address', 'data_id'),)


class GateData(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    bssid = models.CharField(max_length=12)
    data_id = models.PositiveIntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gate_data'
        unique_together = (('bssid', 'data_id'),)


# class GateDevice(models.Model):
#     uuid = models.CharField(primary_key=True, max_length=16)
#     id = models.BigAutoField(unique=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField(blank=True, null=True)
#     last_seen = models.DateTimeField(blank=True, null=True)
#     alias = models.CharField(max_length=30, blank=True, null=True)
#     bssid = models.CharField(max_length=12, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'gate_device'
#         unique_together = (('uuid', 'id'),)


class GateIr(models.Model):
    serial = models.CharField(max_length=10, blank=True, null=True)
    rx_battery = models.IntegerField(blank=True, null=True)
    tx_battery = models.IntegerField(blank=True, null=True)
    charge = models.IntegerField(blank=True, null=True)
    enter = models.IntegerField(blank=True, null=True)
    exit = models.IntegerField(blank=True, null=True)
    ap_mac = models.CharField(max_length=45, blank=True, null=True)
    rssi = models.IntegerField(blank=True, null=True)
    pushed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gate_ir'


class HubSensor(models.Model):
    serial_number = models.CharField(max_length=30)
    child_sensor_id = models.CharField(unique=True, max_length=30)
    child_sensor_type = models.IntegerField()
    active = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hub_sensor'


class RadarSensor(models.Model):
    mac_address = models.CharField(max_length=20)
    motion_detection = models.IntegerField()
    detect_time = models.IntegerField()
    detect_distance = models.IntegerField()
    created_at = models.DateTimeField()
    radar_rssi = models.IntegerField()
    detected_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'radar_sensor'


class SmartplugSensor(models.Model):
    display_name = models.CharField(max_length=45)
    conn_status = models.IntegerField()
    power = models.IntegerField()
    report_interval = models.IntegerField()
    created_at = models.DateTimeField()
    register_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'smartplug_sensor'


class SmartplugTable(models.Model):
    momen_power = models.FloatField()
    current = models.FloatField()
    powerfactor = models.FloatField()
    cumul_power = models.FloatField()
    temperature = models.FloatField()
    switch_status = models.CharField(max_length=45)
    firmware_version = models.CharField(max_length=45)
    voltage = models.FloatField()
    device_id = models.CharField(max_length=45)
    created_at = models.CharField(max_length=45)
    alive = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'smartplug_table'


class SosSensor(models.Model):
    serial_number = models.CharField(max_length=30)
    value = models.IntegerField()
    alive = models.IntegerField()
    battery = models.IntegerField()
    rssi = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sos_sensor'


class SpotCount(models.Model):
    gateway_mac = models.CharField(max_length=30)
    spot_serial = models.CharField(max_length=30)
    count = models.IntegerField()
    pushed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spot_count'


class Spotv2(models.Model):
    mac_address = models.CharField(max_length=20)
    count = models.IntegerField()
    counted_at = models.DateTimeField()
    published_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spotv2'
        unique_together = (('mac_address', 'counted_at'),)


class TemperSensor(models.Model):
    serial_number = models.CharField(max_length=30)
    value = models.IntegerField()
    alive = models.IntegerField()
    battery = models.IntegerField()
    temper = models.IntegerField()
    humid = models.IntegerField()
    rssi = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'temper_sensor'


class Temporary(models.Model):
    generated_id = models.CharField(max_length=16, blank=True, null=True)
    generated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporary'


# class Test(models.Model):
#     id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
#     groupid = models.IntegerField(db_column='GroupId', blank=True, null=True)  # Field name made lowercase.
#     amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'test'
