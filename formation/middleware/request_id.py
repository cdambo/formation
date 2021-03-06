from ..formation import _REQ_HTTP, _REQ_ID
from uuid import uuid4


def request_id(key="x-request-id", idgen=uuid4):
    def request_id_middleware(ctx, next):
        headers = ctx[_REQ_HTTP].headers
        headers[key] = headers.get(key, str(idgen()))
        ctx[_REQ_ID] = headers[key]
        ctx = next(ctx)
        return ctx

    return request_id_middleware
