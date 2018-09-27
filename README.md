# assetmgr
This setting need to be changed in the docker host to get ES running:

https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html

If not it will complain: https://www.google.com/search?q=docker%20elastic%20search%20Native%20controller%20process%20has%20stopped%20-%20no%20new%20native%20processes%20can%20be%20started

To dump the db.script to fill the DB for the testing:

- docker ps
- docker exec -it [container] bash
- inside the container: ./manage.py shell < db.script

Check that the symlinks for prod or dev are correct, we have 3:
- Dockerfile
- docker-compose.yml
- inetrecomgr/settings.py

