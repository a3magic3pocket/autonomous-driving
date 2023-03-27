#!/usr/bin/env python

from PIL import Image
from crnn import detect as crnn_detect
import asyncio
import websockets
import gzip
import numpy as np
import sys
import io


async def hello(websocket):
    compressed = await websocket.recv()
    data = gzip.decompress(compressed)
    buffer = io.BytesIO(data)
    img = Image.open(buffer)
    velocity_img = await get_current_velocity(img)
    # velocity_img = img
    # velocity_img.show()

    greeting = f"Hello! got {velocity_img}"
    print(crnn_detect.detect(velocity_img, './crnn/checkpoints/exp1/best.ckpt'))

    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    # about 100MB
    max_size = 100 * 2**20
    assert sys.maxsize > max_size
    print(f'{sys.maxsize=}')
    print(f'{max_size=}')
    
    async with websockets.serve(
        hello,
        "localhost",
        8765,
        max_size=max_size,
    ):
        await asyncio.Future()  # run forever

async def get_current_velocity(img):
    w, h = img.size
    left_rate = 81 / 1280
    upper_rate = 220 / 720
    right_rate = 125 / 1280
    lower_rate = 236 / 720
    
    return img.crop((
        left_rate * w,
        upper_rate * h,
        right_rate * w,
        lower_rate * h,
    ))
    
if __name__ == "__main__":
    asyncio.run(main())
