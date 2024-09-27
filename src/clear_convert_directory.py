import os
from path_config import CONVERTED_DIR

def delete_all_files_in_converted_directory():
    # normalized 디렉토리 내 모든 파일 삭제
    for file_name in os.listdir(CONVERTED_DIR):
        file_path = os.path.join(CONVERTED_DIR, file_name)

        # 파일인지 확인하고 삭제
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Delete file : {file_path}")

if __name__ == "__main__":
    delete_all_files_in_converted_directory()