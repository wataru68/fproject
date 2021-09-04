#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
# OSに依存している様々な機能を利用するためのモジュール
import sys
# Pythonのインプリンタや実行環境に関する情報を扱うためのライブラリ


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fproject.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    # 上記により
    # プロジェクトの設定ファイルが読み込まれる
    # 指定されたコマンドが検索される
    # コマンドを実行


if __name__ == '__main__':
    main()
