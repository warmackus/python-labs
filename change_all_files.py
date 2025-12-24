# File ID: c86b2fa8 | Updated: 2025-12-22 22:06:48

#!/usr/bin/env python3

import os

import hashlib

from datetime import datetime



def get_file_hash(filepath):

    """Получить хеш файла"""

    with open(filepath, 'rb') as f:

        return hashlib.md5(f.read()).hexdigest()



def modify_file(filepath):

    """Изменить файл уникальным образом"""

    with open(filepath, 'r', encoding='utf-8') as f:

        content = f.read()

    

    # Добавим уникальный комментарий в начало

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_hash = get_file_hash(filepath)[:8]

    unique_comment = f"# File ID: {file_hash} | Updated: {timestamp}\n"

    

    # Если комментарий уже есть, заменим его

    lines = content.split('\n')

    if lines[0].startswith('# File ID:'):

        lines[0] = unique_comment.strip()

    else:

        lines.insert(0, unique_comment.strip())

    

    new_content = '\n'.join(lines)

    

    # Запишем обратно

    with open(filepath, 'w', encoding='utf-8') as f:

        f.write(new_content)

    

    return filepath



# Изменяем ВСЕ .py файлы

modified_count = 0

for root, dirs, files in os.walk('.'):

    for file in files:

        if file.endswith('.py'):

            filepath = os.path.join(root, file)

            try:

                modified = modify_file(filepath)

                print(f"✓ Изменен: {modified}")

                modified_count += 1

            except Exception as e:

                print(f"✗ Ошибка с {filepath}: {e}")



print(f"\n✅ Изменено файлов: {modified_count}")

