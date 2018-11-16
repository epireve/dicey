import websocket
import warnings; warnings.simplefilter('ignore')
import time
import json

try:
    import thread
except ImportError:
    import _thread as thread

def on_message(ws, message):
    # print(message)
    striped = message.lstrip("42[\"betReceipt\",").rstrip("]")
    iteration = json.loads(striped)
    data = json.dumps(iteration)
    # print(json.dumps(iteration))
    message_list = iteration["payload"]["receipt"]
    print(message_list)
    # print(data)
    # for key, value in dict.items(iteration["payload"]["receipt"]):
    #     print(key,":",value, end=' |', flush=True)
    # print("\n")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(10):
            time.sleep(600)
            ws.send("Hello %d" % i)
        time.sleep(600)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://betdice.one/dice/prod/ws/?EIO=3&transport=websocket",
                              on_open = on_open,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    # ws.on_open = on_open
    ws.run_forever()
