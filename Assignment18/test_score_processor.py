import pytest
import os
import tempfile
from score_processor import ScoreProcessor

class TestScoreProcessor:
    
    @pytest.fixture
    def processor(self):
        return ScoreProcessor()
    
    @pytest.fixture
    def temp_file(self):
        """Create a temporary file for testing"""
        temp = tempfile.NamedTemporaryFile(mode='w', delete=False)
        temp_path = temp.name
        temp.close()
        
        yield temp_path
        
       
    
    def test_successful_calculation_with_valid_file(self, processor, capsys):
        """Test with your existing score.txt file"""
        # Make sure score.txt has a single number
        result = processor.process_score_file("score.txt")
        
        print(f"Result: {result}")
        assert isinstance(result, int)
        
        captured = capsys.readouterr()
        assert "File cleanup completed" in captured.out
    
    def test_missing_file_handling(self, processor, capsys):
        """Test missing file"""
        with pytest.raises(FileNotFoundError):
            processor.process_score_file("nonexistent_file.txt")
        
        captured = capsys.readouterr()
        assert "File cleanup completed" in captured.out
    
    def test_with_custom_valid_file(self, processor, temp_file, capsys):
        """Test with a custom valid file"""
        # Write a single number
        with open(temp_file, 'w') as f:
            f.write("25")
        
        result = processor.process_score_file(temp_file)
        assert result == 250
        
        captured = capsys.readouterr()
        assert "Data processed successfully" in captured.out
        assert "File cleanup completed" in captured.out
    
    def test_with_invalid_data(self, processor, temp_file, capsys):
        """Test with invalid data (multiple lines)"""
        # Write multiple numbers (this should fail)
        with open(temp_file, 'w') as f:
            f.write("10\n45\n34")
        
        with pytest.raises(ValueError):
            processor.process_score_file(temp_file)
        
        captured = capsys.readouterr()
        assert "File cleanup completed" in captured.out

# Manual test to run directly
if __name__ == "__main__":
    processor = ScoreProcessor()
    try:
        result = processor.process_score_file("score.txt")
        print(f" Success! Result: {result}")
    except Exception as e:
        print(f"Failed: {e}")