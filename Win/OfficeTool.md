###### 零售许可证（Retail license）

> 产品密钥激活
>
> 通常不使用 Office Tool Plus 进行激活

###### 批量许可证（Volume license）

> 使用 MAK 激活
>
> ```
> 批量激活密钥（Multiple Activation Key）
> MAK 密钥有使用次数上限，可以多次使用并激活 Office。一旦激活成功，激活将永久有效
> ```
>
> 使用 KMS 激活
>
> ```
> 密钥管理服务（Key Management Service）进行激活。通常情况下，一次激活的有效期是 180 天，除非 KMS 指定了另外的策略
> ```

###### vNext 许可证

> Microsoft 365 订阅专属的许可证，由微软服务器生成
>
> vNext 许可证也有一定的设备数量限制，Microsoft 365 个人和家庭版允许五台设备进行使用，Microsoft 365 企业版则可以允许 10 台设备进行使用

###### 激活步骤

- 在许可证管理中安装批量许可证，例如 *Office LTSC 专业增强版 2024 - 批量许可证*

- 在 KMS 管理中设置一个 KMS 主机。KMS 主机可以是一个域名，也可以是一个 IP 地址

  ```
  kms主机地址网查询
  
  https://www.coolhub.top/tech-articles/kms_list.html
  ```

- 点击许可证管理中的**激活**按钮，等待产品激活完毕