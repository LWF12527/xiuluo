import os
import sys
from pathlib import Path

# 注意parent层级
# 获取当前文件的上两级目录（即项目根目录）
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))


current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)