#-------------------------------------------------------------------------------
# Name:        web server
# Purpose:
#
# Author:      m.j_banitaba
#
# Created:     12/07/2016
# Copyright:   (c) User 2016
# Licence:     GNU
#-------------------------------------------------------------------------------

def main():
    import HTTPHandler
    import SocketServer
    PORT = 80
    server_address=('',PORT)
    handler = HTTPHandler.HTTPHandler
    server = SocketServer.TCPServer(server_address, handler)
    print "serving at port", PORT
    server.serve_forever()
    pass

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        import traceback as tr
        tr.print_exc()
