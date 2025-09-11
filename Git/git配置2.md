```
git config --global user.name "yh-cocanie"
git config --global user.email cocanadalope@gmail.com
```

```
You don't have any public SSH keys in your GitHub account. You can add a new public key, or try cloning this repository via HTTPS.
```

1. cmd命令行

```
# 如果系统不支持ED25519，使用RSA
ssh-keygen -t rsa -b 4096 -C "cocanadalope@gmail.com"
```

```
Your identification has been saved in C:\Users\源恒/.ssh/id_rsa
Your public key has been saved in C:\Users\源恒/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:M3MWENV8EFohdgw/8cJcNVowKwUXCA2+oe4Fi3SGRbw cocanadalope@gmail.com
The key's randomart image is:
+---[RSA 4096]----+
|      ..o=O*XX++.|
|      ...o @*+* .|
|       ..oo.*+.  |
|      oE. o..o   |
|     o =S.o      |
|    . = o*       |
|     . o .       |
|      . .        |
|       .         |
+----[SHA256]-----+
```

###### 启动SSH代理并添加密钥

```
# 启动SSH代理
eval "$(ssh-agent -s)"

# 添加SSH私钥到代理
ssh-add ~/.ssh/id_ed25519
```

###### 查看生成的公钥

```
cat ~/.ssh/id_rsa.pub

查看生成的公钥
在本地文件夹下打开git bash
```

###### 在 Github 中添加公钥

```

```

###### 测试链接

```
ssh -T git@github.com
```



```
git clone git@github.com:Linkenpro/MarkNote.git
```

```
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.
```

###### 暂存文件

```
# 或者添加所有修改的文件
git add .
```

###### 提交文件

```
git commit -m "Add new feature"
```

