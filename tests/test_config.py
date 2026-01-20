"""Tests for application configuration."""
from app.config import Config, DevelopmentConfig, ProductionConfig, TestingConfig


class TestConfig:
    """Test configuration classes."""

    def test_base_config(self):
        """Test base configuration."""
        assert Config.SQLALCHEMY_TRACK_MODIFICATIONS is False
        assert Config.DEBUG is False
        assert Config.TESTING is False

    def test_development_config(self):
        """Test development configuration."""
        assert DevelopmentConfig.DEBUG is True
        assert issubclass(DevelopmentConfig, Config)

    def test_production_config(self):
        """Test production configuration."""
        assert ProductionConfig.DEBUG is False
        assert issubclass(ProductionConfig, Config)

    def test_testing_config(self):
        """Test testing configuration."""
        assert TestingConfig.TESTING is True
        assert TestingConfig.SQLALCHEMY_DATABASE_URI == 'sqlite:///test_test.db'
        assert issubclass(TestingConfig, Config)

    def test_config_has_secret_key(self):
        """Test that configuration has a secret key."""
        assert hasattr(Config, 'SECRET_KEY')
        assert Config.SECRET_KEY is not None

    def test_config_has_database_uri(self):
        """Test that configuration has database URI."""
        assert hasattr(Config, 'SQLALCHEMY_DATABASE_URI')
        assert Config.SQLALCHEMY_DATABASE_URI is not None
