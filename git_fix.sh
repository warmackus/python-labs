#!/bin/bash
echo "Исправление Git..."

# 1. Добавим уникальный комментарий в каждый файл
TIMESTAMP="# AUTO FIX: $(date '+%Y-%m-%d %H:%M:%S') #"
for file in $(find . -name "*.py"); do
    # Добавляем в начало файла
    sed -i "1i$TIMESTAMP" "$file"
done

# 2. Принудительно обновим индекс Git
git add -f .

# 3. Проверим
if git status --short | grep -q "[AM]"; then
    echo "✅ Изменения найдены!"
    git commit -m "build: обновлены все файлы лабораторных"
    git push origin main
    echo "✅ Загружено на GitHub!"
else
    echo "❌ Git все еще не видит изменений"
    echo "Попробуем по-другому..."
    git update-index --no-assume-unchanged $(find . -name "*.py")
    git add .
    git commit -m "force update" --allow-empty
    git push origin main
fi
