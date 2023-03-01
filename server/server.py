#!/usr/bin/env python

import asyncio
import websockets
import gzip
import numpy as np

async def hello(websocket):
    compressed = await websocket.recv()
    data = gzip.decompress(compressed)
    converted = np.frombuffer(data, dtype=np.float32)

    greeting = f"Hello! got {converted}"

    await websocket.send(greeting)
    print(f">>> {greeting}")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())