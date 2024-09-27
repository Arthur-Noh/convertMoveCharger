import pandas as pd
from datetime import datetime
import os
from path_config import RAW_DIR, NORMALIZE_DIR

def normalize_data(input_file, output_file):
    # 엑셀 파일 읽기
    df = pd.read_excel(input_file, dtype=str)

    # column 정규화
    df['address'] = df['address'] + ', ' + df['detailAddress']

    # 불필요 column 제거
    df = df.drop(columns=['detailAddress', 'location', 'memo', 'reservationId'])

    # 정규화 데이터 저장
    df.to_excel(output_file, index=False)
    print(f"Success to normalize in {output_file}.")

def process_all_files_in_raw_directory():

    # raw 디렉토리 내 모든 파일 처리하기
    for file_name in os.listdir(RAW_DIR):
        if (file_name.endswith('.xlsx')):
            input_file = os.path.join(RAW_DIR, file_name)

            # 정규화 파일명 생성
            base_name = os.path.splitext(file_name)[0] # 파일명에서 확장자 제거
            current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = os.path.join(NORMALIZE_DIR, f'normalized_{base_name}_{current_time}.xlsx')

            #정규화 함수 호출
            normalize_data(input_file, output_file)

if __name__ == "__main__":
    process_all_files_in_raw_directory()
