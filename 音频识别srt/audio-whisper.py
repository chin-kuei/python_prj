# 音频识别字幕 导出srt文件
import whisper
import os


def convert(sec_num):
    """
    Convert seconds to SRT timestamp format (HH:MM:SS,mmm)
    
    Args:
        sec_num (float): Time in seconds
        
    Returns:
        str: Formatted timestamp
    """
    # Convert to milliseconds once
    ms_total = int(sec_num * 1000)
    
    # Calculate all units at once
    hours, remainder = divmod(ms_total, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    seconds, milliseconds = divmod(remainder, 1000)
    
    # Format using f-string with padding
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


def identify(audio, srt):
    try:
        if not os.path.exists(audio):
            raise FileNotFoundError(f"Audio file not found: {audio}")
            
        print(f'正在识别: {audio}')
        model = whisper.load_model("large-v2")
        result = model.transcribe(audio, fp16=False)
        
        with open(srt, mode='w', encoding='utf-8') as f:
            f.write('\n')
            for line in result["segments"]:
                f.write(f"{line['id']}\n")
                f.write(f"{convert(line['start'])} --> {convert(line['end'])}\n")
                f.write(f"{line['text']}\n\n")
                
    except Exception as e:
        print(f"Error processing {audio}: {str(e)}")


if __name__ == '__main__':
    # 音频文件夹路径
    audio_folder = 'D:\\temp'
    file_list = os.listdir(audio_folder)
    for file in file_list:
        audio_path = os.path.join(audio_folder, file)
        srt_path = os.path.splitext(os.path.join(audio_folder, file))[0] + '.srt'
        identify(audio_path, srt_path)

    print('结束')
