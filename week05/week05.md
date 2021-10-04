# Homework 2

## Phần cơ bản
- Làm quen với bộ lọc mean/median/sharpen
- Làm quen với bộ lọc cạnh

+ `q_1`: Sử dụng file `week05_q1.py`.
Cài đặt bộ lọc mean/median/sharpen, không sử dụng các hàm có sẵn.
Sử dụng các file ảnh ví dụ từ các bài tập trước (`font.png`)
    
+ `q_2`: Dựa trên hàm nhân chập trong file `week05_q2.py`,
cài đặt tính độ lớn của gradient theo công thức ở slide 18 với bộ lọc cạnh sobel,
sử dụng input với tham số `s` là kích thước của nhân gaussian và mode same,
giá trị ngoài ảnh được lấy là 0 


## Phần nâng cao 

+ `q_3`: So sánh tốc độ của hàm convolution trong q_1 và hàm convolution của scipy.signal.convolve2d.
Đề xuất và cài đặt 1 số phương pháp tăng tốc độ: `week05_fast_convolution.py`    

+ `q_4`: Cài đặt thuật toán Canny edge detector theo phần bài giảng,
phát triển dựa trên question 2, `week05_canny.py` 
