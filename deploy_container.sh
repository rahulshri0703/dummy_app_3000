docker stop  $(docker ps -a -q)
docker rm -f $(docker ps -a -q)
docker pull rahulshri0703/dummy_3000:latest
docker run -d -p 5000:3000 rahulshri0703/dummy_3000:latest