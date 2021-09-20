# Homework 2

## Phần cơ bản

Các bạn submit bằng file: `week03.py`,

Dữ liệu các bạn tải về trên website môn học.
Mỗi task được lập trình bởi 1 hàm trong file `week03.py` 

+ `q_0`: Làm quen với tham số input/output trong python
(`https://docs.python.org/3/howto/argparse.html`)

`python.py week03.py -i input_file -o output_file -q 0`


+ `q_1`: Đọc vào file với 3 kênh màu BGR input từ với đường dẫn.
Áp dụng thuật toán đổi về kênh màu gray và ghi ra file output.

`python.py week03.py -i input_file -o output_file -q 1`


+ `q_2`: Đọc vào file input từ với đường dẫn.
Áp dụng Histogram Equalization để để chuẩn hóa ảnh và ghi ra file output.
Đầu ra là ảnh đã được chuẩn hóa.   

`python.py week03.py -i input_file -o output_file -q 2`


+ Tìm hiểu các hàm tương ứng của opencv.

## Phần nâng cao 

Các bạn có thể chọn 1 trong 2 task sau:

+ `week03_CLAHE.py`: cài đặt thuật toán CLAHE, tham khảo ở
`http://www.realtimerendering.com/resources/GraphicsGems/gemsiv/clahe.c`.
So sánh với thuật toán cân bằng Historgram gốc.   

+ `week03_histogram_matching`: Tìm hiểu và cài đặt thuật toán
`histogram matching`. Input đầu vào là ảnh và ảnh reference.