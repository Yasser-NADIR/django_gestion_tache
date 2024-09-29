run_db:
	docker build -t gestion_tache_db db/.
	echo "image created the will be running ....."
	docker run --rm -n db -d -p 33061:3306 gestion_tache_db