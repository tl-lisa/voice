import websocket
import _thread
import time

def on_message(ws, message):
    print('messate')
    print(message)

def on_error(ws, error):
    print('error')
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed 123 ###")

def on_open(ws):
    print('jump into open')
    def run(*args):
        print('in open run')
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    _thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://35.234.17.150/socket/websocket?token=master12token&nonce=master12nonce",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever()
