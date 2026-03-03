import pytest
from unittest.mock import patch
from langchain_core.documents import Document
from src.ingest import load_and_chunk_pdf


def test_missing_file_raises_error():
    """Tests that the function properly catches missing files."""
    with pytest.raises(FileNotFoundError):
        load_and_chunk_pdf("data/fake_non_existent_file.pdf")


@patch("src.ingest.PyPDFLoader")
@patch("src.ingest.os.path.exists")
def test_actual_chunking_logic(mock_exists, mock_pdf_loader):
    """Tests the actual function using mock/dummy data."""
    # 1. Force the OS check to pass so it doesn't raise an error
    mock_exists.return_value = True

    dummy_document = [Document(page_content="Car Engine. " * 50)]
    mock_pdf_loader.return_value.load.return_value = dummy_document

    chunks = load_and_chunk_pdf("fake_manual.pdf", chunk_size=50, chunk_overlap=10)

    assert len(chunks) > 1, "Should create multiple chunks"
    assert len(chunks[0].page_content) <= 50, "Chunk size should respect the limit"
