from pay.processor import PaymentProcessor
import pytest

# insert API_Key here temporarily, but never actually do this


def test_api_key_invalid() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge("1249190007575069", 12, 2024, 100)