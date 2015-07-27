from cffi import FFI
ffi = FFI()

ffi.set_source(
    "magnetic._internals._sane_fromfd",
    """
    #include <sys/types.h>
    #include <sys/socket.h>

    int magnetic_get_sock_family(int sockfd, int * family){
        struct sockaddr_storage addr;
        socklen_t addr_s;
        int flag = getsockname(sockfd, (struct sockaddr *) &addr, &addr_s);
        *family = (int) addr.ss_family;
        return flag;
    }

    int magnetic_get_sock_type(int sockfd, int * type){
        int socktype;
        socklen_t socklen = sizeof(socktype);
        int flag = getsockopt(sockfd, SOL_SOCKET, SO_TYPE, &socktype, &socklen);
        *type = socktype;
        return flag;
    }

    int magnetic_get_sock_proto(int sockfd, int * proto){
        int sockproto;
        socklen_t socklen = sizeof(sockproto);
        int flag = getsockopt(sockfd, SOL_SOCKET, SO_PROTOCOL, &sockproto, &socklen);
        *proto = sockproto;
        return flag;
    }

    """,
    libraries=[]
)

ffi.cdef("""
    int magnetic_get_sock_family(int sockfd, int * family);
""")

ffi.cdef("""
    int magnetic_get_sock_type(int sockfd, int * type);
""")

ffi.cdef("""
    int magnetic_get_sock_proto(int sockfd, int * proto);
""")

if __name__ == "__main__":
    ffi.compile()
