#!/usr/bin/env python

import asyncio
import websockets
import gzip
import numpy as np
from PIL import Image
import io
import ssl

async def hello():
    uri = "ws://localhost:8765"
    # async with websockets.connect(uri) as websocket:
    # uri = "wss://0l75dgay7yn-496ff2e9c6d22116-8765-colab.googleusercontent.com"
    # uri = "wss://0l75dgay7yn-496ff2e9c6d22116-8765-colab.googleusercontent.com/"
    async with websockets.connect(uri, origin="*") as websocket:
        img = Image.open('test.png').convert("L")
        data = np.array(img, dtype=np.uint8)
        print('data', data)
        print('data', data.shape)
        
        # data = np.array([1,2,3,4], dtype=np.float32)
        # print(f"{data=}")
        compressed = gzip.compress(data)
        
        # name = input("What's your name? ")
        
        await websocket.send(compressed)
        print(f">>> send_binary")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())