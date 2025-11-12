import vlc

rtsp_url = "rtsp://admin:pw123456@192.168.10.231:554/Streaming/Channels/101"
rtsp_url2 = "rtsp://admin:pw123456@192.168.10.231:554/Streaming/Channels/201"
instance = vlc.Instance()
instance2 = vlc.Instance()

player = instance.media_player_new()
player2 = instance2.media_player_new()

media = instance.media_new(rtsp_url)
media2 = instance2.media_new(rtsp_url2)

player.set_media(media)
player2.set_media(media2)

player.play()
player2.play()

while True:
    pass
