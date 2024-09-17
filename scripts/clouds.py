import random

# 1 đám mây
class Cloud:
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth

    # Cập nhật vị trí của đám mây theo thời gian
    def update(self):
        # Di chuyển đám mây theo hướng ngang với tốc độ đã thiết lập
        self.pos[0] += self.speed

    # Vẽ đám mây lên bề mặt tro chơi
    # offset: Tọa độ của màn hình để điều chỉnh vị trí đám mây theo nền
    def render(self, surf, offset = (0, 0)):
        # Tính toán vị trí hiển thị của đám mây dựa trên offset và depth
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
        
        # Vẽ hình ảnh của đám mây lên bề mặt, với việc điều chỉnh tọa độ để đám mây lặp lại khi ra khỏi màn hình
        surf.blit(
            self.img, 
            (
                render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(),
                render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()
            )
        )

# Nhiều đám mây
class Clouds:
    def __init__(self, cloud_images, count = 16):
        self.clouds = []

        # Tạo ra số lượng đám mây đã chỉ định (mặc định là 16)
        for i in range(count):
            # Mỗi đám mây có vị trí ngẫu nhiên, hình ảnh ngẫu nhiên, tốc độ và độ sâu khác nhau
            self.clouds.append(
                Cloud(
                    (random.random() * 99999, random.random() * 99999), # Vị trí ngẫu nhiên của đám mâ
                    random.choice(cloud_images), # Hình ảnh ngẫu nhiên từ danh sách hình ảnh đám mây
                    random.random() * 0.05 + 0.05, # Tốc độ ngẫu nhiên (tron khoảng 0.05 - 1)
                    random.random() * 0.6 + 0.2 # Độ sâu ngẫu nhiên (trong khoảng 0.2 - 0.8)
                )
            )
            
        # Sắp xếp các đám mây theo depth để tạo ra hiệu ứng lớp khi hiển thị
        self.clouds.sort(key = lambda x : x.depth)

    # Cập nhật lại vị trí của tất các các đám mây
    def update(self):
        # Duyệt qua từng đám mây và gọi hàm update để di chuyển đám mây
        for cloud in self.clouds:
            cloud.update()

    # vẽ tất cả đám mây
    def render(self, surf, offset = (0, 0)):
        for cloud in self.clouds:
            cloud.render(surf, offset = offset)

