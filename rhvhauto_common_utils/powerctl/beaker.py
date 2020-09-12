import http.client
import ssl
import xmlrpc.client

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


class CookieTransport(xmlrpc.client.SafeTransport):
    """add cookie support"""

    def __init__(self):
        super().__init__()
        self._cookie = []

    def parse_response(self, response: http.client.HTTPResponse):
        self._cookie.append(response.headers.get("Set-Cookie").split(";", 1)[0])
        return super().parse_response(response)

    def send_headers(self, connection: http.client.HTTPConnection, headers) -> None:
        if self._cookie:
            connection.putheader("Cookie", "".join(self._cookie))
        super().send_headers(connection, headers)


class BeakerRPC:
    """"""
    BKR_RPC_URL = "https://beaker.engineering.redhat.com/RPC2"

    def __init__(self, cred: tuple, url: str = None):
        self.url = url or self.BKR_RPC_URL
        self.cred = cred
        self.transport = CookieTransport()

    @property
    def proxy(self):
        return xmlrpc.client.ServerProxy(self.url, transport=self.transport)

    def _login(self):
        self.proxy.auth.login_password(self.cred[0], self.cred[1])

    def _who_am_i(self):
        self.proxy.auth.who_am_i()

    def reserve(self, bkr_name: str):
        self.proxy.systems.reserve(bkr_name)

    def release(self, bkr_name: str):
        self.proxy.systems.release(bkr_name)

    def power(self, action: str, bkr_name: str, clear_netboot: bool = False, force: bool = False, delay: int = 0):
        """
        action (string) – ‘on’, ‘off’, or ‘reboot’
        force (boolean) – whether to power the system even if it is in use
        delay (int or float) – number of seconds to delay before performing the action (default none)
        """
        self.proxy.systems.power(action, bkr_name, clear_netboot, force, delay)
