import os

class ScoreProcessor:
    def process_score_file(self, file_path: str) -> int:
        file_handle = None

        try:
            file_handle = open(file_path, 'r')
            content = file_handle.read().strip()
            
            score = int(content)
            result = score * 10

            
        except FileNotFoundError:
            print(" The file  was not found. Please check the file path.")
            raise 
            
        except ValueError:
            print("The file contains invalid data. Expected a numeric value.")
            raise  
            
        else:
            print(f"Data processed successfully: {score} * 10 = {result}")
            return result
            
        finally:
            if file_handle is not None:
                file_handle.close()
                print("File cleanup completed")
            else:
                print("File cleanup completed (no file was opened)")