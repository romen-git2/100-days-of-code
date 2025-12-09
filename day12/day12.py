class ConfigurationManager:
    _instance = None
    _config_data = None

    def __new__(cls):
        """
        __new__ is called BEFORE __init__
        using it to control the creation of the object
        """
        if cls._instance is None:
            print("Creating the FIRST and ONLY instance...")
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            # initialize state (simulate loading from file)
            cls._instance._load_config()
        else:
            print("Instance already exists. Returning existing one.")

        return cls._instance

    def _load_config(self):
        # simulate reading a JSON file
        print("Loading settings from disk (simulated)...")
        self._config_data = {
            "api_key": "sk-12345",
            "model_version": "gpt-4",
            "max_retries": 3
        }

    def get_setting(self, key):
        return self._config_data.get(key)


# client code
if __name__ == "__main__":
    # create the first instance
    config1 = ConfigurationManager()
    print(f"Config 1 Model: {config1.get_setting('model_version')}")
    print(f"Config 1 ID: {id(config1)}")

    # try to create a second instance
    config2 = ConfigurationManager()
    print(f"Config 2 Model: {config2.get_setting('model_version')}")
    print(f"Config 2 ID: {id(config2)}")

    # prove they are the exact same object
    if config1 is config2:
        print("Config1 and config2 are the same object.")
    else:
        print("They are different objects.")
