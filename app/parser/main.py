import json



def main():
	with open('references/switch/enchmarks.json', 'r') as f:
		data = json.load(f)

	print(data['benchmarks'][0]['name'])

if __name__ == "__main__":
	main()
