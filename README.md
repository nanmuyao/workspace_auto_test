# workspace_auto_test
# workspace_auto_test
# workspace_auto_test

# 项目根目录下的conftest.py文件会被自动加载,出现了未自动加载的情况
1. 调试命令pytest --fixtures
2. 调试命令pytest --fixtures --collectonly
3. 删除文件重新创建，因为.pytest_cache文件夹的原因，导致未自动加载