from inso import create_app
from inso import routine

app = create_app()

if __name__ == '__main__':
	app.run(debug=True)

	routine.routine()
