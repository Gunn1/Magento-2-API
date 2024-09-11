import pytest

def test_import_magento_api_2():
    try:
        import magento_api_2.magento
        import magento_api_2.gui
    except ImportError as e:
        pytest.fail(f"Import failed: {e}")