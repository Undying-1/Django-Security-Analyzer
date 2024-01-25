import os

import bandit
from bandit.core.config import BanditConfig
from bandit.core.manager import BanditManager

from core.settings.base import BASE_DIR

# Путь к папке для анализа
folder_path = os.path.join(BASE_DIR, "media/source_code/")


# Создание экземпляра менеджера Bandit
manager = BanditManager(BanditConfig('bandit.yaml'), agg_type='file')


# Запуск анализа
manager.discover_files( targets='.',recursive=True,excluded_paths='venv')
print(manager.files_list)

# files = bandit.manager._get_files_from_dir(folder_path)
# for file in files:
#     for f in file:
#         print(f)