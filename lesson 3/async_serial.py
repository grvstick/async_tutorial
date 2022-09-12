import asyncio
from serial_asyncio import open_serial_connection

async def main():
    port = "/dev/ttyUSB0"
    reader, writer = await open_serial_connection(url=port, baudrate=1_000_000)
    q = asyncio.Queue()
    tasks = asyncio.gather(main_task(q), writer_task(writer, q), reader_task(reader))
    await tasks


async def main_task(send_q: asyncio.Queue):
    while True:
        await send_q.put("HELLO")
        await asyncio.sleep(5)

async def writer_task(writer: asyncio.StreamWriter, q: asyncio.Queue):
    while True:
        msg: str = await q.get()
        packet = msg.encode('utf-8') + b'\n'
        writer.write(packet)
        await writer.drain()

async def reader_task(reader: asyncio.StreamReader):
    while True:
        rx_raw = await reader.readuntil(b'\n')
        data = rx_raw.decode('utf-8')
        process_data(data)

def process_data(data: str):
    print(data)

if __name__ == "__main__":
    asyncio.run(main())