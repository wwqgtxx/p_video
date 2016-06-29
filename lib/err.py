# err.py, p_video/lib/
'''
error class for p_video


Exception
    PVError
        UnknowError
        ConfigError
            NotSupportURLError
            BridgeError
        NetworkError
            DecodingError
            ParseJSONError
            ParseXMLError
        MethodError
'''

class PVError(Exception):
    pass

class UnknowError(PVError):
    pass
class ConfigError(PVError):
    pass
class NetworkERror(PVError):
    pass
class MethodError(PVError):
    pass

class NotSupportURLError(ConfigError):
    pass
class BridgeError(ConfigError):
    pass

class DecodingError(NetworkError):
    pass
class ParseJSONError(NetworkError):
    pass
class ParseXMLError(NetworkError):
    pass


# end err.py


