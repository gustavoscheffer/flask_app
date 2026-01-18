"""Application configuration."""
import os


class Config:
    """Base configuration class."""
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-please-change-in-production'
    
    # Application settings
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development configuration."""
    
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration."""
    
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_test.db'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
