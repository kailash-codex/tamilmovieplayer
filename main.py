# import m3u8

# with open('D2786.mp4.m3u8') as f:
#     m3u8_obj = m3u8.loads(f.read())
#     for playlist in m3u8_obj.playlists:
#         playlist.uri = 'https://cdn1.einthusan.io/etv/content/' + playlist.uri
    

# with open('D2786.mp4.m3u8', 'w') as f:
#     f.write(m3u8_obj.dumps())


def prepend_to_file(file_path, text_to_prepend):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    with open(file_path, 'w') as f:
        for i, line in enumerate(lines, start=1):
            if i >= 7 and i <= 2385:
                if i % 2 == 1:
                    f.write(text_to_prepend + line)
                    print(f'Line {i}: {line.strip()}')
                else:
                    f.write(line)
            else:
                f.write(line)

prepend_to_file("D2786.mp4.m3u8", 'https://cdn1.einthusan.io/etv/content/')