# diary
2023-2 cloud native final exam

# How to start
```bash
git clone https://github.com/d3ng03/diary.git

cd diary/

docker build -t cn-backend ./backend
docker build -t cn-frontend ./frontend
docker build -t cn-db ./db

docker run -d -p 3306:3306 --network cloud_native --name cn-db cn-db
docker run -itd -p 80:80 -v ~/diary/frontend:/usr/share/nginx/html --network cloud_native --name cn-frontend cn-frontend
docker run -itd -p 5000:5000 -v ~/diary/backend:/app --network cloud_native --name cn-backend cn-backend
```
