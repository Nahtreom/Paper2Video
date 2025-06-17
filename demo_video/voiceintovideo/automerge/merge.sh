#!/bin/bash
# 1. 合并 voice1.mp4 和 video1.mp4
ffmpeg -i 1.mp4 -i voice1.mp4 -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 output1.mp4

# 2. 合并 voice2.mp4 和 video2.mp4
ffmpeg -i 2.mp4 -i voice2.mp4 -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 output2.mp4

# 3. 合并 voice3.mp4 和 video3.mp4
ffmpeg -i 3.mp4 -i voice3.mp4 -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 output3.mp4

# 4. 创建拼接列表
echo "file 'output1.mp4'" > file_list.txt
echo "file 'output2.mp4'" >> file_list.txt
echo "file 'output3.mp4'" >> file_list.txt

# 5. 拼接所有视频
ffmpeg -f concat -i file_list.txt -c copy final_output.mp4

# 6. 清理临时文件
rm file_list.txt output1.mp4 output2.mp4 output3.mp4

echo "合并完成！最终视频：final_output.mp4"