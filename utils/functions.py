# -*- coding: utf-8 -*-
import logging
import json
import traceback
from exceptions.exception import InvalidParams


def json_loads(stream):
    try:
        return json.loads(stream)
    except json.JSONDecodeError as e:
        raise InvalidParams(reason=str(e))
    except TypeError as e:
        raise InvalidParams(reason=str(e))
    except Exception as e:
        logging.getLogger('werkzeug').error(e)
        logging.getLogger('werkzeug').error(traceback.format_exc())
        raise InvalidParams(reason='Invalid json data - {}'.format(stream))
