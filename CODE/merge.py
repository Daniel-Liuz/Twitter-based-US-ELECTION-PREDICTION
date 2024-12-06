import pandas as pd

# 创建一个空的DataFrame用来存储合并的结果
merged_df = pd.DataFrame()

# 定义每次读取的块大小
chunksize = 10000
# 循环遍历每个文件，逐块读取并合并
for i in range(1, 21):
    file_name = f'{i}.csv'
    for chunk in pd.read_csv(file_name, chunksize=chunksize):
        # 如果是第二个及以后文件，去掉第一行（列名），假设第一个文件的列名是正确的且要保留
        if i > 1 and chunk.index[0] == 0:
            chunk = chunk.iloc[1:]
        # 将当前块的数据合并到最终的DataFrame中
        merged_df = pd.concat([merged_df, chunk], ignore_index=True)
# 保存最终的合并结果
merged_df.to_csv('all_merged_file.csv', index=False)