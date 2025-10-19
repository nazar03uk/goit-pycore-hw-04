from pathlib import Path
def total_salary(path: str) -> tuple[float, float]:
    total_sum = 0
    num_developers = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    _, salary_str = line.split(',')
                    salary = float(salary_str)
                    total_sum += salary
                    num_developers += 1
                except ValueError:
                    print(f"Помилка: Неправильний формат даних у рядку: '{line}'")
                except Exception as e:
                    print(f"Непередбачена помилка при обробці рядка: {e}")
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом: {path}")
        return 0.0, 0.0
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")
        return 0.0, 0.0
    average_salary = total_sum / num_developers if num_developers > 0 else 0.0
    return total_sum, average_salary
test_file_path = "salary_file.txt"
with open(test_file_path, 'w', encoding='utf-8') as f:
    f.write("Alex Korp,3000\n")
    f.write("Nikita Borisenko,2000\n")
    f.write("Sitarama Raju,1000\n")
    f.write("Broken Data\n")
    f.write("Jane Doe,5000\n")
total, average = total_salary(test_file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
total_err, average_err = total_salary("non_existent_file.txt")