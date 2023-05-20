import yaml

class Config:
    def __init__(self, path):
        with open(path, 'r', encoding="utf-8") as f:
            self.d = yaml.safe_load(f)

    def set_config(self, d=None, **kwargs):
        def funcdict(d=None, **kwargs):
            if d is not None:
                funcdict.__dict__.update(d)
            funcdict.__dict__.update(kwargs)
            return funcdict.__dict__
        funcdict(self.d, **kwargs)
        return funcdict