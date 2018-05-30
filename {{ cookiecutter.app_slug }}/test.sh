docker build -t test .
docker run -v "$(pwd)/opt/ml/":/opt/ml/ -it test train
docker run -p 8080:8080 -v "$(pwd)/opt/ml/":/opt/ml/ -it test serve
