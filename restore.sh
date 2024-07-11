# #!/bin/bash

# # 设置远程 EOS 地址
# export EOS_MGM_URL=root://eosuser.cern.ch  # 或 root://eosproject.cern.ch

# # 输入文件路径
input_file='address_fxid_v33.txt'

# 读取文件并循环恢复
while IFS= read -r fxid; do
    echo "Restoring $fxid..."
    eos recycle restore -p fxid:$fxid
done < "$input_file"

echo "Restoration completed."
