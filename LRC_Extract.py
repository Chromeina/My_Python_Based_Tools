from os import listdir
from os.path import join, isfile, splitext

path = input('請輸入要處理的路徑: ')
# path = input('Enter the path to process: ')
path = path.replace("\\", '/')
file_list = listdir(path)

for file_name in file_list:
    print('正在處理: ' + file_name)
    # print('Processing: ' + file_name)
    full_path = join(path, file_name)

    if file_name.endswith('.flac'):
        extension_length = 4
        is_music = True
    elif file_name.endswith('.mp3'):
        extension_length = 3
        is_music = True
    else:
        extension_length = len(splitext(full_path))
        is_music = False

    if isfile(full_path) and is_music:
        music_file = open(full_path, 'rb')
        music_data = music_file.read()
        music_file.close()
        try:
            head_position = music_data.find(b'\x4C\x59\x52\x49\x43\x53\x3D')
            tail_position = music_data.find(b'\x00\x00\x00\x74\x69\x74\x6C\x65')
            if head_position == -1 or tail_position == -1:
                print(file_name + ' 沒有歌詞檔案!')
                # print(file_name + ' doesn't contain lyrics!')
            else:
                lyrics_file = open(full_path[:-extension_length] + 'lrc', 'wb')
                lyrics_file.write(music_data[head_position+7:tail_position-1])
                lyrics_file.close()
        except ValueError:
            print(file_name + ' 沒有歌詞檔案!')
            # print(file_name + ' doesn't contain lyrics!')
    else:
        print(file_name + ' 不是音樂檔案!')
        # print(file_name + ' isn't a music file!')
