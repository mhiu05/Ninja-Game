import pygame

import os

# Đường dẫn gốc đến thư mục chứa các hình ảnh
BASE_IMG_PATH = 'data/images/'

# Hàm để tải 1 hình ảnh từ thư mục
def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    # Loại bỏ nền đen
    img.set_colorkey((0, 0, 0))
    return img

# Hàm để tải 1 loạt hình ảnh từ thư mục
def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images

# Hàm Animation quản lý việc hiển thị và cập nhật animation
class Animation:
    # Hàm khởi tạo
    def __init__(self, images, img_dur = 5, loop = True):
        self.images = images # Danh sách các hình ảnh cho animation
        self.loop = loop # Có lặp lại animation ko
        self.img_duration = img_dur # Số khung hình mỗi ảnh trong animation kéo dài
        self.done = False # Biến đánh dấu khi animation hoàn thành
        self.frame = 0 # Biến đếm số khung hình hiện tại của animation

    # Hàm tạo bản sao của animation, giữ nguyên các thuộc tính
    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)
    
    # Cập nhật trạng thái animation (điều chỉnh frame hiện tại)
    def update(self):
        if self.loop: # Nếu animation đc đặt ở chết độ lặp
            # Cập nhật frame hiện tại, sử dụng phép chia lấy dư để lặp lại khi hết ảnh
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else: # Nếu ko lặp lại
            # Tăng giá trị frame, ko vượt quá tổng số khung hình của animation
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            # Kiểm tra nếu frame đạt đến khung cuối cùng thì đánh dấu animation đã hoàn thành
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True

    # Trả về hình ảnh hiện tải của animation dựa trên frame hiện tại
    def img(self):
        # Chọn hình ảnh tương ứng với chỉ số frame hiện tại
        return self.images[int(self.frame / self.img_duration)]