# coding=utf-8
__author__ = 'lxn3032'


class RpcException(Exception):
    def __init__(self, session_id, reqid, msg):
        super(RpcException, self).__init__(msg)
        self.session_id = session_id
        self.reqid = reqid


class RpcTimeoutException(RpcException):
    def __init__(self, session_id, reqid):
        msg = 'rpc timeout on {}/{}'.format(session_id, reqid)
        super(RpcTimeoutException, self).__init__(session_id, reqid, msg)


class RpcRemoteException(RpcException):
    def __init__(self, resp):
        errors = resp['errors']
        session_id = resp['session_id']
        reqid = resp['id']
        error_type = errors['type']
        tb = errors['tb']
        msg = '{}: {}\n\n|--   Remote Traceback   --|\n\n{}\n\n|--   Remote Traceback end   --|'.format(error_type, errors['message'], tb)
        super(RpcRemoteException, self).__init__(session_id, reqid, msg)
        self.error_type = error_type
        self.stack = errors['stack']
        self.traceback = errors['tb']
        self.message = errors['message']