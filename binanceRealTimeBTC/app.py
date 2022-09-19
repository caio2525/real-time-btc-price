import asyncio
from binance import AsyncClient, BinanceSocketManager
import sys

api_key = 'ygLyQROn7y7SdNvMoJepOdhZJV4OJUPeq1hhYe2929CopY2ZqGREhnWnVy1FQMEs'

api_secret = 'aACSH2BCvZKNwp7bbQR5vtMOJAGMvJ8SUB2Cdfw5sBF1g8sRjhRevQfu6EYpssKC'

async def main():
    client = await AsyncClient.create(api_key, api_secret)
    bm = BinanceSocketManager(client)
    # start any sockets here, i.e a trade socket
    ts = bm.trade_socket('BTCUSDT')
    # then start receiving messages
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            print('BTC/USDT:', res['p'])

    await client.close_connection()

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
