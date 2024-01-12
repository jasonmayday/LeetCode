# --------------------------------------------------------------
# 给定一个文件 file.txt，转置它的内容。
# 你可以假设每行列数相同，并且每个字段由 ' ' 分隔。

# --------------------------------------------------------------
# 示例：
# 假设 file.txt 文件内容如下：
#   name age
#   alice 21
#   ryan 30

# --------------------------------------------------------------
# 应当输出：
#   name alice ryan
#   age 21 30

# Read from the file file.txt and print its transposed content to stdout.

# 通过 head -n 命令可以获取文件指定行数的内容，再使用 wc -w 即可获取当前行的所有列数。由于本题每行列数相同，因此我们取第一行即可。
columns=$(cat file.txt | head -n 1 | wc -w)
# 获取每行的总列数为2列。接下来再写个循环来输出：
for i in $(seq 1 $columns)
do
# 可以使用 awk 命令处理文本，配置 print 命令来获取指定列的数据：
awk '{print $'''$i'''}' file.txt | xargs
done

