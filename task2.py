from pathlib import Path
from typing import List, Dict, Any
def get_cats_info(path: str) -> List[Dict[str, str]]:
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    parts = line.split(',')
                    if len(parts) == 3:
                        cat_id, name, age = parts
                        cat_dict = {
                            "id": cat_id,
                            "name": name,
                            "age": age
                        }
                        cats_info.append(cat_dict)
                    else:
                        print(f"Помилка: Некоректна кількість полів у рядку: '{line}'")
                except Exception as e:
                    print(f"Непередбачена помилка при обробці рядка: {e}")
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом: {path}")
        return []
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")
        return []
    return cats_info
test_file_path = "cats_file.txt"
with open(test_file_path, 'w', encoding='utf-8') as f:
    f.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
    f.write("60b90c2413067a15887e1ae2,Vika,1\n")
    f.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
    f.write("60b90c3b13067a15887e1ae4,Simon,12\n")
    f.write("60b90c4613067a15887e1ae5,Tessi,5\n")
    f.write("invalid_line\n")
cats_info = get_cats_info(test_file_path)
print(cats_info)
cats_info_err = get_cats_info("non_existent_cats.txt")