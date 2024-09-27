import pandas as pd
from datetime import datetime
import os
from path_config import NORMALIZE_DIR, CONVERTED_DIR
import csv

def convert_data(input_file, output_file):
    # 정규화된 엑셀 파일 읽기
    df = pd.read_excel(input_file, dtype=str)

    # 새로운 형식으로 데이터 프레임 변환
    new_df = pd.DataFrame({
        'driver_id': df['worker'],
        'user_name': df['name'],
        'user_phone': df['phoneNumber'],
        'charge_address': df['address'],
        'car_model': df['carModel'],
        'car_number': df['carNumber'],
        'status': ['waiting'] * len(df),
        'requested_charge_amount': [20] * len(df),
        'charging_reservation_time': df['datetime'],
    })

    # 변환된 데이터를 CSV 파일로 저장
    new_df.to_csv(output_file, index=False, encoding='UTF-8-sig', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    print(f"Success to normalize in ${output_file}.")

def convert_all_files_in_normalized_directory():
    # normalized 디렉토리 내 모든 파일 처리
    for file_name in os.listdir(NORMALIZE_DIR):
        if (file_name.endswith('.xlsx')):
            input_file = os.path.join(NORMALIZE_DIR, file_name)

            # 변환될 파일명 생성
            base_name = os.path.splitext(file_name)[0]
            current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = os.path.join(CONVERTED_DIR, f'converted_{base_name}_{current_time}.csv')

            # 변환 함수 실행
            convert_data(input_file, output_file)

if __name__ == '__main__':
    convert_all_files_in_normalized_directory()