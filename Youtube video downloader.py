from pytube import YouTube

def show_description(yt):
	print('\n\nTITLE:', yt.title)  
	print('VIDEO ID:', yt.video_id)  
	print('DESCRIPTION:', yt.description)  
	print('LENGTH:', yt.length)  
	print('THUMBNAIL:', yt.thumbnail_url)  
	print('VIEWS', yt.views)  
	print('RATING', yt.rating)  
	print('AGE RESTRICTION:', yt.age_restricted, '\n\n') 


def all_progressive_nonprogressive(yt):
	count = 1
	for i in yt.streams.order_by('resolution'):
		print(count, i) #.download()
		count += 1

	choice = int(input("Enter your choice: "))
	yn = input("You want to downaload (Y/N): %s \n" %str(yt.streams.order_by('resolution')[choice-1]))

	if yn.upper() == 'Y':
		print("Downloading file now.......")
		yt.streams.order_by('resolution')[choice-1].download()
		input("File downloaded! Press any key to exit the program.")

	else: 
		input("Cannot understand your query. Press any key to exit.")


def progressive(yt):
	count = 1
	for i in yt.streams.filter(progressive=True).order_by('resolution'):
		print(count, i) #.download()
		count += 1
	
	choice = int(input("Enter your choice: "))
	yn = input("You want to downaload (Y/N): %s \n" %str(yt.streams.filter(progressive=True).order_by('resolution')[choice-1]))

	if yn.upper() == 'Y':
		print("Downloading file now.......")
		yt.streams.filter(progressive=True).order_by('resolution')[choice-1].download()
		input("File downloaded! Press any key to exit the program.")

	
	else: 
		input("Cannot understand your query. Press any key to exit.")



def download_video(yt):
	yn = input("Do you want progressive video? \nProgressive videos usually have sound. N will show both kind of video options\n(Y/N): ")

	if yn.lower() == 'n':
		all_progressive_nonprogressive(yt)

	elif yn.lower() == 'y':
		progressive(yt)

	else:
		input("Incorrect input. Press any key to exit.")


def main():

	# link of the video to be downloaded
	link=input("Enter YouTube video link: ")

	try:
		# object creation using YouTube
		# which was imported in the beginning
		yt = YouTube(link) 
		show_description(yt) 
		download_video(yt)
	except:
		input("Connection Error. press any key to exit.") #to handle exception


if __name__ == '__main__':
	main()