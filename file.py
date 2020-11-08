# r	Mở file chỉ để đọc.
# r+	Mở file để đọc và ghi.
# w	Tạo một file mới để ghi, nếu file đã tồn tại thì sẽ bị ghi mới.
# w+	Tạo một file mới để đọc và ghi, nếu file tồn tại thì sẽ bị ghi mới.
# a	Mở file để ghi thêm vào cuối file, nếu không tìm thấy file sẽ tạo mới một file để ghi mới.
# a+	Mở file để đọc và ghi thêm vào cuối file, nếu không tìm thấy file sẽ tạo mới một file để đọc và ghi mới.

f = open('text.txt', 'r')
str = f.read()
# ddojc theo dong 
# line1 = f.readline()
# line2 = f.readline()
print("Noi dung file", str)
f.close()

wr = open('file_write.txt', 'w');
info = 'name: Quynh \n';
wr.write(info)
wr.close;



