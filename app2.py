import websockets
import asyncio
import json

url = 'wss://stream.binance.com:9443/ws/btcusdt@trade'

async def main():
    print('Trying to stablish connection')
    try:
        async with websockets.connect(url) as ws:
            while True:
                msg = await ws.recv()
                print('BTC/USDT:', json.loads(msg)['p'])
    except Exception as e:
        print('Could Connect to the api')
        print(e)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
