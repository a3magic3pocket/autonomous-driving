from PIL import Image
import datetime


class Utils:
    def get_current_velocity(img: Image):
        w, h = img.size
        left_rate = 81 / 1280
        upper_rate = 220 / 720
        right_rate = 125 / 1280
        lower_rate = 236 / 720

        cropped_img = img.crop(
            (
                left_rate * w,
                upper_rate * h,
                right_rate * w,
                lower_rate * h,
            )
        )
        return cropped_img

    def get_current_time_string():
        KST = datetime.timezone(datetime.timedelta(hours=+9))
        now = datetime.datetime.utcnow().replace(tzinfo=KST)
        return now.strftime("%Y-%m-%d_%H+%M+%S+%f")

    def get_screenshot_path(img_dir_path: str = ""):
        return f"{img_dir_path}/screenshot_{Utils.get_current_time_string()}.png"
