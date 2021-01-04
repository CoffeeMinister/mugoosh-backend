from api import app

def main():
	print("--Starting API--")
	app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
