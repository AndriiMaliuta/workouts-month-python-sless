deploy:
	gcloud functions deploy workouts-month-python \
		--gen2 --trigger-http --runtime=python310 \
		--region=us-central1 --source=. \
		--entry-point=workouts_month --allow-unauthenticated --memory=256MB