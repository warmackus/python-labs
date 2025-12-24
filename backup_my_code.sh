#!/bin/bash
echo "Создаю backup твоего кода..."

# Создаем папку для бэкапа
BACKUP_DIR="$HOME/python-labs-my-code-$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# Копируем ВСЕ .py файлы
cp -r ~/python-labs/* "$BACKUP_DIR/"

echo "✅ Код сохранен в: $BACKUP_DIR"
echo "Можешь сравнить:"
echo "diff -r ~/python-labs/ \"$BACKUP_DIR/\" | head -20"
