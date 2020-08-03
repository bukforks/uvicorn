import urllib


def get_remote_addr(transport):
    socket_info = transport.get_extra_info("socket")
    if socket_info is not None:
        try:
            info = socket_info.getpeername()
            return (str(info[0]), int(info[1])) if isinstance(info, tuple) else None
        except OSError:
            # This case appears to inconsistently occur with uvloop
            # bound to a unix domain socket.
<<<<<<< HEAD
            family = None
            info = None
        else:
            family = socket_info.family

        if family in (socket.AF_INET, socket.AF_INET6):
            return (str(info[0]), int(info[1]))
        elif hasattr(socket, "AF_UNIX") and family is socket.AF_UNIX:
            if isinstance(info, tuple):
                # fd case
                # <uvloop.PseudoSocket fd=13, family=AddressFamily.AF_UNIX, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 38634)>
                return (str(info[0]), int(info[1]))
            else:
                # unix socket case
                # <uvloop.PseudoSocket fd=21, family=AddressFamily.AF_UNIX, type=SocketKind.SOCK_STREAM, proto=0, laddr=/tmp/gunicorn.sock>
                return None
        return None
=======
            return None

>>>>>>> 0abbb6bf596eb991ea40be1e12db0206af288440
    info = transport.get_extra_info("peername")
    if info is not None and isinstance(info, (list, tuple)) and len(info) == 2:
        return (str(info[0]), int(info[1]))
    return None


def get_local_addr(transport):
    socket_info = transport.get_extra_info("socket")
    if socket_info is not None:
        info = socket_info.getsockname()
<<<<<<< HEAD
        family = socket_info.family
        if family in (socket.AF_INET, socket.AF_INET6):
            return (str(info[0]), int(info[1]))
        elif hasattr(socket, "AF_UNIX") and family is socket.AF_UNIX:
            if isinstance(info, tuple):
                # fd case
                # <uvloop.PseudoSocket fd=13, family=AddressFamily.AF_UNIX, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 38634)>
                return (str(info[0]), int(info[1]))
            else:
                # unix socket case
                # <uvloop.PseudoSocket fd=21, family=AddressFamily.AF_UNIX, type=SocketKind.SOCK_STREAM, proto=0, laddr=/tmp/gunicorn.sock>
                return None
        return None
=======

        return (str(info[0]), int(info[1])) if isinstance(info, tuple) else None
>>>>>>> 0abbb6bf596eb991ea40be1e12db0206af288440
    info = transport.get_extra_info("sockname")
    if info is not None and isinstance(info, (list, tuple)) and len(info) == 2:
        return (str(info[0]), int(info[1]))
    return None


def is_ssl(transport):
    return bool(transport.get_extra_info("sslcontext"))


def get_client_addr(scope):
    client = scope.get("client")
    if not client:
        return ""
    return "%s:%d" % client


def get_path_with_query_string(scope):
    path_with_query_string = urllib.parse.quote(
        scope.get("root_path", "") + scope["path"]
    )
    if scope["query_string"]:
        path_with_query_string = "{}?{}".format(
            path_with_query_string, scope["query_string"].decode("ascii")
        )
    return path_with_query_string
