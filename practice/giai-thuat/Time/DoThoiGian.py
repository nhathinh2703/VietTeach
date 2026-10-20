from datetime import datetime

# Lấy thời gian (startTime)
startTime = datetime.now()
for i in range(100000):
    print(i)
# Lấy thời gian (endTime)
endTime = datetime.now()

timeProcess = endTime - startTime

print(f'Thời gian bắt đầu: {startTime}')
print(f'Thời gian kết thúc: {endTime}')
print(f'Thời gian thực hiện: {timeProcess}')