

import os
from dotenv import load_dotenv

load_dotenv()


class OpenAIConfig:
    API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

    @classmethod
    def validate(cls):
        """Validate required OpenAI configuration."""
        assert cls.API_KEY, "OPENAI_API_KEY is not set"
        assert cls.MODEL_NAME, "OPENAI_MODEL_NAME is not set"
        

class Config:
    """Global configuration class"""
    OPENAI = OpenAIConfig

    @classmethod
    def validate(cls):
        """Validate all configuration classes."""
        cls.OPENAI.validate()


Config.validate()

config = Config()
