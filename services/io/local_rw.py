# import os
# import json
# from werkzeug.utils import secure_filename



# class LOCAL_RW_TMP:
#     def __init__(self, file) -> None:
#         file_name = secure_filename(file)
#         self.file_path = os.path.join(tempfile.gettempdir(), file_name)


#     def read(self, content='') -> list:
#         try:
#             if os.path.exists(self.file_path):
#                 with open(self.file_path, 'r') as f:
#                     content = f.read()

#             if content == '':
#                 return []
#             return json.loads(content)

#         except Exception:
#             return []


#     def write(self, content: list) -> bool:
#         all_data = content

#         try:
#             with open(self.file_path, 'w', encoding='utf-8') as f:
#                 json.dump(all_data, f, ensure_ascii=False, indent=4)

#             return True

#         except Exception:
#             return False
