import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received {} from {}".format(message, addr))

    writer.write(data)
    await  writer.drain()

    print("Sent {} to {}".format(message, addr))
    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, "localhost", 8888)
    addr = server.sockets[0].getsockname()
    print("Serving on {}".format(addr))
    async with server:
        await server.serve_forever()

asyncio.run(main())
