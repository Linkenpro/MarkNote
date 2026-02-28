@echo off
:: 1. 设置编码为 UTF-8，防止中文乱码
chcp 65001 > nul

:: 2. 获取当前时间并格式化为 YYYY-MM-DD HH:MM
:: 使用 WMIC 获取标准时间，避免系统区域设置影响
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"

:: 截取年(4)、月(2)、日(2)、时(2)、分(2)
set "YY=%dt:~0,4%"
set "MM=%dt:~4,2%"
set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%"
set "Min=%dt:~10,2%"

:: 组合成目标格式：2026-02-28 09:05
set "COMMIT_MSG=%YY%-%MM%-%DD% %HH%:%Min%"

echo ==========================================
echo 正在执行自动提交流程...
echo 提交信息将设为：[%COMMIT_MSG%]
echo ==========================================
echo.

:: 3. 执行核心逻辑
:: 注意：这里直接调用 git 命令，因为我们在 .bat 中运行，Git Bash 的环境变量通常已加载
:: 如果提示 'git' 不是内部或外部命令，说明需要配置环境变量或使用完整路径

echo [1/3] 正在添加文件 (git add .)...
git add .
if errorlevel 1 goto error

echo [2/3] 正在提交代码 (git commit -m "...")...
git commit -m "%COMMIT_MSG%"
if errorlevel 1 goto error_commit_warning

echo [3/3] 正在推送到远程 (git push)...
git push
if errorlevel 1 goto error

echo.
echo ==========================================
echo ✅ 操作全部成功完成！
echo ==========================================
echo.
goto end

:error_commit_warning
echo.
echo ⚠️ 警告：没有需要提交的变化 (Nothing to commit)。
echo 可能是文件没有变动，或者刚才已经提交过了。
echo.
goto end

:error
echo.
echo ❌ 发生错误！请检查上面的红色报错信息。
echo 常见原因：
echo 1. 网络连接问题 (push 失败)
echo 2. 远程仓库有更新，需要先 pull
echo 3. 文件名包含特殊字符
echo.

:end
:: 4. 关键修改：暂停，等待用户按回车键
echo.
echo 按 [回车键] 关闭窗口...
pause > nul