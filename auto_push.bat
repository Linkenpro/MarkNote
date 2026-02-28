@echo off
:: 设置编码为 UTF-8，确保中文正常显示
chcp 65001 > nul

:: ==========================================
:: 1. 获取时间 (使用 PowerShell，兼容所有新版 Windows)
:: ==========================================
for /f "delims=" %%i in ('powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"') do (
    set "COMMIT_MSG=%%i"
)

echo ==========================================
echo 正在执行自动提交流程...
echo 提交信息将设为：[%COMMIT_MSG%]
echo ==========================================
echo.

:: 检查 Git 是否可用
git --version > nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到 Git 命令。请确认已安装 Git 并配置好环境变量。
    pause
    exit /b 1
)

:: ==========================================
:: 2. 执行 Git 流程
:: ==========================================

echo [步骤 1/3] 正在添加文件 (git add .)...
git add .
if errorlevel 1 goto error_end

echo [步骤 2/3] 正在检查并提交代码...
:: 先检查是否有文件变动
git diff-index --quiet HEAD --
if %errorlevel% equ 0 (
    echo.
    echo [提示] 工作区是干净的，没有检测到文件变化，无需提交。
    echo.
    goto success_end
)

:: 如果有变动，则执行提交
git commit -m "%COMMIT_MSG%"
if errorlevel 1 (
    echo.
    echo [警告] 提交命令执行异常，请检查上方输出。
    goto error_end
)

echo [步骤 3/3] 正在推送到远程 (git push)...
git push
if errorlevel 1 goto error_end

:: ==========================================
:: 3. 成功结束
:: ==========================================
:success_end
echo.
echo ==========================================
echo [成功] 操作已全部完成！
echo ==========================================
echo.
goto wait_close

:: ===4. 错误处理===
:error_end
echo.
echo ==========================================
echo [失败] 操作过程中遇到错误，请检查上方红色信息。
echo 常见原因：
echo 1. 网络断开或 SSH 密钥未配置
echo 2. 远程仓库有更新，请先拉取 (git pull)
echo ==========================================
echo.

:: ===5. 等待用户按回车关闭===
echo 按 [回车键] 关闭窗口...
pause > nul