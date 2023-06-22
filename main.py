import pytube


def download_youtube_video(video_link, output_folder):
    youtube = pytube.YouTube(video_link)
    video = youtube.streams.get_highest_resolution()
    video_path = video.download(output_folder)
    return video_path


if __name__ == "__main__":
    video_link = input("Ingresa el enlace del video: ")
    output_folder = "./videos"
    video_path = download_youtube_video(video_link, output_folder)
    print("El video se ha descargado correctamente en:", video_path)
