from PIL import Image
import os

def get_current_velocity(img, name):
    w, h = img.size
    left_rate = 81 / 1280
    upper_rate = 220 / 720
    right_rate = 125 / 1280
    lower_rate = 236 / 720
    
    cropped_img = img.crop((
        left_rate * w,
        upper_rate * h,
        right_rate * w,
        lower_rate * h,
    ))
    
    cropped_img.save(f'cropped/{name}')

if __name__ == "__main__":
    img_dir_name = 'test_images'
    names = os.listdir(img_dir_name)
    for i, name in enumerate(names):
        path = f'{img_dir_name}/{name}'
        try:
            img = Image.open(path)
            # get_current_velocity(img, name)
            get_current_velocity(img, f'_{i}.png')
        except:
            print(path)
            continue
        
    