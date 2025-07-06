# “Thử Thách Xây Dựng Lớp Học Số”
# Yêu cầu:
# 	1. Tạo file buoi6_1_thuchanh.py.
# 	2. Định nghĩa class Student.
# 	3. Viết __init__ nhận ho_ten, nam_sinh, 	ma_sv và tạo các thuộc tính tương ứng.
# 	4. Tạo 2 đối tượng sv1 (bản thân), sv2 (bạn 	bè).
# 	5. In thông tin của 2 sinh viên ra màn hình.
# Kiểm tra thông tin năm nhập, báo lỗi nếu không hợp lệ
# Tạo thêm phương thức để tính tuổi và in ra số tuổi
nam_hien_tai = 2025

class Student:
    def __init__(self, ho_ten, nam_sinh, ma_sv):
        # Kiểm tra năm sinh có hợp lệ hay không
        if not isinstance(nam_sinh, int):
            raise ValueError("Lỗi: Năm sinh phải là số nguyên.")
        if nam_sinh > nam_hien_tai:
            raise ValueError("Lỗi: Dữ liệu giả dối!!!!")
        if nam_sinh < 1900:
            raise ValueError("Lỗi: Bạn không tồn tại ở server này :)))")
        
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.ma_sv = ma_sv

    def tinh_tuoi(self):
        return nam_hien_tai - self.nam_sinh

    def hien_thi_thong_tin(self):
        print("Họ tên:", self.ho_ten)
        print("Năm sinh:", self.nam_sinh)
        print("Mã sinh viên:", self.ma_sv)
        print("Tuổi:", self.tinh_tuoi())


sv1 = Student("Hân", 2009, "SV001")
sv2 = Student("Linhuan", 2008, "SV002")

sv1.hien_thi_thong_tin()
sv2.hien_thi_thong_tin()
