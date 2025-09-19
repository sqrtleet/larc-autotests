from datetime import datetime


def to_query_params(payload: dict) -> dict:
    def conv(v):
        if isinstance(v, bool):
            return 'true' if v else 'false'
        if isinstance(v, (int, float)):
            return str(v)
        if isinstance(v, datetime):
            iso = v.isoformat(timespec='milliseconds')
            if not iso.endswith('Z'):
                iso += 'Z'
            return iso
        return v

    out = {}
    for k, v in payload.items():
        if isinstance(v, dict):
            for kk, vv in v.items():
                out[f'{k}.{kk}'] = conv(vv)
        else:
            out[k] = conv(v)
    return out
