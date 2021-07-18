import os
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    api_version: str

    @property
    def amqp_uri(self):
        return os.environ["AMQP_URI"]

    @property
    def api_path(self):
        return f"/api/{self.api_version}"

    @property
    def cluster_rpc_proxy_config(self):
        return {
            'AMQP_URI': self.amqp_uri
        }

@lru_cache()
def get_settings():
    return Settings()