#!/usr/bin/env python
#
# *********     Ping Example      *********
#
#
# Available SCServo model on this example : All models using Protocol SCS
# This example is tested with a SCServo(STS/SMS), and an URT
#

import sys
import os

sys.path.append("..")
from scservo_sdk import *                   # Uses FTServo SDK library

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
# portHandler = PortHandler('/dev/ttyUSB0') #ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"
portHandler = PortHandler('/dev/ttyACM0')

# Initialize PacketHandler instance
# Get methods and members of Protocol
packetHandler = sms_sts(portHandler)
# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()

# Set port baudrate 1000000
if portHandler.setBaudRate(1000000):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()

# Get SCServo model number
# 解锁写入锁，掉电不丢失数据。
STS_ID=1
NEW_STS_ID=2
packetHandler.unLockEprom(STS_ID)
sts_comm_result, sts_error = packetHandler.WriteID(STS_ID, NEW_STS_ID)
if sts_comm_result == COMM_SUCCESS and sts_error == 0:
    print(f"成功将舵机 ID 从 {STS_ID} 修改为 {NEW_STS_ID}")
else:
    print(f"修改失败，错误: {packetHandler.getTxRxResult(sts_comm_result)} / {packetHandler.getRxPacketError(sts_error)}")

# Close port
portHandler.closePort()
