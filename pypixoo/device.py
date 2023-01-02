from pypixoo.error_messages import errorPrint
import requests


class Pixoo64():
    def __init__(self, **kwargs):
        ep = errorPrint()
        if kwargs.get("ip"):
            self.ip_address = kwargs.get("ip")
        else:
            ep.out("ERROR: Must provide local IP address for device.",
                   br="bright", fg="red")
            raise AttributeError

    def api_wrapper(self, json):
        return requests.post(f"http://{self.ip_address}:80/post",
                             json=json)

    def currentChannel(self):
        req = self.api_wrapper(json={"Command": "Channel/GetIndex"})
        return [req.status_code, req.json()]

    def selectChannel(self, channel):
        channels = {
                        "faces": 0,
                        "cloud": 1,
                        "visualizer": 2,
                        "custom": 3,
                        "blank": 4
                    }
        selectedChannel = channels.get(channel, 4)
        req = self.api_wrapper(
            json={"Command": "Channel/SetIndex",
                  "SelectIndex": selectedChannel})
        return [req.status_code, req.json()]

    def countdown(self, minute, second, status=1):
        req = self.api_wrapper(
            json={"Command": "Tools/SetTimer",
                  "Minute": minute,
                  "Second": second,
                  "Status": status}
        )
        return [req.status_code, req.json()]
