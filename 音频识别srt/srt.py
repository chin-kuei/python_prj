import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk
import chardet
import os

# 确保 NLTK 的资源已下载
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def extract_unique_words_from_files(srt_files, output_file):
    """
    从多个 SRT 文件中提取所有单词，去重并恢复为原型形式，保存到一个 TXT 文件中。

    Args:
        srt_files (list): 输入的 SRT 文件路径列表。
        output_file (str): 输出的 TXT 文件路径。
    """
    # 初始化词形还原器
    lemmatizer = WordNetLemmatizer()
    all_unique_words = set()

    for srt_file in srt_files:
        print(f"正在处理文件: {srt_file}")
        # 检测文件编码
        with open(srt_file, 'rb') as file:
            raw_data = file.read()
            detected = chardet.detect(raw_data)
            encoding = detected['encoding']

        # 读取 SRT 文件内容
        with open(srt_file, 'r', encoding=encoding, errors='ignore') as file:
            content = file.read()

        # 使用正则表达式提取所有英文单词
        words = re.findall(r'\b[a-zA-Z]+\b', content)

        # 词形还原并去重
        # unique_words = set(lemmatizer.lemmatize(word.lower()) for word in words)
        unique_words = set(words)
        all_unique_words.update(unique_words)  # 合并到总的集合中

    # 将结果写入输出文件
    with open(output_file, 'w', encoding='utf-8') as file:
        for word in sorted(all_unique_words):  # 按字母顺序排序
            file.write(word + '\n')

    print(f"处理完成！所有唯一单词已保存到 {output_file}")

if __name__ == '__main__':
    # 输入的 SRT 文件夹路径
    srt_folder = '/Users/jerik/Downloads/srt_files/'  # 替换为你的 SRT 文件夹路径
    # 输出的 TXT 文件路径
    output_file = '/Users/jerik/Downloads/unique_words.txt'

    # 获取文件夹中所有 SRT 文件的路径
    srt_files = [os.path.join(srt_folder, file) for file in os.listdir(srt_folder) if file.endswith('.srt')]

    # 提取唯一单词并保存
    extract_unique_words_from_files(srt_files, output_file)