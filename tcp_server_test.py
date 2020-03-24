import socket
import time

if "__main__" == __name__:
    server = socket.socket()
    host = "127.0.0.1"
    # host = "10.10.23.108"
    port = 6000

    print(host, "  ", port)
    print("Ready!")

    server.bind((host, port))
    server.listen(5)
    client, addr = server.accept()
    while True:
        # client, addr = server.accept()
        temp = input()
        if temp == "1":
            s = time.time()
            # sendmessage = r"D:\pyWorks\py_tcp_commu\rot180.dcm D:\pyWorks\py_tcp_commu"

            # sendmessage = r"D:\pyWorks\py_tcp_commu\rot90.dcm D:\pyWorks\py_tcp_commu"

            sendmessage = r'D:\pyWorks\body_chest_pos\py_position_detection\testdcm\0.dcm D:\pyWorks\body_chest_pos\py_position_detection\testdcm'
            sendmessage = r'D:\pyWorks\body_chest_pos\py_position_detection\testdcm\0.dcm'

            # sendmessage = r"E:\20190304\Dicom\2.16.840.1.114492.36110150206246011.19063100552.73680.21\2.16.840.1.114492.36110150206246011.19063100605.73680.22\2.16.840.1.114492.36110150206246011.19063105541.27480.3663.dcm E:\20190304\Dicom\2.16.840.1.114492.36110150206246011.19063100552.73680.21\2.16.840.1.114492.36110150206246011.19063100605.73680.22"


            # sendmessage = r"D:\FMI-Coding\Position_training\TestWithCT\1.DCM"
            # sendmessage = r"D:\FMI-Coding\Position_training\TestWithCT\1.DCM D:\FMI-Coding\Position_training\TestWithCT"
            # sendmessage = r"D:\FMI-Coding\Position_training\py_position_detection\testdcm\0.dcm D:\FMI-Coding\Position_training\py_position_detection\data -show"

            # sendmessage = r"C:\Users\scintistar\Desktop\bed_locs\py_position_detection\test\80.dcm C:\Users\scintistar\Desktop\bed_locs\py_position_detection\test -show"
            client.send(sendmessage.encode(encoding="utf8"))

            rec = client.recv(1024).decode()
            print(rec)
            e = time.time()
            print(e - s)
        elif temp == "2":
            s = time.time()
            sendmessage = r"Environment Init"
            client.send(sendmessage.encode(encoding="utf8"))

            rec = client.recv(1024).decode()
            print(rec)
            e = time.time()
            print(e - s)

        # server.close()

