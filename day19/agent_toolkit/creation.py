# reusable singleton metaclass
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# generic factory interface
class AgentFactory:
    """
    A simple registry based factory 
    Register classes with a key, then create them dynamically
    """
    def __init__(self):
        self._creators = {}

    def register_format(self, format_type: str, creator_func):
        self._creators[format_type] = creator_func

    def create(self, format_type: str, *args, **kwargs):
        creator = self._creators.get(format_type)
        if not creator:
            raise ValueError(f"Unknown type: {format_type}")
        return creator(*args, **kwargs)
    
    