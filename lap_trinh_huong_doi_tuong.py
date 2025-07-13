# “Thử Thách Xây Dựng Lớp Học Số”
# Yêu cầu:
# 	1. Tạo file buoi6_1_thuchanh.py.
# 	2. Định nghĩa class Student.
# 	3. Viết __init__ nhận ho_ten, nam_sinh, 	ma_sv và tạo các thuộc tính tương ứng.
# 	4. Tạo 2 đối tượng sv1 (bản thân), sv2 (bạn 	bè).
# 	5. In thông tin của 2 sinh viên ra màn hình.
# Kiểm tra thông tin năm nhập, báo lỗi nếu không hợp lệ
# Tạo thêm phương thức để tính tuổi và in ra số tuổi

# buoi6_1_thuchanh.py từ buổi trước hoặc tạo file mới buoi6_2_thuchanh.py.
# Tiếp tục với class Student bạn đã tạo.
# Thêm một thuộc tính mới vào __init__ là diem_tb (điểm trung bình), khởi tạo với giá trị là 0.0.
# Viết một phương thức tên là cap_nhat_diem(self, diem_moi):
# Phương thức này nhận một tham số diem_moi.
# Nó sẽ cập nhật thuộc tính self.diem_tb của sinh viên bằng diem_moi.
# Viết một phương thức tên là kiem_tra_hoc_luc(self):
# Phương thức này sẽ dựa vào self.diem_tb để print ra học lực của sinh viên (ví dụ: “Giỏi” nếu điểm >= 8.0, “Khá” nếu điểm >= 6.5, …).
# Định nghĩa phương thức __str__(self) cho class Student để nó trả về một chuỗi thông tin đẹp mắt, ví dụ: "SV: [Tên], Mã: [Mã SV], Điểm TB: [Điểm TB]".
# Thử nghiệm:
# Tạo một đối tượng sv1 từ class Student.
# print(sv1) để xem kết quả từ __str__ (lúc này điểm là 0.0).
# Gọi phương thức sv1.cap_nhat_diem(8.5).
# print(sv1) lại một lần nữa để xem điểm đã được cập nhật chưa.
# Gọi phương thức sv1.kiem_tra_hoc_luc() để xem học lực.
# commit code lên GitHub.
nam_hien_tai = 2025

class Student:
    def __init__(self, ho_ten, nam_sinh, ma_sv):
        if not isinstance(nam_sinh, int):
            raise ValueError("Lỗi: Năm sinh phải là số nguyên.")
        if nam_sinh > nam_hien_tai:
            raise ValueError("Lỗi: Dữ liệu giả dối!!!!")
        if nam_sinh < 1900:
            raise ValueError("Lỗi: Bạn không tồn tại ở server này :)))")

        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.ma_sv = ma_sv
        self.diem_tb = 0.0 

    def tinh_tuoi(self):
        return nam_hien_tai - self.nam_sinh

    def cap_nhat_diem(self, diem_moi):
        self.diem_tb = diem_moi

    def kiem_tra_hoc_luc(self):
        if self.diem_tb >= 8.0:
            print("Học lực: Giỏi")
        elif self.diem_tb >= 6.5:
            print("Học lực: Khá")
        elif self.diem_tb >= 5.0:
            print("Học lực: Trung bình")
        else:
            print("Học lực: Yếu")

    def __str__(self):
        return f"SV: {self.ho_ten}, Mã: {self.ma_sv}, Tuổi: {self.tinh_tuoi()}, Điểm TB: {self.diem_tb:.2f}"

    def hien_thi_thong_tin(self):
        print(self)

# menu 
sv1 = Student("Hân", 2009, "SV001")

while True:
    print("\n====== MENU ======")
    print("1. Xem thông tin sinh viên")
    print("2. Cập nhật điểm")
    print("3. Kiểm tra học lực")
    print("4. Thoát")

    lua_chon = input("Chọn chức năng (1-4): ")

    if lua_chon == "1":
        print(sv1)
    elif lua_chon == "2":
        try:
            diem = float(input("Nhập điểm mới: "))
            sv1.cap_nhat_diem(diem)
            print("Đã cập nhật điểm.")
        except ValueError:
            print("Điểm không hợp lệ. Vui lòng nhập số.")
    elif lua_chon == "3":
        sv1.kiem_tra_hoc_luc()
    elif lua_chon == "4":
        print("Kết thúc")
        break
    else:
        print(" Không hợp lệ.")
