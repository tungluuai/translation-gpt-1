<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN - ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH</h3>

  <p align="center">
    NEURAL MACHINE TRANSLATION WITH GPT-1
    <br />
</div>


## GIỚI THIỆU ĐỒ ÁN
- Đồ án "Neural Machine Translation With GPT-1" là một dự án trong lĩnh vực dịch máy sử dụng mô hình GPT-1 với mô hình Transformer là bộ khung chính. Mục tiêu chính của dự án là xây dựng một hệ thống dịch máy tự động hiệu quả dựa trên việc phân tích bài báo: "Improving Language Understanding by Generative Pre-Training" - Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever.

Trình bày sơ lược đồ án.
-	Mục tiêu: dịch từ tiếng Anh ( English ) sang tiếng Việt ( Vietnamese )

## Công nghệ sử dụng 
Ngôn ngữ: Python

Thư viện, framework: Flask, flask, Flask-SQLAlchemy, transformers, torchvision, sentencepiece, sacremoses

## Môi trường thực thi và phát triễn 
1. Python
2. Visual studio code
 
## Cài đặt
1. Clone the repo
  ```sh
  git clone https://github.com/tungluu210201/translation-gpt-1.git
  ```
2. Tạo thư mục theo đường dẫn
  - app\flaskr\model_translation\data
  - vào đường link sau là tải file transformer_model.pth là file trọng số về 
    + https://drive.google.com/drive/u/0/folders/1YQ0ZBsQ8iVX0rZvYgl3PL4x2xKOlw_hX
  - copy bỏ vào thư mục mới tạo ở trên trên
  - nguyên nhân không bỏ vào git là, git không chấp nhận những file lớn hơn 100MB

3. Mở terminal ngay thư mục app

  **Lúc khởi tạo (khi chưa có folder venv)

  B1 : 
  ```sh
  py -m venv venv
  ```
  B2 : 
  ```sh
  venv\Scripts\activate
  ```
  B3 : 
  ```sh
  pip install -r requirements.txt
  ```
  B4 : 
  ```sh
  flask --app flaskr run --debugger --reload --host=0.0.0.0 --port=4201 
  ```
  + chạy với port 4200 (puplic), nếu muốn public ra ngoài phải config lại router
  
  
  ** Lúc khởi tạo (khi có folder venv)// mở terminal ngay thư mục app

  B1 : 
  ```sh
  venv\Scripts\activate
  ```
  B2 :
  ```sh
  flask --app flaskr run --debugger --reload --host=0.0.0.0 --port=4201 
  ```
  + chạy với port 4200 (puplic), nếu muốn public ra ngoài phải config lại router
3. Sau khi chạy có thể truy cập vào đường link: http://localhost:4201/

4. Hoàn thành.

### KẾT THÚC.

<br/>

